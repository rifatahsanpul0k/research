"""CLI: python -m better_model.run --config better_model/configs/reference.json."""

import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import subprocess
import time
import traceback

import anndata as ad
import numpy as np
import pandas as pd
import torch
from scipy import sparse
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import (adjusted_rand_score, normalized_mutual_info_score,
                             adjusted_mutual_info_score, homogeneity_score, v_measure_score,
                             fowlkes_mallows_score, calinski_harabasz_score, davies_bouldin_score)

from .config import ModelConfig, PreprocessConfig
from .data import align_annotations, align_modalities, preprocess
from .graphs import build_graphs
from .training import train, save_checkpoint, selection_score, partition_diagnostics


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path, obj):
    path = Path(path)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(obj, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def environment():
    versions = {}
    for name in ("torch", "torch-geometric", "scanpy", "anndata", "numpy", "scipy",
                 "scikit-learn", "scikit-misc", "pandas", "h5py"):
        versions[name] = importlib.metadata.version(name)
    root = Path(__file__).resolve().parents[1]
    def git(*args):
        result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
        return result.stdout.strip() if result.returncode == 0 else "unavailable"
    return {"python": platform.python_version(), "platform": platform.platform(), "packages": versions,
            "git_commit": git("rev-parse", "HEAD"), "git_status": git("status", "--porcelain"),
            "cuda": torch.version.cuda, "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
            "reproducibility": "seeded; CUDA scatter kernels may be nondeterministic",
            "source_sha256": {p.name: sha256(p) for p in Path(__file__).parent.glob("*.py")}}


def resolve_inputs(spec, data_root):
    directory = Path(data_root) / spec["name"]
    if (directory / "raw").is_dir():
        directory = directory / "raw"
    modality = spec["preprocess"]["aux_modality"]
    paths = {"rna": directory / spec.get("rna_file", "adata_RNA.h5ad"),
             "aux": directory / spec.get("aux_file", f"adata_{modality}.h5ad")}
    if spec.get("annotation_file"):
        paths["annotations"] = directory / spec["annotation_file"]
    for name, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"Missing {name}: {path}; place source files here or change --data-root")
    hashes = {name: sha256(path) for name, path in paths.items()}
    expected = spec.get("expected_sha256", {})
    # The repository records an incomplete E18 ATAC download. A filename is not verification.
    if spec["name"] == "Mouse_Brain_E18_S1" and not expected.get("aux"):
        raise ValueError("E18 ATAC remains gated: supply expected_sha256.aux from a verified complete source")
    for name, value in expected.items():
        if hashes.get(name) != value:
            raise ValueError(f"Source checksum mismatch: {name}")
    return paths, hashes


def load_inputs(spec, data_root):
    paths, hashes = resolve_inputs(spec, data_root)
    rna, aux = align_modalities(ad.read_h5ad(paths["rna"]), ad.read_h5ad(paths["aux"]))
    labels = None
    if "annotations" in paths:
        frame = pd.read_csv(paths["annotations"], index_col=0)
        labels = align_annotations(frame, rna.obs_names, spec["annotation_column"])
    return rna, aux, labels, {"paths": {k: str(v.resolve()) for k, v in paths.items()}, "sha256": hashes}


def evaluate(embedding, predicted, labels, config, excluded_labels=()):
    score, _ = selection_score(embedding, predicted, ModelConfig(n_clusters=config.n_clusters))
    result = {"silhouette": score, **partition_diagnostics(predicted, config.n_clusters)}
    if 1 < len(np.unique(predicted)) < len(predicted):
        result.update(calinski_harabasz=float(calinski_harabasz_score(embedding, predicted)),
                      davies_bouldin=float(davies_bouldin_score(embedding, predicted)))
    else:
        result.update(calinski_harabasz=None, davies_bouldin=None)
    mask = np.zeros(len(predicted), dtype=bool) if labels is None else (
        labels.notna() & ~labels.isin(excluded_labels)).to_numpy()
    result["n_annotated_evaluated"] = int(mask.sum())
    result["n_unannotated_or_excluded"] = int((~mask).sum())
    for key, func in (("ari", adjusted_rand_score), ("nmi", normalized_mutual_info_score),
                      ("ami", adjusted_mutual_info_score), ("homogeneity", homogeneity_score),
                      ("v_measure", v_measure_score), ("fmi", fowlkes_mallows_score)):
        result[key] = float(func(labels[mask].astype(str), predicted[mask])) if mask.sum() > 1 else None
    return result


def baseline_embeddings(prepared):
    def pca(x):
        return PCA(n_components=min(30, min(x.shape) - 1), svd_solver="full").fit_transform(x)
    first, second = pca(prepared.rna), pca(prepared.aux)
    def unit_block(x):
        return x / max(float(np.linalg.norm(x)), 1e-12)
    pos = prepared.positions.astype(float)
    pos = (pos - pos.mean(axis=0)) / np.maximum(pos.std(axis=0), 1e-12)
    return {"RNA_PCA": first, "AUX_PCA": second,
            "CONCAT_EQUAL": np.concatenate((unit_block(first), unit_block(second)), axis=1), "SPACE": pos}


def synthetic_inputs(seed=42):
    """Small engineering fixture, not a biological benchmark."""
    rng = np.random.default_rng(seed)
    groups = np.repeat(np.arange(3), 16)
    rate = np.full((3, 36), 1.0)
    for i in range(3):
        rate[i, i * 12:(i + 1) * 12] = 12
    rna_x = rng.poisson(rate[groups]).astype(float)
    aux_rate = np.ones((3, 9))
    for i in range(3):
        aux_rate[i, i * 3:(i + 1) * 3] = 15
    aux_x = rng.poisson(aux_rate[groups]).astype(float)
    obs = pd.DataFrame(index=[f"synthetic-{i}" for i in range(len(groups))])
    rna = ad.AnnData(sparse.csr_matrix(rna_x), obs=obs.copy())
    aux = ad.AnnData(sparse.csr_matrix(aux_x), obs=obs.copy())
    pos = np.c_[groups * 8.0, np.zeros(len(groups))] + rng.normal(size=(len(groups), 2))
    rna.obsm["spatial"] = aux.obsm["spatial"] = pos
    return rna, aux, pd.Series(groups.astype(str), index=obs.index), {"kind": "synthetic", "seed": seed}


def smoke_config():
    return {"compute_class": "LOCAL_LIGHT", "seeds": [42], "baselines": True,
            "datasets": [{"name": "SYNTHETIC_SMOKE", "n_clusters": 3,
                          "preprocess": {"aux_modality": "ADT", "hvg_flavor": "seurat", "n_hvg": 30, "min_cells": 1}}],
            "model": {"hidden_dim": 16, "latent_dim": 8, "pretrain_epochs": 3, "finetune_epochs": 2,
                      "n_neighbors": 4, "pair_block_size": 16}}


def run_suite(configuration, data_root, output_dir, smoke=False):
    if configuration.get("compute_class") not in ("LOCAL_LIGHT", "COLAB_GPU", "COLAB_CPU"):
        raise ValueError("Declare compute_class: LOCAL_LIGHT, COLAB_GPU or COLAB_CPU")
    if not smoke and configuration["compute_class"] == "LOCAL_LIGHT":
        raise ValueError("Full neural runs need COLAB_GPU or COLAB_CPU; use --smoke for local engineering checks")
    if configuration["compute_class"] == "COLAB_GPU" and not torch.cuda.is_available():
        raise RuntimeError("This configuration requires a GPU runtime; enable a Colab GPU, or use --smoke locally")
    device = "cuda" if configuration["compute_class"] == "COLAB_GPU" else "cpu"
    seeds = configuration["seeds"]
    if not seeds or len(set(seeds)) != len(seeds) or any(type(s) is not int or s < 0 for s in seeds):
        raise ValueError("seeds must be a nonempty list of unique nonnegative integers")
    names = [s["name"] for s in configuration["datasets"]]
    if not names or len(set(names)) != len(names) or any(Path(n).name != n or n in (".", "..") for n in names):
        raise ValueError("Dataset names must be unique simple directory names")
    # Record every default explicitly, including per-dataset K, before training.
    resolved = json.loads(json.dumps(configuration))
    for spec in resolved["datasets"]:
        spec["model_resolved"] = ModelConfig(**{**configuration.get("model", {}), "n_clusters": spec["n_clusters"]}).validate().to_dict()
        spec["preprocess"] = asdict(PreprocessConfig(**spec["preprocess"]).validate())
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=False)  # Never overwrite a prior run.
    write_json(output_dir / "config.json", configuration)
    write_json(output_dir / "resolved_config.json", resolved)
    write_json(output_dir / "environment.json", environment())
    # uv-created environments need not contain pip.
    installed = sorted({f"{d.metadata['Name']}=={d.version}" for d in importlib.metadata.distributions()
                        if d.metadata.get("Name")})
    (output_dir / "requirements.freeze.txt").write_text("\n".join(installed) + "\n")
    # Save source alongside dirty-tree hashes so local uncommitted code is reproducible.
    sources = output_dir / "source"
    sources.mkdir()
    for path in Path(__file__).parent.glob("*.py"):
        (sources / path.name).write_bytes(path.read_bytes())
    run_state = {"status": "RUNNING", "started_at": utc_now(), "compute_class": configuration["compute_class"],
                 "experiment_id": output_dir.name, "kind": "synthetic engineering smoke" if smoke else "transductive research",
                 "claim": "No held-out generalization or biological superiority claim"}
    write_json(output_dir / "status.json", run_state)
    start = time.perf_counter()
    rows = []
    try:
        for spec in configuration["datasets"]:
            model_config = ModelConfig(**{**configuration.get("model", {}), "n_clusters": spec["n_clusters"]}).validate()
            prep_config = PreprocessConfig(**spec["preprocess"]).validate()
            rna, aux, labels, input_record = synthetic_inputs() if smoke else load_inputs(spec, data_root)
            dataset_dir = output_dir / spec["name"]
            dataset_dir.mkdir()
            write_json(dataset_dir / "inputs.json", input_record)
            prepared = preprocess(rna, aux, prep_config)
            np.savez_compressed(dataset_dir / "preprocessing.npz", **prepared.transforms)
            write_json(dataset_dir / "preprocessing.json", prepared.metadata)
            graph, graph_info = build_graphs(prepared.rna, prepared.aux, prepared.positions, model_config, device)
            write_json(dataset_dir / "graph.json", graph_info)
            np.savez_compressed(dataset_dir / "graph.npz", **{
                name: getattr(graph, name).cpu().numpy() for name in (
                    "sim_edge_index", "sim_edge_weight", "dist_edge_index", "dist_edge_weight",
                    "common_edge_index", "common_edge_weight")})
            base = baseline_embeddings(prepared) if configuration.get("baselines", True) else {}
            for seed in seeds:
                seed_dir = dataset_dir / f"seed_{seed}"
                seed_dir.mkdir()
                seed_start = time.perf_counter()
                def progress(row):
                    with (seed_dir / "history.jsonl").open("a") as stream:
                        stream.write(json.dumps(row, allow_nan=False) + "\n")
                    if row["epoch"] == 1 or row["epoch"] % 25 == 0:
                        print(f"{spec['name']} seed={seed} epoch={row['epoch']} stage={row['stage']} loss={row['total_loss']:.4f}", flush=True)
                result = train(graph, model_config, seed, progress)
                save_checkpoint(seed_dir / "model.pt", result, model_config, seed,
                                (prepared.rna.shape[1], prepared.aux.shape[1]))
                # Load annotations only into post-training evaluation and exports.
                metrics = evaluate(result.embedding, result.labels, labels, model_config, spec.get("excluded_labels", []))
                write_json(seed_dir / "metrics.json", metrics)
                write_json(seed_dir / "selection.json", {"selected": result.selected, "stage1_bridge": result.bridge})
                output = prepared.output.copy()
                output.obsm["X_astra"] = result.embedding
                output.obsm["gate_spatial"] = result.gate_spatial
                output.obsm["gate_modality"] = result.gate_modality
                output.obs["astra_cluster"] = pd.Categorical(result.labels.astype(str))
                output.obs["mean_rna_gate"] = result.gate_modality.mean(axis=1)
                if labels is not None:
                    output.obs["reference_annotation"] = labels.astype("category")
                output.layers["reconstructed_scaled_rna"] = result.reconstruction_scaled
                # This reconstruction is standardized model output, not counts or valid DE input.
                output.uns["astra"] = {"seed": seed, "selected_epoch": result.selected["epoch"],
                                       "selected_stage": result.selected["stage"], "backend": result.selected["backend"],
                                       "model_config_json": json.dumps(model_config.to_dict())}
                output.write_h5ad(seed_dir / "result.h5ad")
                output.obs.to_csv(seed_dir / "assignments.csv", index_label="barcode")
                rows.append({"dataset": spec["name"], "seed": seed, "method": "ASTRA",
                             "selected_epoch": result.selected["epoch"], "selected_stage": result.selected["stage"],
                             "seconds": time.perf_counter() - seed_start, **metrics})
                baseline_assignments = pd.DataFrame(index=prepared.output.obs_names)
                for name, embedding in base.items():
                    predictions = KMeans(n_clusters=model_config.n_clusters, n_init=10, random_state=seed).fit_predict(embedding)
                    baseline_assignments[name] = predictions
                    rows.append({"dataset": spec["name"], "seed": seed, "method": name,
                                 **evaluate(embedding, predictions, labels, model_config, spec.get("excluded_labels", []))})
                if len(baseline_assignments.columns):
                    baseline_assignments.to_csv(seed_dir / "baseline_assignments.csv", index_label="barcode")
                pd.DataFrame(rows).to_csv(output_dir / "metrics.csv", index=False)
                print(f"Saved {seed_dir}; ARI={metrics['ari']}, selected epoch={result.selected['epoch']}", flush=True)
        table = pd.DataFrame(rows)
        metrics = [key for key in ("ari", "nmi", "ami", "silhouette", "max_cluster_fraction") if key in table]
        table.groupby(["dataset", "method"])[metrics].agg(["mean", "std", "count"]).to_csv(output_dir / "summary.csv")
        run_state.update(status="COMPLETED", completed_at=utc_now(), seconds=time.perf_counter() - start)
    except Exception as error:
        run_state.update(status="FAILED", completed_at=utc_now(), error=f"{type(error).__name__}: {error}")
        (output_dir / "failure.txt").write_text(traceback.format_exc())
        raise
    finally:
        write_json(output_dir / "status.json", run_state)
        write_json(output_dir / "artifacts.json", {str(p.relative_to(output_dir)): sha256(p)
                                                  for p in output_dir.rglob("*") if p.is_file() and p.name != "artifacts.json"})
    return output_dir


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("better_model/configs/reference.json"))
    parser.add_argument("--data-root", type=Path, default=Path("04_datasets"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--smoke", action="store_true", help="Small synthetic end-to-end run on CPU")
    parser.add_argument("--preflight", action="store_true", help="Validate configuration, input IDs and checksums without training")
    args = parser.parse_args()
    configuration = smoke_config() if args.smoke else json.loads(args.config.read_text())
    if args.preflight:
        for spec in configuration["datasets"]:
            ModelConfig(**{**configuration.get("model", {}), "n_clusters": spec["n_clusters"]}).validate()
            PreprocessConfig(**spec["preprocess"]).validate()
            rna, aux, labels, record = synthetic_inputs() if args.smoke else load_inputs(spec, args.data_root)
            print(json.dumps({"dataset": spec["name"], "rna_shape": rna.shape, "aux_shape": aux.shape,
                              "annotated_spots": int(labels.notna().sum()) if labels is not None else 0,
                              "inputs": record}, indent=2))
        return
    stamp = datetime.now(timezone.utc).strftime("EXP-%Y%m%d-%H%M%S-%f")
    output = args.output or Path("better_model/outputs") / stamp
    print(run_suite(configuration, args.data_root, output, args.smoke))


if __name__ == "__main__":
    main()

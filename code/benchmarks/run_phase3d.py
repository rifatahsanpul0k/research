"""Execute one frozen Phase 3D MOFA+ or SCOT project-data configuration.

This entry point is intended to run in the declared Colab runtime. It refuses
to execute a COLAB_* configuration unless ASTRA_COLAB_CONFIRMED=1 is set by
the thin Colab controller.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "LOKY_MAX_CPU_COUNT"):
    os.environ[_name] = "1"

import h5py
import numpy as np
import scipy
import sklearn
from scipy import sparse

from code.benchmarks.common.evaluation import cluster_and_evaluate
from code.benchmarks.common.failures import write_failure_artifacts
from code.benchmarks.common.h5ad import H5ADView, load_h5ad, load_labels, sha256
from code.benchmarks.common.io import write_json_atomic
from code.benchmarks.common.preprocessing import adt_representation, atac_representation, rna_representation, row_diagnostics, zscore_columns
from code.benchmarks.common.validation import validate_embedding, validate_row_mapping
from code.benchmarks.methods.mofaplus import fit as fit_mofaplus
from code.benchmarks.methods.scot import fit as fit_scot

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "02_omics/01_measurement_and_data_generation/DOWNLOAD_MANIFEST.json"
REGISTRY = ROOT / "experiments.csv"
ALLOWED_METHODS = {"MOFAPLUS", "SCOT"}
ALLOWED_COMPUTE = {"COLAB_CPU", "COLAB_HIGH_MEMORY"}
SEEDS = {1729, 2718, 31415}
DATASETS = {
    "LN_A1": ("10x_human_lymph_node_A1", "ADT", "annotation.csv", "manual-anno"),
    "LN_D1": ("10x_human_lymph_node_D1", "ADT", "annotation.csv", "manual-anno"),
    "MB_E11": ("Mouse_Brain_E11_S1", "ATAC", "anno.csv", "cluster"),
    "MB_E13": ("Mouse_Brain_E13_S1", "ATAC", "anno.csv", "cluster"),
    "MB_E15": ("Mouse_Brain_E15_S1", "ATAC", "anno.csv", "cluster"),
}


def _utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def _rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _package_versions() -> dict[str, str]:
    names = ("numpy", "scipy", "scikit-learn", "h5py", "mofapy2", "POT")
    out = {}
    for name in names:
        try:
            out[name] = version(name)
        except PackageNotFoundError:
            out[name] = "NOT_INSTALLED"
    return out


def environment_record(classification: str) -> dict[str, object]:
    gpu = "NOT_APPLICABLE"
    cuda = "NOT_APPLICABLE"
    try:
        query = subprocess.run(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"], capture_output=True, text=True, check=False)
        if query.returncode == 0 and query.stdout.strip():
            gpu = query.stdout.strip().splitlines()[0]
            cuda = "nvidia-smi_reported"
    except OSError:
        pass
    memory = {}
    meminfo = Path("/proc/meminfo")
    if meminfo.exists():
        for line in meminfo.read_text().splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                memory[key] = value.strip()
    return {
        "compute_classification": classification,
        "execution_platform": "Google Colab" if "COLAB" in classification else "local",
        "colab_runtime_type": os.environ.get("COLAB_RUNTIME_TYPE", "UNKNOWN") if "COLAB" in classification else "NOT_APPLICABLE",
        "python_version": platform.python_version(),
        "interpreter": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "gpu_model": gpu,
        "cuda_version": cuda,
        "ram_class": os.environ.get("ASTRA_COLAB_RAM_CLASS", "UNKNOWN") if "COLAB" in classification else "LOCAL_RECORDED_SEPARATELY",
        "packages": _package_versions() | {"scikit_learn_runtime": sklearn.__version__, "h5py_runtime": h5py.__version__, "scipy_runtime": scipy.__version__},
        "thread_environment": {name: os.environ.get(name, "UNSET") for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "LOKY_MAX_CPU_COUNT")},
        "memory_info": memory,
    }


def expected_checksums() -> dict[str, str]:
    result = {}
    for record in json.loads(MANIFEST.read_text()):
        if record.get("status") != "complete":
            continue
        path = ROOT / "04_datasets" / record["dataset_id"] / "raw" / record["filename"]
        result[_rel(path)] = record["sha256"]
    return result


def verify_sources(spec: tuple[str, str, str, str], checksums: dict[str, str]) -> tuple[H5ADView, H5ADView, np.ndarray, dict[str, object], dict[str, str]]:
    folder, second_modality, annotation_name, label_column = spec
    raw = ROOT / "04_datasets" / folder / "raw"
    rna_path = raw / "adata_RNA.h5ad"
    second_path = raw / f"adata_{second_modality}.h5ad"
    rna = load_h5ad(rna_path, checksums[_rel(rna_path)])
    second = load_h5ad(second_path, checksums[_rel(second_path)])
    validate_row_mapping(rna.observation_ids, second.observation_ids)
    if not np.array_equal(rna.coordinates, second.coordinates):
        raise ValueError("paired coordinates differ")
    labels, annotation = load_labels(raw / annotation_name, rna.observation_ids, label_column)
    annotation_path = raw / annotation_name
    if sha256(annotation_path) != checksums[_rel(annotation_path)]:
        raise ValueError("annotation checksum mismatch")
    paths = {_rel(path): sha256(path) for path in (rna_path, second_path, annotation_path)}
    return rna, second, labels, annotation, paths


def mofa_atac(matrix: sparse.csr_matrix, feature_ids: list[str]) -> tuple[np.ndarray, dict[str, object]]:
    if not sparse.issparse(matrix):
        matrix = sparse.csr_matrix(matrix)
    if not np.isfinite(matrix.data).all() or np.any(matrix.data < 0):
        raise ValueError("MOFA ATAC source contains invalid stored values")
    logged = matrix.copy().astype(np.float64)
    logged.data = np.log1p(logged.data)
    mean = np.asarray(logged.mean(axis=0)).ravel()
    second = np.asarray(logged.power(2).mean(axis=0)).ravel()
    variance = np.maximum(second - mean * mean, 0.0)
    count = min(2000, matrix.shape[1])
    positions = np.lexsort((np.arange(matrix.shape[1]), -variance))[:count]
    result = zscore_columns(logged[:, positions].toarray())
    selected = [feature_ids[int(i)] for i in positions]
    return result, {
        "source_semantics": "SOURCE_PROVIDED_PROCESSED_X_COUNT_OR_FRAGMENT_SEMANTICS_UNKNOWN",
        "transform": "log1p_on_stored_nonzero_values",
        "feature_selection": "top_population_variance_after_log1p_stable_position_ties",
        "selected_features": count,
        "selected_positions": [int(i) for i in positions],
        "selected_feature_ids": selected,
        "selected_feature_ids_sha256": hashlib.sha256(("\n".join(selected) + "\n").encode()).hexdigest(),
        "scaling": "feature_population_zscore_constant_to_zero",
    }


def prepare_views(method: str, rna: H5ADView, second: H5ADView, second_modality: str) -> tuple[list[np.ndarray], list[list[str]], list[dict[str, object]]]:
    rna_values, rna_meta = rna_representation(rna.matrix, rna.feature_ids, n_features=2000)
    if second_modality == "ADT":
        second_values, second_meta = adt_representation(second.matrix, second.feature_ids)
    elif method == "MOFAPLUS":
        second_values, second_meta = mofa_atac(second.matrix, second.feature_ids)
    else:
        second_values, second_meta = atac_representation(second.matrix, second.feature_ids)
    return [rna_values, second_values], [rna_meta.get("selected_feature_ids", rna.feature_ids), second_meta.get("selected_feature_ids", second.feature_ids)], [rna_meta, second_meta]


def _write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def append_registry(row: dict[str, object]) -> None:
    with REGISTRY.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    if any(item.get("experiment_id") == row["experiment_id"] for item in rows):
        raise ValueError(f"experiment already registered: {row['experiment_id']}")
    rows.append({field: str(row.get(field, "")) for field in fields})
    _write_csv(REGISTRY, fields, rows)


def run(config_path: Path) -> dict[str, object]:
    config = json.loads(config_path.read_text())
    method = config.get("method")
    classification = config.get("compute_classification")
    if method not in ALLOWED_METHODS:
        raise ValueError("Phase 3D runner accepts only MOFAPLUS or SCOT")
    if classification not in ALLOWED_COMPUTE:
        raise ValueError("project-data Phase 3D runs require COLAB_CPU or COLAB_HIGH_MEMORY")
    if os.environ.get("ASTRA_COLAB_CONFIRMED") != "1":
        raise RuntimeError("set ASTRA_COLAB_CONFIRMED=1 only inside the verified Colab controller")
    if config.get("seed") not in SEEDS:
        raise ValueError("seed is outside the frozen Phase 3D seed policy")
    if config.get("dataset") not in DATASETS:
        raise ValueError("dataset is outside the frozen Phase 3D eligibility matrix")
    head = _git_head()
    if config.get("start_commit") != head:
        raise ValueError(f"repository HEAD {head} does not match frozen start commit {config.get('start_commit')}")
    identity = config["experiment_id"]
    output = ROOT / "08_experiments" / identity
    if output.exists():
        raise FileExistsError(f"immutable experiment directory already exists: {output}")
    output.mkdir(parents=True)
    native = output / "native_output"
    native.mkdir()
    started = _utc()
    clock = time.perf_counter()
    try:
        checksums = expected_checksums()
        rna, second, labels, annotation, input_hashes = verify_sources(DATASETS[config["dataset"]], checksums)
        views, feature_ids, preprocessing = prepare_views(method, rna, second, DATASETS[config["dataset"]][1])
        write_json_atomic({"config": config, "input_checksums": input_hashes, "annotation": annotation, "preprocessing": preprocessing}, output / "preprocessing.json")
        write_json_atomic(config, output / "config.json")
        _write_csv(output / "identity_map.csv", ["original_observation_id", "method_internal_id"], [{"original_observation_id": x, "method_internal_id": x} for x in rna.observation_ids])
        if method == "MOFAPLUS":
            embedding, native_meta = fit_mofaplus(views, rna.observation_ids, feature_ids, config, native)
        else:
            effective_config = dict(config)
            effective_config["official_source_root"] = str(ROOT / "external/SCOT")
            embedding, native_meta = fit_scot(views, rna.observation_ids, feature_ids, effective_config, native)
        embedding = np.asarray(embedding, dtype=np.float64)
        if embedding.ndim != 2:
            embedding = np.squeeze(embedding)
        validate_embedding(embedding.tolist(), len(rna.observation_ids))
        validate_row_mapping(rna.observation_ids, rna.observation_ids)
        diagnostics = row_diagnostics(embedding)
        if not diagnostics["finite"] or diagnostics["collapsed"]:
            raise ValueError("method output failed finite/collapse validation")
        np.savez_compressed(output / "embedding.npz", embedding=embedding)
        clusters, metrics, cluster_sizes = cluster_and_evaluate(embedding, labels, int(config["seed"]))
        _write_csv(output / "clusters.csv", ["original_observation_id", "cluster"], [{"original_observation_id": x, "cluster": int(y)} for x, y in zip(rna.observation_ids, clusters, strict=True)])
        write_json_atomic(metrics, output / "metrics.json")
        qc_status = "PASS_WITH_FLAGS" if any(v == 1 for v in cluster_sizes.values()) else "PASS"
        write_json_atomic({"native": native_meta, "representation_diagnostics": diagnostics, "cluster_sizes": cluster_sizes, "execution_status": "SUCCEEDED", "scientific_qc_status": qc_status}, output / "validation.json")
        runtime = time.perf_counter() - clock
        environment = environment_record(classification)
        provenance = {
            "experiment_id": identity,
            "timestamp_utc": _utc(),
            "dataset": config["dataset"],
            "method": method,
            "code_commit": _git_head(),
            "compute_classification": classification,
            "environment": environment,
            "preprocessing": preprocessing,
            "seed": {"method": config["seed"], "numpy": 0, "clustering": config["seed"]},
            "parameters": {key: value for key, value in config.items() if key.endswith("options") or key in {"k", "epsilon", "projection"}},
            "hardware": {"gpu_model": environment["gpu_model"], "cuda_version": environment["cuda_version"], "ram_class": environment["ram_class"]},
            "input_checksums": input_hashes,
            "output_paths": {"embedding": _rel(output / "embedding.npz"), "native_output": _rel(native), "metrics": _rel(output / "metrics.json")},
            "runtime_seconds": runtime,
            "runtime_scope": "preprocessing_method_fit_common_clustering_metrics_and_artifact_serialization",
            "exit_status": "SUCCEEDED",
        }
        write_json_atomic(provenance, output / "provenance.json")
        (output / "stdout.log").write_text(f"{identity} SCIENTIFIC_BASELINE_RUN SUCCEEDED\n")
        (output / "stderr.log").write_text("")
        (output / "STATUS").write_text("SUCCEEDED\n")
        artifact_names = ["config.json", "preprocessing.json", "identity_map.csv", "embedding.npz", "clusters.csv", "metrics.json", "validation.json", "provenance.json", "stdout.log", "stderr.log", "STATUS"]
        write_json_atomic({"experiment_id": identity, "artifacts": [{"path": name, "sha256": sha256(output / name), "bytes": (output / name).stat().st_size} for name in artifact_names]}, output / "saved_artifacts_manifest.json")
        append_registry({
            "experiment_id": identity,
            "parent_experiment_id": "",
            "comparison_group_id": f"P3D-{config['dataset']}-{method}",
            "question_id": "P3D_CLASSICAL_INTEGRATION_REPRODUCTION",
            "status": "SUCCEEDED",
            "dataset_ids": DATASETS[config["dataset"]][0],
            "dataset_version": "PHASE1D_SHA256_MANIFEST",
            "preprocessing_version": "PHASE_3D_CONFIG_FREEZE_2026-09-12",
            "split_manifest": "NOT_APPLICABLE_UNSUPERVISED_FULL_DATA",
            "random_seeds": json.dumps(config["seed"]),
            "initial_representation_id": method,
            "representation_method_id": method,
            "model": method,
            "code_commit": _git_head(),
            "hyperparameters_path": _rel(config_path),
            "learned_embedding_path": _rel(output / "embedding.npz"),
            "downstream_task": "common_KMeans_clustering",
            "evaluation_metrics_path": _rel(output / "metrics.json"),
            "runtime_seconds": runtime,
            "hardware_software_environment": _rel(output / "provenance.json"),
            "saved_artifacts_manifest": _rel(output / "saved_artifacts_manifest.json"),
            "biological_evaluation_path": _rel(output / "metrics.json"),
            "reproducibility_status": "R3_PROJECT_DATA",
            "run_record_path": _rel(output / "provenance.json"),
            "started_at": started,
            "finished_at": _utc(),
            "notes": f"Phase 3D {method}; agreement with reference annotation; compute={classification}; no ranking or biological factor interpretation",
        })
        return {"experiment_id": identity, "status": "SUCCEEDED", "runtime_seconds": runtime, "metrics": metrics, "cluster_sizes": cluster_sizes, "scientific_qc_status": qc_status}
    except Exception as error:
        write_failure_artifacts(output, identity, error, "METHOD_ERROR", "phase3d_execution", traceback.format_exc())
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.config), indent=2, sort_keys=True))


"""Execute the frozen Phase 3C transparent baseline series."""

from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import subprocess
import sys
import time
import traceback
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

# Freeze local CPU parallelism before importing NumPy/scikit-learn.
for _thread_variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "LOKY_MAX_CPU_COUNT"):
    os.environ[_thread_variable] = "1"

import h5py
import numpy as np
import scipy
import sklearn

from code.benchmarks.common.evaluation import cluster_and_evaluate
from code.benchmarks.common.failures import write_failure_artifacts
from code.benchmarks.common.h5ad import H5ADView, load_h5ad, load_labels, sha256
from code.benchmarks.common.io import write_json_atomic
from code.benchmarks.common.preprocessing import row_diagnostics
from code.benchmarks.common.validation import validate_embedding, validate_row_mapping
from code.benchmarks.methods.transparent import Representation, build_representations

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT_ROOT = ROOT / "08_experiments"
DOWNLOAD_MANIFEST = ROOT / "02_omics/01_measurement_and_data_generation/DOWNLOAD_MANIFEST.json"
REGISTRY = ROOT / "experiments.csv"
RESULTS = EXPERIMENT_ROOT / "PHASE_3C_BASELINE_RESULTS.csv"
PREFLIGHT = EXPERIMENT_ROOT / "PHASE_3C_INPUT_PREFLIGHT.json"
SEEDS = (1729, 2718, 31415)
FIRST_ID = "EXP-LN-A1-PCA-KMEANS-S1729"


@dataclass(frozen=True)
class DatasetSpec:
    canonical_id: str
    registry_id: str
    slug: str
    folder: str
    annotation: str
    label_column: str
    second_modality: str | None


DATASETS = (
    DatasetSpec("LN_A1", "10x_human_lymph_node_A1", "LN-A1", "10x_human_lymph_node_A1", "annotation.csv", "manual-anno", "ADT"),
    DatasetSpec("LN_D1", "10x_human_lymph_node_D1", "LN-D1", "10x_human_lymph_node_D1", "annotation.csv", "manual-anno", "ADT"),
    DatasetSpec("MB_E11", "Mouse_Brain_E11_S1", "MB-E11", "Mouse_Brain_E11_S1", "anno.csv", "cluster", "ATAC"),
    DatasetSpec("MB_E13", "Mouse_Brain_E13_S1", "MB-E13", "Mouse_Brain_E13_S1", "anno.csv", "cluster", "ATAC"),
    DatasetSpec("MB_E15", "Mouse_Brain_E15_S1", "MB-E15", "Mouse_Brain_E15_S1", "anno.csv", "cluster", "ATAC"),
    DatasetSpec("MB_E18", "Mouse_Brain_E18_S1", "MB-E18", "Mouse_Brain_E18_S1", "anno.csv", "cluster", None),
)

RESULT_FIELDS = [
    "experiment_id", "dataset", "modalities", "baseline", "representation", "embedding_dim",
    "clustering", "cluster_count", "cluster_count_source", "seed", "ARI", "NMI", "silhouette",
    "runtime_seconds", "runtime_scope", "status", "metric_output_location", "provenance_location",
]


def _utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def _relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _git_dirty() -> bool:
    return bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True).strip())


def environment_record() -> dict[str, object]:
    return {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "os": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "cpu_class": "Apple M2 8-core",
        "ram_gib": 16,
        "gpu_class": "Apple M2 integrated Metal 8-core",
        "cuda_available": False,
        "packages": {
            "numpy": np.__version__, "scipy": scipy.__version__, "scikit_learn": sklearn.__version__,
            "h5py": h5py.__version__,
        },
        "thread_environment": {name: os.environ.get(name, "UNSET") for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "LOKY_MAX_CPU_COUNT")},
    }


def expected_checksums() -> dict[str, str]:
    records = json.loads(DOWNLOAD_MANIFEST.read_text())
    expected = {}
    for record in records:
        if record.get("status") == "complete":
            path = ROOT / "04_datasets" / record["dataset_id"] / "raw" / record["filename"]
            expected[str(path)] = record["sha256"]
    return expected


def verify_all_sources(stage: str) -> dict[str, object]:
    expected = expected_checksums()
    files = []
    for name, digest in sorted(expected.items()):
        path = Path(name)
        observed = sha256(path)
        if observed != digest:
            raise ValueError(f"source checksum mismatch at {stage}: {path}")
        files.append({"path": _relative(path), "expected_sha256": digest, "observed_sha256": observed, "match": True})
    record = {"stage": stage, "checked_at": _utc(), "manifest": _relative(DOWNLOAD_MANIFEST), "files": files, "all_match": True,
              "e18_atac_verified": False, "e18_atac_status": "NOT_APPLICABLE_E18_ATAC_UNVERIFIED"}
    destinations = {
        "before_first_scientific_run": PREFLIGHT,
        "after_first_scientific_run": EXPERIMENT_ROOT / "PHASE_3C_FIRST_GATE_POSTCHECK.json",
        "after_remaining_series": EXPERIMENT_ROOT / "PHASE_3C_SOURCE_POSTCHECK.json",
    }
    if stage in destinations:
        write_json_atomic(record, destinations[stage])
    return record


def load_dataset(spec: DatasetSpec, checksums: dict[str, str]) -> tuple[H5ADView, H5ADView | None, np.ndarray, dict[str, object], dict[str, str]]:
    raw = ROOT / "04_datasets" / spec.folder / "raw"
    rna_path = raw / "adata_RNA.h5ad"
    rna = load_h5ad(rna_path, checksums[str(rna_path)])
    second = None
    paths = {_relative(rna_path): rna.file_sha256}
    if spec.second_modality:
        second_path = raw / f"adata_{spec.second_modality}.h5ad"
        second = load_h5ad(second_path, checksums[str(second_path)])
        paths[_relative(second_path)] = second.file_sha256
        validate_row_mapping(rna.observation_ids, second.observation_ids)
        if not np.array_equal(rna.coordinates, second.coordinates):
            raise ValueError("paired H5AD coordinate arrays differ")
    annotation_path = raw / spec.annotation
    labels, annotation = load_labels(annotation_path, rna.observation_ids, spec.label_column)
    paths[_relative(annotation_path)] = sha256(annotation_path)
    if paths[_relative(annotation_path)] != checksums[str(annotation_path)]:
        raise ValueError("annotation checksum mismatch")
    return rna, second, labels, annotation, paths


def experiment_id(spec: DatasetSpec, baseline: str, seed: int) -> str:
    return f"EXP-{spec.slug}-{baseline}-KMEANS-S{seed}"


def method_id(baseline: str) -> str:
    return {"RNA": "BASE_RNA", "ADT": "BASE_SECOND", "ATAC": "BASE_SECOND", "CONCAT": "BASE_CONCAT",
            "SPACE": "BASE_SPACE", "PCA": "PCA_CLASSICAL"}[baseline]


def intended_ids() -> list[str]:
    ids = []
    for spec in DATASETS:
        baselines = ["RNA", "PCA", "SPACE"] + ([] if spec.second_modality is None else [spec.second_modality, "CONCAT"])
        for baseline in baselines:
            ids.extend(experiment_id(spec, baseline, seed) for seed in SEEDS)
    if len(ids) != len(set(ids)):
        raise RuntimeError("planned experiment IDs are not unique")
    return ids


def _write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def _registry_rows() -> tuple[list[str], list[dict[str, str]]]:
    with REGISTRY.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


def append_registry(row: dict[str, object]) -> None:
    fields, rows = _registry_rows()
    existing = {item["experiment_id"] for item in rows}
    if row["experiment_id"] in existing:
        raise ValueError(f"experiment ID already registered: {row['experiment_id']}")
    rows.append({field: str(row.get(field, "")) for field in fields})
    _write_csv(REGISTRY, fields, rows)


def append_result(row: dict[str, object]) -> None:
    rows: list[dict[str, str]] = []
    if RESULTS.exists():
        with RESULTS.open(newline="", encoding="utf-8-sig") as stream:
            rows = list(csv.DictReader(stream))
    if any(item["experiment_id"] == row["experiment_id"] for item in rows):
        raise ValueError(f"result ID already recorded: {row['experiment_id']}")
    rows.append({field: str(row.get(field, "")) for field in RESULT_FIELDS})
    _write_csv(RESULTS, RESULT_FIELDS, rows)


def _save_embedding(path: Path, values: np.ndarray) -> None:
    temporary = path.with_suffix(".tmp.npz")
    np.savez_compressed(temporary, embedding=np.asarray(values, dtype=np.float64))
    temporary.replace(path)


def execute_one(spec: DatasetSpec, representation: Representation, observation_ids: list[str], labels: np.ndarray,
                annotation: dict[str, object], input_checksums: dict[str, str], seed: int) -> dict[str, object]:
    identity = experiment_id(spec, representation.baseline, seed)
    output = EXPERIMENT_ROOT / identity
    if output.exists():
        raise FileExistsError(f"immutable experiment directory already exists: {output}")
    output.mkdir(parents=True)
    started = _utc()
    start_clock = time.perf_counter()
    config = {
        "experiment_id": identity,
        "run_type": "SCIENTIFIC_BASELINE_RUN",
        "freeze": "PHASE_3C_CONFIG_FREEZE_2026-09-12",
        "dataset": spec.canonical_id,
        "dataset_registry_id": spec.registry_id,
        "modalities": representation.modalities,
        "baseline": representation.baseline,
        "representation": representation.baseline,
        "seed": {"python": seed, "numpy": seed, "clustering": seed, "representation": 0, "metric_subsample": 0},
        "preprocessing": representation.preprocessing,
        "clustering": {"backend": "KMeans", "cluster_count_source": "reference_annotation_count", "parameters": {"init": "k-means++", "n_init": 20, "max_iter": 300, "tol": 1e-4, "algorithm": "lloyd", "random_state": seed}},
        "metrics": ["ARI", "NMI_arithmetic", "silhouette_euclidean_sample_500_random_state_0"],
        "input_checksums": input_checksums,
        "output_directory": _relative(output),
        "status": "RUNNING",
    }
    (output / "config.yaml").write_text(json.dumps(config, indent=2, sort_keys=True) + "\n")
    write_json_atomic(environment_record(), output / "environment.json")
    _write_csv(output / "identity_map.csv", ["original_observation_id", "method_internal_id"],
               ({"original_observation_id": value, "method_internal_id": value} for value in observation_ids))
    validate_row_mapping(observation_ids, observation_ids)
    embedding_dim = validate_embedding(representation.values, len(observation_ids))
    diagnostics = row_diagnostics(representation.values)
    if not diagnostics["finite"] or diagnostics["collapsed"]:
        raise ValueError("representation failed finite/collapse validation")
    _save_embedding(output / "embedding.npz", representation.values)
    clusters, metrics, cluster_sizes = cluster_and_evaluate(representation.values, labels, seed)
    _write_csv(output / "clusters.csv", ["original_observation_id", "cluster"],
               ({"original_observation_id": value, "cluster": int(cluster)} for value, cluster in zip(observation_ids, clusters, strict=True)))
    write_json_atomic(metrics, output / "metrics.json")
    write_json_atomic(representation.preprocessing, output / "preprocessing.json")
    write_json_atomic(cluster_sizes, output / "cluster_sizes.json")
    runtime = time.perf_counter() - start_clock
    validation = {
        "status": "PASS", "run_type": "SCIENTIFIC_BASELINE_RUN", "expected_observations": len(observation_ids),
        "observed_embedding_rows": int(representation.values.shape[0]), "identity_order_preserved": True,
        "annotation": annotation, "representation_diagnostics": diagnostics, "cluster_sizes": cluster_sizes,
        "empty_clusters": int(metrics["cluster_count"] - len(cluster_sizes)),
        "singleton_clusters": int(sum(value == 1 for value in cluster_sizes.values())),
        "source_checksums_matched_preflight": True,
    }
    write_json_atomic(validation, output / "validation.json")
    finished = _utc()
    config["status"] = "SUCCEEDED"
    (output / "config.yaml").write_text(json.dumps(config, indent=2, sort_keys=True) + "\n")
    provenance = {
        "experiment_id": identity, "timestamp_utc": finished, "started_at": started, "finished_at": finished,
        "dataset": spec.canonical_id, "dataset_registry_id": spec.registry_id, "method": representation.baseline,
        "code_commit": _git_head(), "working_tree_dirty": _git_dirty(), "runner_sha256": sha256(Path(__file__)),
        "environment": environment_record(), "preprocessing": representation.preprocessing,
        "seed": config["seed"], "parameters": {"clustering": config["clustering"], "metrics": config["metrics"]},
        "hardware": {"class": "LOCAL_CPU", "cpu": "Apple M2 8-core", "ram_gib": 16},
        "input_checksums": input_checksums,
        "output_paths": {"embedding": _relative(output / "embedding.npz"), "identity_map": _relative(output / "identity_map.csv"), "clusters": _relative(output / "clusters.csv"), "metrics": _relative(output / "metrics.json"), "validation": _relative(output / "validation.json")},
        "runtime_seconds": runtime,
        "runtime_scope": "clustering_metrics_and_artifact_serialization_after_shared_representation_build",
        "shared_representation_build_timing": "recorded_separately_by_repeatability_validation_not_allocated_to_seed_runs",
        "exit_status": "SUCCEEDED", "run_type": "SCIENTIFIC_BASELINE_RUN",
    }
    write_json_atomic(provenance, output / "provenance.json")
    (output / "stdout.log").write_text(f"{identity} SCIENTIFIC_BASELINE_RUN SUCCEEDED\n")
    (output / "stderr.log").write_text("")
    (output / "STATUS").write_text("SUCCEEDED\n")
    artifact_names = ["config.yaml", "environment.json", "identity_map.csv", "embedding.npz", "clusters.csv", "metrics.json", "preprocessing.json", "cluster_sizes.json", "validation.json", "provenance.json", "stdout.log", "stderr.log", "STATUS"]
    artifacts = [{"path": name, "sha256": sha256(output / name), "bytes": (output / name).stat().st_size} for name in artifact_names]
    write_json_atomic({"experiment_id": identity, "artifacts": artifacts}, output / "saved_artifacts_manifest.json")
    result = {
        "experiment_id": identity, "dataset": spec.canonical_id, "modalities": representation.modalities,
        "baseline": representation.baseline, "representation": representation.baseline,
        "embedding_dim": embedding_dim, "clustering": "KMeans", "cluster_count": metrics["cluster_count"],
        "cluster_count_source": "reference_annotation_count", "seed": seed,
        "ARI": metrics["ARI"]["result"], "NMI": metrics["NMI"]["result"], "silhouette": metrics["silhouette"]["result"],
        "runtime_seconds": runtime, "runtime_scope": "post_representation_clustering_metrics_and_artifact_serialization", "status": "SUCCEEDED",
        "metric_output_location": _relative(output / "metrics.json"), "provenance_location": _relative(output / "provenance.json"),
    }
    registry = {
        "experiment_id": identity, "parent_experiment_id": "", "comparison_group_id": f"P3C-{spec.canonical_id}-{representation.baseline}",
        "question_id": "P3C_INFRASTRUCTURE_VALIDATION", "status": "SUCCEEDED", "dataset_ids": spec.registry_id,
        "dataset_version": "PHASE1D_SHA256_MANIFEST", "preprocessing_version": "PHASE_3C_CONFIG_FREEZE_2026-09-12",
        "split_manifest": "NOT_APPLICABLE_UNSUPERVISED_FULL_DATA", "random_seeds": json.dumps(config["seed"], sort_keys=True),
        "initial_representation_id": method_id(representation.baseline), "representation_method_id": method_id(representation.baseline),
        "model": "transparent_baseline", "code_commit": _git_head(), "hyperparameters_path": _relative(output / "config.yaml"),
        "learned_embedding_path": _relative(output / "embedding.npz"), "downstream_task": "common_KMeans_clustering",
        "evaluation_metrics_path": _relative(output / "metrics.json"), "runtime_seconds": runtime,
        "hardware_software_environment": _relative(output / "environment.json"),
        "saved_artifacts_manifest": _relative(output / "saved_artifacts_manifest.json"),
        "biological_evaluation_path": _relative(output / "metrics.json"), "reproducibility_status": "R3_PROJECT_DATA_BASELINE",
        "run_record_path": _relative(output / "provenance.json"), "started_at": started, "finished_at": finished,
        "notes": "SCIENTIFIC_BASELINE_RUN; K from reference annotation count is privileged; runtime excludes shared representation build; source X semantics and coordinate units remain UNKNOWN",
    }
    append_registry(registry)
    append_result(result)
    return result


def record_failure(identity: str, error: BaseException, category: str, stage: str) -> None:
    write_failure_artifacts(EXPERIMENT_ROOT / identity, identity, error, category, stage, traceback.format_exc())


def run(first_only: bool, remaining: bool) -> list[dict[str, object]]:
    if first_only == remaining:
        raise ValueError("choose exactly one of --first-only or --remaining")
    plans = intended_ids()
    fields, registry_rows = _registry_rows()
    del fields
    registered = {row["experiment_id"] for row in registry_rows}
    if first_only and FIRST_ID in registered:
        raise ValueError(f"first gate already registered: {FIRST_ID}")
    if remaining and FIRST_ID not in registered:
        raise ValueError("first gate has not passed and been registered")
    before = verify_all_sources("before_first_scientific_run" if first_only else "before_remaining_series")
    checksums = expected_checksums()
    results = []
    for spec in DATASETS:
        if first_only and spec.canonical_id != "LN_A1":
            continue
        rna, second, labels, annotation, source_hashes = load_dataset(spec, checksums)
        representations = build_representations(rna, None if first_only else second, None if first_only else spec.second_modality)
        for baseline, representation in representations.items():
            for seed in SEEDS:
                identity = experiment_id(spec, baseline, seed)
                selected = identity == FIRST_ID if first_only else identity != FIRST_ID
                if not selected:
                    continue
                if identity not in plans or identity in registered:
                    raise ValueError(f"invalid or reused experiment ID: {identity}")
                try:
                    result = execute_one(spec, representation, rna.observation_ids, labels, annotation, source_hashes, seed)
                    results.append(result)
                    print(f"SUCCEEDED {identity} ARI={result['ARI']:.6f} NMI={result['NMI']:.6f} silhouette={result['silhouette']:.6f}", flush=True)
                except Exception as error:
                    record_failure(identity, error, "METHOD_OR_EVALUATION_ERROR", "execute_one")
                    raise
        if first_only:
            break
    after = verify_all_sources("after_first_scientific_run" if first_only else "after_remaining_series")
    if not before["all_match"] or not after["all_match"]:
        raise RuntimeError("source preservation verification failed")
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--first-only", action="store_true")
    group.add_argument("--remaining", action="store_true")
    arguments = parser.parse_args()
    results = run(arguments.first_only, arguments.remaining)
    print(f"completed={len(results)}", flush=True)


if __name__ == "__main__":
    main()

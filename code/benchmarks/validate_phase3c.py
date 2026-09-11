"""Validate the completed Phase 3C run matrix and machine-readable artifacts."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

from code.benchmarks.common.h5ad import sha256
from code.benchmarks.common.io import write_json_atomic
from code.benchmarks.run_phase3c import EXPERIMENT_ROOT, FIRST_ID, REGISTRY, RESULTS, intended_ids

ROOT = Path(__file__).resolve().parents[2]


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def main() -> None:
    expected = set(intended_ids())
    results = csv_rows(RESULTS)
    registry = csv_rows(REGISTRY)
    directories = {path.name for path in EXPERIMENT_ROOT.glob("EXP-*") if path.is_dir()}
    result_ids = {row["experiment_id"] for row in results}
    registry_ids = {row["experiment_id"] for row in registry}
    checks: dict[str, object] = {
        "expected_experiment_count": len(expected),
        "results_count": len(results),
        "registry_count": len(registry),
        "directory_count": len(directories),
        "id_sets_equal": expected == result_ids == registry_ids == directories,
        "first_gate_present": FIRST_ID in expected,
        "all_status_succeeded": all(row["status"] == "SUCCEEDED" for row in results + registry),
        "scientific_only_registry": all("SCIENTIFIC_BASELINE_RUN" in row["notes"] for row in registry),
        "complex_methods_absent": not ({"MOFA+", "SCOT", "totalVI", "MultiVI", "SpatialGlue", "Garfield", "SCIGMA", "ARISE"} & {row["model"] for row in registry}),
        "e18_baselines_exact": {row["baseline"] for row in results if row["dataset"] == "MB_E18"} == {"RNA", "PCA", "SPACE"},
        "unique_experiment_ids": len(result_ids) == len(results) and len(registry_ids) == len(registry),
    }
    artifact_errors = []
    json_count = csv_count = embedding_count = 0
    for identity in sorted(expected):
        directory = EXPERIMENT_ROOT / identity
        if (directory / "STATUS").read_text() != "SUCCEEDED\n":
            artifact_errors.append(f"{identity}:STATUS")
        config = json.loads((directory / "config.yaml").read_text())
        if config["experiment_id"] != identity or config["run_type"] != "SCIENTIFIC_BASELINE_RUN":
            artifact_errors.append(f"{identity}:config")
        manifest = json.loads((directory / "saved_artifacts_manifest.json").read_text())
        for artifact in manifest["artifacts"]:
            path = directory / artifact["path"]
            if sha256(path) != artifact["sha256"] or path.stat().st_size != artifact["bytes"]:
                artifact_errors.append(f"{identity}:{artifact['path']}")
        for path in directory.glob("*.json"):
            json.loads(path.read_text())
            json_count += 1
        for path in directory.glob("*.csv"):
            csv_rows(path)
            csv_count += 1
        embedding = np.load(directory / "embedding.npz")["embedding"]
        validation = json.loads((directory / "validation.json").read_text())
        if list(embedding.shape) != validation["representation_diagnostics"]["shape"] or not np.isfinite(embedding).all():
            artifact_errors.append(f"{identity}:embedding")
        identity_rows = csv_rows(directory / "identity_map.csv")
        cluster_rows = csv_rows(directory / "clusters.csv")
        if [row["original_observation_id"] for row in identity_rows] != [row["original_observation_id"] for row in cluster_rows]:
            artifact_errors.append(f"{identity}:identity_order")
        embedding_count += 1
    checks.update({"parsed_json_files": json_count, "parsed_csv_files": csv_count, "validated_embeddings": embedding_count,
                   "artifact_errors": artifact_errors, "artifact_integrity": not artifact_errors})
    for name in ("PHASE_3C_INPUT_PREFLIGHT.json", "PHASE_3C_FIRST_GATE_POSTCHECK.json", "PHASE_3C_SOURCE_POSTCHECK.json"):
        checks[name] = json.loads((EXPERIMENT_ROOT / name).read_text())["all_match"]
    repeatability = json.loads((EXPERIMENT_ROOT / "PHASE_3C_REPEATABILITY.json").read_text())
    checks["repeatability_records"] = len(repeatability["records"])
    checks["repeatability_all_pass"] = repeatability["all_pass"]
    checks["no_failure_artifacts"] = not any(EXPERIMENT_ROOT.glob("EXP-*/failure.json"))
    checks["all_pass"] = all(value is True for key, value in checks.items() if key not in {"expected_experiment_count", "results_count", "registry_count", "directory_count", "parsed_json_files", "parsed_csv_files", "validated_embeddings", "repeatability_records", "artifact_errors"}) and not artifact_errors
    write_json_atomic(checks, EXPERIMENT_ROOT / "PHASE_3C_MACHINE_VALIDATION.json")
    print(json.dumps(checks, indent=2))
    if not checks["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

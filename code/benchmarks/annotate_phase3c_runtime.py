"""Add the accurate runtime scope to Phase 3C artifacts created before it was explicit."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from code.benchmarks.common.h5ad import sha256
from code.benchmarks.common.io import write_json_atomic

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENTS = ROOT / "08_experiments"
SCOPE = "post_representation_clustering_metrics_and_artifact_serialization"


def rewrite_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def main() -> None:
    results_path = EXPERIMENTS / "PHASE_3C_BASELINE_RESULTS.csv"
    with results_path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        rows = list(reader)
        fields = list(reader.fieldnames or [])
    if "runtime_scope" not in fields:
        fields.insert(fields.index("status"), "runtime_scope")
    for row in rows:
        row["runtime_scope"] = SCOPE
        directory = EXPERIMENTS / row["experiment_id"]
        provenance_path = directory / "provenance.json"
        provenance = json.loads(provenance_path.read_text())
        provenance["runtime_scope"] = "clustering_metrics_and_artifact_serialization_after_shared_representation_build"
        provenance["shared_representation_build_timing"] = "recorded_separately_by_repeatability_validation_not_allocated_to_seed_runs"
        write_json_atomic(provenance, provenance_path)
        manifest_path = directory / "saved_artifacts_manifest.json"
        manifest = json.loads(manifest_path.read_text())
        for artifact in manifest["artifacts"]:
            if artifact["path"] == "provenance.json":
                artifact["sha256"] = sha256(provenance_path)
                artifact["bytes"] = provenance_path.stat().st_size
        write_json_atomic(manifest, manifest_path)
    rewrite_csv(results_path, rows, fields)

    registry_path = ROOT / "experiments.csv"
    with registry_path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        registry = list(reader)
        registry_fields = list(reader.fieldnames or [])
    for row in registry:
        if row["experiment_id"].startswith("EXP-") and "runtime excludes shared representation build" not in row["notes"]:
            row["notes"] = row["notes"] + "; runtime excludes shared representation build"
    rewrite_csv(registry_path, registry, registry_fields)
    print(f"annotated_runtime_scope={len(rows)}")


if __name__ == "__main__":
    main()

"""Recompute frozen seed-1729 runs and compare them to saved Phase 3C artifacts."""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path

import numpy as np

from code.benchmarks.common.evaluation import cluster_and_evaluate
from code.benchmarks.common.io import write_json_atomic
from code.benchmarks.run_phase3c import DATASETS, EXPERIMENT_ROOT, ROOT, expected_checksums, experiment_id, load_dataset, verify_all_sources
from code.benchmarks.methods.transparent import build_representations


def main() -> None:
    checksums = expected_checksums()
    records = []
    for spec in DATASETS:
        started = time.perf_counter()
        rna, second, labels, annotation, _ = load_dataset(spec, checksums)
        del annotation
        representations = build_representations(rna, second, spec.second_modality)
        build_seconds = time.perf_counter() - started
        for baseline, representation in representations.items():
            identity = experiment_id(spec, baseline, 1729)
            directory = EXPERIMENT_ROOT / identity
            saved_embedding = np.load(directory / "embedding.npz")["embedding"]
            with (directory / "clusters.csv").open(newline="") as stream:
                saved_clusters = np.asarray([int(row["cluster"]) for row in csv.DictReader(stream)])
            recomputed_clusters, recomputed_metrics, _ = cluster_and_evaluate(representation.values, labels, 1729)
            saved_metrics = json.loads((directory / "metrics.json").read_text())
            metric_differences = {name: abs(recomputed_metrics[name]["result"] - saved_metrics[name]["result"]) for name in ("ARI", "NMI", "silhouette")}
            record = {
                "experiment_id": identity,
                "dataset": spec.canonical_id,
                "baseline": baseline,
                "shared_dataset_representation_build_seconds": build_seconds,
                "embedding_exact_equal": bool(np.array_equal(saved_embedding, representation.values)),
                "embedding_max_absolute_difference": float(np.max(np.abs(saved_embedding - representation.values))),
                "clusters_exact_equal": bool(np.array_equal(saved_clusters, recomputed_clusters)),
                "metric_absolute_differences": metric_differences,
                "pass": bool(np.array_equal(saved_embedding, representation.values) and np.array_equal(saved_clusters, recomputed_clusters) and max(metric_differences.values()) == 0.0),
            }
            records.append(record)
            print(identity, "PASS" if record["pass"] else "FAIL", flush=True)
    source_postcheck = verify_all_sources("repeatability_validation_postcheck")
    report = {
        "validation_type": "REPEATABILITY_VALIDATION_NOT_A_NEW_SCIENTIFIC_EXPERIMENT",
        "seed": 1729,
        "records": records,
        "all_pass": all(record["pass"] for record in records),
        "source_files_unchanged": source_postcheck["all_match"],
        "timing_note": "Shared dataset representation-build timing covers all eligible representations for that dataset and is not allocated to individual seed runs.",
    }
    write_json_atomic(report, EXPERIMENT_ROOT / "PHASE_3C_REPEATABILITY.json")
    if not report["all_pass"] or not report["source_files_unchanged"]:
        raise SystemExit(1)
    print(f"repeatability_records={len(records)} all_pass=true")


if __name__ == "__main__":
    main()

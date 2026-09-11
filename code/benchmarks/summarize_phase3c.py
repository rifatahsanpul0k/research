"""Derive Phase 3C aggregate and QC tables from canonical run artifacts."""

from __future__ import annotations

import csv
import json
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENTS = ROOT / "08_experiments"
RESULTS = EXPERIMENTS / "PHASE_3C_BASELINE_RESULTS.csv"


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    with RESULTS.open(newline="", encoding="utf-8-sig") as stream:
        results = list(csv.DictReader(stream))
    groups: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in results:
        groups[(row["dataset"], row["baseline"], row["modalities"])].append(row)
    aggregates = []
    for (dataset, baseline, modalities), rows in sorted(groups.items()):
        item: dict[str, object] = {
            "dataset": dataset, "baseline": baseline, "modalities": modalities, "runs": len(rows),
            "seeds": ";".join(str(x) for x in sorted(int(row["seed"]) for row in rows)),
            "runtime_scope": ";".join(sorted({row["runtime_scope"] for row in rows})),
        }
        for metric in ("ARI", "NMI", "silhouette", "runtime_seconds"):
            values = [float(row[metric]) for row in rows]
            item[f"{metric}_mean"] = statistics.mean(values)
            item[f"{metric}_sd"] = statistics.stdev(values) if len(values) > 1 else 0.0
        aggregates.append(item)
    aggregate_fields = ["dataset", "baseline", "modalities", "runs", "seeds", "runtime_scope"] + [f"{metric}_{suffix}" for metric in ("ARI", "NMI", "silhouette", "runtime_seconds") for suffix in ("mean", "sd")]
    write_csv(EXPERIMENTS / "PHASE_3C_BASELINE_AGGREGATES.csv", aggregate_fields, aggregates)

    flags = []
    for row in results:
        validation = json.loads((ROOT / row["provenance_location"]).with_name("validation.json").read_text())
        sizes = [int(value) for value in validation["cluster_sizes"].values()]
        observations = int(validation["expected_observations"])
        dominant_fraction = max(sizes) / observations
        labels = []
        if validation["singleton_clusters"]:
            labels.append("SINGLETON_CLUSTER_PRESENT")
        if dominant_fraction >= 0.90:
            labels.append("DOMINANT_CLUSTER_GE_90_PERCENT")
        if validation["representation_diagnostics"]["duplicate_rows"]:
            labels.append("DUPLICATE_REPRESENTATION_ROWS")
        if labels:
            flags.append({
                "experiment_id": row["experiment_id"], "dataset": row["dataset"], "baseline": row["baseline"],
                "cluster_count": row["cluster_count"], "minimum_cluster_size": min(sizes), "maximum_cluster_size": max(sizes),
                "dominant_cluster_fraction": dominant_fraction, "singleton_clusters": validation["singleton_clusters"],
                "flags": ";".join(labels), "disposition": "RETAIN_WITH_CAUTION_NO_TUNING",
            })
    flag_fields = ["experiment_id", "dataset", "baseline", "cluster_count", "minimum_cluster_size", "maximum_cluster_size", "dominant_cluster_fraction", "singleton_clusters", "flags", "disposition"]
    write_csv(EXPERIMENTS / "PHASE_3C_QC_FLAGS.csv", flag_fields, flags)

    flagged_groups = {(row["dataset"], row["baseline"]) for row in flags}
    result_groups = {(row["dataset"], row["baseline"]): sum(1 for item in results if item["dataset"] == row["dataset"] and item["baseline"] == row["baseline"]) for row in results}
    datasets = ["LN_A1", "LN_D1", "MB_E11", "MB_E13", "MB_E15", "MB_E18"]
    status_rows = []
    for baseline in ("RNA", "ADT", "ATAC", "CONCAT", "PCA", "SPACE"):
        row = {"baseline": baseline}
        for dataset in datasets:
            count = result_groups.get((dataset, baseline), 0)
            if count:
                suffix = "_WITH_QC_FLAGS" if (dataset, baseline) in flagged_groups else ""
                row[dataset] = f"SUCCEEDED_{count}_OF_3{suffix}"
            elif dataset == "MB_E18" and baseline in {"ATAC", "CONCAT"}:
                row[dataset] = "NOT_APPLICABLE_E18_ATAC_UNVERIFIED"
            elif baseline == "ADT":
                row[dataset] = "NOT_APPLICABLE_NO_ADT"
            elif baseline == "ATAC":
                row[dataset] = "NOT_APPLICABLE_NO_ATAC"
            else:
                row[dataset] = "NOT_APPLICABLE"
        status_rows.append(row)
    status_fields = ["baseline", "LN_A1", "LN_D1", "MB_E11", "MB_E13", "MB_E15", "MB_E18"]
    write_csv(EXPERIMENTS / "PHASE_3C_DATASET_BASELINE_STATUS.csv", status_fields, status_rows)
    print(f"aggregates={len(aggregates)} qc_flagged_runs={len(flags)} status_rows={len(status_rows)}")


if __name__ == "__main__":
    main()

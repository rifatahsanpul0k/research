"""Paired candidate-versus-reference summary; no automatic model promotion."""

import argparse
import json
from pathlib import Path

import pandas as pd


def compare(reference, candidate):
    reference, candidate = Path(reference), Path(candidate)
    configs = []
    tables = []
    for directory in (reference, candidate):
        status = json.loads((directory / "status.json").read_text())
        if status["status"] != "COMPLETED":
            raise ValueError(f"Incomplete run: {directory}")
        configs.append(json.loads((directory / "resolved_config.json").read_text()))
        table = pd.read_csv(directory / "metrics.csv")
        tables.append(table.loc[table.method == "ASTRA"].set_index(["dataset", "seed"]))
    if set(configs[0]["seeds"]) != set(configs[1]["seeds"]):
        raise ValueError("Comparisons require identical seed sets")
    specs = [{spec["name"]: spec for spec in c["datasets"]} for c in configs]
    if specs[0].keys() != specs[1].keys():
        raise ValueError("Comparisons require identical dataset sets")
    for name in specs[0]:
        a, b = specs[0][name], specs[1][name]
        for key in ("n_clusters", "preprocess", "excluded_labels", "annotation_column"):
            if a.get(key) != b.get(key):
                raise ValueError(f"Incomparable {name}: {key} differs")
        for key in ("pretrain_epochs", "finetune_epochs", "evaluate_every", "silhouette_sample_size"):
            if a["model_resolved"][key] != b["model_resolved"][key]:
                raise ValueError(f"Different training/selection budgets for {name}: {key}")
        for filename in ("inputs.json", "preprocessing.json"):
            first = json.loads((reference / name / filename).read_text())
            second = json.loads((candidate / name / filename).read_text())
            first.pop("paths", None)
            second.pop("paths", None)
            if first != second:
                raise ValueError(f"Different source or preprocessing for {name}: {filename}")
    expected = {(name, seed) for name in specs[0] for seed in configs[0]["seeds"]}
    for table in tables:
        if not table.index.is_unique or set(table.index) != expected:
            raise ValueError("Missing or duplicated dataset-seed results")
    columns = ["ari", "nmi", "ami", "silhouette", "max_cluster_fraction"]
    joined = tables[0][columns].join(tables[1][columns], lsuffix="_reference", rsuffix="_candidate")
    for metric in columns:
        joined[f"delta_{metric}"] = joined[f"{metric}_candidate"] - joined[f"{metric}_reference"]
    deltas = [f"delta_{metric}" for metric in columns]
    summary = joined.groupby(level="dataset")[deltas].agg(["mean", "std", "count"])
    return joined, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    joined, summary = compare(args.reference, args.candidate)
    args.output.mkdir(parents=True, exist_ok=False)
    joined.to_csv(args.output / "paired_deltas.csv")
    summary.to_csv(args.output / "summary.csv")
    print(summary.to_string())
    print("Deltas are candidate minus reference. Seed variability is not biological replication.")


if __name__ == "__main__":
    main()

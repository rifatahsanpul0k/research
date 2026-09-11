# Canonical input contracts

DatasetInput contains dataset_id, modality, matrix_path, observation_ids, feature_ids, counts_or_processed, optional coordinates, labels and metadata. Each path must be read-only or derived, and each axis must have an explicit sidecar.

The implementation in code/benchmarks/common/config.py validates canonical dataset IDs and required identity fields. Method adapters may extend the contract but cannot omit provenance.

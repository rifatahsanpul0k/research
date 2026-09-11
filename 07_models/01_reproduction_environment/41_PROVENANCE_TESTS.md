# Provenance tests

A reproducible run must answer: which raw file, preprocessing, code commit, parameters, seed, compute classification and environment? The v2 validator rejects any missing field and prevents an `UNRESOLVED` run from entering `RUNNING` or `SUCCEEDED`. Checksums are recomputed without modifying inputs.

For Colab, validation also requires runtime type, Python/package versions, GPU model and CUDA version fields, using `NOT_APPLICABLE` where appropriate rather than inferred values.

Output rows must preserve observation mapping, and each metric must link to the embedding/config used.

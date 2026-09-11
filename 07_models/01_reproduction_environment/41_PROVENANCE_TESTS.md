# Provenance tests

A reproducible run must answer: which raw file, preprocessing, code commit, parameters, seed and environment? The validator rejects any missing field. Checksums are recomputed without modifying inputs.

Output rows must preserve observation mapping, and each metric must link to the embedding/config used.

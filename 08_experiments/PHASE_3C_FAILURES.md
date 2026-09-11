# Phase 3C failures and diagnostic flags

No scientific run ended in `FAILED`, `INVALID` or `BLOCKED`: all 84 eligible configurations reached `SUCCEEDED`, and no experiment directory contains `failure.json`.

Failure-path infrastructure was tested with a temporary synthetic directory. It preserves `failure.json`, `stderr.log`, `stdout.log` and `STATUS` with the declared failure category and stage.

Twenty-seven successful runs received post-run cluster-size flags in [PHASE_3C_QC_FLAGS.csv](PHASE_3C_QC_FLAGS.csv). These are retained scientific outputs, not erased failures. A singleton cluster or dominant cluster can reveal an unstable or outlier-driven partition without proving that a rare biological group is invalid. The E11/E13 ATAC flags are especially material because a dominant cluster contains at least 90% of observations.

The original run records omitted an explicit label for runtime scope. This metadata issue was corrected without changing embeddings, clusters, metrics or configurations: per-run runtime covers clustering, metrics and serialization after shared representation construction. The artifact manifests were refreshed for the changed provenance files, and the correction is recorded in `RESEARCH_LOG.md`.

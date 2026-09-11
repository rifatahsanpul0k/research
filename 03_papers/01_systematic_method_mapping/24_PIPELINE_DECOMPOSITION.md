# Pipeline decomposition

Phase 3A · 2026-09-12 · proposed design; no local performance results.

Use Input → P (preprocessing) → R (initial representation/structure) → M (learned model) → Z (learned representation) → C (clustering/task). Save every intermediate artifact and parameter. Graph construction belongs in R, while a GNN belongs in M. This decomposition supports ablations and separates representation from downstream clustering.

## Evidence class and boundary

**FACT:** project dimensions, availability and source identities are taken from the targeted registries and source ledger. **INTERPRETATION:** compatibility and planning statements apply the recorded input contracts. **PROPOSED:** benchmark policies are prospective and have not been executed. No model was trained, no benchmark was run, and no novelty claim is made.

See [SOURCES.md](SOURCES.md), [METHOD_DATASET_MATRIX.csv](METHOD_DATASET_MATRIX.csv), [METHOD_PIPELINES.csv](METHOD_PIPELINES.csv), and [BENCHMARK_SHORTLIST.csv](BENCHMARK_SHORTLIST.csv).

# Feature compatibility

Phase 3A · 2026-09-12 · proposed design; no local performance results.

RNA methods usually require consistent gene identifiers; ADT requires antibody/epitope identities; ATAC requires peak coordinates or a documented gene-activity/regulatory mapping. Mouse stage peak sets have low direct overlap, so column-wise concatenation is invalid. Options for later design are union-coordinate peak space, coordinate overlap, gene-activity matrices, regulatory feature mappings, or latent alignment without identical peaks; each changes information and assumptions and none is executed here.

## Evidence class and boundary

**FACT:** project dimensions, availability and source identities are taken from the targeted registries and source ledger. **INTERPRETATION:** compatibility and planning statements apply the recorded input contracts. **PROPOSED:** benchmark policies are prospective and have not been executed. No model was trained, no benchmark was run, and no novelty claim is made.

See [SOURCES.md](SOURCES.md), [METHOD_DATASET_MATRIX.csv](METHOD_DATASET_MATRIX.csv), [METHOD_PIPELINES.csv](METHOD_PIPELINES.csv), and [BENCHMARK_SHORTLIST.csv](BENCHMARK_SHORTLIST.csv).

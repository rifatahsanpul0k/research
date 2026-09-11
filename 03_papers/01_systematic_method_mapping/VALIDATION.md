# Phase 3A validation

## Checks

- Required Phase 3A Markdown and four planning CSV artifacts are present: METHOD_DATASET_MATRIX.csv, METHOD_PIPELINES.csv, BENCHMARK_SHORTLIST.csv and EVALUATION_MATRIX.csv.
- METHOD_DATASET_MATRIX.csv contains A1, D1, E11, E13, E15 and E18 columns with per-cell reasons and decomposed modality/pairing/feature/spatial/label/representation fields.
- METHOD_PIPELINES.csv separates preprocessing, initial/structural representation, learned model, objective, latent output and clustering backend.
- BENCHMARK_SHORTLIST.csv contains Core, Extended and Reference only planning tiers; tiers are not performance rankings.
- E18 local ATAC unavailability remains explicit; no cross-stage peak harmonization was performed.
- Method-native preprocessing, graph construction, clustering backend, biological versus computational evaluation, seed and hyperparameter policies are documented.
- Recent Garfield, SCIGMA and ARISE provenance is recorded with UNKNOWN/qualified fields where direct verification is incomplete.
- Literature numbers, where present, are labeled LITERATURE_REPORTED; no project RESULT exists.
- No experiments, model training, benchmark execution, novelty analysis or representation taxonomy expansion occurred.
- The core shortlist includes non-graph controls, classical/factor methods, generative methods, transport/alignment, graph methods and newer learned methods; tiers are planning categories, not scores.

## Final checks

CSV parsing, unique identifiers, source anchors and `git diff --check` are required before phase completion. Repomix and code-only Graphify are refreshed at completion and reported in RESEARCH_LOG.md. Changes remain local and uncommitted.

Final refresh: Repomix exited 0 with 451 files and 468,770 tokens and no suspicious files. Graphify `--code-only` exited 0 with 44 nodes, 67 edges and 7 communities (16 re-extracted, 23 cached). These are repository-context snapshots, not biological or benchmark results.

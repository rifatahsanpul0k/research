# Phase 2A validation — 2026-09-11

**Current status (governance audit, 2026-09-11):** the operating-rules file now exists and Phase 2A has been reviewed against it. See [OPERATING_RULES_AUDIT.md](OPERATING_RULES_AUDIT.md) for targeted source/notation corrections, final checks and the compliance decision. The original 40-file validation and execution counts below are historical snapshots; the audit is the additional 41st phase document.

## Scope and progression

All 36 ordered topics in the Phase 2A brief are covered. The chain is: measured tables and axis identity → vectors → geometry/probability → distance/dependence → linear algebra → dimension/compression → latent coordinates → optimization → evaluation. Multimodal pairing, unequal feature counts, missingness and biological interpretation qualify this chain throughout.

The required directory contains 36 numbered topic notes plus CONCEPT_MAP.md, TOY_CALCULATIONS.md, SOURCES.md and this file: 40 Markdown artifacts. The exact filename inventory is checked against section 37 of the supplied brief. The [concept map](CONCEPT_MAP.md) defines shared notation; [toy calculations](TOY_CALCULATIONS.md) give intermediate steps rather than final answers alone.

## Conceptual review

| Required check | Review result and location |
|---|---|
| Symbols defined | Shared glossary plus local definitions cover indices, operators, distributions, maps and scores. Reused letters are disambiguated. The norm exponent differs from feature count; sample covariance differs from the SVD diagonal. |
| Matrix dimensions | Topics 01–02, 06, 12, 15–16 and 27–30 state dimensions. Column vectors represent individual rows through transposition; all-observation affine maps use X times W-transpose. Kernel entries are scalars, distinct from their n-by-n matrix. |
| Distance versus similarity | Topics 03–05 distinguish metrics, squared loss, cosine and centered correlation, including zero-vector/constant-profile edge cases. Addition preserves coordinate count, not norm. |
| Correlation versus causation | Topic 07 supplies a dependent but uncorrelated example and links Phase 1B evidence requirements. Observation-profile correlation differs from feature correlation across observations. |
| Probability and uncertainty | Topics 08–11 distinguish probability mass, density, likelihood, posterior, mean and mode. Distribution assumptions are stated rather than assigned to an assay from integer-looking values. |
| Linear algebra consistency | Rank bounds are bounds, not empirical rank estimates. Full/thin/compact SVD shapes are distinct. Uncentered singular-value energy is not automatically explained centered variance. Eigenvectors and latent axes can be nonunique. |
| Optimization | Topics 17–20 distinguish argmin from minimum, affine from linear, local from global, and L1 zeros from L2 shrinkage. The toy learning-rate convergence bound is not a research recommendation. |
| High-dimensional geometry | Topics 21–22 state distributional assumptions for distance concentration and random orthogonality; large p alone is not a universal impossibility result. |
| Local/global and neighborhoods | Topics 23–24 use hand-defined point sets. Metric, preprocessing, ties and eligibility determine neighbor membership. No scientific graph is constructed. |
| Multimodal imbalance | Topic 29 uses verified A1 RNA/ADT dimensions, shows concatenated shape, and separates feature-count imbalance from scale-dependent numerical dominance. Pairing is required before shared-row notation. |
| Missingness versus zero | Topic 30 uses an explicit mask and demonstrates observed mean 1 versus zero-filled mean 2/3. Missing E18 ATAC is not treated as a biological zero. |
| Latent variables versus measurement | Topics 27–28 distinguish functions and inferred variables from measured features; an invertible change of latent coordinates can preserve reconstruction. |
| Testing and evaluation | Topics 31–36 distinguish p-values, confidence intervals, effects and FDR. Labels, geometry and sampling assumptions have separate roles. |
| ARI/NMI/silhouette limits | Topics 33–35 derive pair counts, entropy normalization and nearest-other-cluster mean distances. Degenerate cases and chance-model/normalization conventions are explicit. |
| Biological evaluation | Topic 36 and the taxonomy retain the permanent computational + statistical + biological principle. Numeric compactness and annotation agreement alone do not establish biological populations. |

This was a mathematical/content review, not an automated proof that every explanation is exhaustive or that a learner has mastered it.

## Synthetic arithmetic

Run from the repository root:

~~~bash
python3 code/data_inspection/check_phase2a_toys.py
~~~

The checker passed **59 checks** using fixed synthetic arrays, probabilities and partitions only. It verifies mean, sample/population variance, covariance, distance, cosine/Pearson, standardization, matrix multiplication, explicit eigen/SVD factors, truncation, gradients, kernels, information quantities, pair-based ARI, NMI and silhouette, along with selected edge cases and elementary probability/testing examples. The scalar regularization examples were checked by direct substitution during the content review.

The calculations document shows centered products, pair distances, all six partition pairs, entropy terms and each silhouette component. Selected reproducible results: feature correlation 0.9764801654; crossed-partition ARI −0.5; partial-partition ARI 0 and arithmetic NMI 0.3437110185; mean silhouette 0.8357031736. Comparing the same partial partition illustrates that ARI and NMI answer different mathematical questions.

The script checks arithmetic and some independently calculated identities. It does not establish biological validity, benchmark an implementation, fit a model, choose a representation or process a biological matrix.

## Evidence and provenance

[SOURCES.md](SOURCES.md) records 13 newly registered references actually used and two reused biological/statistical sources. Author-hosted books, foundational publications and official documentation support the notes. Full-text, landing-page and abstract-only access are explicitly distinguished. No irrelevant paper cards or inaccessible-full-text reading claims were created.

Actual dimensions are cited to the prior Phase 1E reports, read without reopening the raw assays. A1/D1 rows remain spots; mouse rows remain spatial capture locations with unresolved physical units. E18 ATAC remains unavailable. Shape-derived ratios, covariance storage sizes and rank bounds are calculations on documented dimensions, not new dataset analyses.

## Integrity and context protocol

At phase start, Repomix completed with 236 files, 253,966 tokens and no suspicious files. Its packed project context was read for project scope, prior data statistics, biological interpretation and taxonomy conventions. Initial Graphify code-only completed with 31 nodes, 47 edges and five communities. It analyzed repository structure, including supported JSON inputs; these are not biological nodes or relationships.

Final exact-inventory, local-link, registry, preservation and whitespace checks, followed by the requested Repomix/Graphify refresh, are recorded in the final execution record below.

## Open questions and readiness

- Resolved by this audit: ASTRA_OPERATING_RULES.md now exists and compliance is recorded in OPERATING_RULES_AUDIT.md.
- Later study must examine observation-model adequacy, identifiability constraints and uncertainty for particular representation families.
- Numerical rank tolerance, conditioning and finite-precision behavior need deeper treatment before implementation.
- Biological replication and held-out units require unresolved donor/embryo/section metadata; mathematical row counts do not resolve them.
- Continuous information estimation, dependence assumptions for testing, feature harmonization and missingness mechanisms need method-specific review later.
- Choosing which weak or rare signals to preserve requires a biological question and independent evidence.

The mathematical prerequisites are prepared for a subsequent Phase 2B review; this does not certify human mastery. The previously missing governance instructions are resolved by the operating-rules audit. Phase 2B remains unstarted. No research training, benchmarking, imputation, scientific graph construction, representation ranking or novelty analysis occurred. Changes remain local and uncommitted.

## Final execution record

- **Inventory and notation:** Exact 40-file match against the supplied brief; balanced mathematical delimiters/environments and no unexpected control characters. Symbol meaning and dimensional compatibility were reviewed separately as described above.
- **Links:** All 80 local Markdown links/anchors in the 40 documents resolve.
- **Registries:** All six CSV registries parse with consistent columns and unique row IDs. Papers: 124 rows/15 columns; methods: 29/12; datasets: 6/31; codebases: 0/16; representations: 0/12; experiments: 0/27. Known paper DOIs are unique; all 13 new references have populated fields and existing extraction paths; all 17 new methods resolve their paper IDs and record paths.
- **Preservation:** datasets.csv, experiments.csv, representations.csv and codebases.csv match HEAD byte-for-byte. The changed-file review contains no prior biology/omics report edits or raw-data files. Existing Graphify structural/cache artifacts were refreshed.
- **Arithmetic:** The fixed-input checker exited 0 with all 59 checks passed.
- **Whitespace:** git diff --check passed.
- **Final Repomix:** repomix . --compress exited 0; 277 files, 287,403 tokens; no suspicious files detected. This is an execution snapshot before appending these final status lines and before the following Graphify refresh.
- **Final Graphify:** graphify . --code-only exited 0; 17 re-extracted inputs, 21 cached/unchanged; 41 nodes, 65 edges, six communities. It skipped 225 non-code files and 20 unclassified files. Some supported inputs are JSON; the tool's code-input count is not a count of Python programs. No scientific observation graph was constructed.
- **Historical stopping status:** Explicit Phase 2A mathematical deliverables and checks were finished while missing-rule review remained pending. That pending item is now superseded by OPERATING_RULES_AUDIT.md. Phase 2B is unstarted; changes are local/uncommitted.

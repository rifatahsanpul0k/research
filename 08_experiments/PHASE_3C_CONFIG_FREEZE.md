# Phase 3C configuration freeze

Frozen before scientific results were generated on 2026-09-12. Changes after execution require a new experiment series and IDs. Phase 3C evaluates infrastructure and transparent reference points; it does not tune or rank representations.

## Eligible matrix

| Baseline | A1 | D1 | E11 | E13 | E15 | E18 |
|---|---|---|---|---|---|---|
| RNA-only | PLANNED | PLANNED | PLANNED | PLANNED | PLANNED | PLANNED |
| ADT-only | PLANNED | PLANNED | NOT_APPLICABLE_NO_ADT | NOT_APPLICABLE_NO_ADT | NOT_APPLICABLE_NO_ADT | NOT_APPLICABLE_NO_ADT |
| ATAC-only | NOT_APPLICABLE_NO_ATAC | NOT_APPLICABLE_NO_ATAC | PLANNED | PLANNED | PLANNED | NOT_APPLICABLE_E18_ATAC_UNVERIFIED |
| simple concatenation | PLANNED_RNA_ADT | PLANNED_RNA_ADT | PLANNED_RNA_ATAC | PLANNED_RNA_ATAC | PLANNED_RNA_ATAC | NOT_APPLICABLE_E18_ATAC_UNVERIFIED |
| RNA PCA | PLANNED | PLANNED | PLANNED | PLANNED | PLANNED | PLANNED |
| coordinates-only | PLANNED | PLANNED | PLANNED | PLANNED | PLANNED | PLANNED |

All experiments are within-dataset. No mouse stage is pooled or used to define another stage's features.

## Frozen inputs and labels

- Canonical datasets map to the existing source folders: `LN_A1`, `LN_D1`, `MB_E11`, `MB_E13`, `MB_E15`, `MB_E18`.
- H5AD `X` is used as the source-provided processed matrix. Its count/fragment and prior-processing semantics remain `UNKNOWN`; it is not called raw UMI or raw fragment data.
- No row is filtered. Observation IDs come from the H5AD observation index and must be unique. Paired views must have identical ordered IDs.
- Annotation CSVs are joined by barcode, never by row position. `manual-anno` is used for lymph node and `cluster` for mouse brain.
- Labels are excluded from preprocessing and representation fitting. The only label-derived fit input is `K`, recorded as `cluster_count_source = reference_annotation_count`.
- Coordinates come from `obsm/spatial`; units remain `UNKNOWN`. No conversion to physical distance is made.
- Every complete source file must match the SHA-256 value in the Phase 1D download manifest before the first run and after the series.

## Frozen preprocessing and representations

All floating-point calculations use `float64` unless a library routine documents an internal choice.

### RNA-only (`BASE_RNA`)

1. Require finite, nonnegative source `X`.
2. Apply `log1p` directly to source `X`; do not library-size normalize because source count semantics are unresolved.
3. Compute population variance for every feature across all observations without labels.
4. Select the 2,000 largest-variance features, or all features if fewer exist; break ties by original feature position.
5. Center and divide each selected feature by its population standard deviation; constant features become zero.

The saved representation is the resulting `n × min(2000,p)` matrix. Feature IDs and selection positions are saved.

### ADT-only (`BASE_SECOND` for Suite L)

For each observation with vector `x`, calculate

\[
g=\exp\left(\frac{1}{p}\sum_{j=1}^{p}\log(1+x_j)\right),\qquad
y_j=\log\left(1+\frac{x_j}{g}\right).
\]

Then z-score each ADT feature with population standard deviation; constants become zero. This is the exact Phase 3C CLR convention. It is a mathematical transform of source `X`, not a claim about molecule counts.

### ATAC-only (`BASE_SECOND` for Suite B)

For sparse nonnegative source matrix `X`, let row sum be `r_i`, document frequency be `df_j`, and `n` be observations:

\[
TF_{ij}=X_{ij}/r_i,\qquad IDF_j=\log\left(1+\frac{n}{1+df_j}\right),\qquad T=TF\,IDF.
\]

Zero-sum rows remain zero. Apply scikit-learn randomized `TruncatedSVD` with 31 components, `random_state=0`, `n_iter=7`, and default tolerance. Drop component 1 and z-score the remaining 30 component columns. No peak harmonization occurs.

### Simple concatenation (`BASE_CONCAT`)

Concatenate the frozen RNA-only block with the applicable frozen ADT-only or ATAC-only block. Both blocks are already column-standardized. Scale each block by

\[
\frac{\sqrt n}{\sqrt 2\lVert Z_{block}\rVert_F}
\]

so each nonzero block contributes mean squared row norm `1/2`, then concatenate. There is no learned weighting.

### RNA PCA (`PCA_CLASSICAL`)

Apply scikit-learn PCA to the frozen RNA-only representation with 30 components, `svd_solver=randomized`, `random_state=0`, `n_oversamples=10`, `iterated_power=4`, `power_iteration_normalizer=QR`, `whiten=false`, and explicit centering performed by PCA. No additional scaling occurs.

### Coordinates-only (`BASE_SPACE`)

Center each of the two coordinate columns and divide by its population standard deviation; a constant coordinate becomes zero. The saved representation is `n × 2`. Coordinate units remain `UNKNOWN`.

## Frozen clustering, seeds and metrics

- Common clustering: `sklearn.cluster.KMeans(init="k-means++", n_init=20, max_iter=300, tol=1e-4, algorithm="lloyd")`.
- Three predeclared seeds: `1729`, `2718`, `31415`. Each seed is a separate immutable experiment ID.
- Cluster count: number of nonmissing reference annotation categories for that dataset. This privileged choice is disclosed in every artifact.
- Metrics: adjusted Rand index using `sklearn.metrics.adjusted_rand_score`; normalized mutual information using `average_method="arithmetic"`; Euclidean silhouette using `sample_size=min(500,n)` and fixed metric-subsample `random_state=0`.
- Runtime is wall-clock seconds on the recorded local host and supports engineering diagnosis only.
- CPU thread controls are fixed to one for OpenMP, OpenBLAS, MKL and Accelerate/vecLib; joblib logical CPU discovery is fixed to eight. These values are captured in `environment.json`.
- No UMAP, t-SNE, MClust, Leiden, graph construction, supervised feature selection or label-based parameter search is permitted in this series.

Experiment IDs follow `EXP-{DATASET}-{BASELINE}-KMEANS-S{SEED}`. The first required gate is `EXP-LN-A1-PCA-KMEANS-S1729`. The full matrix may proceed only after that directory, its identity mapping, metrics, provenance, validation, registry row and source-preservation checks pass.

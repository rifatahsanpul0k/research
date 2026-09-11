# Distributional properties

The read-only report records shape, CSR/dense encoding, dtype, stored-value extrema, logical zero fraction, total value sum, row-total min/median/mean/variance, and detected-feature min/median/mean/variance. Row totals are assay-specific: RNA may be molecule-like counts, ATAC peak counts may be fragment-like, and ADT values are antibody-tag signal. No unverified conversion is made.

All 11 available matrices are CSR float32 in X. Matrix dimensions and distributions are in `DATASET_STATISTICS.md` and machine-readable `matrix_statistics.json`. The report includes explicit zeros separately and does not densify. Means and variances are descriptive population moments of row summaries; they are not inferential estimates. Distribution comparison across tissues or stages is confounded by assay, feature set and capture depth. Evidence: AnnData [S22], 10x HDF5 format [S20], source studies [S27,S29].

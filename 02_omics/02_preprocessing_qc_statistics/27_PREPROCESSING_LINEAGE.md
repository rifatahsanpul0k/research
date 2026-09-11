# Preprocessing lineage

Every future transformation should be recorded as: **input** (file, matrix key, checksum, feature/observation IDs) → **operation** (formula/tool/version) → **parameters** (cutoffs, pseudocount, target, reference set) → **output** (file, shape, dtype, sparsity, checksum) → **rationale** (biological/statistical reason) → **losses/risks** (zeros, rare features, scale, confounding).

For this phase the lineage is intentionally observational: source H5AD X was opened read-only; CSR arrays were summarized; no values, rows or columns were changed. `matrix_statistics.json`, alignment JSONs and annotation summaries are derived outputs, not replacement matrices. A lineage entry must distinguish a software default from a biological rationale and a study-specific decision. This makes future representation comparisons auditable. Evidence: AnnData format [S22], 10x matrix documentation [S20], Luecken & Theis [S16].

# 18. QC foundations

QC asks whether an observation and its library are interpretable for the intended assay. RNA descriptors include total assigned counts, detected genes, mitochondrial fraction, low complexity, unusually high counts, and doublet indicators. ATAC descriptors include fragments, TSS enrichment, nucleosome-associated fragment patterns, and fraction in peaks. ADT descriptors include total counts, detected markers, background, and outliers [S09][S16].

These metrics are summaries of measurement quality, not cell identity. High mitochondrial RNA can indicate damage but can also be biological; high counts can indicate a large/active cell or a multiplet. Thresholds depend on tissue, chemistry, depth, and study design. There is no universal cutoff [S16].

QC decisions alter rows, columns, and missingness. Retain raw files and record metric definitions, thresholds, exclusions, and reasons in metadata. This phase does not choose thresholds or run filtering.

**Evidence:** [S09], [S16], [S18].

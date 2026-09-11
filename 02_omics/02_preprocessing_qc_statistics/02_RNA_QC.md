# RNA quality-control quantities

### A–C. Meaning, mechanism, relationships

For an RNA feature matrix (X), library size (L_i=\sum_jX_{ij}) is the total stored signal for observation (i); detected features (G_i=\sum_j1(X_{ij}>0)) is the number of genes with positive stored value. In UMI workflows these can approximate captured molecules and genes, but only when the source semantics document that interpretation [S01,S03,S04]. They measure depth and breadth together with biology: a large cell, an active state, a damaged cell, or a technical depth difference can each alter them. They are inputs to QC and normalization, not cell-type labels.

### D–F. Measurement, numerical form, project relevance

Compute row sums and positive-value counts from CSR row segments without densifying. For C1=(8,0,3), (L_1=11,G_1=2); for C2, (L_2=9,G_2=3). Plot or tabulate distributions by sample and stage before any cutoff. RNA QC matters in single-cell data because capture depth varies; in spatial data a spot footprint and tissue content affect both quantities; in multi-omics, RNA depth is one modality-specific covariate and cannot define ATAC or ADT quality. Similar (L,G) values do not establish equivalent biology.

### G. Misconceptions; H. Evidence

There is no universal minimum (L_i) or (G_i): chemistry, nuclei, tissue, sequencing depth and study design matter. High depth can be a doublet; low depth can be a rare, real cell. Our report uses distributions only and applies no filter. Evidence: Zheng et al. [S01], UMI-tools [S04], Luecken & Theis [S16], and the source-specific QC fields in `04_datasets/*/QC_NOTES.md`.

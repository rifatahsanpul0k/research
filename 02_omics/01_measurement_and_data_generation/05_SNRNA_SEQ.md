# 5. Single-nucleus RNA-seq

snRNA-seq uses isolated nuclei rather than intact cells. Nuclear RNA includes unspliced pre-mRNA and has a composition different from cytoplasmic RNA; therefore intronic reads can be informative and gene detection profiles differ from scRNA-seq [S05].

Preparation removes cytoplasm and can be useful for frozen or difficult tissue, while nuclei isolation can damage or lose nuclear material and changes the sampled compartment. The same representation (X\in\mathbb N_0^{n\times p}) does not imply the same biological quantity: a row is a nucleus-derived library, not a whole-cell transcriptome.

For spatial and developmental tissue, dissociation/nuclei preparation can alter representation of fragile cell types and RNA classes. Do not infer scRNA versus snRNA from an `adata_RNA.h5ad` filename; use protocol and metadata.

**Evidence:** [S05], [S16].

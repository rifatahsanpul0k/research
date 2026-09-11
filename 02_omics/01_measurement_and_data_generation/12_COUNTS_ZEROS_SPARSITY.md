# 12. Counts, zeros, and sparsity

For a matrix (X\in\mathbb R^{n\times p}), numerical sparsity is (\#\{X_{ij}=0\}/(np)). Sparse storage records nonzero entries and their indices; it does not explain why omitted values are zero.

RNA zeros can reflect sampling, capture, degradation, ambient context, or true low expression. ADT zeros can reflect absent/low epitope, affinity, background subtraction, or panel sensitivity. ATAC zeros can reflect inaccessible chromatin, limited fragments, peak construction, or cell-specific sampling. Thresholding and filtering add further zeros [S07][S15][S16].

Equal zero fractions across modalities do not imply equal biology. A zero in a 31-marker ADT panel and a zero in a 117,473-region ATAC matrix have different feature and sampling meanings. Do not call every zero dropout, absence, or evidence for a separate cell state.

**Evidence:** [S07], [S09], [S15], [S16].

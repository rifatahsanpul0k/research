# LSI foundations

Latent semantic indexing (LSI) in scATAC workflows applies TF-IDF to a peak matrix and then a truncated singular-value decomposition (SVD), (A\approx U_k\Sigma_kV_k^T). Rows can be summarized by coordinates in the retained left-singular space. SVD is a linear algebra operation on the chosen matrix; it is not a biological regulatory model and does not establish peak-to-gene causality [S44,S45].

Changing peak filtering, TF-IDF formula, centering, number of components or whether the first depth-associated component is retained changes the result. Sparse-safe implementations are essential. We record LSI as a conceptual lineage (peak counts → TF-IDF → SVD) and do not run it, compare it, or use it for representation ranking. In spatial multi-omics, coordinate geometry and modality pairing remain separate from the LSI algebra. Evidence: Cusanovich et al. [S44] and Stuart et al. [S45].

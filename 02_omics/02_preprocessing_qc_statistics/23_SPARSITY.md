# Sparsity

For an (n\times p) matrix, logical sparsity is (s=1-\text{nnz}/(np)), where nnz counts entries whose stored value is nonzero. CSR `data` can contain explicit zeros, so stored-entry count and logical nnz must be distinguished. The utility `summarize_matrices.py` counts nonzero values from CSR arrays without densifying and checks the input SHA-256 before and after.

Verified source-matrix sparsities are: A1 RNA 0.891689, A1 ADT 0.023425, D1 RNA 0.939010, D1 ADT 0.020840; E11 RNA 0.925207/ATAC 0.935089; E13 RNA 0.910601/ATAC 0.942814; E15 RNA 0.894722/ATAC 0.917140; E18 RNA 0.934338. E18 ATAC is unavailable. Sparsity is a property of a matrix and representation, not proof of dropout or absence. Centering can destroy sparse storage; binary conversion can increase logical sparsity. Evidence: AnnData/10x formats [S20,S22], Svensson [S15].

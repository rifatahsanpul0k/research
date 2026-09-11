# ATAC feature representations

After peak definition, ATAC data are commonly represented as an (n\times p) observation-by-peak matrix (X). A binary matrix is (B_{ij}=1(X_{ij}>0)); it records detection and discards multiplicity. A count matrix preserves fragment/cut-site counts when those semantics are documented. Both remain sparse and require peak identifiers with genome build and coordinates [S08,S09,S20].

For row (2,0,1), binary conversion gives (1,0,1), while row total changes from 3 to 2. TF-IDF further rescales counts using within-observation term frequency and inverse document frequency (next note). Peak matrices in E11/E13/E15 have 69,370, 123,840 and 141,420 features and are not the same identifier set; no union/intersection harmonization is applied. Representation choice changes rare/common peak influence and later distances. Evidence: Cusanovich et al. [S44], Stuart et al. [S45].

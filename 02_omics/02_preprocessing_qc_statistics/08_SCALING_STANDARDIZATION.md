# Scaling and standardization

Per-feature z-scoring is (z_{ij}=(x_{ij}-\mu_j)/\sigma_j), with (mu_j,sigma_j) computed over a declared reference set. A toy feature (1,2,3) has (mu=2,sigma=\sqrt{2/3}), giving approximately (-1.225,0,1.225). Scaling centers and changes feature variance; it can make a low-count noisy feature contribute as much as a stable high-count feature and can amplify outliers. Sparse matrices often become dense after centering, so implementation must account for memory and semantics.

Scaling RNA, ADT and ATAC together with one formula is unjustified because their units, background and feature counts differ. Spatial coordinates require a separate geometric decision. In predictive work, (mu,sigma) are fit on training observations only. We do not scale the source matrices. Evidence: OSCA [S38], sctransform [S37], and multimodal integration cautions in Stuart & Satija [S43].

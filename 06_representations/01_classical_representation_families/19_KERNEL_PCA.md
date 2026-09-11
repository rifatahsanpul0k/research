# Kernel principal component analysis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Centering and eigencoordinates

For a PSD Gram matrix \(K:n\times n\), define \(J=I_n-\mathbf1_n\mathbf1_n^T/n\) and \(K_c=JKJ\). This centers the implicit feature vectors, not the original measured values. If \(K_cv_j=\lambda_jv_j\), \(v_j^Tv_j=1\), λ_j>0, then training coordinates are
\[
Z_{ij}=\sqrt{\lambda_j}\,v_{ij},\quad Z:n\times k.
\]
The retained eigensystem is PCA in kernel feature space. Gram eigenvalues differ by the covariance denominator n−1 from feature-space sample variances; normalize consistently.[^1][^2]

## Out-of-sample meaning and inverse limits

A new observation needs similarities to the original training observations, with training-centered kernel means applied consistently. Re-centering a separate test batch independently changes the coordinate definition. Kernel PCA coordinates do not directly supply gene loadings. Recovering an input-space point from them is a pre-image problem; it may be nonunique or have no exact solution. An implementation's approximate inverse transform is an additional fitted procedure, not guaranteed inversion.[^2]

Changing the kernel or bandwidth changes the geometry before eigenvectors are selected. Nonlinearity therefore comes with a specified similarity assumption, not proof that omics lie on a particular manifold. A spatial kernel can be used, but a kernel PCA of RNA alone does not encode physical position. Multi-view kernels require matching observation indices and valid combination rules.

Dense kernel construction often costs O(n²p), full eigendecomposition O(n³), and kernel storage O(n²), plus n×k eigenvectors. Truncated/approximate solvers alter cost and may be stochastic. Missing data need explicit kernel handling. In this project, kernel PCA remains a source-backed family description; no eigendecomposition of project observations was attempted. The toy's ordinary PCA decomposition must not be mislabeled kernel PCA merely because it uses a covariance matrix.

## Evidence

[^1]: Schölkopf B; Smola A; Müller KR (1998). [Nonlinear Component Analysis as a Kernel Eigenvalue Problem](https://is.mpg.de/en/publications/1509). See [access record](SOURCES.md#kpca).
[^2]: Official project maintainers (2026). [Decomposing signals in components](https://scikit-learn.org/stable/modules/decomposition.html). See [access record](SOURCES.md#sk_decomp).

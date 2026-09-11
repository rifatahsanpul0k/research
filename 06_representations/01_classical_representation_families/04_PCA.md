# Principal component analysis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Centering, objective and covariance

For \(X\in\mathbb R^{n\times p}\), n>1, define \(\mu=X^T\mathbf1_n/n\in\mathbb R^p\) and \(X_c=X-\mathbf1_n\mu^T\). Centering removes the mean but does not standardize feature variances. The sample covariance is \(C=X_c^TX_c/(n-1)\in\mathbb R^{p\times p}\). PCA describes variation through orthogonal directions; it is a variance criterion, not a biological relevance criterion.[^1]

For a unit vector \(w\in\mathbb R^p\), projected sample variance is
\[
\frac{\|X_cw\|_2^2}{n-1}=w^TCw.
\]
Maximizing this subject to \(w^Tw=1\) gives \(Cw=\lambda w\): differentiating \(w^TCw-\lambda(w^Tw-1)\) yields \(2Cw-2\lambda w=0\). Choose the largest eigenvalue, then successively orthogonal directions. If \(W_k\in\mathbb R^{p\times k}\) contains them, scores are \(Z=X_cW_k\in\mathbb R^{n\times k}\), and \(Z^TZ/(n-1)\) is diagonal.[^2]

## SVD, reconstruction and ambiguity

The thin SVD is \(X_c=U\Sigma V^T\), with h=min(n,p), \(U:n\times h\), \(\Sigma:h\times h\), \(V:p\times h\). The principal directions are columns of V, \(\lambda_j=\sigma_j^2/(n-1)\), and \(Z=U_k\Sigma_k\). Retained variance fraction is \(\sum_{j\le k}\lambda_j/\sum_j\lambda_j\), when total variance is positive. The reconstruction
\[
\widehat X=ZW_k^T+\mathbf1_n\mu^T
\]
has shape n×p; its squared residual is \(\sum_{j>k}\sigma_j^2\). PCA gives the least-squares rank-k approximation of the centered matrix. Retaining all nonzero directions reconstructs these training observations exactly in exact arithmetic; representing arbitrary future observations without loss needs a full feature-space basis.[^2]

Scores describe observations; direction coefficients describe features. “Loadings” can alternatively mean coefficients scaled by standard deviations, so record the convention. Changing both a direction and its score sign preserves reconstruction. Repeated eigenvalues allow rotations within their eigenspace; orthogonality does not mean independence.[^3]

## Manual anchor and project implications

For the five-row toy, \(\mu=(2.6,2.8,2.6)^T\), \(C_{11}=(1.96+5.76+6.76+2.56+0.16)/4=4.3\), and \(C_{12}=(-3.92-4.32-5.72-5.12-0.32)/4=-4.85\). The leading unit direction is approximately (0.534389,−0.691637,−0.485866), giving row-1 score \(1.4(0.534389)-2.8(-0.691637)-1.6(-0.485866)=3.462115\). [The full toy](TOY_REPRESENTATIONS.md) shows the covariance, characteristic polynomial, numerical roots, scores and reconstruction checks.

PCA of standardized data answers a different variance question. A1's large RNA feature block does not justify selecting k or concatenating assays. Spatial positions are not used unless supplied deliberately. Vanilla PCA does not accept arbitrary missing entries; an absent modality cannot be zero-filled by this definition. Dense exact SVD costs approximately O(np min(n,p)); scores/loadings store O(k(n+p)), plus centering information. These are algorithmic/storage estimates, not project timings.[^3]

## Evidence

[^1]: Jolliffe IT; Cadima J (2016). [Principal component analysis: a review and recent developments](https://pubmed.ncbi.nlm.nih.gov/26953178/). See [access record](SOURCES.md#pca).
[^2]: Deisenroth MP; Faisal AA; Ong CS (2020). [Mathematics for Machine Learning](https://mml-book.github.io/). See [access record](SOURCES.md#mml).
[^3]: Official project maintainers (2026). [Decomposing signals in components](https://scikit-learn.org/stable/modules/decomposition.html). See [access record](SOURCES.md#sk_decomp).

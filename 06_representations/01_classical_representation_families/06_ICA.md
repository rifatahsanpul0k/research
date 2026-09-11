# Independent component analysis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Orientation and mechanism

The customary \(X\approx AS\) writes signals by repeated samples: \(X:p\times n\), mixing \(A:p\times k\), sources \(S:k\times n\). To preserve this project's row convention, write instead
\[
X_c\approx T B^T,
\quad X_c:n\times p,\quad T:n\times k,\quad B:p\times k.
\]
Columns of T are sampled realizations of latent sources; they are assumed statistically independent in the model. S in the customary formula is not spatial metadata. Centering/whitening and non-Gaussianity criteria are common elements of FastICA. Standard identifiable linear ICA assumes independent sources, an adequately ranked mixing matrix and at most one Gaussian source, with scale and permutation unresolved.[^1]

## PCA and ICA answer different questions

PCA decorrelates projected coordinates using second moments; ICA seeks stronger independence information. Zero covariance does not imply independence outside special distributions. For a direct counterexample, let U be symmetric about zero with finite moments and set V=U²: Cov(U,V)=0 when E(U³)=0, yet V is determined by U. This arithmetic example is not a cell model.

If column j of T is multiplied by a nonzero scalar and column j of B divided by it, the reconstructed matrix is unchanged. Permuting factor pairs also changes no fit. ICA components need not be orthogonal, positive, or ordered by explained variance. Strong biological dependence between programs can violate the independent-source assumption; calling each component a pathway would require external evidence, not just a large coefficient.

The factor representation stores O(k(n+p)) values; whitening and repeated non-Gaussianity optimization add costs beyond projection. Initialization and convergence affect numerical output.[^2] Spatial/multimodal use requires an explicit input construction; ordinary ICA does not resolve absent views or paired/unpaired correspondence. The author software page and official scikit-learn implementation are distinguished in the code registry; none was run.

## Evidence

[^1]: Hyvärinen A; Oja E (2000). [Independent Component Analysis: Algorithms and Applications](https://www.cs.helsinki.fi/u/ahyvarin/papers/NN00new.pdf). See [access record](SOURCES.md#ica).
[^2]: Official project maintainers (2026). [Decomposing signals in components](https://scikit-learn.org/stable/modules/decomposition.html). See [access record](SOURCES.md#sk_decomp).

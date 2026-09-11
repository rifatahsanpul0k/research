# Sparse principal component analysis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Sparse directions and a specific formulation

Ordinary PCA constrains length and orthogonality, not the number of nonzero coefficients. A direction may therefore involve thousands of features. Sparse PCA adds a penalty or constraint encouraging zeros; different sparse PCA formulations need not produce the same answer. Zou et al. formulate PCA through regression with elastic-net penalties.[^1]

In a rows-as-observations convention, one version minimizes
\[
\|X_c-X_cBA^T\|_F^2+\lambda\|B\|_F^2+\sum_{j=1}^k\lambda_{1j}\|b_j\|_1,
\quad A^TA=I_k.
\]
Here \(X_c:n\times p\), \(A,B:p\times k\), \(b_j\) is B's jth column, \(\lambda,\lambda_{1j}\ge0\); reconstructed data have shape n×p. Sparse direction columns are obtained from B with the method's normalization convention. The \(\ell_1\) term encourages zeros, while the squared norm regularizes magnitude. This is not equivalent to simply deleting small entries of an ordinary PCA solution.[^1]

## What changes

A smaller support makes feature inspection more manageable, but selected genes are not automatically causal regulators. Reconstruction and sparsity compete. Sparse components may be correlated or nonorthogonal, so ordinary PCA explained-variance additivity cannot be assumed. Projection/reconstruction must use the selected implementation's conventions.[^2]

For this project, a sparse direction may still select depth- or batch-associated genes; sparsity does not resolve confounding. RNA, ADT and ATAC require compatible input processing before any chosen sparse formulation. Missing data are not handled merely by sparse loadings: a zero coefficient and a missing assay are different. Output commonly includes n×k scores and p×k sparse coefficients. Iterative fitting has solver- and penalty-dependent cost; coefficient sparsity can reduce storage without making fitting convex jointly. The authors' elasticnet package is registered, while alternative library variants are labeled as such. No penalty or feature subset is selected here.

## Evidence

[^1]: Zou H; Hastie T; Tibshirani R (2006). [Sparse Principal Component Analysis](https://web.stanford.edu/~hastie/Papers/spc_jcgs.pdf). See [access record](SOURCES.md#spca).
[^2]: Official project maintainers (2026). [Decomposing signals in components](https://scikit-learn.org/stable/modules/decomposition.html). See [access record](SOURCES.md#sk_decomp).

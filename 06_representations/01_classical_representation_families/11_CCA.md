# Canonical correlation analysis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Paired blocks and the objective

Let centered \(X:n\times p\) and \(Y:n\times q\) have the same observation order. For \(a\in\mathbb R^p\), \(b\in\mathbb R^q\), canonical variables are \(u=Xa\) and \(v=Yb\), both n-vectors. CCA maximizes their correlation, not the variance of X alone.[^1]

With sample covariances \(C_{XX}:p\times p\), \(C_{YY}:q\times q\), \(C_{XY}:p\times q\),
\[
\max_{a,b}a^TC_{XY}b\quad
\text{subject to }a^TC_{XX}a=b^TC_{YY}b=1.
\]
The normalization makes covariance equal correlation. Under positive definite within-block covariances, whitening produces \(T=C_{XX}^{-1/2}C_{XY}C_{YY}^{-1/2}:p\times q\); its singular vectors determine directions and singular values give canonical correlations. Later pairs satisfy within-view canonical uncorrelatedness constraints.[^2]

## High dimensions and meaning

Centered matrices have rank at most n−1. When p or q exceeds that limit, ordinary covariance inverses do not exist. Pseudoinverses alone do not prevent spurious near-perfect sample correlations; regularization, sparsity or reduced rank changes the estimator. Sparse CCA is one explicitly constrained family, not proof of valid biological coupling.[^3]

Rows paired by physical observation support the cross-covariance calculation. Arbitrarily reordering Y changes it, demonstrating why raw CCA does not match unpaired cells. CCA-based integration pipelines may create anchors by additional procedures; they should not be identified with this basic paired objective.

For project RNA–ADT tables, matching identifiers is necessary, while scale, missingness and the spot unit still matter. Correlated canonical variables do not prove RNA causes protein variation. Outputs include paired n×k score matrices and p×k/q×k directions; view-specific residual variation can be lost. Dense covariance storage is O(p²+pq+q²); SVD-based implementations can avoid some covariance materialization. Missing rows/entries require an explicit supported procedure; baseline complete-data CCA has no automatic spatial model.

## Evidence

[^1]: Hotelling H (1936). [Relations between two sets of variates](https://academic.oup.com/biomet/article-abstract/28/3-4/321/220073). See [access record](SOURCES.md#cca).
[^2]: Official project maintainers (2026). [Cross decomposition](https://scikit-learn.org/stable/modules/cross_decomposition.html). See [access record](SOURCES.md#sk_cross).
[^3]: Witten DM; Tibshirani R; Hastie T (2009). [A penalized matrix decomposition, with applications to sparse principal components and canonical correlation analysis](https://hastie.su.domains/public/Papers/PMD_Witten.pdf). See [access record](SOURCES.md#pmd).

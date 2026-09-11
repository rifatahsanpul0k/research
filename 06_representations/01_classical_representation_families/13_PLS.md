# Partial least squares

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Covariance between two blocks

For paired, centered \(X:n\times p\), \(Y:n\times q\), a first-component two-block PLS-SVD formulation seeks
\[
\max_{\|a\|_2=\|b\|_2=1}a^TX^TYb,
\quad a:p,\ b:q.
\]
The singular vectors of XᵀY supply the weights; scores t=Xa and u=Yb have length n. Dividing the objective by n−1 gives sample covariance. PLS-regression additionally builds a predictive relationship from X to Y using a sequence of components. Deflation rules and normalization differ among PLS-SVD, PLSCanonical and PLSRegression; later components cannot be inferred from this first-pair objective alone.[^1][^2]

| Method | First-pair target | Main distinction |
|---|---|---|
| PCA | Variance within X | No second block required |
| CCA | Correlation of Xa and Yb | Unit score variances under within-block covariances |
| PLS-SVD | Cross-block covariance under unit weight norms | Retains scale sensitivity |

Multiplying one Y feature by 100 changes its cross-covariance contribution. CCA's score-variance constraints and PLS's weight-norm constraints therefore answer different questions. High covariance does not imply a large standardized association, much less causation.

## Project implications

PLS can be supervised when Y is an outcome, or a two-view descriptive relationship when Y is another assay. This role must be stated in the method record. A measured RNA–ADT pair is not necessarily a direct gene–protein causal measurement; observation mixtures and assay response remain relevant. Prediction of an unavailable view requires validation and is not its measurement.

Output typically contains n×k scores, p×k and q×k weights/loadings and, for regression, a p×q prediction map or its factorized equivalent. Iterative matrix-vector implementations avoid forming every cross-product, but costs depend on n,p,q,k and iteration count. Basic complete-data implementations do not automatically handle missing views, although other PLS variants may. Spatial data can be an explicit block; spatial modeling is not intrinsic. No response prediction or fitting was run.

## Evidence

[^1]: Wold S; Sjöström M; Eriksson L (2001). [PLS-regression: a basic tool of chemometrics](https://www.sciencedirect.com/science/article/pii/S0169743901001551). See [access record](SOURCES.md#pls).
[^2]: Official project maintainers (2026). [Cross decomposition](https://scikit-learn.org/stable/modules/cross_decomposition.html). See [access record](SOURCES.md#sk_cross).

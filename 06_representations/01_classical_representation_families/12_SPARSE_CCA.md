# Sparse canonical correlation analysis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Why constraints change the representation

With paired centered blocks \(X:n\times p\), \(Y:n\times q\), p,q≫n can make unconstrained sample CCA poorly identified. Sparse CCA uses penalties or constraints to restrict selected features. A penalized matrix-decomposition example is
\[
\max_{a,b}a^TX^TYb,
\quad \|a\|_2\le1,\ \|b\|_2\le1,
\quad \|a\|_1\le c_x,\ \|b\|_1\le c_y,
\]
where a:p, b:q and nonnegative c_x,c_y control feasible sparsity. Products are scalar; output scores Xa,Yb each have length n. Witten et al.'s sparse CCA treatment uses a diagonal within-block covariance approximation in this formulation.[^1]

This is not the same as the full-covariance CCA constraints in [note 11](11_CCA.md). It is also not simply applying thresholding after ordinary CCA. A method name must be accompanied by its objective and scaling convention.

## Interpretability, assumptions and cost

Zero direction coefficients define a selected feature subset. Selected gene/antibody pairs may be easier to inspect, but selection is sensitive to penalties, correlated substitutes and sampling. Sparsity does not establish the uniqueness or causality of those features. A highly correlated gene omitted in favor of another is not proved irrelevant.

The pairing requirement remains. Missing assays are not sparse zeros, and completely unpaired modalities need an additional correspondence model. For A1, sparse RNA coefficients may reduce the number of involved genes but do not equalize assay noise or guarantee balanced contribution from 31 ADTs.

Coefficient storage can be sparse, while explicit XᵀY costs O(npq) arithmetic and O(pq) memory; algorithms can instead use alternating matrix-vector products. Iteration count, initialization and penalty path determine actual cost. Selection and penalty tuning would have to remain within future training splits; no values are tuned here. The authors' PMA package is registered as the matching implementation. PCA, CCA and sparse CCA are related mechanisms with distinct objectives, not ranked alternatives.

## Evidence

[^1]: Witten DM; Tibshirani R; Hastie T (2009). [A penalized matrix decomposition, with applications to sparse principal components and canonical correlation analysis](https://hastie.su.domains/public/Papers/PMD_Witten.pdf). See [access record](SOURCES.md#pmd).

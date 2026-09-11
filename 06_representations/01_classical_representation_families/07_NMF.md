# Nonnegative matrix factorization

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Representation and constraints

For nonnegative \(X\in\mathbb R_+^{n\times p}\), choose k and seek
\[
X\approx WH,\qquad W\in\mathbb R_+^{n\times k},\quad H\in\mathbb R_+^{k\times p}.
\]
Rows of W are observation factor contributions; rows of H are feature profiles. Nonnegativity makes reconstruction additive, motivating a parts-based interpretation in the original work. The interpretation is algebraic: a factor is not established as a biological pathway by the constraints.[^1]

A squared-error formulation minimizes \(\|X-WH\|_F^2\). Other divergence choices define other fitting criteria and noise assumptions. The problem is generally nonconvex jointly even though one block can be optimized with the other fixed. Ordinary centered/scaled data with negative entries do not satisfy the nonnegative input condition.[^2]

## Non-uniqueness and loss

For a positive diagonal \(D:k\times k\), \((WD)(D^{-1}H)=WH\). Factor permutation also preserves the product, and additional inequivalent nonnegative solutions can occur. A reconstruction objective alone does not identify pathway membership. Initialization, rank and regularization may change the result. Zeros in a factor are coefficients, not statements of biological absence.

As a synthetic illustration, a profile (2,0,1) with weight 3 contributes (6,0,3) additively. Two overlapping profiles can explain the same expressed genes; overlap is not an error in itself. For project RNA counts, nonnegativity is only one input condition, not proof that a squared-error NMF likelihood is appropriate. ADT and ATAC have different measurement mechanisms and feature semantics.

Factor storage is O(nk+kp); a dense reconstruction-gradient pass is typically O(npk), with iteration count and convergence additional. Compressing to W discards residuals and requires H for approximate reconstruction. Missingness needs an explicitly masked/model-specific variant, not zero-filling. Spatial coordinates are unused unless an additional declared mechanism is supplied. No factorization or rank selection was performed.

## Evidence

[^1]: Lee DD; Seung HS (1999). [Learning the parts of objects by non-negative matrix factorization](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/lee-nature-99.pdf). See [access record](SOURCES.md#nmf).
[^2]: Official project maintainers (2026). [Decomposing signals in components](https://scikit-learn.org/stable/modules/decomposition.html). See [access record](SOURCES.md#sk_decomp).

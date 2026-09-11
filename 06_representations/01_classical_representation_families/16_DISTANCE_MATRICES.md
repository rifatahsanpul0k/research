# Pairwise distance matrices

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## From features to relationships

For rows x_iᵀ of \(X:n\times p\), define \(D_{ij}=d(x_i,x_j)\); \(D:n\times n\). D compares observations rather than naming measured features. Common definitions include:

| Dissimilarity | Formula for x,y∈Rᵖ | Required qualification |
|---|---|---|
| Euclidean | \(\sqrt{\sum_g(x_g-y_g)^2}\) | Sensitive to scale |
| Manhattan | \(\sum_g|x_g-y_g|\) | Different aggregation of coordinate differences |
| Cosine distance | \(1-x^Ty/(\|x\|\|y\|)\) | Nonzero norms; not generally a metric |
| Correlation distance | \(1-\operatorname{corr}(x,y)\) | Nonconstant vectors; centering across features here |

Euclidean and Manhattan satisfy metric axioms; the last two need not satisfy triangle inequality. Correlation across features within a row is distinct from gene–gene correlation across observations.[^1]

## Loss and storage

Euclidean D preserves pairwise geometry up to rigid coordinate changes, not original named axes. Translation and rotation leave it unchanged; scaling generally does not. A complete exact Euclidean D can determine a centered configuration up to orthogonal transformation through \(-\tfrac12 JD^{\circ2}J\), where \(J=I_n-\mathbf1_n\mathbf1_n^T/n\) and \(D^{\circ2}\) squares entries. This matrix is a Gram matrix; it does not restore gene meanings.[^2]

Dense storage is O(n²), and naive Euclidean construction is O(n²p). Symmetry permits triangular storage but leaves the quadratic order. A row of D changes dimension when reference observations are added; it is a relational representation relative to a specified reference set, not automatically an inductive fixed-feature vector.

For omics, preprocessing, missingness and feature choice determine distances. Pairwise deletion over different feature subsets can destroy a common geometry. Spatial D requires coordinate units and frame; it is not molecular dissimilarity. No D from the six datasets was computed. The fixed synthetic example exposes these choices without interpreting any distance as biological difference.

## Evidence

[^1]: Blum A; Hopcroft J; Kannan R (2020). [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). See [access record](SOURCES.md#bhk).
[^2]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).

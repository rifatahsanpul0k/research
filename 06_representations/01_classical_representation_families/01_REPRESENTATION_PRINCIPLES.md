# Representation principles

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Objects, mechanisms and meaning

Write \(R=f(X)\), where \(X\in\mathbb R^{n\times p}\) stores observations by measured features, \(f\) includes the declared selection/transformation/fitting rules, and \(R\) is the resulting object. This definition does not require reduction, learning or a vector output. A raw table, a set of neighbor identifiers and a transport plan are all representations, with different semantics. The linear-algebra foundation distinguishes a coordinate description from the underlying object.[^1]

For multi-omics write
\[
R=f(X^{RNA},X^{ADT},X^{ATAC},S,M).
\]
Here \(X^{(m)}\in\mathbb R^{n_m\times p_m}\); \(S\) is a spatial coordinate table with observation IDs and typically two or three coordinate columns; \(M\) is metadata, not the missingness mask used in some Phase 2A notes. Missingness here is \(\Omega^{(m)}\in\{0,1\}^{n_m\times p_m}\). The expression is a possible input signature, not a claim that all views exist or share rows. Integration methods differ in correspondence and feature assumptions.[^2]

Use \(B\) for pairwise similarity, \(K\) for a PSD kernel, \(A\) for adjacency, \(Z\) for latent scores and \(\Pi\) for transport. Each note declares any local notation. Rows are \(x_i^T\); \(x_i\) is a column vector. Frobenius norm squared is the sum of squared matrix entries; \(\mathbf1_n\) is the length-n ones vector; superscript T denotes transpose.

## Pipeline and project interpretation

Keep measurement → preprocessing → initial representation → fitting mechanism → learned object → downstream model/task → evaluation distinct. A PCA fitting algorithm is a mechanism; its scores are a representation; a classifier receiving them is another model. Several objects can coexist, for example named RNA features, spatial coordinates and a kernel, without fusing everything.

Before future use, record the observation unit, feature IDs/order, units, fitted parameters, training scope, missingness and provenance. Similar vectors do not establish biological equivalence; distance does not establish biological dissimilarity. A measured spot may summarize multiple cells, so latent coordinates cannot change its physical unit. Current dataset limits are centralized in [the framework](REPRESENTATION_COMPARISON_FRAMEWORK.md). No empirical biological preservation is established in this phase.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).
[^2]: Argelaguet R; Cuomo ASE; Stegle O; Marioni JC (2021). [Computational principles and challenges in single-cell data integration](https://www.nature.com/articles/s41587-021-00895-7). See [access record](SOURCES.md#integration).

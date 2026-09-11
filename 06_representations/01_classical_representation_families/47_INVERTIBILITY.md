# Invertibility and approximate reconstruction

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## What must be retained to reverse a map

An injective f has at most one input per output on its declared domain; an inverse exists on its image. Approximate reconstruction uses a decoder g to obtain \(\widehat X=g(R)\), which may differ from X. Reconstruction error requires a specified norm/likelihood and is not itself biological fidelity.[^1]

| Representation | Recovery condition |
|---|---|
| Identity/concatenation | Exact with IDs, block order and values |
| Standardization | Exact if means and nonzero scales retained; discarded constant columns need their constants |
| Full-basis PCA | Exact with scores, directions and mean, up to numerical precision |
| Truncated PCA | Exact only for inputs in the retained affine subspace; otherwise residual loss |
| Euclidean distance matrix | Coordinates up to rigid transformations for a realizable complete matrix; original gene axes not recovered |
| Kernel PCA | Input preimage can be nonunique or unavailable |
| Hard labels | Generally many feature vectors per label |

A training matrix of rank r can be reconstructed with r nonzero PCs. This does not make the same r-coordinate map injective for arbitrary future p-dimensional observations when r<p. Distinguish finite-data reconstruction from global invertibility.

## Direct counterexample

For \(f(x_1,x_2)=x_1\), (2,0) and (2,9) both map to 2. No inverse that sees only 2 can identify the omitted second coordinate. If a decoder guesses its conditional mean, that is a model prediction. It does not restore the measured value.

This distinction applies to inferred missing views, pathway aggregates and cluster centroids. Keeping a full residual plus loadings can recover more, at extra storage cost. In this project, a model-derived ATAC prediction would remain a derivative distinct from an unavailable assay. Nothing is reconstructed from project data. Costs of decoding and stored side information belong in future representation records alongside compact coordinates; an n×k object alone may understate its full footprint.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).

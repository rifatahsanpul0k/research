# Feature concatenation

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## A simple, explicit object

For paired \(X:n\times p\), \(Y:n\times q\), concatenation is \(R=[X|Y]:n\times(p+q)\). It preserves both blocks exactly if their boundaries, identities and preprocessing are retained. It is a linear reorganization of input coordinates, not an inferred common latent biology. Without row correspondence the operation has no defensible observation-level meaning.[^1]

**Verified local input context:** Phase 1E reports A1 RNA 3484×18085 and ADT 3484×31, with paired spot identifiers. A hypothetical joint table would therefore be 3484×18116. This is dimension arithmetic using [DATASET_STATISTICS.md](../../02_omics/02_preprocessing_qc_statistics/DATASET_STATISTICS.md) only; no concatenated project table was created. The RNA/ADT column-count ratio is 18085/31≈583.39, which is not a measured influence ratio.

## Weighting and information

For scaled blocks \(R=[\alpha X|\beta Y]\), Euclidean distance obeys
\[
\|r_i-r_j\|_2^2=\alpha^2\|x_i-x_j\|_2^2+
\beta^2\|y_i-y_j\|_2^2.
\]
Here α,β are declared scalar weights; x_i:p and y_i:q. Thus units, feature counts, variances and correlations affect influence. Many similarly scaled RNA differences can accumulate, but dimensional imbalance alone does not prove which block dominates actual distances. A nonzero α,β allows reversal if weights are retained; zeroing a block is lossy.

The construction is interpretable at feature level and stores O(n(p+q)) dense entries or the combined sparse nonzeros. Its simplicity does not address noise, incompatible measurement scales or missing views. A block filled with zero is interpreted as data unless accompanied by a mask and an estimator that respects it. Spatial coordinates can be concatenated too, but that imposes a metric trade-off between physical and molecular units. Keep them separate unless that trade-off is authorized and justified. No weights are selected here.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).

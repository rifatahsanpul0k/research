# 21. Curse of dimensionality

High dimension can make space sparsely sampled, distances less discriminative, estimation unstable and computations expensive. These effects depend on distribution, intrinsic dimension and signal structure; a large feature count alone is not a proof that meaningful neighbors cannot exist. [BHK, chapter 2](SOURCES.md#bhk)

Verified examples from [Phase 1E](../../02_omics/02_preprocessing_qc_statistics/DATASET_STATISTICS.md):

| Matrix | $n$ | $p$ | $p/n$ | Centered-rank upper bound |
|---|---:|---:|---:|---:|
| A1 RNA | 3,484 | 18,085 | 5.19087 | 3,483 |
| E11 ATAC | 1,263 | 69,370 | 54.92478 | 1,262 |

These are dimension-derived ratios and bounds, not computed ranks or intrinsic dimensions. Dense $p\times p$ covariance would contain 327,067,225 entries for A1 and 4,812,196,900 for E11 ATAC. Even when $X$ is sparse, covariance need not be. Pairwise dense observation distances require $n^2$ storage and straightforward computation about $n^2p$ operations; sparsity-aware implementations can reduce work but do not settle interpretation.

A grid with ten bins per coordinate requires $10^p$ bins. Holding $n$ fixed as $p$ grows leaves most empty. This is an illustrative full-dimensional model, not a literal discretization of gene expression.

If independent irrelevant dimensions add comparable noise, they can dominate squared distance and reduce relative contrast between distances. Simultaneously, when $p\ge n$, an unconstrained fit may interpolate data in many ways, allowing noise fitting. Dependence and biological low-dimensional structure can change this picture. Later feature selection or compression therefore needs both statistical and biological checks, particularly for rare populations.

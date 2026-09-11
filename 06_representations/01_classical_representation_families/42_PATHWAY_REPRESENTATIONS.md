# Gene-set and pathway scores

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## From genes to sets

For \(X:n\times p\) and r gene sets \(G_1,\ldots,G_r\), define
\[
R_{ik}=f_k(\{x_{ij}:j\in G_k\}),\quad R:n\times r.
\]
The scoring function is part of the representation. A mean score, rank enrichment and a likelihood-based activity estimate are not interchangeable. GSVA is a representative nonparametric method that transforms expression information into sample-wise gene-set enrichment scores; it is not simply an arithmetic mean and its distribution estimation depends on the input cohort.[^1]

## A transparent toy aggregation

For synthetic row (4,0,1) and G₁={1,3}, the mean is (4+1)/2=2.5. For G₂={2,3}, it is (0+1)/2=0.5. This is a defined teaching score, **not GSVA**. If the sets overlap at feature 3, their scores share a measured contribution; correlation between scores need not indicate independent pathway crosstalk.

An n×r summary may reduce dimensionality when r<p, but large overlapping catalogues may not. Averaging loses within-set composition: (4,0) and (2,2) have the same mean. Signed activation/repression information requires an appropriate model, not arbitrary averaging. A transcript-derived score is not measured metabolic flux or protein activity.

## Project conditions and cost

Reactome pathway definitions include curated and inferred relationships that must be identified by release, species and evidence.[^2] Mapping coverage and the available gene universe change the score; genes excluded from the assay must not be silently interpreted as zero. RNA and ATAC gene-linked summaries are different inputs even when pathway names match.

Simple means require O(nΣ_k|G_k|) work; rank-based/cohort-based methods add distribution and sorting steps. Storage is O(nr) plus set memberships. Some scoring mechanisms use other observations' distributions, so future train/test application must examine cohort dependence and leakage. The official GSVA implementation is recorded, but no pathway scores are calculated for real data and no scoring method is selected.

## Evidence

[^1]: Hänzelmann S; Castelo R; Guinney J (2013). [GSVA: gene set variation analysis for microarray and RNA-Seq data](https://link.springer.com/article/10.1186/1471-2105-14-7). See [access record](SOURCES.md#gsva).
[^2]: Official project maintainers (2026). [Reactome Userguide](https://reactome.org/userguide). See [access record](SOURCES.md#reactome).

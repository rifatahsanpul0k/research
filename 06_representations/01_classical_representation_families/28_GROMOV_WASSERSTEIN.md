# Gromov–Wasserstein relationships

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Comparing internal structure

Let \(D^X:n\times n\) and \(D^Y:m\times m\) describe within-domain relationships, with masses a:n and b:m. A squared-loss GW objective over balanced couplings Π:n×m is
\[
\min_{\Pi\in U(a,b)}\sum_{i,i'=1}^n\sum_{j,j'=1}^m
(D^X_{ii'}-D^Y_{jj'})^2\Pi_{ij}\Pi_{i'j'},
\]
where U(a,b) is the nonnegative coupling set with row/column marginals a,b. This compares relational patterns under a coupling rather than directly subtracting incompatible feature vectors. The expression is a GW loss; distance conventions may additionally use a square root and constant factor.[^1]

## What is gained and what remains assumed

Different feature spaces can be compared if their internal relational structures are meaningfully comparable. That conditional does substantial work: raw distances from different assays may have incompatible scale or biological meaning. A shared shape does not identify which biological entity is which. Symmetries can yield multiple plausible matchings, and the quadratic coupling objective is generally nonconvex.

Fused GW adds a cross-domain feature cost term. PASTE combines molecular information with spatial relationships to align spatial transcriptomics slices; its alignment/coupling is distinct from a learned feature embedding. The existing PASTE publication record and official repository are reused; no slice alignment is performed.[^2]

## Cost and project relevance

Storing D^X,D^Y and Π costs O(n²+m²+nm). Naively evaluating the four-index sum costs O(n²m²); squared-loss algebra permits matrix contractions with lower cost, but does not remove nonconvexity. Solver, initialization and regularization matter.

This framework is relevant to differing modalities and spatial sections, including mouse ATAC feature mismatches, without proving it solves their biological correspondence. Incomplete views, absent cell populations, coordinate registration and cost normalization remain unresolved. An inferred alignment across E11 and E18 would be neither a direct temporal trajectory nor a lineage experiment. No project relational matrix or coupling was constructed.

## Evidence

[^1]: Official project maintainers (2026). [POT user guide](https://pythonot.github.io/). See [access record](SOURCES.md#pot_doc).
[^2]: Zeira R; Land M; Strzalkowski A; Raphael BJ (2022). [Alignment and integration of spatial transcriptomics data](https://www.nature.com/articles/s41592-022-01459-6). See [access record](SOURCES.md#paste).

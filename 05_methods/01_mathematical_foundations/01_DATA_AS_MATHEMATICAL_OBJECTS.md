# 01. Data as mathematical objects

The matrix is the numerical output of an assay and its processing, not a complete cell. Let $X\in\mathbb R^{n\times p}$ have observation index $i=1,\ldots,n$ and feature index $j=1,\ldots,p$. Entry $x_{ij}$ is the stored signal for observation $i$ and feature $j$. We use a column vector $x_i=(x_{i1},\ldots,x_{ip})^\top\in\mathbb R^p$ for algebra, so row $i$ of $X$ is $x_i^\top$. $\mathbb R$ denotes real numbers; a count matrix occupies the nonnegative integer subset when its units justify that interpretation. Float storage alone does not settle count semantics. [VMLS](SOURCES.md#vmls)

| Object | Shape | Biological/measurement interpretation |
|---|---|---|
| $X^{(RNA)}$ | $n\times p$ | Observation-by-gene RNA signal |
| $X^{(ADT)}$ | $n\times q$ | Observation-by-antibody-tag signal; $q$ antibody features |
| $X^{(ATAC)}$ | $n\times r$ | Observation-by-genomic-interval accessibility signal; $r$ peaks |
| $S$ | $n\times2$ | Observation positions in a specified coordinate frame |
| Observation metadata | $n$ records | Sample, region, quality and label provenance |
| Feature metadata | $p,q,$ or $r$ records | Identifiers, annotation and assay-specific feature definitions |

The superscript in parentheses names a modality, not an exponent. Shared $n$ is appropriate only after observation identity is established. A1 RNA is $3484\times18085$, A1 ADT is $3484\times31$, and E11 ATAC is $1263\times69370$. These verified shapes come from [local Phase 1E reports](../../02_omics/02_preprocessing_qc_statistics/DATASET_STATISTICS.md); they are not three views from one common specimen.

A1/D1 rows are spatial spots. Mouse rows are spatial capture locations with exact physical units still unresolved. Do not relabel all $n$ rows “cells.” RNA, antibody binding, accessibility and position describe different aspects of tissue. [Biological units](../../01_biology/03_cellular_tissue_biology/16_OBSERVATION_UNITS.md)

E18 ATAC remains unavailable; an unspecified $r$ is a mathematical placeholder, not a verified E18 feature count. Duplicate feature labels in prior inspection require stable identifiers or disambiguation before joins. This phase uses verified shapes and synthetic arithmetic; no research matrices are transformed.

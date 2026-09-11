# Biology to Data

Status: Phase 1A computational bridge complete.

## Biological process to tabular data

Biological reality is molecular and spatial. A table is a recorded abstraction produced by an assay and a processing pipeline.

`biological sample -> measurement chemistry -> molecule capture/detection -> sequencing or readout -> alignment/assignment -> feature identifiers -> matrix + metadata`

For RNA data, a typical simplified chain is:

`cell -> RNA molecules -> captured molecules -> reads/UMIs -> gene assignment -> cells x genes matrix`

For spatial data, the chain adds location:

`tissue section -> spot/cell/bin -> molecule detection -> feature assignment -> matrix + x/y coordinates + tissue metadata`

## Small synthetic expression matrix

| CellGene | GeneA | GeneB | GeneC |
|---|---:|---:|---:|
| C1 | 8 | 0 | 3 |
| C2 | 1 | 6 | 2 |
| C3 | 7 | 0 | 4 |

Rows are observations. In single-cell data, a row may be a cell or nucleus. In spatial omics, a row may be a cell, spot, bin, bead, or segmented region. The row identity must be verified from dataset metadata.

Columns are molecular features. In an RNA matrix, columns may be gene identifiers or transcript identifiers. In a protein matrix, columns may be antibody-derived tags or protein features. In a regulatory-region matrix, columns may be genomic intervals.

Values are assay-dependent measurements. In a count matrix, `8` under `GeneA` for `C1` means that the pipeline assigned eight captured molecules or molecule-derived counts to GeneA for observation C1. It does not directly equal total molecules inside the living cell.

## Companion metadata

| cell_id | sample_id | tissue | x | y | quality_metric |
|---|---|---|---:|---:|---:|
| C1 | S1 | unknown | 12.4 | 8.2 | 0.91 |
| C2 | S1 | unknown | 13.1 | 8.4 | 0.88 |
| C3 | S1 | unknown | 12.8 | 9.0 | 0.90 |

Metadata can carry biological context, spatial coordinates, sample labels, batch labels, or quality measurements. Some metadata fields are measured, some are assigned by processing, and some are inferred by analysis. Those categories must remain separate.

## Why vector similarity is not biological equivalence

Two cells can have similar numerical vectors for several reasons:

| reason for similarity | biological interpretation risk |
|---|---|
| same cell type | plausible biological similarity if supported by markers and context |
| same transient state | similar now, but not necessarily same identity |
| shared cell-cycle phase or stress response | vectors may cluster by state rather than lineage or function |
| same tissue neighborhood | spatial context may shape expression |
| batch or chemistry effect | technical similarity can mimic biology |
| normalization or feature selection | preprocessing can emphasize or suppress differences |
| sparse detection | zeros and low counts can distort distances |

Therefore:

`two similar numerical vectors` does not automatically imply `two biologically equivalent cells`.

For later representation learning, every similarity claim needs supporting evidence: feature meaning, assay level, metadata, known biology, uncertainty, and validation against independent biological information where possible.

## Sources

- Luecken and Theis, 2019, *Molecular Systems Biology*, single-cell RNA-seq analysis and count interpretation.
- Laehnemann D et al. (2020), [Eleven grand challenges in single-cell data science](https://link.springer.com/article/10.1186/s13059-020-1926-6), *Genome Biology* 21:31. DOI: 10.1186/s13059-020-1926-6.
- Svensson V. (2020), [Droplet scRNA-seq is not zero-inflated](https://www.nature.com/articles/s41587-019-0379-5), *Nature Biotechnology* 38:147-150. DOI: 10.1038/s41587-019-0379-5.
- Zeira et al., 2022, *Nature Methods*, spatial transcriptomics as expression measurements with spatial coordinates.
- Argelaguet et al., 2021, *Nature Biotechnology*, single-cell multimodal integration.
- Baysoy et al., 2023, *Nature Reviews Molecular Cell Biology*, single-cell multi-omics technologies.


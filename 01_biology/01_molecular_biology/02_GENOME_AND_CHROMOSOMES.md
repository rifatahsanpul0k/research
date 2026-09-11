# 02. Chromosomes and Genome Organization

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

A genome is the complete DNA information of an organism or cell. Chromosomes are long DNA molecules packaged with proteins and organized in three-dimensional nuclear space. In eukaryotes, chromosomes contain genes, regulatory elements, repetitive sequence, centromeres, telomeres, and large non-coding regions [Alberts 2002, Ch. 4](https://www.ncbi.nlm.nih.gov/books/NBK26821/); [ENCODE Project Consortium 2012](https://www.nature.com/articles/nature11247).

## B. Biological mechanism

Chromosomal DNA is packaged as chromatin. Packaging solves a physical problem, because long DNA molecules must fit in the nucleus, and it creates a regulatory context in which promoters, enhancers, and boundary elements can interact. Higher-order genome organization changes during differentiation and development and is connected to gene regulation, although the causal direction between structure and expression can be context dependent [Oudelaar and Higgs 2021](https://www.nature.com/articles/s41576-020-00303-x).

## C. Relationships

DNA is the molecular material; chromosomes are its cellular packaging; the genome is the full set. Genes and regulatory regions occupy positions within this organized genome. Transcription depends on access to a gene and its regulatory context.

## D. Experimental measurement

Genome organization can be studied by genome sequencing, cytogenetics, chromatin conformation assays, microscopy, and annotation projects. A project may store only derived tables, such as genomic intervals, gene annotations, or region-to-gene links, rather than raw chromosome measurements.

## E. Numerical/computational representation

Genome organization often becomes interval data:

| region_id | chromosome | start | end | region_type | linked_gene |
|---|---:|---:|---:|---|---|
| R1 | chr1 | 950 | 999 | promoter | GeneA |
| R2 | chr1 | 3000 | 3400 | enhancer_candidate | GeneA |

These rows are not expression measurements. They are coordinate-linked annotations or assay-derived regions.

## F. Relevance to our project

Single-cell and spatial data use features whose identities depend on genome organization: genes, transcripts, peaks, or proteins mapped to genes. Spatial omics adds tissue coordinates but still needs molecular feature definitions. Multi-omics requires aligning different feature spaces, often through genomic coordinates or annotation tables. Biological similarity may depend on regulatory context, not only expression vector closeness.

## G. Misconceptions

- Treating nearby genomic features as necessarily functionally related.
- Treating all regulatory region-to-gene mappings as measured facts; many are inferred from correlation, distance, accessibility, or prior annotation.
- Forgetting that reference builds and annotation versions can change genomic coordinates and feature definitions.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, 4th ed., Chapter 4.
- ENCODE Project Consortium, 2012, *Nature*, integrated encyclopedia of DNA elements.
- Oudelaar and Higgs, 2021, *Nature Reviews Genetics*, genome structure and function.


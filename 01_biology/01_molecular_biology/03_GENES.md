# 03. Genes

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

A gene can be operationally identified through genomic sequence encoding a functional RNA or protein product; alternative and overlapping products complicate its boundaries. Gerstein and colleagues group sequences through their products and explicitly separate regulation from their proposed gene definition. Promoters and enhancers regulate genes, but all associated distal regulatory DNA should not automatically be included inside a gene's annotated boundary [Gerstein et al. 2007](https://pubmed.ncbi.nlm.nih.gov/17567988/); [ENCODE Project Consortium 2012](https://www.nature.com/articles/nature11247).

## B. Biological mechanism

A gene is read when transcription machinery recognizes regulatory DNA and synthesizes an RNA transcript from a DNA template strand. In eukaryotes, transcripts may be processed by capping, splicing, and polyadenylation. For protein-coding genes, a mature mRNA can guide translation; for non-coding RNA genes, the RNA is the functional product [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK21050/).

## C. Relationships

Genes are embedded in chromosomes and defined using both sequence and regulation. Coding and non-coding regions clarify what parts of genes or genomes contribute to protein sequence, RNA products, or regulation. Transcription is the immediate process that converts gene information into RNA.

## D. Experimental measurement

Genes are measured indirectly by sequencing DNA, annotating transcripts, measuring RNA abundance, perturbing loci, or detecting protein products. Annotation databases consolidate evidence, but a matrix column named by a gene symbol usually represents an assay-defined measurement assigned to that gene, not the gene itself.

## E. Numerical/computational representation

A gene can appear as an identifier or a column in an expression matrix:

| cell_id | GeneA | GeneB | GeneC |
|---|---:|---:|---:|
| C1 | 8 | 0 | 3 |
| C2 | 1 | 6 | 2 |

Here `GeneA` is a feature label. The value is a measured or processed molecular signal assigned to that gene in that cell.

## F. Relevance to our project

Single-cell data often uses genes as matrix features. Spatial omics can associate gene measurements with tissue coordinates. Multi-omics may connect gene expression to DNA regions, proteins, or regulatory annotations. Biological similarity often depends on which genes are active, but the interpretation requires knowing whether features are gene-level, transcript-level, protein-level, or inferred.

## G. Misconceptions

- Assuming one gene always maps to one transcript and one protein.
- Treating gene expression counts as direct measurements of gene activity without protocol and processing context.
- Treating gene symbols as stable primary keys; durable records should include database identifiers and annotation version.

## H. Evidence

- Gerstein MB et al. (2007), [What is a gene, post-ENCODE? History and updated definition](https://pubmed.ncbi.nlm.nih.gov/17567988/), *Genome Research* 17:669-681. DOI: 10.1101/gr.6339607.
- Alberts et al., *Molecular Biology of the Cell*, Chapter 6.
- ENCODE Project Consortium, 2012, *Nature*, genome annotation and DNA elements.

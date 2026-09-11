# 04. Coding vs Non-Coding Regions

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

Coding sequence is DNA or RNA sequence that specifies amino acid order in a protein. Non-coding sequence does not directly encode a protein amino acid sequence, but it can include regulatory elements, introns, untranslated regions, structural chromosome regions, repetitive elements, and genes whose final products are non-coding RNAs [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK21050/); [ENCODE Project Consortium 2012](https://www.nature.com/articles/nature11247).

## B. Biological mechanism

Protein-coding regions are transcribed into RNA and read as codons during translation after RNA processing. Non-coding regions can regulate when and where transcription occurs, influence RNA processing or stability, or produce functional RNAs. Long non-coding RNAs can participate in chromatin regulation, transcriptional control, RNA processing, translation regulation, and cellular organization [Mattick et al. 2023](https://www.nature.com/articles/s41580-022-00566-8).

## C. Relationships

This distinction refines the gene concept. DNA includes both coding and non-coding regions. Transcription can occur from both protein-coding and non-coding genes. Translation applies to coding RNA regions, while many RNAs are not translated into canonical proteins.

## D. Experimental measurement

Coding regions are studied through genome annotation, transcript sequencing, ribosome profiling, proteomics, and genetic perturbation. Non-coding regions are studied through transcriptomics, regulatory assays, chromatin assays, comparative genomics, perturbation, and annotation projects. Functional status often requires multiple evidence types.

## E. Numerical/computational representation

Coding/non-coding status may appear as feature metadata:

| feature_id | feature_type | product_type | chromosome |
|---|---|---|---|
| GeneA | protein_coding_gene | protein | chr1 |
| LncB | lncRNA_gene | RNA | chr2 |
| RegC | enhancer_candidate | regulatory_region | chr3 |

This metadata changes the meaning of a matrix column or interval row.

## F. Relevance to our project

Single-cell matrices may contain protein-coding and non-coding genes depending on annotation and filtering. Spatial data may preserve location of expression for non-coding RNAs or protein-coding transcripts. Multi-omics integration can connect non-coding regulatory regions to gene expression, but many links are inferred. Representation learning must avoid treating every feature as equivalent merely because all features are numeric columns.

## G. Misconceptions

- Equating non-coding with non-functional.
- Assuming all transcribed non-coding regions have known biological function.
- Assuming a matrix filtered to protein-coding genes captures all relevant biology.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6.
- ENCODE Project Consortium, 2012, *Nature*.
- Mattick et al., 2023, *Nature Reviews Molecular Cell Biology*, lncRNA definitions and functions.


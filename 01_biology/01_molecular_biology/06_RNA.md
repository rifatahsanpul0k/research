# 06. RNA and Major RNA Types

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

RNA, ribonucleic acid, is a nucleotide polymer usually made by transcription from DNA. RNA differs chemically from DNA by using ribose sugar and uracil instead of thymine. Major RNA types include mRNA, rRNA, tRNA, snRNA, snoRNA, miRNA, and long non-coding RNA; some RNAs carry protein-coding information, while others function as structural, catalytic, regulatory, or processing molecules [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26887/); [Mattick et al. 2023](https://www.nature.com/articles/s41580-022-00566-8).

## B. Biological mechanism

RNA molecules are synthesized by RNA polymerases and can fold into structures through intramolecular base pairing. mRNA carries codons to ribosomes; rRNA forms core ribosome components; tRNA adapts codons to amino acids; snRNA participates in splicing; miRNA and lncRNA can regulate expression at several levels [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26887/); [Mattick et al. 2023](https://www.nature.com/articles/s41580-022-00566-8).

## C. Relationships

RNA is produced by transcription and can be the final product of a gene. For protein-coding genes, mRNA is the template for translation. RNA abundance contributes to what researchers call gene expression.

## D. Experimental measurement

RNA can be measured by RNA-seq, single-cell RNA-seq, targeted panels, in situ hybridization, qPCR, nascent RNA assays, and spatial transcriptomics. Different protocols capture different RNA classes and regions, so a dataset's feature table must say what RNA population was measured.

## E. Numerical/computational representation

RNA measurements can be gene-level or transcript-level:

| cell_id | RNA_feature | count |
|---|---|---:|
| C1 | GeneA_mRNA | 8 |
| C1 | LncB_lncRNA | 2 |
| C2 | GeneA_mRNA | 1 |

The same biological sample can also be represented as a sparse cells x genes matrix.

## F. Relevance to our project

Single-cell data frequently measures RNA molecules at cell resolution. Spatial omics can localize RNA abundance in tissue. Multi-omics requires knowing whether RNA is being compared to DNA regions, protein features, or other modalities. Biological similarity inferred from RNA vectors may reflect cell identity, transient state, stress, cell cycle, or technical capture.

## G. Misconceptions

- Treating all RNAs as mRNAs.
- Treating gene-level counts as transcript isoform resolution.
- Assuming RNA abundance always predicts protein abundance.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6.
- Mattick et al., 2023, *Nature Reviews Molecular Cell Biology*.
- Baysoy et al., 2023, *Nature Reviews Molecular Cell Biology*, single-cell multi-omics modalities.


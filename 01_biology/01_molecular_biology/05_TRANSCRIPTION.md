# 05. Transcription

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

Transcription is the cellular process that copies information from a DNA template into RNA. It is the first step in reading many genes and a major control point for gene expression [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26887/).

## B. Biological mechanism

RNA polymerase opens a small region of DNA, uses one DNA strand as a template, and polymerizes ribonucleotides into an RNA molecule by complementary base pairing. Promoters and other regulatory elements help determine where transcription starts, while termination and RNA processing shape the final RNA product. In eukaryotes, transcription is coordinated with RNA processing and chromatin context [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26887/); [Shine et al. 2024](https://pubmed.ncbi.nlm.nih.gov/38509203/).

## C. Relationships

Transcription connects DNA, genes, coding/non-coding regions, and RNA. It precedes translation for protein-coding genes, but it can also produce functional RNAs that are not translated.

## D. Experimental measurement

Scientists observe transcription and transcript abundance using RNA sequencing, nascent RNA assays, single-molecule methods, reporter assays, and perturbation. Standard RNA-seq measures accumulated RNA molecules after biological and technical processing; it is not a direct movie of polymerase activity.

## E. Numerical/computational representation

Transcription-related data often becomes counts:

| cell_id | GeneA_RNA_count | GeneB_RNA_count |
|---|---:|---:|
| C1 | 8 | 0 |
| C2 | 1 | 6 |

The count is evidence of captured RNA molecules assigned to features, not a direct count of transcription initiation events.

## F. Relevance to our project

Single-cell transcriptomic data is often interpreted as gene expression, but the measured values are influenced by transcription, RNA processing, degradation, capture, sequencing depth, and alignment. Spatial omics attaches RNA measurements to locations. Multi-omics can combine transcriptional readouts with DNA, protein, or regulatory measurements. Similarity between cells may reflect shared transcriptional programs, but technical capture and timing can alter vectors.

## G. Misconceptions

- Treating RNA abundance as identical to transcription rate.
- Treating zero counts as proof that no transcription occurred.
- Forgetting that measured RNA may lag behind regulatory events or protein abundance.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6, From DNA to RNA.
- Shine et al., 2024, *Nature Reviews Molecular Cell Biology*, co-transcriptional gene regulation.
- Amezquita et al., 2020, *Genome Biology*, single-cell data sparsity and zero interpretation.


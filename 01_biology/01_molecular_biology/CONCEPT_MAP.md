# Phase 1A Concept Map

Status: Phase 1A concept map complete.

## Required chain

DNA -> regulatory regions -> gene -> transcription -> RNA -> translation -> protein -> cellular function

## Mechanistic links

| step | biological link | measurement form | computational form |
|---|---|---|---|
| DNA -> regulatory regions | DNA sequence contains promoters, enhancers, boundaries, and other regulatory elements | genome annotation, regulatory assays | interval table: `region_id, chr, start, end, type` |
| regulatory regions -> gene | regulatory elements influence when, where, and how much a gene is transcribed | promoter/enhancer annotation, perturbation, chromatin/contact evidence | region-to-gene table with evidence type |
| gene -> transcription | RNA polymerase copies a transcribed genomic region into RNA | RNA-seq, nascent RNA, reporter assays | count or signal assigned to gene/transcript |
| transcription -> RNA | transcription produces RNA molecules that may be processed, spliced, exported, localized, or degraded | RNA sequencing, qPCR, in situ methods | cells x RNA features matrix |
| RNA -> translation | ribosomes decode coding mRNA codons using tRNAs | ribosome profiling, protein synthesis assays | ribosome occupancy or translation proxy table |
| translation -> protein | amino acid chains fold and may be modified, localized, or degraded | proteomics, antibody assays | cells x protein features matrix |
| protein -> cellular function | proteins and functional RNAs execute cellular programs | perturbation, phenotyping, pathway evidence | labels, pathway scores, phenotype tables |

## Interpretation rule for later work

A numeric feature must be traced back to its biological level before interpretation:

`feature_id -> molecule measured -> assay -> annotation -> biological process -> uncertainty`

Example:

`GeneA count = 8 in C1` means eight captured molecules or molecule-derived counts assigned to GeneA under a specific assay and processing pipeline. It does not by itself prove high transcription rate, active translation, protein abundance, or cell identity.

## Sources

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6.
- Oudelaar and Higgs, 2021, *Nature Reviews Genetics*.
- Mattick et al., 2023, *Nature Reviews Molecular Cell Biology*.
- Baysoy et al., 2023, *Nature Reviews Molecular Cell Biology*.


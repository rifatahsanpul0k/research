# Promoters

## A. Biological meaning

A promoter is DNA associated with initiation of transcription. For RNA polymerase II, the core promoter lies around a transcription start site (TSS) and supports assembly of the initiation machinery. A proximal regulatory region contains nearby binding elements that modulate that process. There is no universal fixed promoter interval applicable to all genes.[^PROM]

## B. Mechanism

Core-promoter recognition can involve TFIID, including TATA-binding protein (TBP) and associated factors. General transcription factors and Pol II assemble an initiation complex, enabling DNA opening and the start of RNA synthesis; sequence-specific regulators and cofactors affect this process. Core-promoter sequence architectures differ: a TATA box is one possible element, not a universal requirement. Initiation may concentrate at one position or be dispersed across several positions.[^PROM]

An accessible promoter presents a binding opportunity. Productive transcription also requires appropriate factors and subsequent polymerase activity. Consequently, promoter accessibility, initiation and completed transcript production are separate properties.[^ACCESS][^PROM]

## C. Relationship to previous concepts

The promoter connects Phase 1A's DNA template to transcription initiation. The TSS is the first transcribed position for a particular transcript, whereas the translation start specifies the start of a coding sequence in mRNA. Alternative transcripts can use different promoters. Enhancers studied next influence promoter output without becoming the RNA coding sequence.[^PROM]

## D. Measurement

Mapping RNA 5-prime ends can identify TSS usage. ENCODE describes RAMPAGE as connecting initiation sites with transcript structures. Pol II or TF enrichment assays measure occupancy-related signals; accessibility assays measure enzyme access; reporter assays test a promoter in a construct. These are different observations, and a predicted promoter annotation is not a direct activity measurement.[^ENC][^PROM]

## E. Computational representation

Synthetic coordinates use a toy reference, 0-based half-open intervals [start,end), and strand relative to the reference:

| gene_id | transcript_id | chromosome | strand | TSS_0based | promoter_start | promoter_end | reference |
|---|---|---|---|---:|---:|---:|---|
| G1 | T1 | chrToy | + | 1000 | 800 | 1100 | toy-v1 |
| G2 | T2 | chrToy | - | 2000 | 1900 | 2200 | toy-v1 |

These are chosen windows, not biologically validated promoter boundaries. On the minus strand, upstream means toward larger coordinates. Record the window definition separately from a mapped TSS.

| observation_id | promoter_id | accessibility_fragments | TF_binding_evidence | gene_RNA_count |
|---|---|---:|---|---:|
| C1 | G1_T1_window | 3 | not_measured | 8 |
| C2 | G1_T1_window | 2 | not_measured | 0 |

Do not fill the TF-binding field from a motif match or accessibility count. In a gene-level RNA matrix, contributions from alternative promoters may already be combined.[^PROM]

## F. Relevance to our research

Future RNA/accessibility correspondence needs stable transcript and gene IDs, reference build, strand and TSS provenance. Spatial sampling may combine cells using different promoters. A promoter-to-gene mapping is annotation evidence; promoter activity is a context-specific biological quantity. Retain that distinction in any later representation.

## G. Common misconceptions

- Every promoter contains a TATA box.
- Every gene has exactly one promoter.
- Upstream always means a smaller chromosome coordinate.
- An accessible or Pol-II-occupied promoter guarantees abundant mature RNA.
- A convenient TSS-centered window is the experimentally established promoter.[^PROM][^ACCESS]

## H. Evidence

[^PROM]: Haberle V; Stark A (2018). [Eukaryotic core promoters and the functional basis of transcription initiation](https://pmc.ncbi.nlm.nih.gov/articles/PMC6205604/). Nature Reviews Molecular Cell Biology; review. Locator: Abstract; core-promoter sequence features, transcription initiation patterns, and TSS mapping.

[^ACCESS]: Klemm SL; Shipony Z; Greenleaf WJ (2019). [Chromatin accessibility and the regulatory epigenome](https://www.nature.com/articles/s41576-018-0089-8). Nature Reviews Genetics; review. Locator: Abstract; glossary nucleosome occupancy; accessibility remodelling passages.

[^ENC]: ENCODE Project Consortium; Moore JE; Purcaro MJ; Pratt HE; Epstein CB; Shoresh N; Adrian J; Kawli T; Davis CA; et al. (2020). [Expanded encyclopaedias of DNA elements in the human and mouse genomes](https://www.nature.com/articles/s41586-020-2493-4). Nature; database_resource_paper. Locator: Abstract; Figure 2 and candidate CRE registry description.


# Epigenetics

## A. Biological meaning

The term has multiple usages. A strict operational definition concerns a stable, heritable phenotype associated with chromosomal changes without a DNA-sequence alteration. A broader usage encompasses chromatin-associated regulation even when persistence through division has not been demonstrated. These meanings should be stated rather than silently exchanged.[^EPI][^CONT]

In these notes, epigenetic memory means experimentally supported persistence of a regulatory state. An epigenomic measurement is a snapshot of a selected molecular property; it does not by itself demonstrate memory.

## B. Mechanism

Maintenance of DNA methylation after replication provides one mechanism by which regulatory information can persist in dividing cells. Histone-associated mechanisms and regulatory feedback also contribute to maintenance or re-establishment of chromatin states. Establishment, persistence and resetting are distinct processes.[^METH][^EPI]

Cell identity can be stabilized while remaining responsive to changing developmental conditions. A short-lived signal-induced change is regulation, but requires additional persistence evidence before it satisfies a heritability-based definition of epigenetics.[^EPI]

## C. Relationship to previous concepts

    DNA sequence change: altered nucleotide sequence
    regulatory state change: altered molecular readout context
    epigenetic memory: persistence demonstrated under a stated definition

Methylating a cytosine modifies a DNA base chemically without substituting the underlying C in the conventional sequence. A histone modification acts on protein. Accessibility is a physical property measured with a probe; it is neither DNA methylation nor a specific histone modification.[^METH][^HIST][^CONT]

These states act on Phase 1A's expression chain. They do not add a second protein-coding alphabet.

## D. Measurement

Methylation assays, histone-directed enrichment and accessibility assays examine different chromatin-associated properties. To establish memory, follow persistence over time or cell divisions and test whether a state remains after the inducing signal is removed. A single cross-sectional comparison cannot distinguish persistent memory from continued exposure to a signal.[^EPI][^METH]

## E. Computational representation

Synthetic experimental-design table, not results:

| lineage_id | time | divisions_since_signal | signal_present | sequence_changed | regulatory_state | persistence_evidence |
|---|---|---:|---|---|---|---|
| L1 | t0 | 0 | yes | not_assessed | state_A | induction_only |
| L1 | t1 | 2 | no | not_assessed | state_A | candidate_persistence |

A valid interpretation would additionally require controls, an operational state measurement and evidence about sequence stability. The table shows why an observation-by-mark matrix cannot itself supply all criteria for epigenetic inheritance.

## F. Relevance to our research

Future multimodal similarity may describe present state or persistent identity; those are different questions. Spatially separated cells might differ through local signals, history or lineage. Keep time, exposure and lineage provenance separate from molecular scores. Dataset labels alone cannot establish epigenetic causation.

## G. Common misconceptions

- Every expression difference is epigenetic.
- Every histone mark is independently inherited.
- Epigenetics means completely independent of DNA sequence.
- A transient accessibility change proves regulatory memory.
- Persistence through cell division proves transmission across organismal generations.

The last inference requires a different study design and is not part of this phase.[^EPI][^METH]

## H. Evidence

[^EPI]: Berger SL; Kouzarides T; Shiekhattar R; Shilatifard A (2009). [An operational definition of epigenetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3959995/). Genes & Development; perspective_consensus. Locator: Operational definition; epigenator, initiator and maintainer discussion.

[^CONT]: Mansisidor AR; Risca VI (2022). [Chromatin accessibility: methods, mechanisms, and biological insights](https://pmc.ncbi.nlm.nih.gov/articles/PMC9683059/). Nucleus; review. Locator: Defining and measuring chromatin accessibility; A continuum of chromatin states; Table 1.

[^METH]: Li E; Zhang Y (2014). [DNA Methylation in Mammals](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996472/). Cold Spring Harbor Perspectives in Biology; review. Locator: Overview; DNMT and TET mechanisms; methylation measurement discussion.

[^HIST]: Bannister AJ; Kouzarides T (2011). [Regulation of chromatin by histone modifications](https://pmc.ncbi.nlm.nih.gov/articles/PMC3193420/). Cell Research; review. Locator: Acetylation; lysine methylation; euchromatin and heterochromatin.


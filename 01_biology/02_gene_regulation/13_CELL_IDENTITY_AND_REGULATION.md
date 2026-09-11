# Cell identity and regulatory state

## A. Biological meaning

Cell identity describes a relatively persistent organization of molecular programs and functions; cell state emphasizes condition-dependent variation. Operational boundaries depend on the biological question. Cells with essentially the same genome can differ in transcription and protein function. Current state and developmental ancestry are related but distinct properties.[^REG][^LINE]

## B. Mechanism

The conceptual chain is:

    Genome
      + regulatory elements
      + chromatin state
      + TF activity
      + epigenetic state
        -> gene-expression program
        -> protein program
        -> cell state / identity

These are interacting, partly overlapping descriptions; chromatin and epigenetic state are not independent additive variables. Some regulation persists, while other changes depend on continuing signals. Protein activity and feedback can further affect transcription.[^EPI][^PROT]

## C. Relationship to previous concepts

The chain extends Phase 1A with mechanisms governing DNA readout. It allows the same sequence to support different accessibility and RNA patterns. RNA and protein need not change synchronously because synthesis, removal and modification occur at different steps.[^REG]

Identical DNA is a simplifying comparison, not a claim that every cell in an organism has exactly the same genome: the foundational shared-genome argument already allows specialized exceptions. Dataset-specific genetic identity remains unverified.[^REG]

## D. Measurement

A molecular state can be characterized by expression, chromatin or protein measurements; function requires an appropriate functional observation. Lineage tracing addresses ancestry. Cross-sectional similarity does not establish lineage, stable identity or function, and no single molecular modality fully observes the cell.[^LINE][^PROT]

## E. Computational representation

Synthetic counterexample with equal measured RNA:

| cell | sequence_assumption | RNA_G1 | RNA_G2 | region_E1_accessibility | TF1_nuclear_fraction | function_test |
|---|---|---:|---:|---:|---:|---|
| A | shared | 8 | 2 | 1 | 0.1 | unknown |
| B | shared | 8 | 2 | 4 | 0.8 | unknown |

Counts and fractions are hypothetical and assay-specific. The RNA vectors are identical but other observations differ. Neither row receives a cell-type label or function claim from this table.

A second possible outcome is convergent RNA output from different regulatory configurations. This is a hypothesis consistent with multiple regulatory inputs, not a finding in our project. Preserve separately which modalities are measured, matched and missing.

## F. Relevance to our research

Biological similarity must have a stated target: shared identity, transient state, function, lineage or regulatory potential. Tissue position can help define context but is not itself equivalence. The research implication is to retain context and evidence, not to assume that adding modalities automatically yields a correct similarity measure.

## G. Common misconceptions

Equal sequence does not mean equal regulatory state; equal RNA does not establish equal protein activity; different state need not mean different type; nearby cells need not be related by ancestry. A state label inferred from the same matrix is not independent validation of that matrix's biological meaning.[^REG][^LINE][^PROT]

## H. Evidence

[^REG]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [An Overview of Gene Control](https://www.ncbi.nlm.nih.gov/books/NBK26885/). Molecular Biology of the Cell, 4th edition; textbook_reference. Locator: Figure 7-5 and sections on different cell types and levels of gene control.

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). Nature Reviews Genetics; review. Locator: Introduction; Inferring cell histories in lineage tracing.

[^EPI]: Berger SL; Kouzarides T; Shiekhattar R; Shilatifard A (2009). [An operational definition of epigenetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3959995/). Genes & Development; perspective_consensus. Locator: Operational definition; epigenator, initiator and maintainer discussion.

[^PROT]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/). Molecular Biology of the Cell, 4th edition; textbook_reference. Locator: Many Changes in Proteins Are Driven by Phosphorylation.


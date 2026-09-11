# Transcription factors

## A. Biological meaning

Here, sequence-specific TF means a protein that recognizes DNA sequence patterns and participates in transcriptional control. General transcription factors assemble core transcription machinery. Cofactors assist regulatory complexes and need not themselves recognize a DNA motif. Activator and repressor describe effects in a context, not necessarily an immutable property of a protein.[^TF][^PROM]

## B. Mechanism

DNA-binding domains favor particular sequences, summarized as motifs. Binding depends on motif sequence, chromatin and other proteins. Combinations of regulators recruit cofactors and influence transcription; a motif is a binding preference, not a record of occupancy.[^TF]

TF RNA abundance is separated from function by translation, turnover, localization, modification and partner availability. For example, phosphorylation can change protein interactions and localization without changing its RNA. Even an available nuclear TF needs an appropriate target environment.[^PROT][^ACCESS]

Thus:

    TF-gene RNA expression
      -> possible TF protein availability
      -> context-dependent binding and regulatory action

None of these arrows is a one-to-one conversion. High expression of a transcription-factor gene does not necessarily imply high transcription-factor activity.

## C. Relationship to previous concepts

TFs are proteins from Phase 1A that act on promoters, enhancers and other elements from topics 2-4. They connect protein state back to transcription. This feedback regulates sequence readout; it does not transfer amino-acid sequence into DNA.[^TF][^DOGMA]

## D. Measurement

| Approach | Quantity or evidence | Limitation |
|---|---|---|
| RNA abundance | TF transcript signal | Not protein activity |
| Protein detection/localization | Abundance or compartment | Not automatically transcriptional effect |
| DNA-binding assay | Binding specificity | In vitro preference need not equal in-cell occupancy |
| ChIP-type enrichment | Protein-associated genomic DNA | Association does not prove direct binding or regulation |
| TF perturbation and target readout | Regulatory response | Can include indirect responses |

TF-binding specificity and developmental function require more than a single assay.[^TF]

## E. Computational representation

An illustrative position-probability matrix P has dimensions 4 x L, with rows A,C,G,T and columns motif positions; L is motif length. For L=2:

| Base | position_1 | position_2 |
|---|---:|---:|
| A | 0.7 | 0.1 |
| C | 0.1 | 0.1 |
| G | 0.1 | 0.7 |
| T | 0.1 | 0.1 |

Each column sums to 1. These toy probabilities describe sequence preference, not probability of TF binding in a cell. Related TFs can have similar motifs.[^TF]

| observation_id | TF1_RNA_count | TF1_protein | nuclear_fraction | activity_evidence |
|---|---:|---|---|---|
| C1 | 20 | not_measured | not_measured | unknown |
| C2 | 3 | not_measured | not_measured | unknown |

No activity ranking follows from these invented RNA counts.

## F. Relevance to our research

Future regulatory networks must distinguish TF transcript, protein, motif, occupancy and inferred activity features. Similar motif-associated accessibility profiles need not identify the same active TF. In spatial data, tissue position supplies context but cannot substitute for activity evidence. Any representation must retain the origin of its TF features.

## G. Common misconceptions

Motif occurrence is not binding; binding is not regulatory effect; TF RNA is not TF activity; target co-expression does not establish direct regulation. A cofactor is not necessarily a sequence-specific TF.[^TF][^PROT]

## H. Evidence

[^TF]: Spitz F; Furlong EEM (2012). [Transcription factors: from enhancer binding to developmental control](https://www.nature.com/articles/nrg3207). Nature Reviews Genetics; review. Locator: Abstract; binding specificity, combinatorial regulation and developmental control.

[^PROM]: Haberle V; Stark A (2018). [Eukaryotic core promoters and the functional basis of transcription initiation](https://pmc.ncbi.nlm.nih.gov/articles/PMC6205604/). Nature Reviews Molecular Cell Biology; review. Locator: Abstract; core-promoter sequence features, transcription initiation patterns, and TSS mapping.

[^PROT]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/). Molecular Biology of the Cell, 4th edition; textbook_reference. Locator: Many Changes in Proteins Are Driven by Phosphorylation.

[^ACCESS]: Klemm SL; Shipony Z; Greenleaf WJ (2019). [Chromatin accessibility and the regulatory epigenome](https://www.nature.com/articles/s41576-018-0089-8). Nature Reviews Genetics; review. Locator: Abstract; glossary nucleosome occupancy; accessibility remodelling passages.

[^DOGMA]: Crick F (1970). [Central Dogma of Molecular Biology](https://www.nature.com/articles/227561a0). Nature; conceptual_article. Locator: Abstract; sequence-information transfer definition.


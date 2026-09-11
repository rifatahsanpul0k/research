# Enhancer-promoter interactions

## A. Biological meaning

An enhancer-promoter interaction may refer to physical proximity, a biochemical regulatory relationship, or a computational prediction. State which meaning is intended. Distal regulation allows one region to contribute to several genes and several regions to contribute to one gene; mapping these relationships is context-dependent.[^ENH][^LINK]

## B. Mechanism

Enhancer-bound regulators can influence promoter activation through interactions among proteins and chromatin. Genomic organization can favor some encounters and restrict others, while biochemical compatibility also matters. There is no universally settled mechanism that turns a given measured contact into a fixed transcriptional response.[^SELECT]

Contact, activation and RNA accumulation have different temporal meanings. An enhancer-promoter pair may be physically permissive before substantial output is detected. This makes a static contact-to-expression correspondence an incomplete description.[^ENH]

## C. Relationship to previous concepts

Topics 2-10 established local regulatory elements, TFs and chromatin context. Distal regulation connects that context to a target beyond immediate sequence adjacency. It does not change Phase 1A's distinction between a gene and its associated regulatory DNA.

Illustrative proposed relationships:

    E1 -> G1
    E1 -> G3
    E2 -> G1
    E3 -> G2

These are synthetic hypotheses; arrows are not observations or constructed research graphs.

## D. Measurement

Chromosome-conformation assays report proximity-related signals, often across a population. Imaging measures locus positions at its resolution. Reporters measure regulatory capability in a construct. Endogenous region perturbation plus target RNA measurement tests an effect in a particular context. These assays address complementary questions.[^ENH]

Fulco and colleagues used CRISPR perturbations to test regulatory relationships and to assess predictions. A predicted relationship must remain labeled inferred even when other relationships in the same study were experimentally tested. A perturbation effect also needs specificity controls and does not automatically reveal every intervening mechanism.[^LINK]

## E. Computational representation

Let R have q region rows and p gene columns. For the example above q=3 and p=3. The table records candidate status only:

| region | G1 | G2 | G3 |
|---|---|---|---|
| E1 | candidate | unknown | candidate |
| E2 | candidate | unknown | unknown |
| E3 | unknown | candidate | unknown |

Do not replace unknown with a verified-negative zero. A numerical R needs an explicit value definition: a binary call, effect size, arbitrary weight or calibrated probability has different meaning.

An edge list, rectangular matrix, bipartite relation, weighted network, probabilistic table, tensor across contexts, set of targets, knowledge graph, hypergraph for jointly supported multiway relationships, or learned latent representation could describe selected aspects. Pairwise records alone do not justify simultaneous multiway interactions. These are unranked storage/abstraction possibilities, not implemented methods.

## F. Relevance to our research

Future regulatory annotations must preserve source context, target transcript/promoter where relevant, assay, direction, effect and uncertainty. A spatial tissue coordinate cannot identify a nuclear enhancer-promoter contact. RNA-plus-ATAC correspondence needs mapping evidence beyond feature proximity. The biological relationship does not select graphs or any other representation as preferred.

## G. Common misconceptions

Physical interaction is not necessarily functional regulation; prediction is not experimental verification; one enhancer does not imply one target; absence of a tested effect is conditional on assay sensitivity and context.[^ENH][^LINK]

## H. Evidence

[^ENH]: Friedman MJ; Wagner T; Lee H; Rosenfeld MG; Oh S (2024). [Enhancer-promoter specificity in gene transcription: molecular mechanisms and disease associations](https://www.nature.com/articles/s12276-024-01233-y). Experimental & Molecular Medicine; review. Locator: Introduction; Identification of enhancer-promoter interactions; Functional validation of enhancers.

[^LINK]: Fulco CP; Nasser J; Jones TR; Munson G; Bergman DT; Subramanian V; Grossman SR; Anyoha R; Doughty BR; Patwardhan TA; Nguyen TH; Kane M; Perez EM; Durand NC; Lareau CA; Stamenova EK; Aiden EL; Lander ES; Engreitz JM (2019). [Activity-by-contact model of enhancer-promoter regulation from thousands of CRISPR perturbations](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886585/). Nature Genetics; primary_research. Locator: Abstract; CRISPR perturbation evidence and candidate-link motivation.

[^SELECT]: Yang JH; Hansen AS (2024). [Enhancer selectivity in space and time: from enhancer-promoter interactions to promoter activation](https://www.nature.com/articles/s41580-024-00710-6). Nature Reviews Molecular Cell Biology; review. Locator: Abstract and figure descriptions 1-4.


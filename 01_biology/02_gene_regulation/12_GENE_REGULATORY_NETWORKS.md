# Gene regulatory networks

## A. Biological meaning

A gene regulatory network describes relationships among regulators and gene outputs. A regulator can be represented as a TF gene for naming convenience, although its protein is commonly the acting molecule. A target is the gene or transcript whose production is affected. Activation increases and repression decreases output relative to a specified context and intervention.[^TF]

## B. Mechanism

Direct transcriptional regulation involves a regulator acting at the target's regulatory machinery. An indirect response passes through intermediates. For example, TF1 may regulate a second regulator that changes G2; TF1 and G2 need not have a direct binding relationship. Coordinated regulators and targets can form regulatory modules, but a shared expression pattern alone does not establish shared direct control.[^TF][^REG]

Feedback can maintain programs or produce changing states. A static signed edge omits concentration, timing, cofactors and context. The network is an abstraction of regulation, not the entire molecular mechanism.

## C. Relationship to previous concepts

The shorthand TF_i -> Gene_j compresses multiple steps:

    TF protein availability/activity
      -> action at relevant regulatory DNA and complexes
      -> altered transcription
      -> altered RNA abundance after processing and turnover

An enhancer-to-gene relationship and a TF-to-gene relationship are different entity relationships. Do not equate them simply because both can be drawn as arrows.[^TF][^ENH]

## D. Measurement

| Evidence | Appropriate interpretation |
|---|---|
| TF/target RNA correlation | Statistical association; common inputs and indirect paths possible |
| Motif match in candidate regulatory DNA | Sequence compatibility |
| Occupancy-related enrichment | TF-associated chromatin evidence |
| TF perturbation with target response | Experimental regulatory effect, potentially indirect |
| Occupancy plus specific cis-element perturbation and response | Stronger support for a direct mechanism in tested conditions |

Experiments and inferred predictions answer different questions; combining evidence does not remove its context dependence.[^TF][^LINK]

## E. Computational representation

For r regulators and p targets, define a rectangular effect table A in real r x p space, with A_ij the target log2 RNA fold change after a specified perturbation of regulator i. This is a response matrix, not automatically a direct-regulation adjacency matrix. Inhibiting an activator can produce a negative response, so response sign and regulatory sign must be separate.

Synthetic long table:

| regulator | target | relation_sign | directness | evidence_type | context |
|---|---|---|---|---|---|
| TF1 | G1 | unknown | unknown | correlation_inferred | toy_A |
| TF1 | G2 | positive_candidate | unknown | loss_of_function_response | toy_A |
| TF2 | G3 | negative_candidate | direct_candidate | binding_and_cis_perturbation | toy_B |

No row is a real interaction. Source IDs, interventions, controls, effect estimates, uncertainty and measurement time would be required for empirical rows.

Plausible forms include edge list, adjacency matrix, bipartite graph, weighted network, probability matrix, feature vector, latent embedding, tensor, set and knowledge graph. A square adjacency matrix requires a unified node inventory; a TF-by-target matrix may be rectangular. No form is selected or benchmarked.

## F. Relevance to our research

Future multimodal similarity might ask whether cells share regulator availability, target output or regulatory relationships. Those are distinct biological questions. Spatial co-location is contextual evidence, not proof of intracellular regulation. Store experimentally supported and computationally inferred interactions separately even when they share IDs.

## G. Common misconceptions

Correlation does not prove a directed edge; TF expression is not activity; a perturbation response is not necessarily direct; regulatory sign cannot be read blindly from a knockout fold change; an inferred probability requires calibration before being called a probability of biological truth.[^TF][^LINK]

## H. Evidence

[^TF]: Spitz F; Furlong EEM (2012). [Transcription factors: from enhancer binding to developmental control](https://www.nature.com/articles/nrg3207). Nature Reviews Genetics; review. Locator: Abstract; binding specificity, combinatorial regulation and developmental control.

[^REG]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [An Overview of Gene Control](https://www.ncbi.nlm.nih.gov/books/NBK26885/). Molecular Biology of the Cell, 4th edition; textbook_reference. Locator: Figure 7-5 and sections on different cell types and levels of gene control.

[^ENH]: Friedman MJ; Wagner T; Lee H; Rosenfeld MG; Oh S (2024). [Enhancer-promoter specificity in gene transcription: molecular mechanisms and disease associations](https://www.nature.com/articles/s12276-024-01233-y). Experimental & Molecular Medicine; review. Locator: Introduction; Identification of enhancer-promoter interactions; Functional validation of enhancers.

[^LINK]: Fulco CP; Nasser J; Jones TR; Munson G; Bergman DT; Subramanian V; Grossman SR; Anyoha R; Doughty BR; Patwardhan TA; Nguyen TH; Kane M; Perez EM; Durand NC; Lareau CA; Stamenova EK; Aiden EL; Lander ES; Engreitz JM (2019). [Activity-by-contact model of enhancer-promoter regulation from thousands of CRISPR perturbations](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886585/). Nature Genetics; primary_research. Locator: Abstract; CRISPR perturbation evidence and candidate-link motivation.


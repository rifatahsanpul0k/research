# Gene regulation and chromatin concept map

Read the numbered notes in order, starting with [gene regulation](01_GENE_REGULATION_OVERVIEW.md). The biological chain below extends [Phase 1A](../01_molecular_biology/CONCEPT_MAP.md). Arrows summarize relationships; they do not establish a measured interaction in our datasets.

## Regulatory chain

    DNA sequence / genome
      -> promoters, enhancers, silencers and boundary contexts
      -> chromatin organization
      -> graded, probe-dependent accessibility
      -> opportunities for TF binding
      -> context-dependent transcriptional regulation
      -> RNA production, processing and turnover
      -> translation and protein turnover
      -> protein activity and cellular function

    DNA methylation and histone modifications
      <-> chromatin organization and regulator binding

    Protein/TF activity
      -> feedback onto transcription and chromatin regulation

The sequence, occupancy and chromatin relationships are reciprocal and context-dependent, so the diagram is not a one-way causal pipeline.[^REG][^ACCESS][^METH][^TF]

## Same sequence, different outcomes

    shared genome
      + regulatory element usage
      + chromatin and epigenetic state
      + TF availability and activity
      + developmental/environmental context
        -> expression program
        -> protein program
        -> cell identity / state / function

The plus signs denote interacting influences. Chromatin and epigenetic state overlap conceptually; protein quantity and activity are distinct. RNA abundance is an output of synthesis and removal.[^REG][^PROT][^EPI]

## Concepts, mechanisms and observations

| Topic | Mechanistic link | Observation to distinguish |
|---|---|---|
| [Regulation](01_GENE_REGULATION_OVERVIEW.md) | Control at multiple levels | RNA abundance versus synthesis or protein activity |
| [Promoters](02_PROMOTERS.md) | Initiation near a TSS | Mapped initiation versus chosen annotation window |
| [Enhancers](03_ENHANCERS.md) | Contextual activation of promoters | Candidate mark versus endogenous functional effect |
| [Other elements](04_OTHER_REGULATORY_ELEMENTS.md) | Repression or restricted communication | Silencer assay versus structural boundary |
| [TFs](05_TRANSCRIPTION_FACTORS.md) | Sequence/context-dependent regulatory action | RNA, protein, motif, occupancy and activity |
| [Chromatin](06_CHROMATIN.md) | Dynamic DNA-protein organization | Local protection versus genomic contacts |
| [Accessibility](07_CHROMATIN_ACCESSIBILITY.md) | Physical opportunity for interaction | Probe susceptibility versus expression |
| [Epigenetics](08_EPIGENETICS.md) | Establishment and persistence of regulatory state | Snapshot versus demonstrated memory |
| [Methylation](09_DNA_METHYLATION.md) | Context-dependent DNA modification | Modified-base fraction with coverage |
| [Histone marks](10_HISTONE_MODIFICATIONS.md) | Protein modifications in chromatin | Enrichment versus activity or causation |
| [Distal interactions](11_ENHANCER_PROMOTER_INTERACTIONS.md) | Many-to-many contextual regulation | Contact versus regulatory effect |
| [GRNs](12_GENE_REGULATORY_NETWORKS.md) | Regulators influence targets directly or indirectly | Experimental support versus inference |
| [Identity/state](13_CELL_IDENTITY_AND_REGULATION.md) | Molecular programs and function | Similar measurements versus equivalence |
| [Development](14_DEVELOPMENTAL_REGULATION_BRIDGE.md) | Changing programs and ancestry | Stage, inferred ordering and lineage |

Each linked topic contains its mechanism-specific evidence and measurement limits.

## Evidence paths

    motif occurrence -> sequence-compatible candidate
    accessibility -> measured opportunity under one assay
    TF-associated enrichment -> occupancy-related support
    locus contact -> proximity-related support
    targeted perturbation + response + controls -> contextual functional evidence

These are complementary paths, not a universal ordinal ranking. A binding experiment can answer occupancy better than an indirect perturbation response; causal specificity needs a suitable intervention and controls.[^ENH][^LINK]

## Repository rule for every relationship

    entity IDs + relation meaning + context + assay/source
      + measured/inferred status + units + uncertainty + missingness

These bookkeeping requirements apply equally to tables, matrices, edge lists, bipartite relations, networks, graphs, hypergraphs, tensors, sets, probabilistic relationships, knowledge graphs and latent representations. The diagram expresses no representation preference.

## Evidence

[^REG]: Alberts et al. (2002), [An Overview of Gene Control](https://www.ncbi.nlm.nih.gov/books/NBK26885/), levels of control and Figure 7-5.
[^ACCESS]: Klemm et al. (2019), [Chromatin accessibility and the regulatory epigenome](https://www.nature.com/articles/s41576-018-0089-8), accessibility remodelling.
[^METH]: Li and Zhang (2014), [DNA Methylation in Mammals](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996472/), Overview.
[^TF]: Spitz and Furlong (2012), [Transcription factors](https://www.nature.com/articles/nrg3207), combinatorial developmental regulation.
[^PROT]: Alberts et al. (2002), [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/), protein phosphorylation.
[^EPI]: Berger et al. (2009), [An operational definition of epigenetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3959995/), definition and maintenance.
[^ENH]: Friedman et al. (2024), [Enhancer-promoter specificity](https://www.nature.com/articles/s12276-024-01233-y), interaction identification and functional validation.
[^LINK]: Fulco et al. (2019), [Activity-by-contact study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886585/), perturbation evidence versus predictions.


# Regulatory biology to tabular data

## Scope and interpretation

This document connects biology to numerical records. Examples are synthetic: C1-C3, Gene A-C, Peak 1-4, coordinates and all numerical values are invented. They do not describe any of the six registered datasets. Assay principles are included only to explain values; no assay pipeline, integration model or regulatory graph is implemented.

    regulatory biology
      -> experimental measurement
      -> sequence/readout processing and feature assignment
      -> numerical table + metadata + evidence provenance

The underlying regulation, what the assay responds to, and the stored value are three distinct levels.[^REG][^CONT]

## RNA: observed output

For n observations and p gene features:

\[
X_{\mathrm{RNA}}\in\mathbb{R}^{n\times p}.
\]

Rows are explicitly identified observations: cells, nuclei or spatial sampling units as documented by the assay. Columns are gene IDs associated with an annotation release. Real-valued notation accommodates processed values; an untransformed count table has nonnegative integer entries. RNA abundance reflects production and removal, so it is not a direct transcription-rate measurement.[^REG]

Synthetic count example, n=3 and p=3:

| observation | Gene A | Gene B | Gene C |
|---|---:|---:|---:|
| C1 | 8 | 0 | 3 |
| C2 | 1 | 6 | 2 |
| C3 | 7 | 0 | 4 |

For this example, define values as captured RNA molecule-derived counts assigned to genes. A real table may instead contain reads, deduplicated molecular identifiers or transformed signals. Metadata must establish which. An observed zero records no assigned count, not proof that the cell cannot express the gene. Phase 1A explains [RNA count interpretation](../01_molecular_biology/BIOLOGY_TO_DATA.md).

## Accessibility: observed regulatory opportunity

For n observations and q genomic regions:

\[
X_{\mathrm{ATAC}}\in\mathbb{R}^{n\times q}.
\]

The measurement-level path is:

    DNA in chromatin
      -> Tn5 access and adapter insertion
      -> sequenced DNA fragments
      -> reference mapping and observation assignment
      -> defined genomic regions
      -> counts under an explicit counting rule

This describes the assay's signal origin, not an analysis protocol.[^ATAC]

With n=3 and q=4:

| observation | Peak 1 | Peak 2 | Peak 3 | Peak 4 |
|---|---:|---:|---:|---:|
| C1 | 1 | 0 | 3 | 0 |
| C2 | 0 | 2 | 1 | 4 |
| C3 | 5 | 0 | 0 | 1 |

Here values mean deduplicated fragments overlapping each interval. They are not gene counts, TF molecules, accessible-allele counts or expression values. Other counting conventions count insertion ends or binary detection. The synthetic 5 is a bookkeeping example, not five accessible alleles; real values require ploidy, barcode and counting-rule checks.

The following metadata gives the otherwise opaque peak labels a meaning:

| peak_id | chromosome | start | end | reference | proposed_role |
|---|---|---:|---:|---|---|
| Peak 1 | chrToy | 800 | 1100 | toy-v1 | promoter_window_candidate |
| Peak 2 | chrToy | 3000 | 3300 | toy-v1 | unknown |
| Peak 3 | chrToy | 5000 | 5400 | toy-v1 | enhancer_candidate |
| Peak 4 | chrToy | 7000 | 7200 | toy-v1 | unknown |

Coordinates are 0-based half-open. These artificial annotations are not functional evidence. In particular, ATAC enrichment makes a region a candidate for interpretation, not a validated enhancer.[^ENC]

### Zeros and missingness

A zero can result from little biological access or failure to capture/retain evidence. Probe bias, limited sampling and chromatin dynamics affect what is observed.[^CONT] An unmeasured modality is a different situation.

Define an availability mask W_ATAC in {0,1}^(n x q): 1 means a value was recorded under the assay's feature scheme; 0 means unavailable. A recorded count of zero can have W_ATAC=1. The mask does not claim every accessible molecule was detected. Retain both count and availability rather than replacing all unknowns with zeros.

A binary detection table can summarize counts as present/absent evidence, but it does not convert accessibility biology into an on/off switch.

## Regulatory relationships: evidence about mapping

With q regions and p genes:

\[
R\in\mathbb{R}^{q\times p}.
\]

R_ij can encode evidence concerning region i and gene j, once its semantics are defined. Let i index regions and j genes. Multiple legitimate definitions exist:

| R value type | Example interpretation | Required qualification |
|---|---|---|
| Binary | 1 denotes a call meeting a specified criterion | 0 may mean not called, not a proven negative |
| Weighted | Contact enrichment, effect size or score | Units and scale; weights are not probabilities by default |
| Probabilistic | Estimated probability of a defined interaction | Conditioning context and calibration evidence |
| Experimentally supported | Value derived from a controlled perturbation | Tested intervention, direction, time and specificity |
| Computationally inferred | Value produced from associations or a prediction procedure | Inputs, assumptions and lack of direct verification |

The first three describe value encodings; the last two describe evidence provenance. They are independent axes. A binary value can be either inferred or experimentally supported. A confidence score is not automatically calibrated, and an experiment does not remove uncertainty.[^ENH][^LINK]

### One transparent numerical example

Define R_call as a binary table of declared *candidate links*, with q=4 and p=3:

| region | Gene A | Gene B | Gene C |
|---|---:|---:|---:|
| Peak 1 | 1 | 0 | 0 |
| Peak 2 | 0 | 0 | 0 |
| Peak 3 | 1 | 0 | 1 |
| Peak 4 | 0 | 1 | 0 |

Here 1 means included in this invented candidate list; 0 means absent from that list. No zeros are verified negatives. A separate relation-status table records whether a pair is untested, inconclusive, supported or not supported under a specified test.

| region | gene | evidence | effect | confidence | status |
|---|---|---|---|---|---|
| Peak 1 | Gene A | proximity_annotation | unknown | uncalibrated | inferred_candidate |
| Peak 3 | Gene A | hypothetical_contact | unknown | unknown | contact_only |
| Peak 3 | Gene C | hypothetical_perturbation | -0.7 log2 RNA change | unknown | illustrative_tested_response |
| Peak 4 | Gene B | hypothetical_correlation | unknown | uncalibrated | inferred_candidate |

All rows are synthetic. The perturbation row would require assay, controls and sample context before it could support a real conclusion. In an actual registry, record evidence per pair rather than assigning the same status to an entire source study.

### Dimension compatibility does not establish biology

X_ATAC has shape n x q and R has shape q x p. Their product would therefore have shape n x p. This dimensional fact alone does not make the product measured RNA or prove a causal model of expression. It would discard or combine distinct assumptions about region activity, link weights and context. No such product is calculated here.

## Observation alignment is a biological claim

Using the same n in two matrices is justified only when their rows genuinely refer to the same observations, in the same documented order. If RNA and accessibility were measured in different cells, write n_RNA and n_ATAC separately and keep a correspondence table with provenance. Matching row names or tissue labels does not establish paired measurement.

| observation_id | sample_id | observation_unit | RNA_available | ATAC_available | pairing_evidence | tissue_x | tissue_y |
|---|---|---|---|---|---|---|---|
| C1 | toy_sample | cell | yes | yes | assumed_only_for_example | NA | NA |
| C2 | toy_sample | cell | yes | yes | assumed_only_for_example | NA | NA |
| C3 | toy_sample | cell | yes | yes | assumed_only_for_example | NA | NA |

For spatial units, coordinates describe sampling position in tissue, with units and reference frame required. Genomic coordinates instead locate DNA features. Neither coordinate system can substitute for the other. If one spatial observation contains several cells, its regulatory and expression signals can be mixtures; actual observation units remain unknown in our registry.

## Additional tabular forms

| Biology/evidence | Possible table | Value interpretation |
|---|---|---|
| DNA methylation | observation x CpG site, plus coverage | Modified-base fraction; NA for absent coverage |
| Histone modifications | region x mark, plus sample | Assay enrichment, not deterministic activity |
| TF motif | base x motif position | Sequence preference, not cell-specific binding |
| TF regulation | regulator x target or long relation table | Experimental response or inferred relationship |
| Development | observation x metadata | Supplied stage, measured lineage or inferred state |

Mechanistic details and measurement limits are in [methylation](09_DNA_METHYLATION.md), [histone modifications](10_HISTONE_MODIFICATIONS.md), [TFs](05_TRANSCRIPTION_FACTORS.md) and [development](14_DEVELOPMENTAL_REGULATION_BRIDGE.md).

## Numerical similarity versus biological equivalence

Two similar numerical vectors do not automatically imply two biologically equivalent cells.

| Similarity scenario | Unresolved biological question |
|---|---|
| Similar RNA | Are protein activity and regulatory potential similar? |
| Similar accessibility | Are the same TFs bound and the same targets expressed? |
| Shared zeros | Is this shared biology or limited sampling? |
| Similar region-to-gene scores | Were links tested or merely inferred from shared inputs? |
| Similar stage-associated profiles | Are cells related by lineage, or only similarly measured? |
| Similar spatial aggregates | Do they contain the same cell proportions and states? |

Regulation operates across distinct molecular levels; accessibility is permissive, protein activity has additional controls, and lineage differs from present state.[^REG][^CONT][^PROT][^LINE] These mechanisms motivate the questions; no answer is inferred for our data.

## Representation-neutral record

All of the following are plausible forms, depending on the information being retained: table, count matrix, edge list, adjacency matrix, bipartite graph, weighted network, probability matrix, feature vector, learned latent embedding, tensor, set, knowledge graph and hypergraph. Multiway relations require evidence or an explicit joint hypothesis; pairwise links do not establish them.

Every form must define entities, values, units, context, evidence and missingness. This phase encounters these forms without ranking, constructing or learning them.

## Comprehension checks

1. C1 has zero at Peak 2. Can we call it inaccessible? No: zero is an observation outcome under a counting rule.
2. Peak 3 contacts Gene C. Is it causal regulation? Not from contact alone.
3. TF RNA doubles. Has TF activity doubled? Not established without protein and regulatory evidence.
4. Promoter methylation and gene-body methylation increase. Must both genes decrease expression? No unconditional mapping is valid.
5. Both matrices have three rows. Are modalities paired? Only with observation-level provenance.
6. E11 and E13 cells have similar RNA. Does that prove ancestry? No: lineage needs distinct evidence.

These checks apply the mechanisms and distinctions in the numbered notes, rather than testing an implemented model.

## Evidence

[^REG]: Alberts et al. (2002), [An Overview of Gene Control](https://www.ncbi.nlm.nih.gov/books/NBK26885/), Figure 7-5 and control levels.
[^CONT]: Mansisidor and Risca (2022), [Chromatin accessibility: methods, mechanisms, and biological insights](https://pmc.ncbi.nlm.nih.gov/articles/PMC9683059/), A continuum of chromatin states and Table 1.
[^ATAC]: Buenrostro et al. (2013), [Transposition of native chromatin](https://pubmed.ncbi.nlm.nih.gov/24097267/), assay-principle abstract.
[^ENC]: ENCODE Project Consortium et al. (2020), [Expanded encyclopaedias of DNA elements](https://www.nature.com/articles/s41586-020-2493-4), candidate regulatory element registry.
[^ENH]: Friedman et al. (2024), [Enhancer-promoter specificity](https://www.nature.com/articles/s12276-024-01233-y), functional validation.
[^LINK]: Fulco et al. (2019), [Activity-by-contact study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886585/), perturbation evidence versus predicted links.
[^PROT]: Alberts et al. (2002), [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/), phosphorylation and activity.
[^LINE]: Wagner and Klein (2020), [Lineage tracing meets single-cell omics](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/), state versus ancestry.


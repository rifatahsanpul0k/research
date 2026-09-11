# Phase 1C — source-backed preparation

**Historical preparation snapshot.** The missing brief was supplied in the next turn. Final topic artifacts are in [03_cellular_tissue_biology](03_cellular_tissue_biology/CONCEPT_MAP.md); see its [validation record](03_cellular_tissue_biology/VALIDATION.md) for current status. The original pending-input statements below are retained as history.

Status: **in_progress; not a completed phase or a substitute for the requested topic artifacts**. Prepared 2026-09-11. The received brief contains complete sections 0–13 and only the beginning of section 14. Its final line is `* neura`. The remaining scope, artifact requirements and stopping condition are unavailable; the user has been asked for the remaining text. Final filenames and completion criteria will follow that text.

## Repository and scope

Phase 1A's ten topics and two integration documents and Phase 1B's fourteen topics, integration documents, sources and validation are present. The working tree was clean at `eddb50b` before the requested Graphify invocation. `graphify . --code-only` found zero supported code files, skipped 69 non-code files and exited 1 with an empty-graph diagnostic. This is expected for the current repository, not a research failure or scientific evidence. It modified the existing tracked `graphify-out/cache/stat-index.json`.

The following are preliminary findings in the supplied order. They preserve useful work while the request is incomplete. No dataset was accessed, no dataset annotations were inferred, and no assay methodology, integration algorithm, ML model, benchmark, scientific graph or experiment was developed. Numerical examples below are invented teaching examples, not project observations.

## 1. Cell identity

Cell identity needs multiple kinds of evidence: phenotype, developmental lineage and state. Phenotype means observed characteristics; it does not itself establish ancestry. Type labels express a biological classification at a chosen level, subtype labels refine it, and state describes a condition within that classification. A classification should state its criteria and granularity instead of treating a label as an intrinsic, perfectly discrete measurement.[^MORRIS]

For the requested T-cell example, retain `T cell` as the broad category and distinguish naive, activated, memory and exhausted populations. These are not four mutually exclusive, equally transient switches: activation can lead to differentiated effector and memory populations; exhaustion involves altered function and regulatory programs under persistent stimulation. Do not diagnose exhaustion from one inhibitory-receptor measurement.[^WHERRY]

Working integration, rather than an additive numerical law:

```text
genome + regulatory program + RNA program + protein/activity state + environment
                                  -> observed phenotype
```

This connects the previous foundations to a multicomponent view of cellular identity; it does not establish which component caused a particular observation.[^WAGNER]

## 2. Cellular heterogeneity

Organize the eventual notes around genetic variation, epigenetic regulation, transcription, protein abundance/activity, signaling exposure, developmental history, cycle, metabolism and environment. These are potentially interdependent sources of variation, not automatically identifiable independent axes. Published conceptual work distinguishes persistent type characteristics, changing states, spatial context, allele-related variation and technical variation.[^WAGNER]

The computational consequence is an inference constraint: different vectors need not indicate different types, and matching measured vectors cannot establish equality of unmeasured biological properties. This follows from observing only selected features of a multicomponent system, not from a particular algorithm. The formal counterexample below makes the distinction explicit.

## 3. Differentiation

Differentiation is acquisition of specialized cellular properties. Stem-cell status requires self-renewal and differentiation capacity; proliferation alone is insufficient. Potency concerns the range of possible descendants under specified conditions. Multipotency is restricted relative to pluripotency; totipotency additionally encompasses the lineages needed for a whole conceptus. A potency claim needs functional context rather than merely a marker label.[^TABANSKY]

In blood formation, stem cells produce more stem cells and committed progenitors whose outputs are more restricted. Progenitor and precursor terminology needs an explicit tissue-specific convention; it should not imply that every tissue follows one fixed sequence of named stages. Mature function, fate commitment and proliferative capacity are separate questions.[^RENEWAL]

For later elaboration: regulatory change → expression change → protein/function change → differentiation. This is a conceptual connection to Phase 1B, not a universal irreversible progression inferred from a snapshot. Reprogramming demonstrates that differentiated identity is not an absolute physical prohibition on another fate.[^TABANSKY]

## 4. Cell lineage

Lineage concerns descent through cell divisions. Similarity of current states is a different relation: close relatives can acquire different phenotypes, and comparable phenotypes can be reached by different histories. A developmental trajectory organizes changes in state; its interpretation as actual ancestry requires additional evidence. Lineage tracing supplies historical information that a molecular snapshot alone does not contain.[^LINEAGE]

For example, an observed parent `P` producing daughters `A` and `B` establishes a sister relationship. An expression table containing similar rows for `A` and `C` does not establish that `C` is another daughter of `P`. A branch in a state description is not by itself an observed division or fate decision. This is a logical example, not a proposed trajectory method.

## 5. Cell cycle

| Phase | Biological event |
|---|---|
| G0 | Noncycling condition; duration and capacity for re-entry vary |
| G1 | Interval before DNA synthesis; growth and preparation |
| S | DNA replication |
| G2 | Interval after replication and before mitosis |
| M | Chromosome segregation and cell division |

The table describes the standard animal-cell framework, not universal fixed phase durations. Microscopy observes division; DNA-content measurements and incorporation of labeled DNA precursors provide complementary evidence. DNA content alone does not distinguish G0 from G1, or G2 from M.[^CYCLE]

Cyclin/CDK-dependent regulation coordinates transcription of products needed for subsequent cycle events. Thus cycle-associated expression can differ within the same type.[^BERTOLI] Later analysis must decide whether proliferation is part of the biological question before treating it as unwanted variation; no correction algorithm is selected here.

## 6. Cell signaling

A ligand binds a compatible receptor and can initiate intracellular responses. Receptors may be at the surface or inside the cell. Cascades can change protein activity and transcription; small intracellular mediators such as calcium and cyclic AMP are second messengers. Autocrine signals act on the producing cell, paracrine signals locally, endocrine signals at distant targets through circulation, and contact-dependent signals require cell contact.[^SIGNAL]

```text
Cell A produces/presents ligand
  -> ligand reaches a competent receptor on/in Cell B
  -> intracellular response
  -> altered regulatory, expression or protein state
```

Ligand RNA and receptor RNA do not establish every step. Protein availability, ligand delivery, receptor competence and a downstream response remain separate requirements. Therefore co-expression is compatibility evidence rather than proof of active communication.[^SIGNAL]

## 7. Cell–cell interactions

Keep physical contact, adhesion, signaling and functional outcome distinct. A contact may permit receptor engagement without proving a particular downstream effect; extracellular signaling need not imply persistent contact. In lymphoid organs, antigen presentation and interactions with supporting cells help organize immune responses.[^SIGNAL][^JANEWAY]

For future evidence tables, record the interacting entities, context, observation time, contact evidence, molecular evidence and response evidence separately. Missing response evidence is `unknown`, not `no response`. This is a documentation convention, not construction of an interaction graph.

## 8. Extracellular matrix and microenvironment

Extracellular matrix comprises organized extracellular macromolecules. It supplies attachment substrates and binds or presents growth factors; its receptors can transduce signals. Matrix composition and organization therefore affect biochemical exposure as well as structural support. A local environment is more than the set of nearby cell labels.[^ECM]

The eventual niche discussion should specify the supported cellular function and evidence that the environment maintains or changes it. Neighboring cells can differ in receptor competence or in access to matrix-associated signals; adjacency does not guarantee identical exposure.[^ECM][^SIGNAL] Mechanical sensing needs deeper source-backed treatment when the full phase is assembled.

## 9. Tissue organization

Layers, compartments, regions, boundaries and niches describe different organizational properties; they should not be used as interchangeable labels. Lymph-node follicles, paracortex and medulla provide an anatomical example. Their organization brings selected cells and antigens together, and changes during immune responses.[^JANEWAY]

The project implication is to store anatomical location independently from cell-type annotation. A mixed compartment can contain multiple types; a repeated type label does not establish physical adjacency. Spatial scale, section identity and evidence for region boundaries must accompany any eventual location label.

## 10. Distinct biological relationships

These are conceptual definitions for future interpretation, not fitted scores, recommended similarity metrics or constructed graphs.

| Symbol/relation | Question and required semantics |
|---|---|
| \(S^{molecular}_{ij}\) | Similarity of specified measured molecular features; identify modality, units and selected features |
| \(D^{spatial}_{ij}\) | Physical separation in a declared coordinate system, dimension and unit; larger distance means less proximity |
| \(S^{functional}_{ij}\) | Similarity of defined functions, supported by stated functional evidence |
| \(S^{regulatory}_{ij}\) | Similarity of regulatory programs; distinguish observed regulatory activity from inferred signatures |
| Lineage relationship | Shared ancestry or ancestor–descendant relation with historical evidence; no universal scalar is assumed |
| Interaction evidence | Support for a specific contact or communication event, with direction, time and context where relevant |

The literature treats phenotype, state, spatial context and ancestry as distinguishable aspects; historical information requires evidence beyond present-state similarity.[^MORRIS][^WAGNER][^LINEAGE] Correlation between two relation types is not a definition of their equivalence.

**Synthetic counterexample.** Suppose a targeted measurement returns these molecule counts:

| Observation | Gene A | Gene B | Position x (µm) | Position y (µm) |
|---|---:|---:|---:|---:|
| C1 | 8 | 2 | 0 | 0 |
| C2 | 8 | 2 | 100 | 0 |
| C3 | 1 | 9 | 1 | 0 |

Assume for this example that all rows are individual cells in one plane and measurement frame. C1 and C2 have identical measured vectors but are 100 µm apart. C3 is 1 µm from C1 and has a different measured vector. Neither ancestry, function, cell type nor communication is given by this table. An unmeasured active protein could differ even when both measured counts match. Conversely, two rows explicitly known to share a type could differ in these counts. These constructions demonstrate lack of logical implication; they assert no actual values or labels for the six project datasets.

## 11. Boundaries and transitional states

Morphogen gradients supply graded positional signals that can regulate different expression responses and fates. A continuous input and distinct downstream domains can coexist.[^GRADIENT] Cellular organization can also include continuous states alongside categorical descriptions.[^WAGNER]

Consequently, a later cluster label would require biological interpretation and validation. A transition zone should not automatically be called a new type. A mixed molecular profile needs scrutiny of both a possible biological transition and the observation unit before assigning such meaning. Source-backed treatment of technical mixtures and of specific anatomical boundaries remains outstanding; this preparation makes no dataset-specific diagnosis.

## 12. Human lymph-node foundations

Lymph nodes receive lymph draining tissues and support immune surveillance by bringing antigen and lymphocytes together. B cells participate in antibody responses and can differentiate into antibody-secreting plasma cells; T cells provide other adaptive functions. Macrophages and dendritic cells contribute to antigen handling and immune responses.[^JANEWAY]

| Region | Preliminary anatomical meaning |
|---|---|
| Capsule / subcapsular sinus | Outer enclosure / sinus immediately beneath it |
| Cortex / follicles | Outer region containing lymphoid follicles |
| Paracortex | T-cell-rich zone containing dendritic cells |
| Medulla | Inner region organized into cords and sinuses; includes plasma cells |

Histology supplies structural evidence for these regions.[^HISTOLOGY] Cords, sinuses, vessels and the hilum require fuller anatomical treatment before section 12 is considered complete.

Stromal populations include fibroblastic reticular and follicular dendritic cells; vascular and lymphatic endothelial cells form distinct components. Follicular dendritic cells should not be collapsed into the same category as conventional hematopoietic dendritic cells merely because their names overlap.[^STROMA]

For `10x_human_lymph_node_A1` and `10x_human_lymph_node_D1`, these are background expectations. They establish no verified region, cell-type, vessel or state labels in either dataset. The dataset registry remains unchanged.

## 13. Why lymph-node spatial structure matters

Stromal cells produce chemokines that organize lymphocyte migration and supply survival signals. High endothelial venules support lymphocyte entry from blood. Distinct stromal territories and lymphatic spaces help establish different local opportunities for encounters.[^STROMA]

Thus identity, local environment and physical position are sensible joint interpretive variables. This is a biological synthesis, not evidence that all three have been measured independently or that their effects are additive. B-rich regions, T-rich regions, vascular structures, stromal boundaries and sinus regions are hypotheses to check against actual specimen evidence, not labels to populate from textbook expectations.

## 14. Embryonic mouse-brain foundation — scope incomplete

The received text explicitly names `Mouse_Brain_E11_S1`, `Mouse_Brain_E13_S1`, `Mouse_Brain_E15_S1` and `Mouse_Brain_E18_S1`, then ends during its study list. One introductory finding can be retained: in the developing rodent nervous system, neuroepithelial cells, radial glia and basal progenitors contribute to neuron production. Radial glia connect progenitor biology with tissue organization.[^NEUROGENESIS]

This does not verify the sampled brain regions, exact embryonic staging convention, specimen pairing, developmental lineage or annotations of those four folders. No stage-by-stage claims are assigned to them. Detailed coverage awaits the rest of section 14 and any following sections.

## What remains before completion

- Obtain the rest of the brief and reconcile the final topic order, required artifacts and stopping condition.
- Expand definitions, mechanisms, measurement principles, numerical examples, misconceptions and comprehension checks in the requested format. The short sections above do not satisfy a full phase assessment.
- Complete all listed heterogeneity mechanisms, potency/commitment terminology, adhesion and immune interactions, mechanical environment, detailed lymph-node anatomy and the complete embryonic-brain scope.
- Verify the conceptual chain across molecules, regulatory programs, cellular functions and tissue organization; preserve the six relationship distinctions throughout.
- Update tracking to reflect actual final coverage, validate citations and local links, and rerun Graphify at phase completion. No subsequent phase is authorized by this preparation.

## Sources and access depth

Only sources used above are listed. Access date: 2026-09-11. Bibliographic verification is distinct from full-text access; this is a focused foundation reading, not an exhaustive literature review. Methods, algorithms, supplements and disease-treatment sections were not reviewed. No paper files or datasets were downloaded.

[^MORRIS]: Morris SA (2019). *The evolving concept of cell identity in the single cell era*. Development 146:dev169748. DOI [10.1242/dev.169748](https://doi.org/10.1242/dev.169748). [PubMed](https://pubmed.ncbi.nlm.nih.gov/31249002/). Abstract and author-hosted indexed introductory passages inspected; phenotype/lineage/state framing only.
[^WHERRY]: Wherry EJ, Kurachi M (2015). *Molecular and cellular insights into T cell exhaustion*. Nature Reviews Immunology 15:486–499. DOI [10.1038/nri3862](https://doi.org/10.1038/nri3862). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4889009/). Abstract and indexed introductory text inspected; naive-to-effector/memory context and persistent exhaustion, not treatment guidance.
[^WAGNER]: Wagner A, Regev A, Yosef N (2016). *Revealing the vectors of cellular identity with single-cell genomics*. Nature Biotechnology 34:1145–1160. DOI [10.1038/nbt.3711](https://doi.org/10.1038/nbt.3711). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5465644/). Introduction and Box 1 indexed text inspected; biological distinctions only, no methods studied.
[^TABANSKY]: Tabansky I, Stern JNH (2016). *Basics of Stem Cell Biology as Applied to the Brain*. In Pfaff D, Christen Y (eds), Stem Cells in Neuroendocrinology. Springer. DOI [10.1007/978-3-319-41603-8_2](https://doi.org/10.1007/978-3-319-41603-8_2). [NCBI Bookshelf NBK435799](https://www.ncbi.nlm.nih.gov/books/NBK435799/). Opening summary and basic biology sections inspected.
[^RENEWAL]: Alberts B, Johnson A, Lewis J, Raff M, Roberts K, Walter P (2002). *Renewal by Multipotent Stem Cells: Blood Cell Formation*. Molecular Biology of the Cell, 4th ed. Garland Science. [NCBI Bookshelf NBK26919](https://www.ncbi.nlm.nih.gov/books/NBK26919/). Indexed stem-cell/progenitor and summary passages inspected; historical textbook terminology requires tissue-specific qualification.
[^LINEAGE]: Wagner DE, Klein AM (2020). *Lineage tracing meets single-cell omics: opportunities and challenges*. Nature Reviews Genetics. DOI [10.1038/s41576-020-0223-2](https://doi.org/10.1038/s41576-020-0223-2). Reuses the [Phase 1B source record](../03_papers/WAGNER_KLEIN_LINEAGE_2020/SOURCE_RECORD.md), including its inspected introduction/history sections. Fresh PMC access encountered a browser challenge; no new full-text review is claimed.
[^CYCLE]: Alberts B, Johnson A, Lewis J, Raff M, Roberts K, Walter P (2002). *An Overview of the Cell Cycle*. Molecular Biology of the Cell, 4th ed. Garland Science. [NCBI Bookshelf NBK26869](https://www.ncbi.nlm.nih.gov/books/NBK26869/). Opening phase descriptions and cell-cycle progression measurement section inspected.
[^BERTOLI]: Bertoli C, Skotheim JM, de Bruin RAM (2013). *Control of cell cycle transcription during G1 and S phases*. Nature Reviews Molecular Cell Biology 14:518–528. DOI [10.1038/nrm3629](https://doi.org/10.1038/nrm3629). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4569015/). Abstract and introduction inspected.
[^SIGNAL]: Alberts B, Johnson A, Lewis J, Raff M, Roberts K, Walter P (2002). *General Principles of Cell Communication*. Molecular Biology of the Cell, 4th ed. Garland Science. [NCBI Bookshelf NBK26813](https://www.ncbi.nlm.nih.gov/books/NBK26813/). Receptor, signal-distance, cellular response and small intracellular mediator sections inspected.
[^ECM]: Hynes RO (2009). *The extracellular matrix: not just pretty fibrils*. Science 326:1216–1219. DOI [10.1126/science.1176009](https://doi.org/10.1126/science.1176009). [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536535/). Abstract and ECM/growth-factor signaling sections inspected.
[^GRADIENT]: Ashe HL, Briscoe J (2006). *The interpretation of morphogen gradients*. Development 133:385–394. DOI [10.1242/dev.02238](https://doi.org/10.1242/dev.02238). [PubMed](https://pubmed.ncbi.nlm.nih.gov/16410409/). Abstract inspected; supports only the general graded-cue/response claim.
[^JANEWAY]: Janeway CA Jr, Travers P, Walport M, Shlomchik MJ (2001). *The components of the immune system*. Immunobiology: The Immune System in Health and Disease, 5th ed. Garland Science. [NCBI Bookshelf NBK27092](https://www.ncbi.nlm.nih.gov/books/NBK27092/). Relevant cell, peripheral lymphoid organ and circulation sections inspected. Modern stem-cell terminology is taken from the dedicated sources above, not the chapter's historical use of “pluripotent” for hematopoietic stem cells.
[^HISTOLOGY]: Mercadante AA, Tadi P (updated 2023-05-01). *Histology, Lymph Nodes*. StatPearls, current Bookshelf container 2026. [NCBI Bookshelf NBK559053](https://www.ncbi.nlm.nih.gov/books/NBK559053/). Structure and microscopic anatomy passages inspected; clinical claims and treatment are outside this reading.
[^STROMA]: Mueller SN, Germain RN (2009). *Stromal cell contributions to the homeostasis and functionality of the immune system*. Nature Reviews Immunology 9:618–629. DOI [10.1038/nri2588](https://doi.org/10.1038/nri2588). [Publisher](https://www.nature.com/articles/nri2588). Publisher key points and HEV glossary inspected; PMC full-text access encountered a browser challenge. Species-specific study findings are not assumed to describe the human project specimens.
[^NEUROGENESIS]: Götz M, Huttner WB (2005). *The cell biology of neurogenesis*. Nature Reviews Molecular Cell Biology 6:777–788. DOI [10.1038/nrm1739](https://doi.org/10.1038/nrm1739). [Publisher](https://www.nature.com/articles/nrm1739). Publisher key points/abstract inspected; introductory rodent progenitor classes only. Detailed timing and division-mechanism claims are not extracted.

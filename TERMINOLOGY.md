# Component terminology

This is an operational naming convention for project records. It is not a literature review. A single algorithm can play different roles; identify the role in each pipeline.

| Stage | What is recorded | Example distinction |
|---|---|---|
| Raw data | Acquired observations and accompanying metadata | Count matrix as acquired; provenance determines whether it is actually raw |
| Preprocessing | Filtering, transformations, alignment, feature selection | Normalized values are derived data, not raw counts |
| Initial representation | Object supplied to a learner | Feature matrix, token collection, graph adjacency plus node features |
| Representation-learning mechanism | Procedure that constructs or learns another representation | PCA fitting, contrastive training, or factorization |
| Model | Parameterized computation used for inference or learning | GCN is a graph model; it is not the adjacency matrix |
| Learned embedding | Output coordinates or latent descriptors | PCA scores or encoder output; distinguish parameters from per-observation coordinates |
| Downstream task | Intended use of a representation/model | Clustering or prediction; KMeans is a clustering algorithm |
| Evaluation | Procedure and criteria for judging task outputs | A defined metric with reference, split, and uncertainty |

Example bookkeeping only: acquired matrix -> documented transformation -> feature matrix -> PCA fitting -> fitted projection -> component scores -> KMeans clustering -> predeclared evaluation. This example does not select a baseline. A representation-learning mechanism and its fitted model may describe different aspects of the same stage; record both without inventing an extra transformation. Some pipelines have no learned embedding.

Additional distinctions: cell type versus cell state; observation versus biological sample; sample label versus verified developmental stage; missing value versus observed zero; author-reported finding versus our experimental result; biological interpretation versus causal evidence. Source-backed teaching definitions for biological terms belong in the curriculum notes.

## Phase 1A biological terms

| Term | Working definition for this project | Computational caution |
|---|---|---|
| DNA | Stable nucleotide polymer carrying genome information. | A gene symbol or interval is an annotation of DNA, not the DNA molecule itself. |
| Genome | Complete DNA information of an organism or cell, represented against a reference when stored computationally. | Reference build and annotation version affect feature coordinates and identifiers. |
| Chromosome | Long packaged DNA molecule with genes, regulatory regions, repeats, and structural regions. | Physical chromosome organization is usually not captured by a simple gene matrix. |
| Gene | Genomic sequence identified through functional RNA or protein products; gene-associated regulatory DNA is not automatically inside its annotated boundary. | One gene can have multiple transcripts and products; see corrected Gerstein reference in Phase 1A genes note. |
| Coding region | Sequence that specifies amino acid order in a protein. | Protein-coding annotation does not mean protein abundance was measured. |
| Non-coding region | Sequence that does not directly encode canonical protein sequence but may regulate, structure, or produce functional RNA. | Non-coding does not mean non-functional; function often needs independent evidence. |
| Transcription | DNA-templated RNA synthesis by RNA polymerase. | RNA counts are not direct transcription-rate measurements. |
| RNA | Transcribed nucleotide polymer with coding, regulatory, structural, catalytic, or adaptor roles. | RNA feature tables depend on captured RNA class and annotation granularity. |
| Gene expression | Production of a functional gene product, measured at RNA or protein level depending on assay. | Expression values are assay-dependent proxies, not direct biological state labels. |
| Translation | Ribosome-mediated decoding of mRNA codons into amino acid sequence. | Detected RNA does not prove active translation. |
| Protein | Folded amino acid polymer carrying many cellular functions. | Protein abundance, localization, modification, and activity are distinct quantities. |
| Central dogma | Constraint on residue-by-residue sequence-information transfer; DNA -> RNA -> protein is the common expression route. | Protein feedback on transcription is not reverse sequence transfer; see Crick (1970) in Phase 1A integration note. |

## Phase 1B biological terms

Definitions are contextual working terms. The linked notes provide mechanisms, citations and limitations.

| Term | Biological meaning | Computational caution / source-backed note |
|---|---|---|
| Constitutive expression | Relatively sustained expression in a specified setting | Not unregulated or universally constant; [01](01_biology/02_gene_regulation/01_GENE_REGULATION_OVERVIEW.md) |
| Transcriptional regulation | Control of RNA synthesis | RNA abundance also depends on removal; [01](01_biology/02_gene_regulation/01_GENE_REGULATION_OVERVIEW.md) |
| Post-transcriptional regulation | Control of RNA processing, transport, localization or stability | Gene counts may collapse isoform differences; [01](01_biology/02_gene_regulation/01_GENE_REGULATION_OVERVIEW.md) |
| Translational regulation | Control of protein synthesis from RNA | RNA is not translation rate; [01](01_biology/02_gene_regulation/01_GENE_REGULATION_OVERVIEW.md) |
| Post-translational regulation | Control of protein modification, location, turnover or action | Abundance is not activity; [01](01_biology/02_gene_regulation/01_GENE_REGULATION_OVERVIEW.md) |
| Promoter / core promoter | Regulatory DNA around transcription initiation / machinery-assembly region | Chosen windows are not universal boundaries; [02](01_biology/02_gene_regulation/02_PROMOTERS.md) |
| TSS | Transcription start site for a transcript | Distinct from translation start; strand and annotation matter; [02](01_biology/02_gene_regulation/02_PROMOTERS.md) |
| Enhancer | DNA capable of increasing promoter output in context | A peak or histone mark establishes a candidate, not a proven target; [03](01_biology/02_gene_regulation/03_ENHANCERS.md) |
| Silencer | DNA with context-dependent repressive function | Functional evidence differs from a predicted label; [04](01_biology/02_gene_regulation/04_OTHER_REGULATORY_ELEMENTS.md) |
| Insulator / barrier / boundary | Restricted enhancer communication / restricted chromatin spread / structural domain distinction | These functions are not interchangeable; [04](01_biology/02_gene_regulation/04_OTHER_REGULATORY_ELEMENTS.md) |
| Sequence-specific TF | DNA-recognizing protein involved in transcriptional control | TF RNA, protein, occupancy and activity are distinct; [05](01_biology/02_gene_regulation/05_TRANSCRIPTION_FACTORS.md) |
| Motif | Description of DNA-sequence preference | Match is not binding; [05](01_biology/02_gene_regulation/05_TRANSCRIPTION_FACTORS.md) |
| Cofactor | Protein assisting a regulatory complex | Need not recognize DNA motifs directly; [05](01_biology/02_gene_regulation/05_TRANSCRIPTION_FACTORS.md) |
| Chromatin / nucleosome | DNA with associated proteins and RNAs / histone core with wrapped DNA | Structure is dynamic and scale-dependent; [06](01_biology/02_gene_regulation/06_CHROMATIN.md) |
| Euchromatin / heterochromatin | Broad chromosomal organization categories | Not universal numeric open/closed labels; [06](01_biology/02_gene_regulation/06_CHROMATIN.md) |
| Accessibility | Physical opportunity for interaction with chromatinized DNA | Probe-dependent signal, not expression; [07](01_biology/02_gene_regulation/07_CHROMATIN_ACCESSIBILITY.md) |
| Peak | Analysis-defined enriched genomic interval | Not a molecule, gene or proven enhancer; [07](01_biology/02_gene_regulation/07_CHROMATIN_ACCESSIBILITY.md) |
| Epigenetics / regulatory memory | Heritable non-sequence chromosomal regulation under a strict definition / demonstrated persistence | Broader chromatin usage must be labeled; snapshot does not prove inheritance; [08](01_biology/02_gene_regulation/08_EPIGENETICS.md) |
| CpG / 5mC | Adjacent C and G along DNA / methylated cytosine | CpG is not an interstrand base pair; [09](01_biology/02_gene_regulation/09_DNA_METHYLATION.md) |
| Methylation fraction | Modified-cytosine support divided by informative coverage | Context, coverage and 5hmC ambiguity matter; [09](01_biology/02_gene_regulation/09_DNA_METHYLATION.md) |
| Histone mark | Modification of a histone residue | Association is not a deterministic activity code; [10](01_biology/02_gene_regulation/10_HISTONE_MODIFICATIONS.md) |
| Poised enhancer | Context-defined inactive region with evidence of regulatory preparedness | A label does not guarantee future activation; [10](01_biology/02_gene_regulation/10_HISTONE_MODIFICATIONS.md) |
| Enhancer-promoter interaction | Physical, functional or inferred relationship, as explicitly defined | Contact alone is not regulatory causation; [11](01_biology/02_gene_regulation/11_ENHANCER_PROMOTER_INTERACTIONS.md) |
| Regulatory network / module | Regulator-target relationships / coordinated subset | Experimental and inferred links remain distinct; [12](01_biology/02_gene_regulation/12_GENE_REGULATORY_NETWORKS.md) |
| Direct / indirect regulation | Action at target regulation / effect through intermediates | Perturbation response may be indirect; [12](01_biology/02_gene_regulation/12_GENE_REGULATORY_NETWORKS.md) |
| Cell identity / state | Relatively persistent organization / condition-dependent variation | Operational boundaries require evidence; [13](01_biology/02_gene_regulation/13_CELL_IDENTITY_AND_REGULATION.md) |
| Differentiation / progenitor | Acquisition of specialization / precursor with contextual developmental potential | Stage alone does not assign fate; [14](01_biology/02_gene_regulation/14_DEVELOPMENTAL_REGULATION_BRIDGE.md) |
| Lineage / trajectory | Ancestry through divisions / path through changing states | Molecular ordering is not demonstrated ancestry; [14](01_biology/02_gene_regulation/14_DEVELOPMENTAL_REGULATION_BRIDGE.md) |

## Phase 1C preparation distinctions — historical, 2026-09-11

These entries record the preliminary reading before the complete brief arrived; the completed glossary and notes are linked below. Evidence and qualifications are in [Phase 1C preparation](01_biology/PHASE_1C_PREPARATION.md).

| Term | Working distinction | Evidence location |
|---|---|---|
| Cell type / subtype / state | Classification, refinement and condition within a classification; state does not necessarily mean brief or reversible | Preparation sections 1–2; Morris; Wherry and Kurachi; Wagner et al. |
| Potency / self-renewal | Range of possible descendants / production of cells retaining stem-cell properties; distinct from proliferation alone | Section 3; Tabansky and Stern |
| Lineage / trajectory | Actual descent / description of changing states; similar profiles do not establish ancestry | Section 4; Wagner and Klein |
| G0 / G1 / S / G2 / M | Noncycling condition / pre-replication / replication / post-replication / division | Section 5; Alberts cell-cycle chapter |
| Ligand / receptor / response | Signal molecule / recognizing molecule / downstream effect; expression of a compatible pair does not establish communication | Section 6; Alberts communication chapter |
| Extracellular matrix | Organized extracellular material with structural, adhesive and signaling roles | Section 8; Hynes |
| Molecular / spatial / functional / regulatory / lineage / interaction relation | Six separately specified relationships; one must not silently substitute for another | Section 10; formal definitions and synthetic counterexample |
| Anatomical expectation / verified annotation | General biological knowledge / a documented assignment in a particular dataset | Sections 12–14; dataset annotation status remains unknown |

## Phase 1C completed terminology — 2026-09-11

Definitions below use the cited mechanisms, exceptions and evidence in the linked topic notes. They are working biological distinctions, not annotations of the project datasets.

| Term(s) | Meaning and qualification | Source-backed topic |
|---|---|---|
| Cell; nucleus | Membrane-bounded biological system; nuclear compartment is not a whole cell | [Identity](01_biology/03_cellular_tissue_biology/01_CELL_IDENTITY.md) |
| Identity; phenotype | Integrated cellular characterization; observed molecular, morphological and functional properties | [Identity](01_biology/03_cellular_tissue_biology/01_CELL_IDENTITY.md) |
| Type; subtype; state | Classification; finer classification; condition within a chosen classification | [Identity](01_biology/03_cellular_tissue_biology/01_CELL_IDENTITY.md) |
| Functional state; persistent state | Condition of activity; persistence requires temporal evidence and does not imply irreversibility | [Identity](01_biology/03_cellular_tissue_biology/01_CELL_IDENTITY.md) |
| Heterogeneity; somatic mosaicism | Variation among cells; within-individual genetic variation is one possible contributor | [Heterogeneity](01_biology/03_cellular_tissue_biology/02_CELLULAR_HETEROGENEITY.md) |
| Differentiation; maturation | Acquisition of specialized properties; development of those properties does not by itself establish ancestry | [Differentiation](01_biology/03_cellular_tissue_biology/03_DIFFERENTIATION.md) |
| Potency; self-renewal | Range of potential descendants under specified conditions; production retaining stem-cell capacity | [Differentiation](01_biology/03_cellular_tissue_biology/03_DIFFERENTIATION.md) |
| Stem cell; progenitor; precursor | Stem status requires self-renewal plus differentiation capacity; precursor/progenitor usage requires tissue context | [Differentiation](01_biology/03_cellular_tissue_biology/03_DIFFERENTIATION.md) |
| Commitment; restriction; terminal differentiation | Narrowing of developmental options and context-specific specialized endpoint; not a universal ban on plasticity | [Differentiation](01_biology/03_cellular_tissue_biology/03_DIFFERENTIATION.md) |
| Lineage; trajectory | Descent through divisions; description or inference of state change | [Lineage](01_biology/03_cellular_tissue_biology/04_CELL_LINEAGE.md) |
| Proliferation; cell cycle | Increase in number through division; coordinated replication/division processes | [Cycle](01_biology/03_cellular_tissue_biology/05_CELL_CYCLE.md) |
| G0; G1; S; G2; M | Noncycling; before replication; replication; after replication; mitosis/division | [Cycle](01_biology/03_cellular_tissue_biology/05_CELL_CYCLE.md) |
| Ligand; receptor; second messenger | Binding signal; recognizing/responding molecule; small intracellular mediator | [Signaling](01_biology/03_cellular_tissue_biology/06_CELL_SIGNALING.md) |
| Autocrine; paracrine; endocrine; contact-dependent | Self, local, circulation-mediated distant and contact-required delivery modes | [Signaling](01_biology/03_cellular_tissue_biology/06_CELL_SIGNALING.md) |
| Contact; adhesion; communication | Physical interface; molecular attachment; signal with a recipient response—separate evidence | [Interactions](01_biology/03_cellular_tissue_biology/07_CELL_CELL_INTERACTIONS.md) |
| ECM; stroma; microenvironment; niche | Extracellular material; supporting components; local conditions; functionally specified supporting environment | [Microenvironment](01_biology/03_cellular_tissue_biology/08_MICROENVIRONMENT.md) |
| Layer; region; compartment; functional unit | Different spatial/organizational descriptions, not synonyms for type | [Organization](01_biology/03_cellular_tissue_biology/09_TISSUE_ORGANIZATION.md) |
| Molecular; spatial; functional; regulatory; lineage; interaction relation | Six meanings with distinct observation and evidence requirements | [Relationships](01_biology/03_cellular_tissue_biology/10_SPATIAL_BIOLOGICAL_RELATIONSHIPS.md) |
| Boundary; gradient; transition zone | Interface; spatially varying quantity; area of changing properties | [Transitions](01_biology/03_cellular_tissue_biology/11_BOUNDARIES_AND_TRANSITIONS.md) |
| Capsule; follicle; paracortex; medulla; sinus; hilum | LN enclosure, follicular region, T-rich territory, inner cords/sinuses, lymph-flow spaces and efferent exit region | [Lymph node](01_biology/03_cellular_tissue_biology/12_LYMPH_NODE_FOUNDATIONS.md) |
| FRC; FDC; HEV | Fibroblastic reticular cell; stromal follicular dendritic cell; specialized blood high endothelial venule | [LN spatial biology](01_biology/03_cellular_tissue_biology/13_LYMPH_NODE_SPATIAL_BIOLOGY.md) |
| Neuroepithelial cell; radial glia; intermediate progenitor | Foundational neural progenitor categories with context-dependent output | [Embryonic brain](01_biology/03_cellular_tissue_biology/14_EMBRYONIC_MOUSE_BRAIN.md) |
| Neurogenesis; gliogenesis; migration | Neuron production; glial production; movement—none identical to maturation or ancestry | [Embryonic brain](01_biology/03_cellular_tissue_biology/14_EMBRYONIC_MOUSE_BRAIN.md) |
| VZ; SVZ; cortical plate | Ventricular zone; subventricular zone; developing neuronal compartment in the cortical example | [Embryonic brain](01_biology/03_cellular_tissue_biology/14_EMBRYONIC_MOUSE_BRAIN.md) |
| Stage; age; birthdate | Developmental classification, elapsed-time description and a cell's production time; distinct clocks | [Developmental time](01_biology/03_cellular_tissue_biology/15_DEVELOPMENTAL_TIME.md) |
| Spot; bin; multicellular observation; population | Sampling footprint; spatial aggregation unit; combined contributors; defined collection | [Observation units](01_biology/03_cellular_tissue_biology/16_OBSERVATION_UNITS.md) |
| Positive/negative marker; canonical marker | Supporting detection/exclusion evidence; established context-dependent usage, not deterministic identity | [Annotation](01_biology/03_cellular_tissue_biology/17_BIOLOGICAL_ANNOTATION.md) |
| Manual/reference-based annotation | Expert interpretation/comparison to labeled reference; both require provenance and context | [Annotation](01_biology/03_cellular_tissue_biology/17_BIOLOGICAL_ANNOTATION.md) |
| Hierarchy; is-a; part-of | Nested classification; type inclusion; anatomical containment—distinct from descent | [Hierarchy](01_biology/03_cellular_tissue_biology/18_BIOLOGICAL_HIERARCHY.md) |

Mathematical notation and the representation-neutral inventory are defined in [BIOLOGY_TO_DATA](01_biology/03_cellular_tissue_biology/BIOLOGY_TO_DATA.md). No biological definition here selects a future model or representation.

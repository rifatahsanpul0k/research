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

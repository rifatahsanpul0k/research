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
| Gene | Regulated genomic region producing a functional RNA or protein product. | One gene can have multiple transcripts and products; one matrix column may collapse that structure. |
| Coding region | Sequence that specifies amino acid order in a protein. | Protein-coding annotation does not mean protein abundance was measured. |
| Non-coding region | Sequence that does not directly encode canonical protein sequence but may regulate, structure, or produce functional RNA. | Non-coding does not mean non-functional; function often needs independent evidence. |
| Transcription | DNA-templated RNA synthesis by RNA polymerase. | RNA counts are not direct transcription-rate measurements. |
| RNA | Transcribed nucleotide polymer with coding, regulatory, structural, catalytic, or adaptor roles. | RNA feature tables depend on captured RNA class and annotation granularity. |
| Gene expression | Production of a functional gene product, measured at RNA or protein level depending on assay. | Expression values are assay-dependent proxies, not direct biological state labels. |
| Translation | Ribosome-mediated decoding of mRNA codons into amino acid sequence. | Detected RNA does not prove active translation. |
| Protein | Folded amino acid polymer carrying many cellular functions. | Protein abundance, localization, modification, and activity are distinct quantities. |
| Central dogma | Core information flow from DNA to RNA to protein, with important exceptions and regulation. | Do not infer one-to-one deterministic equivalence among DNA, RNA, and protein measurements. |

# Graph Report - multiomics-research  (2026-09-15)

## Corpus Check
- Large corpus: 592 files · ~221,627 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 630 nodes · 918 edges · 88 communities (37 shown, 51 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 22 edges (avg confidence: 0.87)
- Token cost: 213,654 input · 9,396 output

## Community Hubs (Navigation)
- annotate_phase3c_runtime.py
- failures.py
- sha256()
- type
- provenance.schema.json
- enum
- dataset
- provenance-v2.schema.json
- config.py
- run-config.schema.json
- enum
- enum
- items
- check_phase2a_toys.py
- Phase 3C Scientific Baseline R
- inspect_h5ad.py
- summarize_matrices.py
- Multilayer Perceptron (MLP)
- Preprocessing Principles
- ASTRA Operating Rules
- compare_features.py
- run_full_discordance_audit.py
- Chromatin
- summarize_phase3c.py
- Scaled Dot-Product Attention
- summarize_annotations.py
- Promoters
- Epigenetics
- Cell Identity
- Biology to Data
- Singular Value Decomposition
- Mutual Information
- Representation Principles
- verify_toy.py
- MIDAS
- Message Passing GNN
- inspect_coordinates.py
- 01. DNA
- Gene Regulation Overview
- Enhancer-Promoter Interaction
- Spatial Transcriptomics
- RNA Library-Size Normalization
- LSI Foundations
- Canonical Method Inventory
- Distance
- Important Distributions
- Orthonormal Eigenbasis
- Objective Function
- L1 and L2 Regularization
- RBF Kernel
- Latent Variables
- Optimal Transport Couplings
- common/__init__.py
- benchmarks/__init__.py
- methods/__init__.py
- tests/__init__.py
- code/__init__.py
- Research Log
- Other Regulatory Elements
- Bayesian Foundations
- Affine Map
- Matrix Rank
- Learning Rate (eta)
- Adjusted Rand Index (ARI)
- Silhouette Score
- Independent Component Analysis
- Integrative NMF and LIGER
- Canonical Correlation Analysis
- Diffusion Representations
- t-SNE
- UMAP
- Abstract Simplicial Complex
- Hypergraph
- Tensor Representations
- Inferred Regulatory Activity
- Developmental Time and Pseudot
- Cobolt
- Deep Embedded Clustering (DEC)
- totalVI Neural Method
- Bootstrap Report
- Path
- Dataset Documentation Schema
- Future Experiment Protocol
- Method Taxonomy
- Paper Extraction Schema
- Representation Taxonomy

## God Nodes (most connected - your core abstractions)
1. `execute_one()` - 23 edges
2. `run()` - 22 edges
3. `required` - 16 edges
4. `sha256()` - 15 edges
5. `required` - 15 edges
6. `build_representations()` - 13 edges
7. `load_h5ad()` - 12 edges
8. `load_dataset()` - 12 edges
9. `required` - 12 edges
10. `write_json_atomic()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `scRNA-seq` --references--> `Cell Identity`  [INFERRED]
  02_omics/01_measurement_and_data_generation/04_SCRNA_SEQ.md → 01_biology/03_cellular_tissue_biology/01_CELL_IDENTITY.md
- `Principal Component Analysis` --conceptually_related_to--> `Low-Rank Approximation`  [INFERRED]
  06_representations/01_classical_representation_families/04_PCA.md → 05_methods/01_mathematical_foundations/16_LOW_RANK_APPROXIMATION.md
- `Gene Regulation Overview` --conceptually_related_to--> `Component Terminology`  [INFERRED]
  01_biology/02_gene_regulation/01_GENE_REGULATION_OVERVIEW.md → TERMINOLOGY.md
- `MOFA and MOFA+` --implements--> `Latent Variables`  [INFERRED]
  06_representations/01_classical_representation_families/10_MOFA.md → 05_methods/01_mathematical_foundations/28_LATENT_VARIABLES.md
- `Data as Mathematical Objects` --conceptually_related_to--> `Biology to Data`  [INFERRED]
  05_methods/01_mathematical_foundations/01_DATA_AS_MATHEMATICAL_OBJECTS.md → 02_omics/01_measurement_and_data_generation/BIOLOGY_TO_DATA.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Manifold and Diffusion Geometry** — 06_representations_01_classical_representation_families_20_diffusion_representations, 06_representations_01_classical_representation_families_22_tsne, 06_representations_01_classical_representation_families_23_umap [EXTRACTED 0.85]
- **Spatial Multimodal Data Integration** — 02_omics_01_measurement_and_data_generation_20_primary_dataset_reconnaissance_dataset_a1, 02_omics_01_measurement_and_data_generation_20_primary_dataset_reconnaissance_dataset_e11_e18, 02_omics_01_measurement_and_data_generation_09_spatial_transcriptomics_spatial_transcriptomics [EXTRACTED 0.85]
- **Biological Foundations Chain** — 01_biology_02_gene_regulation_01_gene_regulation_overview, 01_biology_02_gene_regulation_02_promoters, 01_biology_02_gene_regulation_03_enhancers, 01_biology_02_gene_regulation_05_transcription_factors [EXTRACTED 0.90]
- **Regulatory Logic Flow** — 01_biology_02_gene_regulation_06_chromatin_chromatin, 01_biology_02_gene_regulation_07_chromatin_accessibility_accessibility, 01_biology_02_gene_regulation_12_gene_regulatory_networks_grn [EXTRACTED 0.90]
- **Core Governance Documents** — astra_operating_rules_astra_operating_rules, research_master_research_master, source_policy_source_policy, project_brief_project_brief [EXTRACTED 0.95]
- **Clustering Evaluation Metrics** — 05_methods_01_mathematical_foundations_33_ari_adjusted_rand_index, 05_methods_01_mathematical_foundations_35_silhouette_silhouette_score [EXTRACTED 1.00]
- **Epigenetic Control Mechanisms** — 01_biology_02_gene_regulation_08_epigenetics_epigenetics, 01_biology_02_gene_regulation_09_dna_methylation_methylation, 01_biology_02_gene_regulation_10_histone_modifications_histone_marks [EXTRACTED 1.00]
- **Linear Decomposition Methods** — 06_representations_01_classical_representation_families_04_pca_pca, 06_representations_01_classical_representation_families_06_ica_ica, 06_representations_01_classical_representation_families_07_nmf_nmf [EXTRACTED 1.00]
- **Mathematical Foundations for Omics** — 05_methods_01_mathematical_foundations_01_data_as_mathematical_objects, 05_methods_01_mathematical_foundations_04_distance, 05_methods_01_mathematical_foundations_05_similarity [EXTRACTED 1.00]
- **Multimodal Integration Methods** — 06_representations_01_classical_representation_families_11_cca_cca [EXTRACTED 1.00]
- **Phase 3C Baseline Representations** — 08_experiments_phase_3c_config_freeze_base_rna, 08_experiments_phase_3c_config_freeze_base_second_adt, 08_experiments_phase_3c_config_freeze_base_second_atac, 08_experiments_phase_3c_config_freeze_base_concat, 08_experiments_phase_3c_config_freeze_pca_classical, 08_experiments_phase_3c_config_freeze_base_space [EXTRACTED 1.00]
- **Phase 3D Classical Integration Methods** — 08_experiments_phase_3d_config_freeze_mofaplus, 08_experiments_phase_3d_config_freeze_scot [EXTRACTED 1.00]
- **scvi-tools Model Family** — 06_representations_02_deep_learned_representations_07_scvi_scvi, 06_representations_02_deep_learned_representations_08_totalvi_totalvi, 06_representations_02_deep_learned_representations_09_multivi_multivi [EXTRACTED 1.00]
- **Single-Cell Foundation Transformers** — 06_representations_02_deep_learned_representations_23_single_cell_transformers_scgpt, 06_representations_02_deep_learned_representations_23_single_cell_transformers_geneformer [EXTRACTED 1.00]
- **Biological Interpretation Layers** — 06_representations_01_classical_representation_families_43_regulatory_activity, 06_representations_01_classical_representation_families_44_developmental_time [INFERRED 0.80]
- **Spatial Multi-omics GNNs** — 06_representations_02_deep_learned_representations_39_spatialglue_spatialglue, 06_representations_02_deep_learned_representations_38_scglue_scglue [INFERRED 0.85]

## Communities (88 total, 51 thin omitted)

### Community 0 - "annotate_phase3c_runtime.py"
Cohesion: 0.09
Nodes (44): main(), Path, Add the accurate runtime scope to Phase 3C artifacts created before it was…, rewrite_csv(), cluster_and_evaluate(), ndarray, Frozen common KMeans and metric implementation for Phase 3C., sha256() (+36 more)

### Community 1 - "failures.py"
Cohesion: 0.09
Nodes (39): BaseException, Path, Traceable failed-run artifact creation., write_failure_artifacts(), _decode(), H5ADView, _index(), load_h5ad() (+31 more)

### Community 2 - "sha256()"
Cohesion: 0.10
Nodes (28): sha256(), Validation helpers for IDs, embeddings and immutable inputs., validate_embedding(), validate_row_mapping(), validate_unique_ids(), fit(), Thin wrapper around the official mofapy2 implementation., fit() (+20 more)

### Community 3 - "type"
Cohesion: 0.06
Nodes (39): type, type, type, properties, null, type, type, type (+31 more)

### Community 4 - "provenance.schema.json"
Cohesion: 0.06
Nodes (35): additionalProperties, type, type, pattern, type, type, type, null (+27 more)

### Community 5 - "enum"
Cohesion: 0.06
Nodes (35): enum, COLAB_CPU, COLAB_GPU, COLAB_HIGH_MEMORY, LOCAL_LIGHT, UNRESOLVED, compute_classification, additionalProperties (+27 more)

### Community 6 - "dataset"
Cohesion: 0.11
Nodes (30): dataset, experiment_id, method, preprocessing, seed, required, compute_classification, dataset (+22 more)

### Community 7 - "provenance-v2.schema.json"
Cohesion: 0.07
Nodes (29): additionalProperties, allOf, type, type, pattern, type, type, type (+21 more)

### Community 8 - "config.py"
Cohesion: 0.11
Nodes (12): DatasetInput, Any, Typed benchmark configuration objects; no biological data are loaded here., RunConfig, git_head(), Any, Machine-readable run provenance helpers., validate_provenance() (+4 more)

### Community 9 - "run-config.schema.json"
Cohesion: 0.07
Nodes (26): additionalProperties, type, type, pattern, type, minLength, type, type (+18 more)

### Community 10 - "enum"
Cohesion: 0.15
Nodes (23): enum, LN_A1, LN_D1, MB_E11, MB_E13, MB_E15, MB_E18, dataset (+15 more)

### Community 11 - "enum"
Cohesion: 0.16
Nodes (20): enum, BLOCKED, FAILED, INVALID, PLANNED, PREPARING, RUNNING, SUCCEEDED (+12 more)

### Community 12 - "items"
Cohesion: 0.13
Nodes (20): items, minItems, type, additionalProperties, required, type, inputs, items (+12 more)

### Community 13 - "check_phase2a_toys.py"
Cohesion: 0.40
Nodes (9): ari(), check(), choose2(), contingency(), entropy(), information(), main(), Check Phase 2A synthetic arithmetic only; never read datasets or fit models.… (+1 more)

### Community 14 - "Phase 3C Scientific Baseline R"
Cohesion: 0.25
Nodes (9): Phase 3C Scientific Baseline Run, Simple Concatenation (BASE_CONCAT), RNA-only Preprocessing (BASE_RNA), ADT-only Preprocessing (Suite L), ATAC-only Preprocessing (Suite B), Coordinates-only (BASE_SPACE), RNA PCA (PCA_CLASSICAL), MOFA+ Integration (+1 more)

### Community 15 - "inspect_h5ad.py"
Cohesion: 0.47
Nodes (8): column_values(), dataframe(), inspect(), main(), matrix_summary(), plain(), Read H5AD structure and descriptive values without modifying input or…, sha256()

### Community 16 - "summarize_matrices.py"
Cohesion: 0.44
Nodes (8): column_values(), decode(), inspect(), main(), Read-only, sparse-safe H5AD matrix summaries for Phase 1E. The utility never…, sha(), stats(), values()

### Community 17 - "Multilayer Perceptron (MLP)"
Cohesion: 0.25
Nodes (8): Multilayer Perceptron (MLP), Deterministic Autoencoder, Deep Count Autoencoder (DCA), Variational Autoencoder (VAE), scVI, totalVI, MultiVI, BABEL

### Community 18 - "Preprocessing Principles"
Cohesion: 0.33
Nodes (6): Preprocessing Principles, ADT Preprocessing, Zheng et al. (2017), Stoeckius et al. (2017), Buenrostro et al. (2013), AnnData Documentation

### Community 19 - "ASTRA Operating Rules"
Cohesion: 0.40
Nodes (6): ASTRA Operating Rules, Project Brief, Project README, Research Master, Research Questions, Source Policy

### Community 20 - "compare_features.py"
Cohesion: 0.53
Nodes (5): compare(), decode(), ids(), main(), Read-only comparison of AnnData obs/var identifiers; no harmonisation.

### Community 21 - "run_full_discordance_audit.py"
Cohesion: 0.47
Nodes (3): analyze_dataset(), gearys_c(), morans_i()

### Community 22 - "Chromatin"
Cohesion: 0.40
Nodes (5): Chromatin, Nucleosome, Chromatin Accessibility, scATAC-seq, Mouse Brain Datasets (E11-E18)

### Community 23 - "summarize_phase3c.py"
Cohesion: 0.50
Nodes (4): main(), Path, Derive Phase 3C aggregate and QC tables from canonical run artifacts., write_csv()

### Community 25 - "Scaled Dot-Product Attention"
Cohesion: 0.50
Nodes (4): Scaled Dot-Product Attention, Transformer Block, Geneformer, scGPT

### Community 26 - "summarize_annotations.py"
Cohesion: 0.67
Nodes (3): main(), Read-only CSV annotation summary; no label normalization or relabeling., summarize()

### Community 28 - "Promoters"
Cohesion: 0.67
Nodes (3): Promoters, Enhancers, Transcription Factors

### Community 29 - "Epigenetics"
Cohesion: 0.67
Nodes (3): Epigenetics, DNA Methylation, Histone Modifications

### Community 30 - "Cell Identity"
Cohesion: 0.67
Nodes (3): Cell Identity, Cell Lineage, scRNA-seq

### Community 31 - "Biology to Data"
Cohesion: 0.67
Nodes (3): Biology to Data, Measurement Concept Map, Data as Mathematical Objects

### Community 32 - "Singular Value Decomposition"
Cohesion: 0.67
Nodes (3): Singular Value Decomposition, Low-Rank Approximation, Principal Component Analysis

### Community 33 - "Mutual Information"
Cohesion: 0.67
Nodes (3): Mutual Information, Sinkhorn Algorithm, GSVA

### Community 34 - "Representation Principles"
Cohesion: 0.67
Nodes (3): Representation Principles, Multiview Fusion and Alignment, Information Loss Framework

### Community 36 - "MIDAS"
Cohesion: 0.67
Nodes (3): MIDAS, SimCLR, InfoNCE

### Community 37 - "Message Passing GNN"
Cohesion: 0.67
Nodes (3): Message Passing GNN, scGLUE, SpatialGlue

## Knowledge Gaps
- **206 isolated node(s):** `LN_A1`, `LN_D1`, `MB_E11`, `LN_A1`, `LN_D1` (+201 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **51 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `properties` connect `enum` to `enum`, `items`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `properties` connect `provenance-v2.schema.json` to `enum`, `enum`, `provenance.schema.json`, `enum`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `properties` connect `run-config.schema.json` to `items`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **What connects `LN_A1`, `LN_D1`, `MB_E11` to the rest of the system?**
  _206 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `annotate_phase3c_runtime.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09490196078431372 - nodes in this community are weakly interconnected._
- **Should `failures.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09019607843137255 - nodes in this community are weakly interconnected._
- **Should `sha256()` be split into smaller, more focused modules?**
  _Cohesion score 0.09871794871794871 - nodes in this community are weakly interconnected._
# Canonical method inventory

Phase 3A · 2026-09-12 · proposed design; no local performance results.

This is the canonical classification table for Phase 3A. A paper is not a candidate simply because it is registered. Selection status differs from pair compatibility and from successful reproduction. The detailed candidate contracts are in [METHOD_DATASET_MATRIX.csv](METHOD_DATASET_MATRIX.csv); their pipeline records use the same method IDs. Existing methods without a detailed row are retained as components or references, not silently lost. Source IDs for those references remain in [methods.csv](../../methods.csv).

| ID | Method | Tags | Selection | Reason / evidence |
|---|---|---|---|---|
| RNA_LIBRARY_SIZE | Library-size scaling | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| RNA_LOG1P | Log1p transform | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| RNA_HVG | Mean-variance variable-gene selection | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| RNA_ZSCORE | Per-feature z-score | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| ADT_CLR | Centered log-ratio | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| ATAC_BINARY | Binary peak detection | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| ATAC_TFIDF | Term frequency inverse document frequency | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| ATAC_LSI | Latent semantic indexing | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| RNA_QC_METRICS | RNA library size and detected features | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| ATAC_QC_METRICS | ATAC fragments TSS FRiP and nucleosome metrics | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| DOUBLET_FLAG | Doublet suspicion scoring | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| AMBIENT_ESTIMATE | Ambient RNA estimation | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| MATH_MINKOWSKI | Euclidean Manhattan and Minkowski distances | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_COSINE_PEARSON | Cosine and Pearson profile similarity | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_COVARIANCE | Sample covariance and standardization | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_MLE_BAYES | Likelihood MLE and Bayesian updating | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_SVD_FOUNDATION | Full reduced and compact SVD | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_LOWRANK_FOUNDATION | Truncated SVD low-rank approximation | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_GD_FOUNDATION | Gradient descent scalar update | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_L1_L2 | L1 and L2 regularization | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_NEIGHBOR_SETS | Nearest radius and mutual-neighbor sets | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_KERNEL_FOUNDATION | Linear and RBF kernels | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_INFORMATION | Entropy cross-entropy KL and mutual information | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_MASKED_LOSS | Masked reconstruction loss | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_FDR_BH | False discovery rate and BH step-up rule | FOUNDATIONAL | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_CONFUSION_METRICS | Accuracy precision recall specificity and F1 | DOWNSTREAM_ONLY | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_ARI | Adjusted Rand Index | DOWNSTREAM_ONLY | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_NMI | Arithmetic normalized mutual information | DOWNSTREAM_ONLY | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| MATH_SILHOUETTE | Silhouette coefficient | DOWNSTREAM_ONLY | REFERENCE_ONLY | Mathematical/evaluation component, not a standalone omics integration competitor. |
| PCA_CLASSICAL | Principal component analysis | REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_PCA](SOURCES.md#REP_PCA) |
| SPARSE_PCA_CLASSICAL | Sparse PCA | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| ICA_CLASSICAL | Independent component analysis | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| NMF_CLASSICAL | Non-negative matrix factorization | REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_NMF](SOURCES.md#REP_NMF) |
| INMF_LIGER | Integrative NMF (iNMF/LIGER) | INTEGRATION_METHOD | REFERENCE_ONLY | Useful across-sample comparator after batch identity and shared-feature contract resolved; does not by itself establish full spatial multimodal pipeline. |
| FA_CLASSICAL | Classical factor analysis | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| MOFA_MOFA2 | MOFA/MOFA+ | INTEGRATION_METHOD;MULTIOMICS_METHOD | CONDITIONAL | Detailed contract and sources: [REP_MOFA_PLUS](SOURCES.md#REP_MOFA_PLUS), [DOC_MOFA](SOURCES.md#DOC_MOFA) |
| CCA_CLASSICAL | Canonical correlation analysis | INTEGRATION_METHOD;MULTIOMICS_METHOD | INCLUDE | Detailed contract and sources: [REP_CCA](SOURCES.md#REP_CCA) |
| SPARSE_CCA | Sparse CCA | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| PLS_CLASSICAL | Partial least squares | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| MNN_ALIGNMENT | Mutual nearest-neighbor alignment | INTEGRATION_METHOD | REFERENCE_ONLY | Useful across-sample comparator after batch identity and shared-feature contract resolved; does not by itself establish full spatial multimodal pipeline. |
| HARMONY_ALIGNMENT | Harmony alignment | INTEGRATION_METHOD | REFERENCE_ONLY | Useful across-sample comparator after batch identity and shared-feature contract resolved; does not by itself establish full spatial multimodal pipeline. |
| SCANORAMA_ALIGNMENT | Scanorama integration | INTEGRATION_METHOD | REFERENCE_ONLY | Useful across-sample comparator after batch identity and shared-feature contract resolved; does not by itself establish full spatial multimodal pipeline. |
| KERNEL_PCA | Kernel PCA | REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_KPCA](SOURCES.md#REP_KPCA) |
| DIFFUSION_MAP | Diffusion maps | REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_DIFFUSION](SOURCES.md#REP_DIFFUSION) |
| TSNE | t-SNE | DOWNSTREAM_ONLY | REFERENCE_ONLY | Visualization/ordering output is not standalone evidence of integration or lineage. |
| UMAP | UMAP | DOWNSTREAM_ONLY | REFERENCE_ONLY | Visualization/ordering output is not standalone evidence of integration or lineage. |
| OT_CLASSICAL | Optimal transport | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| SINKHORN_OT | Entropic OT/Sinkhorn | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| GW | Gromov-Wasserstein | FOUNDATIONAL | REFERENCE_ONLY | Existing preprocessing or alternative mathematical component; covered by explicit baseline/ablation design rather than extra full competitor. |
| GSVA | Gene-set variation analysis | BIOLOGICAL_PRIOR_METHOD;REPRESENTATION_ONLY | CONDITIONAL | Reference panel/annotation provenance needed; biological-prior extensions deferred beyond core. |
| SCENIC | SCENIC regulon activity | BIOLOGICAL_PRIOR_METHOD;REPRESENTATION_ONLY | CONDITIONAL | Reference panel/annotation provenance needed; biological-prior extensions deferred beyond core. |
| CHROMVAR | chromVAR motif deviations | BIOLOGICAL_PRIOR_METHOD;REPRESENTATION_ONLY | CONDITIONAL | Reference panel/annotation provenance needed; biological-prior extensions deferred beyond core. |
| PSEUDOTIME_CONCEPT | Pseudotemporal ordering (concept) | DOWNSTREAM_ONLY | REFERENCE_ONLY | Visualization/ordering output is not standalone evidence of integration or lineage. |
| DCA_NEURAL | DCA | REPRESENTATION_ONLY | REFERENCE_ONLY | RNA denoising or cross-modal prediction question adds redundant/secondary task to present core; retain source, no performance-based exclusion. |
| SCVI_NEURAL | scVI | REPRESENTATION_ONLY | REFERENCE_ONLY | RNA denoising or cross-modal prediction question adds redundant/secondary task to present core; retain source, no performance-based exclusion. |
| TOTALVI_NEURAL | totalVI | INTEGRATION_METHOD;MULTIOMICS_METHOD | CONDITIONAL | Detailed contract and sources: [TOTALVI_2021](SOURCES.md#TOTALVI_2021), [DOC_TOTALVI](SOURCES.md#DOC_TOTALVI) |
| MULTIVI_NEURAL | MultiVI | INTEGRATION_METHOD;MULTIOMICS_METHOD | CONDITIONAL | Detailed contract and sources: [MULTIVI_2023](SOURCES.md#MULTIVI_2023), [DOC_MULTIVI](SOURCES.md#DOC_MULTIVI) |
| SCGLUE_NEURAL | scGLUE | BIOLOGICAL_PRIOR_METHOD;INTEGRATION_METHOD | CONDITIONAL | Detailed contract and sources: [SCGLUE_2022](SOURCES.md#SCGLUE_2022), [DOC_GLUE](SOURCES.md#DOC_GLUE), [DOC_GLUE_RELEASE](SOURCES.md#DOC_GLUE_RELEASE) |
| COBOLT_NEURAL | Cobolt | INTEGRATION_METHOD;MULTIOMICS_METHOD | CONDITIONAL | Detailed contract and sources: [COBOLT_2021](SOURCES.md#COBOLT_2021) |
| BABEL_NEURAL | BABEL | INTEGRATION_METHOD | REFERENCE_ONLY | RNA denoising or cross-modal prediction question adds redundant/secondary task to present core; retain source, no performance-based exclusion. |
| SPAMI_NEURAL | SpaMI | SPATIAL_MULTIOMICS_METHOD;INTEGRATION_METHOD | CONDITIONAL | Detailed contract and sources: [SPAMI_2025](SOURCES.md#SPAMI_2025) |
| SPATIALGLUE_NEURAL | SpatialGlue | SPATIAL_MULTIOMICS_METHOD;INTEGRATION_METHOD | CONDITIONAL | Detailed contract and sources: [LONG_SPATIALGLUE_2024](SOURCES.md#LONG_SPATIALGLUE_2024), [DOC_SPATIALGLUE_LN](SOURCES.md#DOC_SPATIALGLUE_LN) |
| SCGPT_NEURAL | scGPT | FOUNDATION_MODEL;REPRESENTATION_ONLY | REFERENCE_ONLY | RNA pretraining/vocabulary and tissue/species coverage need a separate transfer question; does not establish current ADT/ATAC/spatial integration. [SCGPT_2024](SOURCES.md#SCGPT_2024) |
| GENEFORMER_NEURAL | Geneformer | FOUNDATION_MODEL;REPRESENTATION_ONLY | REFERENCE_ONLY | RNA pretraining/vocabulary and tissue/species coverage need a separate transfer question; does not establish current ADT/ATAC/spatial integration. [GENEFORMER_2023](SOURCES.md#GENEFORMER_2023) |
| GARFIELD_NEURAL | Garfield | SPATIAL_MULTIOMICS_METHOD;INTEGRATION_METHOD | CONDITIONAL | Detailed contract and sources: [GARFIELD_2026](SOURCES.md#GARFIELD_2026) |
| SCIGMA_NEURAL | SCIGMA | SPATIAL_MULTIOMICS_METHOD;INTEGRATION_METHOD | CONDITIONAL | Detailed contract and sources: [SCIGMA_2026](SOURCES.md#SCIGMA_2026), [DOC_SCIGMA_RNA_ATAC](SOURCES.md#DOC_SCIGMA_RNA_ATAC), [DOC_SCIGMA_RNA_ADT](SOURCES.md#DOC_SCIGMA_RNA_ADT) |
| ARISE_NEURAL | ARISE | SPATIAL_MULTIOMICS_METHOD;INTEGRATION_METHOD | CONDITIONAL | Detailed contract and sources: [ARISE_2026](SOURCES.md#ARISE_2026) |
| HYPERGRAPH_NN | Hypergraph neural network | FOUNDATIONAL | REFERENCE_ONLY | General architecture building block; project-specific construction/implementation is outside Phase3A. |
| RGCN_NEURAL | Relational GCN | FOUNDATIONAL | REFERENCE_ONLY | General architecture building block; project-specific construction/implementation is outside Phase3A. |
| BASE_RNA | RNA separate | REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_PCA](SOURCES.md#REP_PCA) |
| BASE_SECOND | Second modality separate | REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_PCA](SOURCES.md#REP_PCA) |
| BASE_CONCAT | Scaled concatenation | REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_PCA](SOURCES.md#REP_PCA) |
| BASE_SPACE | Coordinates only | SPATIAL_METHOD;REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_KPCA](SOURCES.md#REP_KPCA) |
| SPATIAL_KERNEL | Spatial kernel control | SPATIAL_METHOD;REPRESENTATION_ONLY | INCLUDE | Detailed contract and sources: [REP_KPCA](SOURCES.md#REP_KPCA) |
| WNN_INTEGRATION | WNN | INTEGRATION_METHOD;MULTIOMICS_METHOD | CONDITIONAL | Detailed contract and sources: [WNN_2021](SOURCES.md#WNN_2021), [DOC_WNN](SOURCES.md#DOC_WNN) |
| SCOT_ALIGNMENT | SCOT | INTEGRATION_METHOD;MULTIOMICS_METHOD | CONDITIONAL | Detailed contract and sources: [SCOT_2022](SOURCES.md#SCOT_2022) |
| MIDAS_NEURAL | MIDAS | INTEGRATION_METHOD;MULTIOMICS_METHOD | CONDITIONAL | Detailed contract and sources: [MIDAS_2024](SOURCES.md#MIDAS_2024) |
| SMART_NEURAL | SMART | SPATIAL_MULTIOMICS_METHOD;INTEGRATION_METHOD | CONDITIONAL | Detailed contract and sources: [SMART_2026](SOURCES.md#SMART_2026) |
| PASTE_ALIGNMENT | PASTE | SPATIAL_METHOD;INTEGRATION_METHOD | REFERENCE_ONLY | Detailed contract and sources: [ZEIRA_NATMETHODS_2022](SOURCES.md#ZEIRA_NATMETHODS_2022) |

No image-dependent full pipeline is admitted. An image-required configuration receives EXCLUDE for core scope, even if its parent method offers a separately documented image-free variant. No entire method is rejected based on publication age.

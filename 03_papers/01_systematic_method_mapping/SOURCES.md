# Source and search ledger

Phase 3A · 2026-09-12 · literature synthesis and proposed benchmark design; no local model results.

## Evidence use and search boundary

This is a systematic **project-scoped evidence map**, not an exhaustive PRISMA review or a performance meta-analysis. Searches on 2026-09-12 started with the named Phase 2B/2C methods, then followed primary publications, official code availability and input tutorials. Queries included “Garfield spatial multiomics official”, “SCIGMA Nature Genetics 2026”, “ARISE spatial multiomics”, “SCOT FOSCTTM”, “Signac merging different peak sets”, “scIB batch biological conservation”, and “spatial domain metrics PAS CHAOS”. Follow-up searches added SMART (same dataset lineage), WNN and SCOT (non-neural integration), and SpaMosaic as a counterexample. Search coverage is bounded by these tasks; omission does not establish absence from the literature.

FACT = source or local inspection evidence. Compatibility classifications are INTERPRETATION of input contracts under local constraints. Benchmark policies are PROPOSED design decisions. LITERATURE_REPORTED numbers are never project RESULTs. Local schema checks below are repository validation only.

No source was selected because it reports the largest score. Metadata/abstract access is insufficient for asserting uninspected defaults. Unknown means unresolved, not absent. Repositories were browsed, not cloned, installed or executed. Access date throughout: 2026-09-12; reused foundations retain their earlier source-access qualifications.

## Local dataset evidence

[Phase 1E statistics](../../02_omics/02_preprocessing_qc_statistics/DATASET_STATISTICS.md), [exact ATAC feature IDs](../../02_omics/02_preprocessing_qc_statistics/features_mouse_ATAC.json), [annotations](../../02_omics/02_preprocessing_qc_statistics/annotation_summary.json), [coordinates](../../02_omics/02_preprocessing_qc_statistics/coordinate_summary.json), and [dataset registry](../../datasets.csv). These are prior read-only observations; raw data were not reopened this phase. Count semantics, physical units and biological replicate identities remain unresolved.

## Registered sources actually used

<a id="ARISE_2026"></a>
### ARISE_2026

Wang X; Su Y; Hao G; Wang M; Wang Y; Li X (2026). [ARISE: RNA-anchored shared-edge topology and hierarchical fusion for spatial multi-omics integration](https://academic.oup.com/bioinformatics/article/42/7/btag465/8721301). Bioinformatics 42(7):btag465. DOI: 10.1093/bioinformatics/btag465.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="COBOLT_2021"></a>
### COBOLT_2021

Gong B; Zhou Y; Purdom E (2021). [Cobolt: integrative analysis of multimodal single-cell sequencing data](https://doi.org/10.1186/s13059-021-02556-z). Genome Biology. DOI: 10.1186/s13059-021-02556-z.

Access/use: Reused Phase 1–2 source; 06_representations/02_deep_learned_representations/SOURCES.md; located_online.

<a id="DOC_GLUE"></a>
### DOC_GLUE

Cao ZJ; Gao G; GLUE developers (unknown). [GLUE tutorials](https://scglue.readthedocs.io/en/latest/). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_GLUE_RELEASE"></a>
### DOC_GLUE_RELEASE

GLUE developers (unknown). [GLUE release notes](https://github.com/gao-lab/GLUE/blob/master/docs/release.rst). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_MOFA"></a>
### DOC_MOFA

MOFA developers (unknown). [MOFA2 FAQ](https://biofam.github.io/MOFA2/faq.html). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_MULTIVI"></a>
### DOC_MULTIVI

scvi-tools developers (unknown). [MultiVI model and missing-modality requirements](https://docs.scvi-tools.org/en/stable/user_guide/models/multivi.html). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_SCIB_CONNECTIVITY"></a>
### DOC_SCIB_CONNECTIVITY

scib-metrics developers (unknown). [Graph connectivity metric](https://scib-metrics.readthedocs.io/en/latest/generated/scib_metrics.graph_connectivity.html). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_SCIGMA_RNA_ADT"></a>
### DOC_SCIGMA_RNA_ADT

SCIGMA developers (unknown). [SCIGMA Tutorial 2: RNA and protein](https://scigma-tutorial.readthedocs.io/en/latest/SCIGMA-Spots.html). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_SCIGMA_RNA_ATAC"></a>
### DOC_SCIGMA_RNA_ATAC

SCIGMA developers (unknown). [SCIGMA Tutorial 1: RNA and epigenomics](https://scigma-tutorial.readthedocs.io/en/latest/Tutorial%201%20Spatial%20ATAC-RNA-seq.html). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_SIGNAC_MERGE"></a>
### DOC_SIGNAC_MERGE

Signac developers (unknown). [Merging objects with different peak sets](https://stuartlab.org/signac/articles/merging). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_SPATIALGLUE_LN"></a>
### DOC_SPATIALGLUE_LN

SpatialGlue developers (unknown). [SpatialGlue Tutorial 1: human lymph node](https://spatialglue-tutorials.readthedocs.io/en/latest/Tutorial%201_data%20integration%20for%20human%20lymph%20node%20(10x%20Genomics%20Visium,%20in-house%20data).html). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_TOTALVI"></a>
### DOC_TOTALVI

scvi-tools developers (unknown). [totalVI model and data requirements](https://docs.scvi-tools.org/en/latest/user_guide/models/totalvi.html). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="DOC_WNN"></a>
### DOC_WNN

Seurat developers (unknown). [Weighted nearest neighbor analysis](https://satijalab.org/seurat/archive/v4.3/weighted_nearest_neighbor_analysis). Official project documentation. DOI: not_applicable.

Access/use: Official documentation page inspected for the linked input/metric contract.

<a id="GARFIELD_2026"></a>
### GARFIELD_2026

Zhou W; Fan X; Li L; Zheng J; Liu X; Jin W; Tian L (2026). [Graph-based contrastive learning enables unified integration and niche transfer across single-cell and spatial multi-omics](https://academic.oup.com/bib/article/27/4/bbag432/8762914). Briefings in Bioinformatics 27(4):bbag432. DOI: 10.1093/bib/bbag432.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="GENEFORMER_2023"></a>
### GENEFORMER_2023

Theodoris CV et al. (2023). [Transfer learning enables predictions in network biology](https://doi.org/10.1038/s41586-023-06139-9). Nature. DOI: 10.1038/s41586-023-06139-9.

Access/use: Reused Phase 1–2 source; 06_representations/02_deep_learned_representations/SOURCES.md; located_online.

<a id="LONG_SPATIALGLUE_2024"></a>
### LONG_SPATIALGLUE_2024

Long Y; Ang KS; Sethi R; et al. (2024). [Deciphering spatial domains from spatial multi-omics with SpatialGlue](https://www.nature.com/articles/s41592-024-02316-4). Nature Methods. DOI: 10.1038/s41592-024-02316-4.

Access/use: Reused Phase 1–2 source; https://www.nature.com/articles/s41592-024-02316-4; located_online.

<a id="MATH_SKLEARN_CLUSTER_DOC"></a>
### MATH_SKLEARN_CLUSTER_DOC

Scikit-learn developers (unknown). [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation). scikit-learn official documentation. DOI: not_applicable.

Access/use: Reused Phase 1–2 source; https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation; located_online.

<a id="MIDAS_2024"></a>
### MIDAS_2024

He Z; Hu S; Chen Y; An S; Zhou J; Liu R; Shi J; Wang J; Dong G; Shi J; Zhao J; Ou-Yang L; Zhu Y; Bo X; Ying X (2024). [Mosaic integration and knowledge transfer of single-cell multimodal data with MIDAS](https://www.nature.com/articles/s41587-023-02040-y). Nature Biotechnology 42:1594–1605. DOI: 10.1038/s41587-023-02040-y.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="MULTIVI_2023"></a>
### MULTIVI_2023

Ashuach T et al. (2023). [MultiVI: deep generative model for the integration of multimodal data](https://doi.org/10.1038/s41592-023-01909-9). Nature Methods. DOI: 10.1038/s41592-023-01909-9.

Access/use: Reused Phase 1–2 source; 06_representations/02_deep_learned_representations/SOURCES.md; located_online.

<a id="OMICS_METRICS_2025"></a>
### OMICS_METRICS_2025

Luo S; Germain PL; von Meyenn F; Robinson MD (2025). [On metrics for subpopulation detection in single-cell and spatial omics data](https://academic.oup.com/nar/article/53/18/gkaf921/8266921). Nucleic Acids Research 53(18):gkaf921. DOI: 10.1093/nar/gkaf921.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="REP_CCA"></a>
### REP_CCA

Hotelling H (1936). [Relations between two sets of variates](https://academic.oup.com/biomet/article-abstract/28/3-4/321/220073). Biometrika 28(3–4):321–377. DOI: 10.1093/biomet/28.3-4.321.

Access/use: Reused Phase 1–2 source; Publisher abstract/identity; modern formulation supported by Witten and official cross-decomposition documentation; identity_and_abstract_checked.

<a id="REP_CHROMVAR"></a>
### REP_CHROMVAR

Schep AN; Wu B; Buenrostro JD; Greenleaf WJ (2017). [chromVAR: inferring transcription-factor-associated accessibility from single-cell epigenomic data](https://pubmed.ncbi.nlm.nih.gov/28825706/). Nature Methods 14:975–978. DOI: 10.1038/nmeth.4401.

Access/use: Reused Phase 1–2 source; PubMed abstract and figure captions; official author repository documentation; identity_and_abstract_checked.

<a id="REP_DIFFUSION"></a>
### REP_DIFFUSION

Coifman RR; Lafon S (2006). [Diffusion maps](https://www.math.ucdavis.edu/~strohmer/courses/270/diffusion_maps.pdf). Applied and Computational Harmonic Analysis 21(1):5–30. DOI: 10.1016/j.acha.2006.04.006.

Access/use: Reused Phase 1–2 source; University-hosted original full paper; sections 2–3 diffusion operator and distance; identity_and_relevant_content_checked.

<a id="REP_GSVA"></a>
### REP_GSVA

Hänzelmann S; Castelo R; Guinney J (2013). [GSVA: gene set variation analysis for microarray and RNA-Seq data](https://link.springer.com/article/10.1186/1471-2105-14-7). BMC Bioinformatics 14:7. DOI: 10.1186/1471-2105-14-7.

Access/use: Reused Phase 1–2 source; Original full article; nonparametric gene-set scoring and Methods; identity_and_relevant_content_checked.

<a id="REP_HARMONY"></a>
### REP_HARMONY

Korsunsky I; Millard N; Fan J; Slowikowski K; Zhang F; Wei K; Baglaenko Y; Brenner M; Loh PR; Raychaudhuri S (2019). [Fast, sensitive and accurate integration of single-cell data with Harmony](https://www.nature.com/articles/s41592-019-0619-0). Nature Methods 16:1289–1296. DOI: 10.1038/s41592-019-0619-0.

Access/use: Reused Phase 1–2 source; Paper identity on official project site; official method documentation read; publisher failed and PMC CAPTCHA; identity_and_relevant_content_checked.

<a id="REP_KPCA"></a>
### REP_KPCA

Schölkopf B; Smola A; Müller KR (1998). [Nonlinear Component Analysis as a Kernel Eigenvalue Problem](https://is.mpg.de/en/publications/1509). Neural Computation 10(5):1299–1319. DOI: 10.1162/089976698300017467.

Access/use: Reused Phase 1–2 source; Author institution search-index record; direct page returned 403; exact eigencoordinate formulation supported by official decomposition guide; identity_and_relevant_content_checked.

<a id="REP_MOFA_PLUS"></a>
### REP_MOFA_PLUS

Argelaguet R; Arnol D; Bredikhin D; Deloro Y; Velten B; Marioni JC; Stegle O (2020). [MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data](https://link.springer.com/article/10.1186/s13059-020-02015-1). Genome Biology 21:111. DOI: 10.1186/s13059-020-02015-1.

Access/use: Reused Phase 1–2 source; Original full text; Methods, group/view model, likelihoods and code availability; identity_and_relevant_content_checked.

<a id="REP_NMF"></a>
### REP_NMF

Lee DD; Seung HS (1999). [Learning the parts of objects by non-negative matrix factorization](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/lee-nature-99.pdf). Nature 401:788–791. DOI: 10.1038/44565.

Access/use: Reused Phase 1–2 source; University-hosted original full paper; nonnegative factorization; identity_and_relevant_content_checked.

<a id="REP_OT"></a>
### REP_OT

Peyré G; Cuturi M (2019). [Computational Optimal Transport](https://arxiv.org/abs/1803.00567). Foundations and Trends in Machine Learning 11(5–6):355–607. DOI: 10.1561/2200000073.

Access/use: Reused Phase 1–2 source; Author preprint metadata/overview and book site; detailed solver equations supported by POT documentation; full PDF exceeds tool size; identity_and_relevant_content_checked.

<a id="REP_PCA"></a>
### REP_PCA

Jolliffe IT; Cadima J (2016). [Principal component analysis: a review and recent developments](https://pubmed.ncbi.nlm.nih.gov/26953178/). Philosophical Transactions of the Royal Society A 374:20150202. DOI: 10.1098/rsta.2015.0202.

Access/use: Reused Phase 1–2 source; PubMed identity/abstract; publisher forbidden and PMC CAPTCHA; derivations also supported by MML and official decomposition guide; identity_and_abstract_checked.

<a id="REP_POT"></a>
### REP_POT

Flamary R; Courty N; Gramfort A; Alaya MZ; Boisbunon A; Chambon S; Chapel L; Corenflos A; Fatras K; Fournier N; Gautheron L; Gayraud NT; Janati H; Rakotomamonjy A; Redko I; Rolet A; Schutz A; Seguy V; Sutherland DJ; Tavenard R; Tong A; Vayer T (2021). [POT: Python Optimal Transport](https://jmlr.org/papers/v22/20-451.html). Journal of Machine Learning Research 22(78):1–8. DOI: not_assigned.

Access/use: Reused Phase 1–2 source; Original journal software paper and official POT documentation; identity_and_relevant_content_checked.

<a id="REP_SCANORAMA"></a>
### REP_SCANORAMA

Hie B; Bryson B; Berger B (2019). [Efficient integration of heterogeneous single-cell transcriptomes using Scanorama](https://www.nature.com/articles/s41587-019-0113-3). Nature Biotechnology 37:685–691. DOI: 10.1038/s41587-019-0113-3.

Access/use: Reused Phase 1–2 source; Publisher abstract and code availability; author repository API documentation; publisher body paywalled; identity_and_abstract_checked.

<a id="REP_SCENIC"></a>
### REP_SCENIC

Aibar S; González-Blas CB; Moerman T; Huynh-Thu VA; Imrichova H; Hulselmans G; Rambow F; Marine JC; Geurts P; Aerts J; van den Oord J; Atak ZK; Wouters J; Aerts S (2017). [SCENIC: single-cell regulatory network inference and clustering](https://www.nature.com/articles/nmeth.4463). Nature Methods 14:1083–1086. DOI: 10.1038/nmeth.4463.

Access/use: Reused Phase 1–2 source; Publication identity and workflow verified through official author repository; publisher fetch failed; identity_and_relevant_content_checked.

<a id="SCGLUE_2022"></a>
### SCGLUE_2022

Cao ZJ; Gao G (2022). [Multi-omics single-cell data integration and regulatory inference with graph-linked embedding](https://doi.org/10.1038/s41587-022-01284-4). Nature Biotechnology. DOI: 10.1038/s41587-022-01284-4.

Access/use: Reused Phase 1–2 source; 06_representations/02_deep_learned_representations/SOURCES.md; located_online.

<a id="SCGPT_2024"></a>
### SCGPT_2024

Cui H et al. (2024). [scGPT: toward building a foundation model for single-cell multi-omics using generative AI](https://doi.org/10.1038/s41592-024-02201-0). Nature Methods. DOI: 10.1038/s41592-024-02201-0.

Access/use: Reused Phase 1–2 source; 06_representations/02_deep_learned_representations/SOURCES.md; located_online.

<a id="SCIB_2022"></a>
### SCIB_2022

Luecken MD; Büttner M; Chaichoompu K; et al. (2022). [Benchmarking atlas-level data integration in single-cell genomics](https://www.nature.com/articles/s41592-021-01336-8). Nature Methods 19:41–50. DOI: 10.1038/s41592-021-01336-8.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="SCIGMA_2026"></a>
### SCIGMA_2026

Chang S; Fleischmann A; Ma Y (2026). [Scalable, generalizable and uncertainty-aware integration of spatial multiomics across diverse modalities and platforms with SCIGMA](https://www.nature.com/articles/s41588-026-02706-8). Nature Genetics 58:2284–2302. DOI: 10.1038/s41588-026-02706-8.

Access/use: Publisher metadata, abstract and code availability inspected; detailed input/backend evidence comes from official tutorials, not a claim of full subscription text access.

<a id="SCOT_2022"></a>
### SCOT_2022

Demetci P; Santorella R; Sandstede B; Noble WS; Singh R (2022). [SCOT: Single-Cell Multi-Omics Alignment with Optimal Transport](https://pmc.ncbi.nlm.nih.gov/articles/PMC8812493/). Journal of Computational Biology 29(1):3–18. DOI: 10.1089/cmb.2021.0446.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="SIGNAC_2021"></a>
### SIGNAC_2021

Stuart T; Srivastava A; Madad S; Lareau CA; Satija R (2021). [Single-cell chromatin state analysis with Signac](https://www.nature.com/articles/s41592-021-01282-5). Nature Methods 18:1333–1341. DOI: 10.1038/s41592-021-01282-5.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="SMART_2026"></a>
### SMART_2026

Du Z; Chen Q; Huang W; Chen J; Zheng X (2026). [SMART: spatial multi-omic aggregation using graph neural networks and metric learning](https://www.nature.com/articles/s41467-026-70821-5). Nature Communications 17:2876. DOI: 10.1038/s41467-026-70821-5.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="SPAMI_2025"></a>
### SPAMI_2025

Gao C et al. (2025). [A graph neural network-based spatial multi-omics data integration method for deciphering spatial domains](https://doi.org/10.1371/journal.pcbi.1013546). PLOS Computational Biology. DOI: 10.1371/journal.pcbi.1013546.

Access/use: Reused Phase 1–2 source; 06_representations/02_deep_learned_representations/SOURCES.md; located_online.

<a id="SPAMOSAIC_2026"></a>
### SPAMOSAIC_2026

Yan X; Fang Z; Ang KS; et al. (2026). [Mosaic integration of spatial multi-omics with SpaMosaic](https://www.nature.com/articles/s41588-026-02573-3). Nature Genetics 58:1126–1137. DOI: 10.1038/s41588-026-02573-3.

Access/use: Publisher abstract/metadata inspected; used only as a counterexample to a blanket absence of spatial mosaic methods; no reproduction candidacy asserted.

<a id="TOTALVI_2021"></a>
### TOTALVI_2021

Gayoso A et al. (2021). [Joint probabilistic modeling of single-cell multi-omic data with totalVI](https://www.nature.com/articles/s41592-020-01050-x). Nature Methods 18:272–282. DOI: 10.1038/s41592-020-01050-x.

Access/use: Reused Phase 1–2 source; 06_representations/02_deep_learned_representations/SOURCES.md; located_online.

<a id="WNN_2021"></a>
### WNN_2021

Hao Y; Hao S; Andersen-Nissen E; et al. (2021). [Integrated analysis of multimodal single-cell data](https://pubmed.ncbi.nlm.nih.gov/34062119/). Cell 184:3573–3587.e29. DOI: 10.1016/j.cell.2021.04.048.

Access/use: Primary metadata and selected relevant sections inspected online; no local reproduction.

<a id="ZEIRA_NATMETHODS_2022"></a>
### ZEIRA_NATMETHODS_2022

Zeira R; Land M; Strzalkowski A; Raphael BJ (2022). [Alignment and integration of spatial transcriptomics data](https://www.nature.com/articles/s41592-022-01459-6). Nature Methods. DOI: 10.1038/s41592-022-01459-6.

Access/use: Reused Phase 1–2 source; Nature Methods; located_online.

<a id="ZIMMERMAN_PSEUDOREPLICATION_2021"></a>
### ZIMMERMAN_PSEUDOREPLICATION_2021

Zimmerman KD; Espeland MA; Langefeld CD (2021). [A practical solution to pseudoreplication bias in single-cell studies](https://www.nature.com/articles/s41467-021-21038-1). Nature Communications 12:738. DOI: 10.1038/s41467-021-21038-1.

Access/use: Reused Phase 1–2 source; https://www.nature.com/articles/s41467-021-21038-1; located_online.

## Code evidence

Official repositories, observed manifests, paper-version hints and unresolved execution issues are in [31_CODEBASE_VERIFICATION.md](31_CODEBASE_VERIFICATION.md) and [codebases.csv](../../codebases.csv). Bibliographic alias `SPATIALGLUE_2024` was consolidated into `LONG_SPATIALGLUE_2024`; these denote one publication, not two independent sources.

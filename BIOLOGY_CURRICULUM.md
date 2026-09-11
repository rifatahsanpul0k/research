# Biology Fundamentals and Omics Foundations

Status: Phase 1A molecular biology foundations complete, with documented Phase 1B corrections. Phase 1B gene regulation, epigenetics and chromatin foundations are complete at the verified-notes level. Phase 1C cellular and tissue biology foundations are complete at the reviewed-notes level; see its validation record. Later assay/method phases are not started. This roadmap links source-backed learning notes; study questions do not assert that the listed measurements exist in our datasets.

For every topic, document **biology -> measurement -> numerical representation -> computational relevance**, with primary/authoritative references, uncertainties, and a short explanation in the learner's own words.

| Order | Topic | Biology to understand | Measurement to investigate | Numerical representation to inspect | Computational question |
|---|---|---|---|---|---|
| 1 | DNA and genes | Sequence, loci, gene definitions | Sequencing and reference annotation | Sequences, genomic intervals, gene identifiers | Phase 1A complete; see `01_biology/01_molecular_biology/01_DNA.md` and `03_GENES.md`. |
| 2 | Transcription | RNA production and regulation | Assay capture of transcription-related signals | Gene/transcript count tables | Phase 1A complete; see `01_biology/01_molecular_biology/05_TRANSCRIPTION.md`. |
| 3 | RNA | RNA classes, isoforms, processing | RNA sequencing and capture protocols | Gene/transcript-by-observation matrices | Phase 1A complete; see `01_biology/01_molecular_biology/06_RNA.md`. |
| 4 | Proteins | Abundance, function, modification | ADT and other protein assays | Protein-feature matrices | Phase 1A complete; see `01_biology/01_molecular_biology/09_PROTEINS.md`. |
| 5 | Gene regulation | Regulatory relationships and context | Perturbation evidence, at principle level | Regulatory annotations and relation matrices | Phase 1B notes: 01, 11-13; distinguish association, directness and causal support. |
| 6 | Promoters and enhancers | Regulatory elements and genomic context | Regulatory annotation, contact and functional evidence | Interval and region-to-gene tables | Phase 1B notes: 02-04 and 11; mappings retain evidence and uncertainty. |
| 7 | Transcription factors | Binding, motifs, regulatory activity | Binding and motif-related evidence | Motif, target, and activity tables | Phase 1B note 05; TF expression is not TF activity. |
| 8 | Epigenetics | Mechanisms and persistence of regulation | Methylation and histone assay principles | Site/region-level measurements with coverage | Phase 1B notes 08-10; snapshot versus memory and context-dependent marks. |
| 9 | Chromatin accessibility | Accessible regions and interpretation | Probe-based measurement principles; protocols and peak calling deferred | Fragment, peak, or accessibility matrices | Phase 1B notes 06-07; zeros, units and feature definitions. |
| 10 | Cell types | Identity and classification conventions | Marker and reference annotation workflows | Cell labels and uncertainty records | What evidence supports a cell-type label?  Phase 1C foundation complete; see [ordered notes](01_biology/03_cellular_tissue_biology/CONCEPT_MAP.md). |
| 11 | Cell states | Context-dependent cellular programs | Expression and other state measurements | Scores, covariates, or latent variables | How can state be distinguished from identity and technical effects?  Phase 1C foundation complete; see [ordered notes](01_biology/03_cellular_tissue_biology/CONCEPT_MAP.md). |
| 12 | Tissue organization | Compartments and spatial relationships | Spatial sampling and coordinate assignment | Coordinates and compartment annotations | What spatial scale and observation unit are represented?  Phase 1C foundation complete; see [ordered notes](01_biology/03_cellular_tissue_biology/CONCEPT_MAP.md). |
| 13 | Signaling pathways | Molecular interactions and pathways | Curated evidence and perturbations | Pathway memberships and interaction tables | What is known versus inferred about pathway activity?  Phase 1C foundation complete; see [ordered notes](01_biology/03_cellular_tissue_biology/CONCEPT_MAP.md). |
| 14 | Immune and tissue biology | Human lymph-node and embryonic-brain foundations | Tissue-specific sampling and annotation practices | Cell/compartment annotations | Which tissue-specific distinctions must evaluation preserve?  Phase 1C foundation complete; see [ordered notes](01_biology/03_cellular_tissue_biology/CONCEPT_MAP.md). |
| 15 | Mutations and genetic variants | Variant types and biological effects | Variant detection and annotation | Genotype and variant tables | How are alleles, reference builds, and uncertainty encoded? |
| 16 | GWAS | Association study design and population structure | Genotyping and association estimation | Summary-statistic tables | What can an association establish about disease mechanisms? |
| 17 | eQTL | Genotype-expression associations | Matched genotype/expression studies | Variant-gene association tables | Which tissue, ancestry, and confounding constraints apply? |
| 18 | Disease mechanisms | Links across molecular, cellular, and tissue scales | Disease studies and curated evidence | Disease-association and phenotype tables | How should evidence strength constrain interpretation? |
| 19 | Single-cell sequencing | Isolation, capture, library generation, technical variation | RNA/ATAC/protein workflows and QC | Sparse matrices and observation metadata | What do zeros, counts, depth, and observation identity mean? |
| 20 | Spatial omics | Spatial sampling, resolution, and registration | Coordinate-linked molecular assays | Matrices plus coordinates and metadata | Are observations cells, spots, bins, or something else? |
| 21 | Multi-omics | Shared and modality-specific biological information | Paired and unpaired multimodal designs | Multiple matrices, feature maps, missingness masks | Which correspondences and integration objectives are justified? |

## Completion template for each topic

- Topic ID/title and status: `not_started`, `in_progress`, `verified_notes`, or `needs_revision`.
- Sources with precise supporting locations and evidence classifications.
- Biology: definitions, mechanisms, contextual limits, and remaining uncertainties.
- Measurement: assay process, units, resolution, sources of technical variation, and what is not measured.
- Numerical representation: rows, columns, units, identifiers, sparsity/missingness, and a sourced or explicitly synthetic example.
- Computational relevance: assumptions a representation or evaluation would require; no preferred architecture.
- Dataset connection: verified applicable datasets, or `unknown` pending inspection.
- Comprehension check: explain the full chain; distinguish measured quantities from derived quantities and inferred labels.
- Open questions and evidence needed to resolve them.

Begin with topics 1-4, then regulation/chromatin (5-9), cells/tissues/pathways (10-14), variants/disease (15-18), and assay integration (19-21). Revisit earlier notes when verified dataset technologies become known.

## Phase 1A completion record

- **Scope completed:** DNA; chromosomes and genome organization; genes; coding vs non-coding regions; transcription; RNA and major RNA types; gene expression; translation; proteins; DNA -> RNA -> protein integration.
- **Artifacts:** `01_biology/01_molecular_biology/01_DNA.md` through `10_CENTRAL_DOGMA_INTEGRATION.md`, plus `CONCEPT_MAP.md` and `BIOLOGY_TO_DATA.md`.
- **Boundary:** Did not start epigenetics, chromatin accessibility, scRNA-seq methods, CITE-seq, spatial transcriptomics methods, machine learning, representation comparison, graph construction, experiments, or novelty analysis.
- **Readiness note:** Ready for Phase 1B only as foundational biology learning. Dataset-specific claims remain unknown until dataset access and provenance are verified.

## Phase 1B study record (status at its completion)

- **Status:** verified_notes; Phase 1B complete after conceptual review and structural checks on 2026-09-11. See [validation and readiness](01_biology/02_gene_regulation/VALIDATION.md).
- **Topics, in order:** gene regulation; promoters; enhancers; silencers/insulators/other regulatory elements; transcription factors; chromatin; accessibility; epigenetics; DNA methylation; histone modifications; enhancer-promoter interactions; gene regulatory networks; cell identity/regulatory state; developmental regulation bridge.

## Phase 1D study record (status at its completion)

- **Status:** verified_notes; measurement and data-generation foundations completed 2026-09-11. See [validation](02_omics/01_measurement_and_data_generation/VALIDATION.md).
- **Topics, in order:** sample-to-matrix chain; sequencing; barcodes/UMIs; scRNA-seq; snRNA-seq; droplets; ADT/CITE-seq; scATAC-seq; spatial transcriptomics; spatial protein; multimodal pairing; zeros/sparsity; technical/biological variation; raw/processed levels; feature identifiers; spatial coordinates; sample hierarchy; QC foundations; data formats; primary dataset reconnaissance.
- **Boundary:** No preprocessing algorithms, normalization benchmark, dimension reduction, graph construction, representation learning, model implementation, experiment, or novelty analysis. Phase 1E is ready only after review of the recorded E15/E18 ATAC download uncertainty.
- **Notes:** [Phase 1B concept map](01_biology/02_gene_regulation/CONCEPT_MAP.md) links all 14 A-H topic notes in order.
- **Computational bridge:** [Biology to data](01_biology/02_gene_regulation/BIOLOGY_TO_DATA.md): RNA n x p, accessibility n x q, region-gene q x p, metadata, units, evidence and missingness.
- **Evidence:** [Source register and access limits](01_biology/02_gene_regulation/SOURCES.md); individual biological source records under 03_papers; papers.csv includes only references actually used.
- **Phase 1A cross-check:** corrected the Gerstein reference and gene-boundary explanation; clarified sequence transfer versus regulatory feedback, conceptual arrows versus molecular conversions, and protein abundance versus localization/activity. See RESEARCH_LOG.md.
- **Curriculum coverage:** foundational portions of rows 5-9; introductory bridges for cell identity/state and development. This does not complete the broader cells/tissues/pathways curriculum or any assay-method curriculum.
- **Unresolved:** dataset assays, observation units, pairing, stages, anatomy and annotations remain user-provided or unknown. No data were accessed.
- **Boundary:** no scRNA-seq/scATAC-seq methodology phase, CITE-seq, spatial transcriptomics, multi-omics integration, model implementation, representation comparison, research graph construction, experiment, disease association or novelty analysis.
- **Next authorized phase:** none. Phase 1C: Cellular Biology and Tissue Organization is the next proposed learning phase and has not begun.
- **Readiness:** Ready to begin Phase 1C when requested. Foundational molecular/regulatory reasoning is sufficient; cell/tissue organization and dataset-specific assay interpretation remain future work.

## Phase 1C preparation record — 2026-09-11 (historical snapshot)

Status: **in_progress**, not verified_notes or complete. See [source-backed preparation](01_biology/PHASE_1C_PREPARATION.md). Both prerequisite phases are present; initial Graphify code-only extraction found no code, as expected.

The received brief contains sections 0–13 and ends at `* neura` within section 14. The remaining text was requested. Preliminary evidence covers identity/state, heterogeneity, differentiation, lineage, cycle, signaling, interactions, matrix/environment, tissue organization, six distinct biological relationships, gradients, lymph-node foundations and introductory neural progenitors. This is a preparation record, not a claim that any full Phase 1C topic or all of its mechanisms have been completed.

Next: reconcile the rest of the brief; develop all required artifacts and biological depth; review conceptual consistency; validate evidence and tracking; run final Graphify. Do not advance to assay methodology or computational methods.

## Phase 1C completion record — 2026-09-11

- **Status:** reviewed source-backed foundations complete; [validation and readiness](01_biology/03_cellular_tissue_biology/VALIDATION.md). The missing continuation was supplied and reconciled with the preparation; all 18 requested topics are covered.
- **Topics:** identity; heterogeneity; differentiation; lineage; cycle; signaling; cell interactions; microenvironment; tissue organization; six spatial/biological relationships; boundaries/transitions; lymph-node foundations; LN spatial biology; embryonic mouse brain; developmental time; observation units; annotation; hierarchy.
- **Artifacts:** 18 A–H notes and [concept map](01_biology/03_cellular_tissue_biology/CONCEPT_MAP.md), [biology-to-data bridge](01_biology/03_cellular_tissue_biology/BIOLOGY_TO_DATA.md), [sources](01_biology/03_cellular_tissue_biology/SOURCES.md), validation: 22 files. Historical preparation retained separately.
- **Evidence:** 39 actually used references; 33 newly registered across both Phase 1C turns (14 preparation + 19 completion); six earlier entries reused. Registry total 71.
- **Previous phases:** no additional corrections to Phase 1A or Phase 1B required by this review.
- **Conceptual checks:** type/state; similarity/proximity/communication/ancestry; temporal versus lineage information; individual versus mixed observations; marker uncertainty; annotation hierarchy and anatomy provenance. Synthetic mixture and changing-composition examples are arithmetic demonstrations, not experiments.
- **Unresolved:** actual dataset assays, units, pairing, stages, regions, conditions and annotations remain unverified. Deeper biological study is listed in validation.
- **Readiness:** ready to begin Phase 1D: Omics Measurement Technologies and Data Generation when requested. No later phase has begun. Changes are local and uncommitted.

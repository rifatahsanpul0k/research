# Biology Fundamentals and Omics Foundations

Status: Phase 1A molecular biology foundations complete for DNA -> RNA -> protein. Remaining topics are not started. This is a learning roadmap, not a literature review or set of established biological claims. Complete source-backed notes before advanced method development. Study questions below do not assert that the listed measurements exist in our datasets.

For every topic, document **biology -> measurement -> numerical representation -> computational relevance**, with primary/authoritative references, uncertainties, and a short explanation in the learner's own words.

| Order | Topic | Biology to understand | Measurement to investigate | Numerical representation to inspect | Computational question |
|---|---|---|---|---|---|
| 1 | DNA and genes | Sequence, loci, gene definitions | Sequencing and reference annotation | Sequences, genomic intervals, gene identifiers | Phase 1A complete; see `01_biology/01_molecular_biology/01_DNA.md` and `03_GENES.md`. |
| 2 | Transcription | RNA production and regulation | Assay capture of transcription-related signals | Gene/transcript count tables | Phase 1A complete; see `01_biology/01_molecular_biology/05_TRANSCRIPTION.md`. |
| 3 | RNA | RNA classes, isoforms, processing | RNA sequencing and capture protocols | Gene/transcript-by-observation matrices | Phase 1A complete; see `01_biology/01_molecular_biology/06_RNA.md`. |
| 4 | Proteins | Abundance, function, modification | ADT and other protein assays | Protein-feature matrices | Phase 1A complete; see `01_biology/01_molecular_biology/09_PROTEINS.md`. |
| 5 | Gene regulation | Regulatory relationships and context | Perturbation and paired assay designs | Regulatory annotations and paired matrices | What separates association from causal evidence? |
| 6 | Promoters and enhancers | Regulatory elements and genomic context | Regulatory annotations and accessibility assays | Interval and region-to-gene tables | Which mappings are measured versus inferred? |
| 7 | Transcription factors | Binding, motifs, regulatory activity | Binding and motif-related evidence | Motif, target, and activity tables | What assumptions enter inferred activity scores? |
| 8 | Epigenetics | Mechanisms and persistence of regulation | Methylation and chromatin assays | Site/region-level measurements | Which mechanisms are observed by each assay? |
| 9 | Chromatin accessibility | Accessible regions and interpretation | ATAC assay generation and peak calling | Fragment, peak, or accessibility matrices | How do peak definitions and sparsity affect comparisons? |
| 10 | Cell types | Identity and classification conventions | Marker and reference annotation workflows | Cell labels and uncertainty records | What evidence supports a cell-type label? |
| 11 | Cell states | Context-dependent cellular programs | Expression and other state measurements | Scores, covariates, or latent variables | How can state be distinguished from identity and technical effects? |
| 12 | Tissue organization | Compartments and spatial relationships | Spatial sampling and coordinate assignment | Coordinates and compartment annotations | What spatial scale and observation unit are represented? |
| 13 | Signaling pathways | Molecular interactions and pathways | Curated evidence and perturbations | Pathway memberships and interaction tables | What is known versus inferred about pathway activity? |
| 14 | Immune and tissue biology | Human lymph-node and embryonic-brain foundations | Tissue-specific sampling and annotation practices | Cell/compartment annotations | Which tissue-specific distinctions must evaluation preserve? |
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

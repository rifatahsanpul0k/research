# Tabular single-cell and spatial multi-omics research

Status: research environment initialized on 2026-09-11. No literature review, dataset download, model implementation, or experiment has been performed.

Start with [RESEARCH_MASTER.md](RESEARCH_MASTER.md) for scope and phase gates, [BOOTSTRAP_REPORT.md](BOOTSTRAP_REPORT.md) for the initialization outcome, and [WORKSPACE_INVENTORY.md](WORKSPACE_INVENTORY.md) for the original resource inventory. The user's governing request is preserved verbatim in [PROJECT_BRIEF.md](PROJECT_BRIEF.md).

The next phase is **Biology Fundamentals and Omics Foundations**, using [BIOLOGY_CURRICULUM.md](BIOLOGY_CURRICULUM.md). Representations remain unranked; image-derived inputs are excluded from core research unless later requested.

## Working documents

| Purpose | Document |
|---|---|
| Scope, phases, evidence and reproducibility | [RESEARCH_MASTER.md](RESEARCH_MASTER.md) |
| Questions and prerequisites | [RESEARCH_QUESTIONS.md](RESEARCH_QUESTIONS.md) |
| Source and repository verification | [SOURCE_POLICY.md](SOURCE_POLICY.md) |
| Biological-learning roadmap | [BIOLOGY_CURRICULUM.md](BIOLOGY_CURRICULUM.md) |
| Paper extraction | [PAPER_SCHEMA.md](PAPER_SCHEMA.md) |
| Method families | [METHOD_TAXONOMY.md](METHOD_TAXONOMY.md) |
| Representation families | [REPRESENTATION_TAXONOMY.md](REPRESENTATION_TAXONOMY.md) |
| Dataset metadata and acquisition rules | [DATASET_SCHEMA.md](DATASET_SCHEMA.md) |
| Future experiments only | [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) |
| Component distinctions | [TERMINOLOGY.md](TERMINOLOGY.md) |
| Chronological decisions | [RESEARCH_LOG.md](RESEARCH_LOG.md) |

## Registries

[datasets.csv](datasets.csv) contains six user-specified datasets with external Drive links, unverified descriptive metadata, and explicit unknowns. [papers.csv](papers.csv), [methods.csv](methods.csv), [representations.csv](representations.csv), [codebases.csv](codebases.csv), and [experiments.csv](experiments.csv) are intentionally header-only.

Use stable identifiers and detailed records alongside these indexes. Future ID prefixes: `PAP-`, `MET-`, `REP-`, and `CODE-`, followed by a six-digit sequence. Dataset IDs retain the exact supplied names. Experiment IDs follow `EXPERIMENT_PROTOCOL.md`. Do not create records for resources that have not been identified.

## Directories

| Directory | Intended content |
|---|---|
| `01_biology/` | Source-backed biology learning notes |
| `02_omics/` | Assay generation and omics foundations |
| `03_papers/` | Verified papers and structured extractions |
| `04_datasets/` | Dataset records, manifests, raw/derived separation |
| `05_methods/` | Method definitions and comparisons when authorized |
| `06_representations/` | All representation families, including graphs |
| `07_models/` | Model specifications when authorized |
| `08_experiments/` | Immutable future run records |
| `09_results/` | Evidence linked to completed experiment IDs |
| `10_disease/` | Disease foundations and sourced associations |
| `11_ideas/` | Explicitly labeled later hypotheses/speculation |
| `12_writing/` | Later research writing |
| `code/` | Verified implementations and project code when authorized |

These directories currently contain only `.gitkeep` placeholders to preserve the scaffold in Git. There is no executable research environment or dependency lock yet; requirements must follow verified data and baseline needs.

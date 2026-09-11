# Research master

Initialized: 2026-09-11 (Asia/Dhaka). Status: environment bootstrap complete; research has not begun. Governing scope: the user's initialization brief, preserved in `PROJECT_BRIEF.md`.

## Scope and central question

This project studies computational representations and machine-learning methods for tabular single-cell and spatial multi-omics data.

**How should tabular spatial multi-omics data be represented computationally so that biologically meaningful cellular and tissue structure is preserved and can be effectively used by machine-learning models?**

The project is representation-agnostic. Raw features, latent spaces, matrix factorizations, probabilistic representations, neural embeddings, manifolds, kernels, optimal transport, graphs, hypergraphs, tensors, sets, tokens, prototypes, learned similarities, and hybrids are candidates for study. No family is preferred or ranked. Graph construction is a representation choice, not a prerequisite.

Secondary questions concern measurement fidelity, modality alignment, spatial information, biological interpretation, robustness, missing modalities, generalization, and reproducibility; see `RESEARCH_QUESTIONS.md`. These are planning questions, not research-gap or novelty claims.

## Data boundary

Allowed: gene-expression matrices, RNA counts, ADT/protein measurements, ATAC/chromatin-accessibility matrices, genomic annotations, pathway tables, gene/protein interaction information, disease-association tables, cell/sample metadata, spatial coordinates such as `(x, y)`, and biological knowledge databases.

Excluded from core research unless explicitly requested later: histology, microscopy, H&E images, image patches, CNN image features, and other image-derived representations. Existing labels must have their provenance checked for image dependence before deciding how they may be used. Spatial coordinates are allowed; a coordinate does not establish that an observation is a single cell.

## Primary dataset register

Names and biological groupings below are **user-provided metadata**, not verified file properties. Each Drive URL is recorded in `datasets.csv`; none has been accessed during bootstrap.

| Canonical dataset ID | User-specified biological system | User-specified sample/stage label | Local status |
|---|---|---|---|
| 10x_human_lymph_node_A1 | Human lymph node | A1 | Not present |
| 10x_human_lymph_node_D1 | Human lymph node | D1 | Not present |
| Mouse_Brain_E11_S1 | Mouse embryonic brain | E11 / S1 | Not present |
| Mouse_Brain_E13_S1 | Mouse embryonic brain | E13 / S1 | Not present |
| Mouse_Brain_E15_S1 | Mouse embryonic brain | E15 / S1 | Not present |
| Mouse_Brain_E18_S1 | Mouse embryonic brain | E18 / S1 | Not present |

Technology, modality pairing, observation unit, counts, coordinate availability, labels, donor structure, and original publications are unknown. Do not infer a specific 10x assay from a filename. Do not infer longitudinal pairing, replicate independence, or confirmed developmental timing from sample labels. A result in one biological system does not establish generalization to the other.

## Research sequence and gates

`Learn → Verify → Reproduce → Compare → Hypothesize → Test → Interpret → Refine`

| Phase | Status | Required evidence before progressing |
|---|---|---|
| 0. Environment bootstrap | Complete | Inventory, scope, schemas, registries, protocol, and log initialized |
| 1. Biology Fundamentals and Omics Foundations | Next; not started | Source-backed learning notes linking biology → measurement → numerical representation → computational relevance |
| 2. Dataset and source verification | Not started | Verified provenance, accessible files, modalities, units, annotations, and dataset manifests |
| 3. Representations, methods, and benchmark study | Not started | Structured primary-source extraction, relevant biology and measurement understood, limitations distinguished from hypotheses |
| 4. Baseline reproduction | Not started | Verified official implementations, pinned environments, documented preprocessing and evaluation |
| 5. Controlled comparisons | Not started | Comparable tasks, splits, budgets, metrics, and reproducible baselines |
| 6. Hypothesize and test | Not started | Evidence-supported question and prospective experiment plan; no automatic novelty claim |
| 7. Interpret and refine | Not started | Uncertainty, biological evaluation, limitations, and replication documented |

No literature review, model implementation, experiment, hyperparameter search, architecture proposal, or research conclusion is authorized by this bootstrap task.

## Evidence policy

| Classification | Meaning | Recording requirement |
|---|---|---|
| FACT | Directly supported by a reliable source | Source and precise supporting location; distinguish user report from independent verification |
| RESULT | Directly observed in our experiment | Experiment ID and saved output; bootstrap file inspection is an environment observation, not an experimental result |
| INTERPRETATION | Explanation of evidence | Link underlying evidence and state uncertainty and alternatives |
| HYPOTHESIS | Testable proposition | Identify a prospective test and possible falsifying outcome |
| SPECULATION | Unsupported possibility | Label explicitly; never substitute for established knowledge |

Use `unknown` for unavailable information. Use `not_applicable` only with a reason. Never invent citations, code behavior, scores, hyperparameters, dataset properties, or biological interpretations. Important future claims must be traceable under `SOURCE_POLICY.md`.

## Reproducibility principles

- Keep raw data immutable; record origin, acquisition date, license/access conditions, file checksums, and dataset versions.
- Separate raw data → preprocessing → initial representation → representation-learning mechanism → model → learned embedding → downstream task → evaluation. Record absent stages as not applicable.
- Pin code commits, dependencies, preprocessing, seeds, configurations, and split identifiers. Retain failed and negative runs.
- Define evaluation before testing; prevent preprocessing and selection leakage. Select independent evaluation units after donor/sample structure is verified.
- Record modality availability, spatial-input use, external knowledge, resource budgets, and any departures from baseline protocols.
- Assess each biological system separately; cross-system transfer requires its own explicit evaluation.
- Store biological evaluation and uncertainty alongside numerical metrics. Follow `EXPERIMENT_PROTOCOL.md` before future runs.

## Workspace map

`01_biology/`, `02_omics/`, `03_papers/`, `04_datasets/`, `05_methods/`, `06_representations/`, `07_models/`, `08_experiments/`, `09_results/`, `10_disease/`, `11_ideas/`, `12_writing/`, and `code/` are reserved work areas. The empty legacy `06_graphs/` directory was renamed to `06_representations/`; graphs are one family within that area.

Schemas govern future records; taxonomies are organizational scaffolds, not evidence reviews. Root CSV registries provide stable identifiers. `WORKSPACE_INVENTORY.md` records initial resources and `RESEARCH_LOG.md` records decisions.

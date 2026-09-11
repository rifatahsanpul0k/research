# Research questions

Status: planning only, 2026-09-11. No novelty, research-gap, or empirical-performance claim is made. “Established questions” means questions established by the project brief, not questions resolved by the field. All answers are currently unknown.

## Established questions

- EQ01: How should tabular spatial multi-omics data be represented to preserve biologically meaningful cellular and tissue structure for machine learning?
- EQ02: What biology and measurement processes must we understand before choosing representations or models?
- EQ03: How will we distinguish preprocessing, initial representations, learning mechanisms, models, embeddings, tasks, and evaluation?
- EQ04: How will we verify datasets, sources, and baseline reproducibility before making comparisons?

## Open questions

- OQ01: What modalities, assays, observation units, spatial coordinate systems, and raw/processed files are actually present in each linked dataset?
- OQ02: What do A1, D1, S1, and the E-stage labels denote in the source metadata? What donor, sample, batch, and replicate relationships exist?
- OQ03: Are modalities paired within observations, spatially registered, partially overlapping, or unmatched?
- OQ04: Which annotations exist, how were they produced, and what biological distinctions do their labels support?
- OQ05: Which representations and official baselines are compatible with the verified data and intended tasks?
- OQ06: Which published benchmarks have comparable modalities, preprocessing, and evaluation units?
- OQ07: What data-use conditions, missingness, coordinate units, and feature-identifier conventions apply?

## Exploratory questions

These identify possible lines of learning, not proposed solutions.

- XQ01: Which aspects of a representation can be traced back to measured features or documented biological knowledge?
- XQ02: How might cell state, cell identity, developmental stage, and tissue organization require different definitions of preserved structure?
- XQ03: When would spatial information be an input, an evaluation reference, or both, and what circularity would this introduce?
- XQ04: How might one distinguish shared modality information from modality-specific information?
- XQ05: Under what verified data conditions would external pathway or interaction tables be appropriate?

## Questions requiring experiments

Do not answer or execute these during bootstrap. Tasks, metrics, and feasibility remain undecided.

- TQ01: Under matched tasks and preprocessing, how do eligible representation families compare with simple baselines?
- TQ02: How sensitive are results to preprocessing, seeds, feature selection, missing modalities, and measurement perturbations?
- TQ03: What changes when spatial coordinates or external biological knowledge are included, under controlled input availability?
- TQ04: Does performance persist on biologically independent held-out units once those units are identified?
- TQ05: Does a result reproduce separately within human lymph node and mouse embryonic brain, and under an explicitly defined cross-system transfer task?
- TQ06: Do numerical improvements agree with independent biological evaluation, and at what runtime and memory cost?

Future question records should include ID, classification, supporting sources, prerequisites, status, planned evidence, resolution, and linked experiment IDs when applicable.

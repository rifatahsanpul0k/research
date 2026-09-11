# Research log

Chronological decision record. Dates use Asia/Dhaka unless another timezone is explicitly recorded. Bootstrap filesystem observations are environment evidence, not experimental research results.

## 2026-09-11 - 01: Inspect the initial environment

- **Decision/question:** What resources and prior work are present?
- **Evidence:** Recursive local inventory found 13 empty research directories, 12 zero-byte Markdown files, and Git metadata. Git working tree was clean at `33b125b`. See `WORKSPACE_INVENTORY.md`.
- **Reasoning:** Existing evidence must determine the starting phase; empty filenames do not demonstrate completed research.
- **Alternatives considered:** Infer progress from directory names; instead require actual content.
- **Outcome:** No local papers, data, codebases, experiments, results, or prerequisite learning notes found.
- **Unresolved issues:** External resource access, contents, provenance, and dataset properties remain unknown.

## 2026-09-11 - 02: Establish scope and component boundaries

- **Decision/question:** How should the workspace reflect the user's research constraints?
- **Evidence:** User initialization brief, preserved verbatim in `PROJECT_BRIEF.md`, requires representation-agnostic tabular research and excludes core image-derived representations.
- **Reasoning:** The organizational structure must not imply a preferred method before learning and verification.
- **Alternatives considered:** Retain the empty `06_graphs/` name; create a second representation directory. A single inclusive directory avoids a privileged graph area and overlapping destinations.
- **Outcome:** Renamed the empty directory to `06_representations/`; populated scope, questions, source rules, terminology, and unranked taxonomies. Taxonomy tradeoffs remain assessment prompts pending evidence.
- **Unresolved issues:** Suitable representations, tasks, and methods cannot be selected from the current inventory.

## 2026-09-11 - 03: Register supplied resources without guessing

- **Decision/question:** What can be entered in registries during bootstrap?
- **Evidence:** The user supplied six unique dataset names and Drive links, grouped into human lymph node and mouse embryonic brain. Local data directories were empty.
- **Reasoning:** User-provided descriptions are distinct from verified dataset properties; unavailable metadata must remain unknown.
- **Alternatives considered:** Infer assays from `10x`, treat names as verified metadata, or download data immediately. These would exceed the evidence or the initialization stopping point.
- **Outcome:** Initialized six dataset records with provenance, `user_provided_unverified` metadata, `not_present` local status, and `not_checked` access status. Created five header-only registries for papers, methods, representations, codebases, and experiments.
- **Unresolved issues:** Assays, modalities, pairing, observation units, dimensions, raw counts, coordinates, labels, donor/sample relationships, licenses, and publications require later verification.

## 2026-09-11 - 04: Define foundations and future procedures

- **Decision/question:** What should be ready before research starts, and where should this task stop?
- **Evidence:** The brief specifies Learn -> Verify -> Reproduce -> Compare -> Hypothesize -> Test -> Interpret -> Refine and expressly stops this task after initialization. No completed prerequisites were found.
- **Reasoning:** Roadmaps and schemas can be established without generating empirical claims or choosing an architecture.
- **Alternatives considered:** Begin literature review, install a modeling environment, acquire data, or run baselines now. Deferred because this task authorizes bootstrap only.
- **Outcome:** Initialized the 21-topic curriculum, paper/dataset schemas, future experiment protocol, README, and bootstrap report. Preserved empty directory structure with `.gitkeep` files. Recommended next phase: Biology Fundamentals and Omics Foundations.
- **Unresolved issues:** Learning sources and progress tracking must be populated during the next phase; software/hardware requirements depend on verified data and baselines.

## 2026-09-11 - 05: Validate bootstrap artifacts

- **Decision/question:** Are the initialization artifacts internally consistent and within scope?
- **Evidence:** Filesystem/CSV checks passed for ten populated core documents, an exact SHA-256 match between the preserved brief and user attachment, six unique dataset IDs and URLs matching the brief, explicit unknowns, five header-only registries, resolvable local Markdown links, 24 representation families with all ten requested fields, 21 curriculum topics, and 13 placeholder-only work directories. `git diff --check` reported no whitespace errors.
- **Reasoning:** Structural checks verify initialization without executing research experiments or asserting scientific validity.
- **Alternatives considered:** Run model or dataset tests; unnecessary because neither code nor data was introduced.
- **Outcome:** Bootstrap checks passed; 21 root files and 13 directory placeholders are present. Changes remain local and uncommitted.
- **Unresolved issues:** Scientific content verification and external resource inspection remain future work; these checks do not validate biological or methodological claims.

## 2026-09-11 - 06: Complete Phase 1A molecular biology foundations

- **Decision/question:** What biological foundation is required before reasoning about tabular single-cell and spatial multi-omics data?
- **Evidence:** Source-backed Phase 1A notes were created under `01_biology/01_molecular_biology/`, citing NCBI Bookshelf textbook material, Nature Reviews, Nature, Nature Methods, Nature Biotechnology, Genome Biology, and Molecular Systems Biology sources. The notes cover DNA, chromosomes/genome organization, genes, coding/non-coding regions, transcription, RNA, gene expression, translation, proteins, and DNA -> RNA -> protein integration.
- **Reasoning:** Later computational work needs a stable distinction between biological molecules, assay observations, feature identifiers, matrices, metadata, and interpretations. The DNA -> RNA -> protein chain is sufficient for the requested molecular foundation but not sufficient for dataset-specific assay interpretation.
- **Alternatives considered:** Start epigenetics, chromatin accessibility, scRNA-seq methods, CITE-seq, spatial transcriptomics methods, representation comparison, or ML experiments. Deferred because the stopping condition restricts this phase to molecular biology foundations.
- **Outcome:** Created ten topic files, `CONCEPT_MAP.md`, and `BIOLOGY_TO_DATA.md`; updated `BIOLOGY_CURRICULUM.md`, `TERMINOLOGY.md`, and `papers.csv`.
- **Unresolved issues:** Need deeper future study of RNA processing and isoforms, regulatory-region evidence, protein modifications and activity, assay chemistry, and dataset-specific feature provenance before making biological similarity claims.

## Future entry template

- **Date:** ISO date/time and timezone.
- **Decision/question:** Stable related question, dataset, paper, or experiment IDs.
- **Evidence:** Classification, exact source/artifact, and verification state.
- **Reasoning:** Connection between evidence and decision; uncertainty.
- **Alternatives considered:** Concrete options and why they were not selected.
- **Outcome:** Action or finding, with artifact links; do not upgrade a hypothesis to fact.
- **Unresolved issues:** Missing evidence and next action.

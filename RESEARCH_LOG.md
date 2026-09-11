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

## 2026-09-11 - 07: Open Phase 1B and inspect repository structure

- **Decision/question:** Is the repository ready for gene-regulation foundations, and what can Graphify establish?
- **Evidence:** Clean starting working tree on main at e2e6e62 (Phase 1A committed before this task). All ten Phase 1A topics and both integration documents were present. No applicable AGENTS.md or generated-output Git policy was found. No .gitignore exists; .git/info/exclude contained only its default comments.
- **Action:** Ran graphify . --code-only before literature research. It skipped 27 non-code files, found zero supported code files and exited 1 with an empty-graph diagnostic. It created graphify-out/cache/stat-index.json.
- **Interpretation:** This is a documentation/registry repository, so code-only extraction provides no code relationships. Empty output is not a scientific result or a successful biological consistency check.
- **Preservation:** Retain generated graphify-out content locally as untracked output; do not add an ignore rule, delete it or commit it automatically.
- **Scope:** Follow the supplied Phase 1B order and A-H format; measurement principles only. No dataset access, implementation, method survey, model, experiment, representation ranking or disease analysis.

## 2026-09-11 - 08: Correct Phase 1A bibliography and regulatory interpretation

- **Issue 1:** The intended Gerstein reference had a 2008 Gene title/DOI paired with the authors and in-text year of a different work. Corrected 03_GENES.md and papers.csv to Gerstein et al. (2007), *What is a gene, post-ENCODE? History and updated definition*, Genome Research 17:669-681, DOI 10.1101/gr.6339607, [PubMed PMID 17567988](https://pubmed.ncbi.nlm.nih.gov/17567988/). Retained immutable legacy ID GERSTEIN_GENE_2008, explicitly marking the misleading suffix in notes.
- **Issue 2:** The gene-definition paragraph blurred gene boundaries with associated regulatory DNA. The cited Gerstein definition explicitly separates regulation from the product-based gene definition. Clarified that distal regulatory elements need not be inside the annotated gene, in 03_GENES.md, CONCEPT_MAP.md and TERMINOLOGY.md.
- **Issue 3:** The simplified central-dogma wording could imply that regulatory protein feedback reverses sequence transfer, or that chromosome organization and expression are successive chemical conversions. Clarified 10_CENTRAL_DOGMA_INTEGRATION.md, CONCEPT_MAP.md and TERMINOLOGY.md using [Crick (1970), DOI 10.1038/227561a0](https://www.nature.com/articles/227561a0). The DNA -> RNA -> protein expression route remains; regulation acts on its processes.
- **Issue 4:** Protein abundance, localization and activity were insufficiently separated. Corrected 09_PROTEINS.md and 07_GENE_EXPRESSION.md: synthesis/removal determine total abundance; relocation and modification can change local abundance or activity without changing total abundance. Supporting source: Alberts et al. (2002), [Protein Function, phosphorylation section](https://www.ncbi.nlm.nih.gov/books/NBK26911/), and the already cited RNA-to-protein section.
- **Issue 5:** Amezquita was incorrectly named for the Genome Biology 2020 challenges paper in 05_TRANSCRIPTION.md, 07_GENE_EXPRESSION.md and BIOLOGY_TO_DATA.md. Corrected to [Laehnemann et al., Eleven grand challenges in single-cell data science](https://link.springer.com/article/10.1186/s13059-020-1926-6). The existing registry already identified this work.
- **Issue 6:** Phase 1A BIOLOGY_TO_DATA.md assigned Svensson's zero-inflation correspondence to Genome Biology. Corrected it to [Nature Biotechnology (2020), DOI 10.1038/s41587-019-0379-5](https://www.nature.com/articles/s41587-019-0379-5), matching the existing registry.
- **History:** Prior bootstrap and Phase 1A completion entries are retained. These are explicit corrections, not a claim that the original notes were error-free. No assay-method review was initiated to make bibliographic corrections.

## 2026-09-11 - 09: Develop Phase 1B biological foundations

- **Outcome:** Wrote 14 ordered A-H topic notes, CONCEPT_MAP.md, BIOLOGY_TO_DATA.md and SOURCES.md under 01_biology/02_gene_regulation/. Updated the curriculum and terminology. Added 24 actually used source records and registry entries (38 total rows), including reviews, focused primary work, a resource paper, textbooks and conceptual/consensus articles.
- **Evidence discipline:** Topic footnotes identify source locations; individual SOURCE_RECORD.md files state inspected material and limitations. Publisher subscription previews and intermittent PMC browser challenges are recorded. Bibliographic identity is verified separately from access depth; no full-method or supplement review is claimed from an abstract.
- **Conceptual decisions:** Treat accessibility as dynamic and probe-dependent; TF RNA as distinct from activity; methylation as context-dependent; histone marks as associations with defined scope; contact and inferred links as distinct from experimentally supported regulation; state, trajectory, stage and lineage as different properties.
- **Computational bridge:** Defines RNA n x p, accessibility n x q and region-gene q x p objects, count conventions, coordinates, coverage, missingness masks and evidence semantics. All values are synthetic. Matching dimensions do not establish paired observations or a causal expression model.
- **Representation neutrality:** Encountered tables, matrices, edge lists, bipartite relations, networks/graphs, hypergraphs, probabilities, feature vectors, tensors, sets, knowledge graphs and latent representations without constructing or ranking them. Existing taxonomy families already cover these forms, so REPRESENTATION_TAXONOMY.md was not changed.
- **Development boundary:** E11/E13/E15/E18 remain supplied labels, not independently verified stage metadata. No detailed mouse-brain literature review or data acquisition occurred.
- **Outstanding at this entry:** Final conceptual/structural validation and final Graphify run; see the following validation entry.

## 2026-09-11 - 10: Validate and close Phase 1B

- **Conceptual review:** Checked the chain from DNA/regulatory elements through chromatin, TF action, RNA/protein programs and cell identity. Confirmed that regulatory feedback is not reverse sequence transfer. Checked conditional interpretations of accessibility, TF activity, histone marks, methylation, contact, perturbation responses and lineage. Results and concrete comprehension checks are in [Phase 1B VALIDATION.md](01_biology/02_gene_regulation/VALIDATION.md).
- **Structural checks:** All 16 requested files are present; all 14 topics have A-H sections; local links and footnotes resolve; all 24 new references are actually cited; papers.csv has 38 unique IDs, 15 columns, no duplicate known DOI, no blank/malformed cells and valid extraction paths. Whitespace checks include new untracked notes/source records, in addition to git diff --check.
- **Scope verification:** Dataset/method/representation/experiment/codebase registries and representation taxonomy match HEAD. Assay, model, dataset, experiment, result and disease directories remain placeholder-only. Temporary document-check snippets introduced no repository code or research pipeline.
- **Final Graphify run:** Ran graphify . --code-only again after completing research and supporting records. It skipped 68 non-code files (65 docs and 3 paper-classified files), found zero code and exited 1 with the same empty-graph diagnostic. Graphify's file classifier does not determine the number of biological publications. No graph or code relationships were produced. Preserved graphify-out/cache/stat-index.json locally.
- **Conclusion:** Phase 1B is complete as source-backed foundational notes, with explicitly limited source-access depth and unresolved empirical questions. Graphify was executed twice; it did not produce a nonempty extraction. This limitation does not imply a missing biological analysis.
- **Next phase:** Ready for Phase 1C: Cellular Biology and Tissue Organization when requested. No later phase begun; no commit or push performed.

## Future entry template

- **Date:** ISO date/time and timezone.
- **Decision/question:** Stable related question, dataset, paper, or experiment IDs.
- **Evidence:** Classification, exact source/artifact, and verification state.
- **Reasoning:** Connection between evidence and decision; uncertainty.
- **Alternatives considered:** Concrete options and why they were not selected.
- **Outcome:** Action or finding, with artifact links; do not upgrade a hypothesis to fact.
- **Unresolved issues:** Missing evidence and next action.

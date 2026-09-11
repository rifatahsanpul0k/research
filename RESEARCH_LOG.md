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

## 2026-09-11 - 11: Open Phase 1C and identify incomplete brief

- **Repository:** Clean starting tree at eddb50b; Phase 1A and Phase 1B files and commits present. No repository AGENTS.md found.
- **Graphify:** Ran `graphify . --code-only` before research. Zero supported code files; 69 non-code files skipped (66 docs, 3 papers); exit 1, empty graph. Expected repository result, not scientific evidence or research failure. Existing tracked graphify-out/cache/stat-index.json was refreshed.
- **Input issue:** The 8055-byte attachment has 489 newline characters and ends literally at `* neura` in section 14. This is an incomplete input file, not output truncation. Sections 0–13 are available; final scope/artifact requirements and stopping condition are unavailable. Asked the user for the remaining text while continuing independent evidence work.
- **Scope:** Biological preparation only; no remote datasets, assay methods, algorithms, models, representation rankings, scientific graph construction or experiments.

## 2026-09-11 - 12: Preserve preliminary Phase 1C findings

- **Artifact:** Created 01_biology/PHASE_1C_PREPARATION.md with ordered preliminary findings, six formal relationship distinctions, an explicitly synthetic counterexample, source access depths and an outstanding-work list. Final topic filenames await the complete request.
- **Tracking:** Curriculum now says Phase 1C in_progress; added a preliminary terminology section. Added 14 actually used references to papers.csv (52 total), reusing the existing Wagner–Klein lineage entry without duplication. Citation details and inspected locations are in the preparation document; no irrelevant paper cards or paper downloads were created.
- **Evidence:** NCBI textbooks and publisher/PMC/PubMed review records support the preliminary synthesis. Abstract/indexed/preview access is identified explicitly. The preparation is not a full-text systematic review or a completed set of topic notes.
- **Conceptual constraints:** Type/state/ancestry are separate; persistent T-cell states need qualification; signaling compatibility is not proven communication; physical proximity does not imply molecular equivalence; textbook tissue anatomy is not a dataset annotation.
- **Unresolved:** Remainder of section 14 and any subsequent requirements; deeper known-topic coverage and final conceptual assessment. Phase 1C remains incomplete and no later phase has begun.

- **Preparation validation:** CSV checks passed for 52 rows and 15 fields, unique paper IDs and known DOIs, populated fields, 15 matching footnote references/definitions, and existing local links. Confirmed 12 Phase 1A and 18 Phase 1B Markdown files. `git diff --check` passed. These are preparation integrity checks, not Phase 1C conceptual completion.
- **End-of-preparation Graphify:** Repeated `graphify . --code-only`; zero supported code, 70 non-code files skipped (67 docs, 3 papers), exit 1 with expected empty graph. Rerun at eventual phase completion. Changes remain local and uncommitted.

## 2026-09-11 - 13: Resume Phase 1C from complete continuation

- **Input resolved:** User supplied the remainder of section 14 and sections 15–27. Reconciled with the original brief: 18 ordered A–H topics, 22 required files, biological-only scope, final Graphify and local/uncommitted review.
- **Preservation:** Retained the prior preparation and marked it historical with links to final artifacts. Existing local preparation changes were continued, not discarded. Prerequisite Phase 1A/1B content remains unchanged.
- **Research:** Extended source work on somatic/metabolic variation, cell junctions/mechanics/niches, domain-specific LN migration/anatomy, embryonic neural development, staging, observation compartments and annotation hierarchy. Read measurement papers only for biological unit/evidence distinctions; no assay-method review or implementation started.

## 2026-09-11 - 14: Assemble and conceptually review Phase 1C

- **Artifacts:** Created all 18 requested topic files plus CONCEPT_MAP.md, BIOLOGY_TO_DATA.md, SOURCES.md and VALIDATION.md under 01_biology/03_cellular_tissue_biology/. Updated curriculum and terminology with final coverage and retained preparation history.
- **References:** 39 sources actually cited in the completed notes; 19 additional entries this turn, 33 total added during Phase 1C, 71 total registry rows. Prior entries reused without duplicate IDs/DOIs. Institutional resource dates remain unknown where not supplied. Access limitations and supporting locations are recorded; no PDFs, code or datasets acquired.
- **Conceptual review:** Checked the molecular-program → phenotype → signaling/differentiation → interactions/environment → tissue organization chain with feedback; distinguished type/state, proximity/communication, resemblance/ancestry, stage/cycle/maturation, regions/types and cells/nuclei/mixtures. Validated the synthetic weighted-mixture and composition-change arithmetic.
- **Scope qualifications:** Mouse cortical examples are not whole-brain rules or project annotations. Embryonic progenitor/gliogenic processes are distinct from adult anatomy. FDCs differ from conventional DCs; microglia are not assigned neural-progenitor ancestry; S1 is not inferred to name somatosensory cortex.
- **Prior phases:** No additional Phase 1A or Phase 1B corrections required after reviewing their identity/developmental bridge and integration principles. This finding is not a claim of exhaustive re-review of every earlier source.
- **Remaining checks:** Final links/citations/registry/whitespace validation and requested code-only Graphify; results follow. Phase 1D remains unstarted.

## 2026-09-11 - 15: Validate and stop after Phase 1C

- **Conceptual completion:** All 18 ordered topics and required integration documents reviewed against the 12 biological distinctions and comprehension checks in VALIDATION.md. Completion is based on those checks, not mere file existence.
- **Integrity:** Passed exact 22-file inventory, 18 A–H structures, matching footnotes, 318 local links/anchors, 39 cited sources, 71-row/15-column registry, unique IDs/known DOIs, populated fields and existing extraction paths. Bibliographic identity/access depth are documented separately from unrestricted full-text availability.
- **Preservation:** datasets.csv matches HEAD byte-for-byte; no Phase 1A/1B files changed. Synthetic examples checked arithmetically. `git diff --check` passed.
- **Final Graphify:** `graphify . --code-only` exited 1 with expected empty graph; 0 supported code files, 92 non-code files skipped (89 docs, 3 papers), 19 unclassified files skipped. Existing tracked cache refreshed. No scientific graph constructed.
- **Outcome:** Phase 1C complete at reviewed-notes level; ready for Phase 1D when requested. Actual assays, observation units, donor/embryo relationships, anatomy and annotations remain unverified. No subsequent phase, ML work, benchmark, data analysis or experiment begun. All changes local and uncommitted for review.

## 2026-09-11 - 16: Begin and complete Phase 1D measurement foundations

- **Scope:** Completed the requested chain from specimen preparation through reads/signals, feature assignment, counts, matrices, metadata, coordinates, and annotations. No preprocessing algorithm, normalization benchmark, dimension reduction, graph construction, representation learning, model implementation, experiment, or novelty analysis was performed.
- **Context protocol:** Refreshed Repomix and ran Graphify at the start; generated Repomix output is ignored as disposable context. Graphify remains a structural/code check and is not biological evidence.
- **Evidence:** Added 35 actually used Phase 1D sources covering sequencing, droplets, UMIs, nuclei, CITE-seq/ADT, ATAC, spatial assays, QC/data hierarchy, official 10x/Illumina/AnnData/NIST/Ensembl formats, GEO records, MISAR-seq, and dataset-author documentation. Source classes and access depth are in `SOURCE_INDEX.json`; `papers.csv` was extended without duplicate source IDs.
- **Dataset reconnaissance:** All six user-linked Drive folders were visibly accessible. Each contained two H5AD files and one annotation CSV. Complete files were downloaded unchanged to ignored `04_datasets/*/raw/` directories and source IDs/URLs were recorded. A1 H5AD inspection verified RNA 3,484 × 18,085 CSR and ADT 3,484 × 31 CSR, shared 3,484 × 2 spatial arrays, feature metadata, and barcode IDs. The GEO record verifies the lymph-node Visium RNA/protein study and reports A1/D1 dimensions; SMART documentation verifies the E18.5 MISAR example dimensions and metadata fields. E11, E13, and E15 ATAC H5ADs pass read-only inspection with local dimensions recorded in the reconnaissance note. E18 ATAC was visible in Drive but not downloaded completely; it remains UNKNOWN and is excluded. A leftover E15 partial transfer is ignored and excluded.
- **Artifacts:** Added 20 topic notes, concept map, biology-to-data bridge, sources, validation, six dataset dossiers, remote-file manifest, and a read-only H5AD inspector. Raw data are Git-ignored; no large biological file is committed.
- **Conceptual review:** Confirmed read ≠ molecule, observation barcode ≠ UMI, protein abundance ≠ activity, accessibility ≠ expression, spot/bin ≠ cell, pairing ≠ row-number coincidence, zero ≠ universal absence, processed X ≠ raw counts, and coordinate numbers require units and frame. Two similar vectors are not automatically biologically equivalent.
- **Unresolved:** Exact raw FASTQ availability, chemistry/version, annotation releases, coordinate units, donor/embryo and section hierarchy, licensing, processing history, and complete E15/E18 ATAC checksums remain open. These are recorded as UNKNOWN rather than inferred from filenames.
- **Outcome:** Phase 1D is complete at source-backed notes plus partial dataset reconnaissance. Ready for Phase 1E only after review of the explicit unresolved dataset and transfer fields. Changes remain local and uncommitted.
- **Final checks:** Read-only inspection passed for all 17 complete H5AD files recorded in the manifest; checksum verification found no mismatch. Repomix completed with 183 files and no suspicious files. Final Graphify code-only completed with 4 code files, 9 nodes, 17 edges, and 2 communities. `git diff --check` passed.

## 2026-09-11 - 17: Begin and complete Phase 1E preprocessing/QC/statistical foundations

- **Scope:** Documented preprocessing assumptions, RNA/ADT/ATAC/spatial QC concepts, normalization and transformation formulas, count distributions, HVGs, scaling, missingness, confounding, doublets, ambient contamination, outliers, lineage and leakage. No matrix was transformed or filtered.
- **Read-only reconnaissance:** Added sparse-safe utilities for matrix summaries and identifier comparisons. All 11 complete local X matrices are CSR float32; exact logical sparsity, row totals/detections, coordinates, metadata and annotation categories are recorded. E18 ATAC remains unavailable and was not inferred.
- **Alignment:** A1/D1 RNA and ADT have same unique identifier sets and order with repeated IDs reported; E11/E13/E15 RNA similarly share order with repeated IDs. ATAC feature sets differ sharply (pairwise overlaps 3, 4 and 16); no harmonization. Paired observation IDs match in RNA/ADT or RNA/ATAC files where both exist.
- **Evidence:** Added Phase 1E method/statistical sources S36–S48 and corresponding papers/method registry rows. Sources distinguish biological rationale, statistical assumptions, software documentation and common practice.
- **Boundary:** No TF-IDF, LSI/SVD, graph, integration model, representation ranking, clustering, experiment, disease analysis or novelty claim. Phase 1E stops after validation and awaits explicit Phase 2A authorization.
- **Final checks:** Repomix completed with 236 files and no suspicious files. Graphify code-only completed with 16 re-extracted code files, 31 nodes, 47 edges and 5 communities; it created no scientific graph. `git diff --check` and CSV/JSON validation passed.

## 2026-09-11 - 18: Phase 2A mathematical and statistical foundations

- **Scope:** Created 36 ordered mathematical topic notes and four integration/source/validation documents in `05_methods/01_mathematical_foundations/`. Reviewed the data → vector → geometry/probability → linear algebra → latent coordinates → optimization → evaluation chain. No Phase 2B method study, research-model training, representation comparison, imputation or biological experiment was performed.
- **Operating-rule limitation:** The required `ASTRA_OPERATING_RULES.md` was not found in the workspace, searched ancestors or attachments. Requested its location from the user and proceeded with the explicit Phase 2A requirements. Verification against that missing file remains pending; full operating-rule compliance is not claimed.
- **Context:** Ran the requested Repomix and Graphify commands at the start and read packed project context. Initial Repomix: 236 files, 253,966 tokens, no suspicious files. Initial Graphify: 31 nodes, 47 edges, five communities. Graphify is a repository-structure tool, not a scientific graph operation.
- **Data boundary:** Reused verified Phase 1E dimensions and unit qualifications without opening or transforming raw assays. A1 RNA/ADT dimensional imbalance and E11 ATAC rank/storage bounds are derived arithmetic. E18 ATAC remains unavailable.
- **Evidence/tracking:** Registered 13 actually used mathematical/foundational references and reused two existing biological/statistical entries; source access limits are recorded. Added 17 foundation-method entries, expanded terminology, and clarified mathematical dimensions plus the permanent computational/statistical/biological evaluation principle in the taxonomy. Registry totals: 124 papers and 29 methods; no representation instances or experiments added.
- **Review:** Checked axis conventions, sample/population variance, full/thin/compact SVD, metric assumptions, concentration assumptions, missingness, latent nonidentifiability and metric edge cases. Corrected a rounded correlation and scalar-versus-matrix kernel notation during review. The synthetic checker passed 59 arithmetic checks; intermediate derivations are in TOY_CALCULATIONS.md.
- **Status:** Mathematical artifacts prepared; final integrity/context refresh follows in VALIDATION.md. Full missing-rule compliance review remains unresolved. Phase 2B remains unstarted, and changes are local/uncommitted.
- **Final validation:** Exact 40-file inventory, 80 local links/anchors, mathematical delimiters, all six CSV registries, unique IDs/known DOIs, new reference/method paths and source-ID relationships passed. Unchanged dataset/experiment/representation/codebase registries match HEAD; git diff --check passed. Synthetic checker: 59 passes. Final Repomix exited 0 with 277 files, 287,403 tokens and no suspicious files; final code-only Graphify exited 0 with 41 nodes, 65 edges, six communities (17 re-extracted inputs, 21 cached). These counts record the tool execution before this status append. Mathematical deliverables are finished; missing-rule compliance review remains pending.

## 2026-09-11 - 19: Restore governance and audit Phase 2A

- **Authorization and scope:** User requested the missing operating-rules file and a compliance review before Phase 2B. Created ASTRA_OPERATING_RULES.md by consolidating original project/phase instructions and the current requirements, including the permanent Repomix → Graphify → targeted originals → literature order. No previously existing verbatim file is claimed recovered.
- **Review:** Audited Phase 2A scope, representation neutrality, biological distinctions, notation/dimensions, worked examples, source identity/relevance, registries and repository changes. No PCA benchmarking, representation comparison, scientific graph construction, research training, integration experiment or novelty analysis was found.
- **Corrections:** Found an undefined determinant operator in the toy's shared notation and an unverified missingness attribution to MML. Added the determinant definition to CONCEPT_MAP.md; corrected sources in 30_MISSING_DATA.md using Seaman et al. (2013), DOI 10.1214/13-STS415, journal reprint sections 2/5. The loss remains a defined teaching objective. Directed 25_KERNELS.md to verified BHK section 5.3; made its 2018 manuscript/2020 publication distinction explicit. No existing formulas or worked arithmetic changed.
- **Tracking:** Added one actually used source to papers.csv (125 total), corrected two source relationships in methods.csv (29 total), updated SOURCES.md and superseded missing-governance status in VALIDATION.md. Created OPERATING_RULES_AUDIT.md with rule-by-rule findings. TERMINOLOGY.md and representations.csv required no audit edits. Earlier phase records and original validation counts remain historical.
- **Evidence limits:** No fabricated citation identified; full-text versus metadata/abstract access remains explicit. The missingness paper's author-deposited journal reprint was readable; some publisher endpoints remain inaccessible. This is a source-traceability correction, not an inference of a false mathematical claim from failed access.
- **Validation:** Existing fixed-input checker passed all 59 checks. Final registry/link/whitespace and Repomix/Graphify results follow in the audit record. No raw biological files were opened or modified by the audit; no new full-dataset checksum verification is claimed.
- **Outcome:** Phase 2A compliant following targeted source/notation corrections, subject to final checks. Governance blocker resolved; Phase 2B remains unstarted. All work local and uncommitted.
- **Final audit checks:** Passed original 40-file preservation plus audit, 206 local links/anchors, notation delimiter checks, six CSV registries, unique IDs/known DOIs and source relationships. The 34 other numbered notes, toy document, checker and terminology are unchanged from the pre-audit snapshot. git diff --check passed. Final Repomix exited 0 (280 files, 310,350 tokens, no suspicious files); final Graphify exited 0 (41 nodes, 65 edges, six communities; 16 re-extracted inputs, 22 cached). Graphify includes JSON inputs and reports manifest requeues; all six Python modules have nodes. These tool counts precede this status append. Phase 2A compliance is confirmed after the documented corrections; no governance blocker remains and Phase 2B has not begun.
## 2026-09-11 - 20: Phase 2B representation families and classical methods

- **Authorization and scope:** User explicitly authorized Phase 2B. Created 50 classical representation-family notes plus comparison, toy, concept-map, source and validation artifacts. No Phase 2C topics, research model training, real-data transformation, benchmark, ranking, hyperparameter search, biological graph construction or novelty analysis was performed.
- **Context:** Ran Repomix and Graphify at the beginning and completion as required. Their counts are recorded in the Phase 2B validation artifact and are repository-context snapshots only.
- **Evidence:** Reviewed original or authoritative literature and official documentation for PCA, sparse PCA, ICA, NMF, iNMF/LIGER, factor analysis, MOFA/MOFA+, CCA/sparse CCA, PLS, MNN, Harmony, Scanorama, diffusion maps, t-SNE, UMAP, OT/Sinkhorn/GW, spatial alignment, multilayer/heterogeneous/hypergraph/tensor structures, pathway and regulatory priors. Access limitations are recorded in `06_representations/01_classical_representation_families/SOURCES.md` and `papers.csv`.
- **Representation neutrality:** The framework records mathematical object, assumptions, support, loss and cost without performance scores or recommendations. Graphs, latent spaces, concatenation and dimensional reduction remain optional families. `representations.csv` and `methods.csv` mark records `studied_not_fitted`; official repositories are recorded without cloning.
- **Numerical teaching artifact:** The fixed synthetic matrix is used to show raw, standardized, PCA, distances, similarity, KNN, adjacency, kernel, prototype and membership representations. `verify_toy.py` passes 47 checks. The toy adjacency is not a biological graph and no project data enter the checker.
- **Open questions:** Spatial coordinate units/registration, donor/section hierarchy, complete assay pairing, cross-modal feature maps, annotation releases/evidence filters, suitable metrics/costs/likelihoods and biological interpretation remain unresolved. These are prerequisites for any later fitting or comparison.
- **Outcome:** Phase 2B is complete and ready for review. Phase 2C is not authorized or started. Changes remain local and uncommitted.


## 2026-09-11 - 21: Phase 2C deep learned representations

- **Scope:** Added 62 deep/generative/contrastive/graph/foundation notes and six support artifacts. No fitting, benchmarking, tuning, ranking, novelty analysis, disease association, or Phase 3A work.
- **Evidence:** Primary/authoritative sources are indexed for DCA, scVI, totalVI, MultiVI, Cobolt, BABEL, scGLUE, SpatialGlue, SpaMI, graph/attention foundations, scGPT and Geneformer. Garfield, SCIGMA and ARISE remain qualified where direct verification is incomplete.
- **Governance:** Architecture, objective, prior, downstream task and evaluation remain separate; similarity != equivalence, correlation != causation, graph quality matters, and latent != measured biology. Raw data were not modified. Phase 2B checkpoint 498ff0d is on origin/main; Phase 2C remains local/uncommitted.
- **Validation:** 62 numbered notes and six support artifacts are present; source anchors resolve; CSV registries parse with unique identifiers (papers 170, methods 69, representations 48, codebases 30); `git diff --check` passed. Final Repomix exited 0 with 406 files and 423,744 tokens and no suspicious files. Final code-only Graphify exited 0 with 44 nodes, 67 edges and 7 communities (16 re-extracted, 23 cached). These are repository-context checks, not experiments.

# Phase 2A operating-rules audit — 2026-09-11

## 1. Rules checked and review basis

Governing document: [ASTRA_OPERATING_RULES.md](../../ASTRA_OPERATING_RULES.md). This audit was explicitly authorized before Phase 2B. The rules consolidate the original project brief's evidence/source/representation policies and the Phase 1B–1E context procedures with the current governance request; no previously existing file is claimed to have been recovered verbatim.

Reviewed the completed 36-topic phase, shared notation, worked calculations, source index, synthetic checker, Phase 2A registry additions, terminology, taxonomy clarification, research log and changed-file scope. Broad context came from refreshed compressed Repomix, then Graphify structure; exact claims and calculations were checked in original files before targeted external source verification. A hash snapshot taken before audit edits distinguishes these corrections from the earlier uncommitted Phase 2A work.

| Operating rule | Audit finding |
|---|---|
| Authorized phase and stopping point (§1) | No PCA benchmarking, representation comparison, scientific graph construction, research ML training, multimodal integration experiment or novelty analysis found. Phase 2B has not begun. |
| Context protocol (§2) | Start refreshes succeeded; packed scope/source/validation context and Graphify function nodes were inspected. Original notes, code and registries were used for exact evidence. Final refresh results follow below. |
| Evidence classes and honesty (§3) | Cited definitions/source facts are distinguished from derived arithmetic. Synthetic rows, distributions, partitions and scalar updates are labeled synthetic. Candidate biological meanings are conditional interpretations, not observed results. Dataset unknowns remain unknown. No fabricated citation or biological result was identified. |
| Authoritative sources (§4) | Textbooks and foundational statistical papers suit the mathematical scope. Source identity, relevance and access depth were checked; two citation locators were corrected as detailed below. |
| Raw preservation (§5) | The checker contains fixed arrays and no dataset reads/writes or model-fit calls. The reviewed change scope contains no raw assay changes or new derived biological matrices. This audit did not reopen or modify raw assays; it does not claim a new full-dataset checksum verification. |
| Representation neutrality (§6) | No inherently superior representation family is declared. SVD optimality is explicitly limited to its numerical loss; it is not presented as biological superiority. The taxonomy change states mathematical conventions and the evaluation principle only. |
| Tracking and corrections (§7) | Registry additions correspond to actual foundation notes and used sources. The audit records all corrections in RESEARCH_LOG.md; no representation/experiment instances were created. |
| Validation and Git policy (§8) | Math, arithmetic, source/registry links, changed-file scope and whitespace checked. All changes remain local and uncommitted. Tool execution records below distinguish counts from scientific evidence. |

The audit supports these findings from the work products, code and recorded execution history. Repository structure alone cannot prove that an unrecorded external action never happened.

## 2. Compliant items

### Scope and scientific distinctions

The only Phase 2A executable added was [check_phase2a_toys.py](../../code/data_inspection/check_phase2a_toys.py). It verifies fixed teaching examples using explicit matrix factors and hand-assigned labels. It does not train models, fit clusters or build a biological graph. The Graphify graph contains repository function/module relationships; the Mermaid concept map is an explanatory diagram. Neither is a representation of biological observations.

| Required distinction | Evidence in the completed notes |
|---|---|
| Distance != biological dissimilarity | [04_DISTANCE.md](04_DISTANCE.md): metric and scale define numerical separation; distance does not establish biological identity, ancestry or coupling |
| Similarity != biological equivalence | [05_SIMILARITY.md](05_SIMILARITY.md): cosine/correlation depend on axes and transformations; scores do not certify equal molecular states |
| Correlation != causation | [07_CORRELATION.md](07_CORRELATION.md): dependent-but-uncorrelated example; correlation has no intervention or direction of regulation |
| Latent variable != directly measured biology | [28_LATENT_VARIABLES.md](28_LATENT_VARIABLES.md): inferred/constructed coordinates and nonidentifiability are explicit |
| High ARI/NMI/silhouette != biological correctness | [33_ARI.md](33_ARI.md), [34_NMI.md](34_NMI.md), [35_SILHOUETTE.md](35_SILHOUETTE.md): agreement/geometry limitations and [three-layer evaluation](36_BIOLOGICAL_VS_COMPUTATIONAL_EVALUATION.md) |
| Zero != missing value | [30_MISSING_DATA.md](30_MISSING_DATA.md): observed mask versus zero, excluded rows and missing modalities; no imputation |

### Mathematical integrity

Symbols are defined locally or in the [shared glossary](CONCEPT_MAP.md), with the determinant omission corrected below. Matrix products respect the observation-row/column-vector convention. In particular:

- X(n×p) times W-transpose(p×k) produces Z(n×k); the bias outer product has the same shape.
- Centered covariance is p×p with the sample n−1 denominator; prior population summaries use n.
- Full, thin and compact SVD factor dimensions reconstruct n×p. Singular values, covariance eigenvalues and uncentered energy are not conflated.
- A Gram matrix is n×n; each entry is a scalar. Cross-modality covariance is p1×p2 after row pairing.
- Latent transformations ZR and B times inverse-transpose(R) preserve reconstruction with compatible dimensions.
- Probability mass, density, likelihood, posterior, expectation, p-value, confidence interval, effect size and FDR remain distinct.
- Concentration examples state distributional assumptions. ARI states its fixed-margin chance model; NMI declares arithmetic normalization; silhouette uses nearest other-cluster average distance and explicit edge-case conventions.

[TOY_CALCULATIONS.md](TOY_CALCULATIONS.md) retains intermediate sums, centered products, six pair comparisons, entropy terms and individual silhouette calculations. All existing 59 arithmetic checks pass. No formula, worked number or algorithm in that document needed replacement. The scalar L1/L2 examples and shape-derived ratios were also checked by direct substitution/recalculation during review.

### Source integrity

No fabricated publication was identified. Bibliographic records and appropriate author/publisher/official documentation sources support the citations. Original access limitations remain documented rather than being turned into full-text reading claims.

| Source IDs | Audit evidence and limits |
|---|---|
| MATH_VMLS_2018; MATH_CONVEX_2004 | Stanford author pages identify books/authors and provide authorized text links; appropriate linear algebra and optimization references |
| MATH_BHK_2020 | Cornell manuscript title/authors checked; its title page is dated 4 January 2018, distinct from the 2020 Cambridge publication. The distinction is now explicit. Chapter 2/3 locators support geometry/SVD; section 5.3 directly supports kernel definitions. |
| MATH_BLITZSTEIN_HWANG_2019 | Harvard author/course page identifies the second-edition probability text. The earlier full-text access limit remains recorded. |
| MATH_MML_2020 | Author site confirms authors, Cambridge 2020 publication and mathematical coverage. No full-book review is claimed; missingness and broad kernel attributions were corrected. |
| MATH_GRAY_INFORMATION_2023 | Author PDF title/copyright pages confirm corrected first edition dated June 26, 2023, originally published in 1990; entropy/relative-entropy chapter locators checked |
| MATH_HUBERT_ARABIE_1985 | Springer article page confirms publication identity; official metric documentation supports formula/conventions beyond abstract access |
| MATH_VINH_2010 | JMLR publication page verifies title/authors/venue; entropy normalization and chance-adjustment discussion is appropriate |
| MATH_ROUSSEEUW_1987 | Publisher-indexed record confirms title/DOI; direct publisher page retrieval failed during this audit. Official documentation supplies the already cited silhouette definitions/conventions. |
| MATH_SKLEARN_CLUSTER_DOC; MATH_SKLEARN_EVAL_DOC | Official pages accessible and display version 1.9.1; used for definitions and conventions, not installed implementations or research scores |
| MATH_SHALIZI_TESTING_2019; MATH_BH_1995 | CMU course notes and Wiley publication metadata/abstract checked; testing terminology and original independent-test qualification retained |
| SCT_2019 | Genome Biology article's count/depth and negative-binomial passages support assay-specific statistical context; its method was not run |
| ZIMMERMAN_PSEUDOREPLICATION_2021 | Nature Communications Results/Discussion text accessible during audit; within-individual correlation supports the replication caution |
| MATH_SEAMAN_MISSING_2013 | Newly used journal electronic reprint, sections 2 and 5, directly supports masks and missingness assumptions; journal DOI and author-deposited copy registered |

Canonical links and exact bibliographic identities are in [SOURCES.md](SOURCES.md) and papers.csv. The [Seaman reprint](https://arxiv.org/pdf/1306.2812) states its relation to the published journal article. Failed access to alternative sites supplied no scientific evidence and generated no extra paper cards.

### Registry integrity

Reviewed methods.csv, papers.csv, representations.csv, TERMINOLOGY.md and RESEARCH_LOG.md. The 17 Phase 2A methods are foundation records, not fitted representation instances. Two existing method source fields were corrected; one actually used missingness source was added. Final totals are 29 methods and 125 papers. The 14 new Phase 2A/audit sources plus two reused biological papers are accounted for in the source index. representations.csv remains unchanged and header-only.

TERMINOLOGY.md's Phase 2A terms correctly distinguish the requested concepts and needed no audit edits. The research log retains earlier history and appends the governance resolution and corrections.

## 3. Violations or gaps found

1. **Missing governance artifact:** ASTRA_OPERATING_RULES.md did not exist; the earlier pending-compliance status was warranted.
2. **Incomplete source-to-claim traceability:** the missingness note cited an MML book landing page without a verified supporting passage for masks/missingness assumptions. This is an attribution gap, not a finding that the book is fabricated or that missingness mathematics is false. The kernel note similarly had a broad geometry locator; a directly checked existing-source section now replaces it.
3. **Minor symbol-definition omission:** the toy eigenvalue derivation used det without explicitly defining the determinant operator.
4. **Superseded status:** the validation/source records still described missing governance as unresolved. They now point to this audit while preserving historical execution counts.

No out-of-scope research activity, representation preference, incorrect formula or worked-arithmetic discrepancy was found. Because source/notation gaps did require targeted corrections, this is not recorded as an audit with zero findings.

## 4. Corrections made

- Created the root operating-rules file with the permanent context order and standing project policies.
- Added a concise determinant definition and its 2×2 formula to the shared notation glossary.
- Replaced missingness attribution with Seaman et al.; identified the masked loss as a defined teaching objective, not a copied claim.
- Pointed the kernel citation to BHK section 5.3 and synchronized its method source ID; recorded the manuscript date separately from the published book year.
- Registered the one newly used source, corrected the missingness method source ID and removed the unsupported MML attribution from the source index.
- Resolved current governance status in VALIDATION.md and SOURCES.md and appended corrections to RESEARCH_LOG.md.

## 5. Files modified by this audit

Created:

- [ASTRA_OPERATING_RULES.md](../../ASTRA_OPERATING_RULES.md)
- This OPERATING_RULES_AUDIT.md

Corrected:

- [CONCEPT_MAP.md](CONCEPT_MAP.md): determinant definition only
- [25_KERNELS.md](25_KERNELS.md): citation locator only
- [30_MISSING_DATA.md](30_MISSING_DATA.md): source attribution and teaching-objective clarification; equations unchanged
- [SOURCES.md](SOURCES.md): source coverage, provenance/access updates and governance resolution
- [VALIDATION.md](VALIDATION.md): current status supersedes the historical missing-file limitation
- [papers.csv](../../papers.csv): one new used reference and two existing source notes
- [methods.csv](../../methods.csv): two corrected source relationships
- [RESEARCH_LOG.md](../../RESEARCH_LOG.md): audit/correction record

The other 34 numbered notes, toy calculations, checker, terminology and representation taxonomy were not changed by this audit. Existing Graphify metadata/cache files may refresh through the required structural scan; those are generated context artifacts, not content corrections. No correct topic was recreated.

## 6. Unresolved issues

No governance blocker remains; final checks passed. Earlier scientific unknowns remain open: complete E18 ATAC availability, coordinate units, donor/embryo/section hierarchy, biological label provenance, observation-model adequacy and future method-specific identifiability/uncertainty. These are not resolved by a mathematical compliance audit.

Some sources remain abstract/landing-page accessible only; no claim of exhaustive full-book or full-article review is made. The source-specific checks above support the scope of the current notes. This audit does not certify human mastery, future model validity or the completeness of earlier dataset inspections.

## 7. Final Phase 2A status and validation

Compliance review: **Phase 2A is compliant with ASTRA_OPERATING_RULES.md following the documented source/notation corrections. No existing mathematical formula or worked arithmetic required rework.**

Phase 2B readiness: the governance and foundation-review prerequisite is resolved and final checks passed. Starting Phase 2B still requires explicit authorization. It remains unstarted; changes remain local and uncommitted.

### Final execution record

- **Artifact inventory:** All original 40 Phase 2A files remain, plus this audit (41 phase Markdown files). Root operating-rules file exists. The 34 untouched numbered notes, original worked calculations and checker match the pre-audit hash snapshot. The two other numbered notes have source-only/attribution clarifications; no equation changed.
- **Notation and arithmetic:** Mathematical delimiters/environments and control-character checks passed. The existing checker exited 0 with 59 passes; supplemental determinant/regularization and shape arithmetic was checked by substitution. Definitions/dimensions were reviewed manually as described above; static checks alone do not prove mathematical meaning.
- **Links:** All 206 local links/anchors checked across the phase directory, root operating rules and terminology resolve.
- **Registries:** All six CSV registries parse with consistent row lengths and unique IDs; known DOIs have no duplicates. Papers: 125; methods: 29; datasets: 6; codebases, representations and experiments: zero rows. All 14 Phase 2A/audit source IDs occur in SOURCES.md; 17 foundation-method rows have valid source IDs and existing record paths. Terminology required no edit.
- **Preservation:** Dataset, representation, experiment and codebase registries match HEAD byte-for-byte. Research/model/representation/result/idea directories contain only their placeholders. Changed-file and hash review found only the documented audit edits in preexisting Phase 2A material. Raw files were not reopened for checksumming.
- **Whitespace:** git diff --check passed before the requested final refresh and after recording its results.
- **Final Repomix:** repomix . --compress exited 0, packing 280 files and 310,350 tokens; no suspicious files detected. The bundle is generated/ignored context. Counts are the execution snapshot before these status lines were appended.
- **Final Graphify:** graphify . --code-only exited 0: 41 nodes, 65 edges, six communities; 16 inputs re-extracted, 22 cached/unchanged. It skipped 227 non-code and 20 unclassified files. All six Python inspection/checker modules have function nodes, including ten nodes from the synthetic checker. The tool requeues 16 manifest entries without nodes; its input classification includes JSON and is not a Python-file count or a guarantee of exhaustive extraction. No scientific graph was built.
- **Stop:** Phase 2A compliant after the documented corrections; Phase 2B remains unstarted. Changes remain local and uncommitted.

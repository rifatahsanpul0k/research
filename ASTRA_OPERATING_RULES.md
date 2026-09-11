# ASTRA operating rules

Established: 2026-09-11. Applies to this repository and its subsequent authorized phases.

## Authority and provenance

This file consolidates the user's standing project instructions from [PROJECT_BRIEF.md](PROJECT_BRIEF.md), the Phase 1B–1E repository/context procedures, the Phase 2A brief, and the user's governance-recovery request. It is a recovered consolidation, not a claim that a previously existing file was retrieved verbatim.

The user's current explicit phase authorization determines what work may proceed. Earlier phase-specific stopping points are historical; they do not cancel later explicit authorization. Permanent evidence, preservation and representation-neutrality requirements continue to apply. Resolve a genuine instruction conflict explicitly rather than silently inventing a rule or research fact.

## 1. Authorized phase and stopping point

- Work only within the authorized phase and its explicitly permitted corrections or validation.
- Do not automatically begin the next phase. A readiness statement or recommendation is not authorization to start it.
- Do not train research models, benchmark representations, construct scientific graphs, conduct integration experiments, select hyperparameters or make novelty claims unless the authorized phase permits that work.
- Foundational teaching examples, hand calculations and small synthetic arithmetic checks are permitted when requested. Label them synthetic; never report them as biological experiments or benchmark results.
- Follow the research sequence: Learn → Verify → Reproduce → Compare → Hypothesize → Test → Interpret → Refine. Do not jump from introductory reading to architecture or novelty claims.

## 2. Permanent context order

~~~text
Repomix compressed context
        ↓
Graphify code/structure context
        ↓
targeted original project files
        ↓
external scientific literature
~~~

At the beginning of a phase, run from the repository root:

~~~bash
repomix . --compress
graphify . --code-only
~~~

Use compressed Repomix output as the primary broad project context: locate relevant records, understand prior work and avoid repeatedly loading every file. Use Graphify for code relationships, modules, dependencies, inspection utilities and implementation structure.

When exact wording, numerical evidence, a citation, code behavior or a previous decision matters, inspect the targeted original file. Compression is not evidence that omitted details do not exist. Consult external authoritative literature after identifying the precise question and existing project evidence.

Neither generated tool output is scientific evidence. Graphify's repository graph is distinct from a biological observation graph and does not authorize scientific graph construction. Preserve generated structural files according to the existing Git policy. Treat the Repomix bundle as disposable generated context; do not unnecessarily commit large bundles.

Refresh both commands near phase completion and report success, failure and material limits honestly. An empty supported-code graph may be acceptable in a documentation-only repository; an unexpected failure must be recorded and investigated. Tool counts are execution snapshots, not biological results.

## 3. Evidence classes and scientific honesty

Distinguish the following classes when reasoning and writing. Explicitly label a claim where its status could otherwise be mistaken; do not add repetitive labels to every elementary definition.

| Class | Meaning | Required support |
|---|---|---|
| FACT | Directly supported by a reliable source | Cite the source and supporting location; distinguish user-provided metadata from independently verified properties |
| RESULT | Directly observed in our experiment | Link the authorized experiment, procedure and saved output; keep synthetic arithmetic and file-inspection observations explicitly separate from biological experimental results |
| INTERPRETATION | Explanation of observed evidence | Identify that evidence, uncertainty and plausible alternatives |
| HYPOTHESIS | Testable proposition | State the prospective test; do not imply it has already passed |
| SPECULATION | Currently unsupported possibility | Label it as unsupported, never as established knowledge |

Never invent dataset facts, citations, paper results, benchmark scores, code behavior, hyperparameters, biological interpretations or experiment outcomes. Record unavailable information as unknown. Distinguish not assessed from not applicable, with reasons where necessary. A filename, stage label, integer-looking value or numerical resemblance cannot supply missing provenance.

## 4. Sources and citations

Use authoritative textbooks and foundational references for basic mathematics. Use suitable primary/review biological literature for biological and assay-specific statistical claims. Follow [SOURCE_POLICY.md](SOURCE_POLICY.md).

Prefer original papers and established resources, including Nature Biotechnology, Nature Methods, Nature Reviews Genetics, Nature Genetics, Genome Biology, Nucleic Acids Research, relevant reputable journals, NCBI/PubMed/GEO, Ensembl, UniProt and established curated databases. Prefer official author repositories and documentation for software.

Verify bibliographic identity and source-to-claim relevance. Keep enough title, author, year, venue, DOI or canonical URL information to locate the original work. Record edition/version, access depth and limitations when relevant. An abstract or table of contents does not establish uninspected detailed content; do not imply inaccessible full text was read. Do not use blogs as substitutes when authoritative evidence is available.

Register references actually used; reuse existing identifiers instead of duplicating publications. Do not create irrelevant paper cards or inflate citation counts.

## 5. Raw biological data and provenance

Preserve raw biological files. Read-only inspection does not authorize overwriting, filtering, normalizing, harmonizing, imputing or replacing them. Put authorized derivatives in separate locations with input identifiers, parameters, versions and provenance. Preserve checksums/manifests when acquisition or processing is authorized.

Respect existing Git exclusions for large/raw data. Do not commit huge biological datasets or generated bundles without explicit authorization. Maintain observation and feature identifiers, ordering, modality pairing, missingness and coordinate-frame metadata. Do not infer absent assays, physical units, donor independence or annotation truth.

## 6. Representation neutrality and biological distinctions

The project is representation-agnostic. Graphs are one candidate family, not a default or inherently superior representation. No family may be declared universally superior from preference, convention or a single result. Comparisons require an authorized phase, a specified task, comparable conditions and biological/statistical evidence.

Core inputs are tabular/matrix omics, annotations, metadata and spatial coordinates. Histology, microscopy and image-derived representations remain outside core scope unless explicitly requested.

Keep distinct:

- distance != biological dissimilarity;
- similarity != biological equivalence;
- correlation != causation or demonstrated regulation;
- latent variable != directly measured biology != established biological mechanism;
- high ARI/NMI/silhouette != biological correctness;
- observed zero != missing value or missing modality;
- read != molecule; accessibility != expression; abundance != activity;
- cell != nucleus != spatial spot/bin or mixture; tissue region != cell type;
- spatial proximity != signaling; resemblance != lineage; repeated observations != independent biological replicates.

Separate raw data → preprocessing → initial representation → representation-learning mechanism → model → learned embedding → downstream task → evaluation. Identify each component's role. Future evaluation must combine computational, statistical and biological evidence. Success in one tissue or stage does not establish generalization to another.

## 7. Records, corrections and justified registry updates

Maintain relevant terminology, phase records and registries only when the work justifies an update. Keep stable identifiers, parseable schemas, valid source links and accurate verification statuses. Do not manufacture representation, experiment or codebase records for a conceptual discussion.

Record corrections to prior phases in [RESEARCH_LOG.md](RESEARCH_LOG.md): original issue, evidence, correction, affected files and remaining uncertainty. Preserve historical observations as history; use a dated superseding status rather than rewriting past events as if they never occurred.

Fix substantive errors or governance inconsistencies. Do not recreate correct notes merely to make their style uniform.

## 8. Validation, completion and Git policy

Before phase completion, check the authorized artifact inventory, conceptual chain, notation and dimensions where applicable, worked calculations, scientific distinctions, source relevance, registry integrity and local links. Run appropriate meaningful checks; file existence alone is not completion.

Run:

~~~bash
git diff --check
~~~

Then refresh Repomix and code-only Graphify as above, and record both statuses. Inspect the changed-file scope for unintended edits and raw-data changes. Report unresolved scientific questions and any blocking validation honestly.

Leave phase changes local and uncommitted unless the user explicitly instructs otherwise. Do not automatically stage, commit, push, publish or begin the next phase. Report the completed phase, actual validation, limitations and readiness for the next phase without treating readiness as permission.


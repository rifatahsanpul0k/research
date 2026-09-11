# Source policy

Status: policy initialized; no literature review or source verification performed.

## Priority and source classes

Prefer original peer-reviewed papers and authoritative technical or biological resources. Priority journals: Nature Biotechnology, Nature Methods, Nature Reviews Genetics, Nature Genetics, Genome Biology, Nucleic Acids Research, Briefings in Bioinformatics, Bioinformatics, and PLOS Computational Biology. Relevant work from other reputable journals is eligible; venue alone does not validate a claim.

Preferred biological resources include NCBI, PubMed, GEO, UniProt, Ensembl, Gene Ontology, STRING, Reactome, Open Targets, DisGeNET, Bioconductor, and other established databases. Record resource release/version and access date. A database annotation is not automatically experimental ground truth.

| Source class | Intended use | Required distinction |
|---|---|---|
| Primary paper | Original method, experiment, or dataset evidence | Attribute results to the specific dataset, task, protocol, and version |
| Review | Conceptual orientation and routes to original work | Verify consequential empirical claims against the cited primary source |
| Preprint | Provisional research evidence | Mark peer-review status and version; track later publication without double counting |
| Official documentation/repository | Implementation, release, and usage evidence | Separate documented behavior from code inspected and behavior reproduced |
| Authoritative database | Curated biological records | Record identifiers, provenance, evidence codes where available, and release |
| Third-party source | Discovery or supplementary explanation | Label secondary status; do not silently substitute for the original implementation or result |
| User-provided link/description | Project input and discovery lead | Record as user-provided and unverified until checked |

## Citation rules

1. Verify title, authors, year, venue, DOI, and canonical URL against the publisher or an authoritative bibliographic record. Leave unavailable fields `unknown`.
2. Attach important claims to exact sections, pages, figures, tables, supplementary items, or versioned code locations. Record access dates for changing resources.
3. Distinguish author-reported findings from our reproduced results and interpretations. Preserve the evaluation context, uncertainty, and qualifications.
4. Do not cite an abstract as evidence for uninspected detailed methods or supplements. Record paywall, missing supplement, and inaccessible-link limitations.
5. Link preprint and journal versions under a stable paper ID with a version history. Check corrections or retractions during later verification.
6. Record quotations accurately and sparingly. Do not invent citations or infer support from a paper title.
7. Record biological explanations only after supporting sources are studied. Bootstrap roadmap entries are learning prompts, not sourced teaching notes.

## Code verification

Prefer (1) the official repository linked by the paper, (2) the authors' verified GitHub/GitLab organization, (3) official documentation, then (4) explicitly labeled third-party implementations.

Record the paper-to-repository link evidence, owner, repository URL, access date, license, release/tag, exact commit, submodules, environment files, datasets required, instructions, and local path. If official ownership is uncertain, mark it unverified. Inspect installation and execution requirements before use; do not infer behavior from the README alone.

Track separately: `not_verified`, `identity_verified`, `code_inspected`, `environment_ready`, `execution_attempted`, `reproduced`, `partially_reproduced`, and `blocked`. Later statuses require evidence and a linked log or experiment record. Downloading a repository is not reproduction. Document any modifications and baseline deviations.

## Unknowns and provenance

Use `unknown` for unavailable facts, `not_assessed` for pending assessments, and `not_applicable` only with an explanation. Each registry row must identify its evidence origin and verification status. No external source was opened merely to initialize this workspace.

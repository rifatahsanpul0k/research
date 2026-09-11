# Phase 3B validation

Validated 2026-09-12. Phase 3B stops at engineering planning and environment verification; no project-data method run or comparative result was produced.

| Check | Result | Evidence |
|---|---|---|
| Required inventory | PASS | All 45 numbered notes, seven named top-level artifacts, three configuration examples, two JSON schemas and 11 CORE manifests exist. |
| Frozen candidate set | PASS | `REPRODUCTION_STATUS.csv`, `ENVIRONMENT_MATRIX.csv` and `METHOD_EXECUTION_ORDER.csv` each parse with 11 unique CORE rows. No tier changed. |
| Repository provenance | PASS | Six shared official/author repositories cover all CORE candidates; every status row and manifest has a 40-character selected commit. Current HEAD is explicitly distinguished from a paper-exact release. |
| Manifest contract | PASS | All 11 YAML manifests parse and contain method, paper, repository, commit, license, environment, input, preprocessing, command, output, embedding, clustering, seed, issue and reproduction-level fields. |
| Dependency isolation | PASS | Conflicts, sharing groups and hardware constraints are documented. The ignored baseline uv environment has fixed direct requirements. |
| Baseline R1 | PASS | Python 3.11.8 imported NumPy 2.4.4, SciPy 1.17.1 and scikit-learn 1.9.1; PCA on a synthetic 3 × 2 matrix returned a finite 3 × 1 array. Five shared baseline candidates are R1. This was an `ENGINEERING_SMOKE_TEST`. |
| Remaining reproduction levels | PASS | MOFA+, SCOT, totalVI, MultiVI, SpatialGlue and Garfield remain R0 with blockers recorded. No unsupported R1/R2/R3 claim was made. |
| Canonical data policies | PASS | Six IDs, observation/feature identity, immutable raw inputs, modality-specific feature rules, ATAC strategy alternatives and provenance-aware caching are specified. |
| E18 gate | PASS | `E18_ATAC_VERIFIED = false`; the blocked example cannot silently substitute another stage. |
| Execution contracts | PASS | Config, experiment ID, metadata, output, status, seed, determinism, logging and native/common policies are present. Both JSON schemas parse. |
| Infrastructure | PASS | Five stdlib unit tests passed; all benchmark Python files compiled. Tests cover config/status, row mapping, finite embeddings, seeds, JSON, checksums and provenance completeness. |
| Structured files | PASS | All Phase 3B CSV, YAML and JSON artifacts parse. All six root registries parse; `experiments.csv` remains header-only. |
| Raw-data boundary | PASS | `git diff -- 04_datasets datasets.csv experiments.csv` is empty. No raw file was opened or transformed during Phase 3B. Existing Phase 1D checksums remain the baseline. |
| Secret hygiene | PASS | Targeted private-key/token-pattern scan returned no match; the environment record excludes serial numbers, device UUIDs and credentials. External clones, environments, experiment outputs and Python caches are ignored. |
| Git whitespace | PASS | `git diff --check` returned no error before the final context refresh. |
| Repomix | PASS | Final structural refresh before this record append: 530 files, 488,589 tokens, no suspicious files. |
| Graphify | PASS | Final code-only refresh before this record append: 234 nodes, 298 edges, 20 communities; 23 files cached and 28 re-extracted. |

Graphify shows the new benchmark functions grouped under `code/benchmarks/common/`; provenance, configuration, seeds, I/O and validation each have a separate module. Tests depend on these common modules, while the data-inspection utilities remain outside the benchmark package. No scientific method adapter exists yet, so no cross-method coupling was introduced and no method writes to raw-data directories.

Phase 3B is complete. Phase 3C remains unstarted. All changes are local and uncommitted.

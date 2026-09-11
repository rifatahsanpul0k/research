# Phase 3C validation

Validated 2026-09-12. Phase 3C contains scientific baseline results, so completion requires evidence beyond file existence.

| Check | Result | Evidence |
|---|---|---|
| Pre-result freeze | PASS | `PHASE_3C_CONFIG_FREEZE.md` and the Phase 3C pre-execution research-log entry fixed inputs, transforms, dimensions, KMeans, three seeds, metrics and exclusions before the first result. |
| First end-to-end gate | PASS | `EXP-LN-A1-PCA-KMEANS-S1729` completed first; 3,484 × 30 finite embedding, barcode-preserved identity, metrics/provenance/artifact manifest and registry row validated before continuation. |
| Intended matrix | PASS | 28 eligible dataset–baseline combinations × three seeds = 84 unique experiment IDs. Results, registry and directories have identical 84-ID sets. |
| Dataset eligibility | PASS | A1/D1 RNA+ADT, E11/E13/E15 RNA+ATAC and all six coordinate/RNA tracks were used only within dataset. E18 contains exactly RNA, PCA and SPACE; E18 ATAC and concatenation are explicitly not applicable. |
| Complex-method exclusion | PASS | No MOFA+, SCOT, totalVI, MultiVI, SpatialGlue, Garfield, SCIGMA, ARISE, deep model, GNN or novel representation appears in the experiment registry. |
| Source preservation | PASS | All 17 complete Phase 1D source files matched recorded SHA-256 before the first run, after it and after the full series. `git diff -- 04_datasets datasets.csv` is empty. |
| Identity and annotation | PASS | All H5AD observation IDs are unique; paired modalities have identical order and coordinates; annotations have exact ID-set coverage and are joined by barcode. No observation was removed. |
| Representation validity | PASS | All 84 embeddings have expected rows, finite values, positive total variance and zero duplicate rows. Identity-map and cluster-file observation order agree. |
| Metrics and clustering provenance | PASS | Every metrics JSON records implementation, scikit-learn 1.9.1, parameters, inputs and result. K is explicitly sourced from reference annotation count. Representation and clustering remain separate. |
| QC diagnostics | PASS WITH FLAGS | Every requested KMeans solution has nonempty clusters. Twenty-seven runs have singleton clusters; dominant ≥90% clusters in E11/E13 ATAC explain high silhouette with near-zero ARI/NMI. Flags are retained without tuning or deletion. |
| Repeated seeds | PASS | Seeds 1729, 2718 and 31415 are individually reported; generated aggregates contain mean and sample SD without hiding runs. |
| Exact repeatability | PASS | Recomputed all 28 seed-1729 combinations: embeddings bitwise equal, clusters identical and metric differences zero. The repeatability activity is labeled validation and excluded from `experiments.csv`. |
| Runtime provenance | PASS WITH LIMITATION | Per-run duration is explicitly scoped to clustering, metrics and serialization after shared representation construction. Dataset-level shared-build timing is in the repeatability record; it is not allocated to seed runs. No efficiency comparison is claimed. |
| Failure preservation | PASS | No scientific failure occurred. The temporary failure-path test verifies preservation of category, stage, error, logs and status. No failed directory was deleted. |
| Machine artifact audit | PASS | 84 directories, 588 parsed JSON files, 168 parsed experiment CSV files, 84 loaded embeddings and every per-run artifact checksum passed; details are in `PHASE_3C_MACHINE_VALIDATION.json`. |
| Registry integrity | PASS | Root registries parse with unique experiment IDs; `experiments.csv` contains exactly the 84 scientific runs and no smoke/repeatability entries. Methods/codebases/reproduction status were updated only for the executed transparent baselines. |
| Tests and compilation | PASS | Twelve tests passed; all benchmark Python files compiled. Tests include source immutability, identity joins, feature IDs, preprocessing shapes, finite values, experiment IDs, metrics and failure logging. |
| Structured formats | PASS | All root/Phase 3B/Phase 3C CSV and tracked JSON files parse; all 11 manifests, three planning examples and 84 experiment configs parse as YAML. |
| Secret and Git checks | PASS | Repomix found no suspicious file; targeted credential patterns found no match; `git diff --check` passed after the final context refresh. |
| Repomix | PASS | Final refresh before this status update: 580 files, 761,264 tokens, no suspicious files. Ignored 599 MB experiment directories are represented through registries and root summaries. |
| Graphify | PASS | Final code-only refresh: 333 nodes, 566 edges and 23 communities; 52 files cached and 21 re-extracted. |

Graphify shows the transparent adapter depends on shared H5AD/preprocessing modules and does not depend on another method adapter. The runner calls centralized evaluation, failure, I/O, identity and provenance-related helpers. H5AD sources are opened read-only, and all write paths are under `08_experiments`; no raw-data mutation path exists in the baseline code.

Phase 3C is complete with material QC cautions and an explicit runtime limitation. These results validate the infrastructure and provide configuration-specific reference points; they do not establish a preferred representation or biological equivalence. Phase 3D remains unstarted. All changes are local and uncommitted.

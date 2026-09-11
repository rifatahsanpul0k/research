# Compute environment policy

Effective 2026-09-12 for scientific workloads authorized after Phase 3C. Historical Phase 3C configurations remain accurate records of their local execution.

## Selection classes

| Classification | Use |
|---|---|
| `LOCAL_LIGHT` | Repository management, Git, Repomix, Graphify, documentation, dataset inspection, checksums, metadata, small preprocessing checks, synthetic/unit tests, configuration/provenance generation, lightweight classical algorithms, smoke tests and light debugging. |
| `COLAB_CPU` | Substantial remote CPU work that does not benefit materially from a GPU. |
| `COLAB_GPU` | Neural networks, VAEs, scVI, totalVI, MultiVI, GNNs, SpatialGlue, SpaMI, Garfield, SCIGMA and other GPU-beneficial representation learning. |
| `COLAB_HIGH_MEMORY` | Large matrix factorization, large optimal-transport computation and other memory-intensive runs. |
| `UNRESOLVED` | Evidence is insufficient to select an executable class. A scientific run must not enter `RUNNING` until this is resolved. |

The local machine remains the control plane for repository work, inspection, validation and small computation. Google Colab through the user's local Colab extensions is the preferred available execution plane when GPU, greater memory or substantial compute is beneficial. Paid or other external compute requires explicit user authorization.

## Reproducible Colab chain

~~~text
GitHub research repository
        ↓
Colab runtime
        ↓
checkout exact repository commit
        ↓
install exact environment
        ↓
mount/access dataset
        ↓
load frozen experiment config
        ↓
execute repository code
        ↓
save artifacts
        ↓
sync compact reproducibility records
        ↓
review locally
~~~

The notebook is an environment bootstrap, execution controller or debugging interface. Scientific method logic belongs in repository modules/scripts and must run from configuration without manual notebook-cell edits.

Each Colab scientific run records experiment ID, compute classification, Colab runtime type, Python version, GPU model and CUDA version where relevant, package versions, external repository commit, frozen configuration, all controlled seeds, source checksums, preprocessing, runtime, outputs and logs. Use `NOT_APPLICABLE` for genuinely irrelevant GPU/CUDA fields and `UNKNOWN` only when evidence is unavailable; never infer hardware.

Datasets are mounted or accessed through an approved storage mechanism and opened without overwriting source files. Preserve checksums, observation IDs, feature IDs and modality alignment. Do not commit large datasets, checkpoints, large embeddings, temporary matrices or caches. Sync configs, provenance, metrics, summaries, necessary small outputs, logs, environment manifests and checksums.

Future configurations use `schemas/run-config-v2.schema.json`; future provenance uses `schemas/provenance-v2.schema.json`. The v1 schemas remain available to validate historical Phase 3B/3C records.

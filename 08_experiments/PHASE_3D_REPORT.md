# Phase 3D classical integration and alignment report

Status: **IN PROGRESS — R3 project-data execution pending a verified Colab runtime.**

Phase 3D is restricted to MOFA+ and SCOT v1. The configuration freeze, source verification, engineering gates and config-driven Colab controller are complete. No project-data result is reported in this record because this session has no attached Colab execution runtime.

## Scope

The frozen matrix contains five within-dataset paired suites (`LN_A1`, `LN_D1`, `MB_E11`, `MB_E13`, `MB_E15`) × two methods × three seeds = 30 planned R3 runs. E18 remains excluded from multimodal integration because `E18_ATAC_VERIFIED = false`; no stage pooling, cross-stage peak harmonization or spatial-coordinate view was added.

MOFA+ uses separate RNA and ADT/ATAC continuous transformed views with Gaussian likelihoods and 10 fixed factors. SCOT uses official v1 graph construction and entropic Gromov–Wasserstein alignment with fixed `k=50`, `epsilon=1e-3`, and an explicitly recorded barycentric projection for common evaluation. Full settings are frozen in [PHASE_3D_CONFIG_FREEZE.md](PHASE_3D_CONFIG_FREEZE.md).

## Engineering reproduction status

- MOFA+ official `mofapy2` entry-point build test: PASS (R1/R2 engineering check).
- SCOT v1 import/initialization: PASS (R1 engineering check).
- SCOT v1 fixed-parameter API alignment on a small official-API-shaped example: PASS (R2 engineering check).
- Project-data R3: PENDING_COLAB_RUNTIME; no `experiments.csv` rows or scientific scores have been created for Phase 3D.

The engineering checks are not biological experiments and are stored under `07_models/02_classical_integration/engineering/`. The thin controller at `code/benchmarks/colab/phase3d_controller.ipynb` installs the declared environment and calls `code/benchmarks/run_phase3d.py`; it contains no method implementation. Because the Phase 3D files are currently uncommitted, a fresh checkout at the frozen starting commit does not contain them; execution requires a reviewed commit or an explicitly checksummed working-tree synchronization step.

## Interpretation boundary

There is no Phase 3D numerical comparison yet. When R3 runs are available, individual metrics, native coupling/factor outputs, common KMeans results, QC flags, runtimes and aggregates will be reported separately from literature-reported values. No overall winner, biological factor meaning, disease association or novelty claim is permitted in this phase.

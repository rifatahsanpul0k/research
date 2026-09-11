# Execution strategy

Freeze CORE, EXTENDED and REFERENCE_ONLY from Phase 3A. Each method receives an isolated environment chosen from its official instructions: uv/venv for transparent Python baselines, an R environment or container for MOFA+/MClust, repository environment for SCOT and SpatialGlue, and isolated PyTorch environments for scvi-tools and Garfield. Do not force incompatible packages into one environment.

The chain is paper → official repository → selected commit/tag → environment → canonical input → preprocessing → command/config → seed → raw output → parsed metrics. Phase 3B establishes the chain and R0/R1 readiness; it does not execute project-data R3 runs.

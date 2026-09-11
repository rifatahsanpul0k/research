# Phase 3D validation

Validated 2026-09-12. This is a preparation checkpoint; project-data R3 execution is pending a verified Colab runtime.

| Check | Result | Evidence |
|---|---|---|
| Phase 3C checkpoint | PASS | Phase 3C and the compute-policy update are committed at `951a61ca15239a7f644b60ec56dd1a463cd5570f`; `HEAD == origin/main` at preparation start. |
| Working-tree handling | PASS WITH USER FILE | Existing generated Graphify state and user-owned `hello.ipynb` were preserved; no destructive cleanup was performed. |
| Configuration freeze | PASS | `PHASE_3D_CONFIG_FREEZE.md` was created before any project-data result and fixes methods, datasets, preprocessing, factors, SCOT settings, seeds, clustering, metrics and compute classes. |
| Planned matrix | PASS | 30 immutable JSON configs (five paired datasets × two methods × three seeds) and `CONFIG_CHECKSUMS.json` generated; E18 multimodal runs are absent. |
| Official sources | PASS | MOFA+ source mirror is commit `90418e5021b3ae735ebf1fea5d7e07cae71c8bb7` (`mofapy2 0.7.5`); SCOT v1 source is commit `14649be6e14017dcfe7ba619091b33d1df55f6a9`. |
| R1/R2 engineering | PASS | MOFA+ official entry-point build test passed; SCOT v1 import/initialization and fixed-parameter alignment passed. Logs and JSON records are under `07_models/02_classical_integration/engineering/`. |
| Adapter contract | PASS | MOFA+ namespaces feature IDs by view while retaining original IDs; SCOT preserves coupling, marginals, permutation and projection metadata. |
| Colab controller | PASS WITH SYNC GATE | `phase3d_controller.ipynb` checks out the exact commit, installs method-specific packages, captures runtime context and invokes the repository runner with `ASTRA_COLAB_CONFIRMED=1`; the uncommitted Phase 3D files must be reviewed/committed or transferred with an explicit checksum before a fresh checkout can run them. |
| Project-data R3 | PENDING | No Colab runtime is attached; no scientific result, metric or `experiments.csv` row has been fabricated. |
| Unauthorized methods | PASS | No totalVI, MultiVI, SpatialGlue, Garfield, SCIGMA, ARISE, VAE, GNN, disease or novelty work was executed. |
| Source preservation | PASS | No raw biological file was modified by preparation or engineering checks. Full source checksum pre/post gates occur in the R3 runner. |
| Tests and formats | PASS | Python compilation, 18 benchmark tests, JSON/CSV/YAML parsing and `git diff --check` passed at the preparation checkpoint. |
| Repomix | PASS | Final refresh: 639 files, 915,211 tokens, no suspicious files. The compressed bundle is repository context, not scientific evidence. |
| Graphify | PASS | Final code-only refresh: 491 nodes, 836 edges and 28 communities; 92 files cached and 54 re-extracted. This is structural context, not a biological graph. |

Phase 3D is not complete until the declared Colab R3 runs execute or are explicitly blocked by an external-state decision. Phase 3E remains unstarted. Changes remain local and uncommitted.

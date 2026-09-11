# Phase 2B validation

Status: **Phase 2B complete; Phase 2C not started.** All work is local and uncommitted.

## Scope checks

- 50 numbered topic notes, the comparison framework, toy representations, concept map, source index and this validation record exist.
- The review covers raw/vector, selection, latent factors, pairwise distances/similarities/kernels, neighborhoods, manifolds, transport, spatial objects, graphs, multiplex/heterogeneous/hypergraphs, tensors, sets, prototypes, cluster summaries, probabilistic summaries and biological priors.
- PCA, ICA, NMF, iNMF/LIGER, factor analysis, MOFA/MOFA+, CCA, sparse CCA, PLS, concatenation, MNN, Harmony, Scanorama, diffusion maps, t-SNE, UMAP, OT/Sinkhorn/GW, pathway/SCENIC/chromVAR and structural families are covered.
- No project matrix was transformed; no research model was trained; no representation benchmark, score, ranking, hyperparameter search, real-data graph, or novelty analysis was performed. Tiny arithmetic examples use a clearly synthetic matrix only.
- No deep architecture or Phase 2C topic was studied in depth.

## Conceptual checks

- PCA is distinguished from factor analysis, ICA and NMF by objective, constraints and ambiguities.
- CCA and PLS use different normalization/objectives; CCA requires paired rows.
- t-SNE and UMAP limitations as visualization versus downstream coordinates are explicit.
- Neighborhood sets are kept distinct from graph encodings; graph, hypergraph and heterogeneous graph semantics are separated.
- OT/GW couplings are distinguished from embeddings; GW compares within-domain relations.
- Biological priors and regulatory/pathway scores are not treated as ground truth or measured activity.
- Chronological E11<E13<E15<E18 and inferred pseudotime are separate.
- Distance ≠ biological dissimilarity; similarity ≠ equivalence; correlation ≠ causation; latent variable ≠ directly measured biology; high ARI/NMI/silhouette ≠ biological correctness; zero ≠ missing.
- Every comparison row states mathematical object, dimensions, requirements, linearity, supervision, determinism, spatial/multimodal/missing support, interpretability, prior, cost, loss, assumptions and failure modes without scores.

## Numerical checks

`python3 verify_toy.py` passes 47 fixed checks: mean/centering, sample covariance, characteristic polynomial, eigensystem, PCA scores and reconstruction, standardized values, distances, cosine/RBF matrices, KNN/ties/adjacency, prototype distances, memberships, OT marginal/cost arithmetic and A1 concatenation dimension arithmetic. The checker has no project-data input.

## Source and registry checks

`SOURCES.md` records actual source use and access depth. `papers.csv` was expanded only with sources used in these notes; `methods.csv` records conceptual methods as `studied_not_fitted`; `representations.csv` records family-level objects with `status=studied_not_fitted`; `codebases.csv` records official repositories/documentation without cloning or reproduction. Official library implementations are labelled as libraries where they are not the original authors' code.

## Repository checks

`git diff --check` passed after the final edits. The final `repomix . --compress` exited 0 with 338 files, 380,028 tokens and no suspicious files. The final `graphify . --code-only` exited 0 with 44 nodes, 67 edges and 7 communities (16 re-extracted code inputs, 23 cached; 283 non-code files skipped). Both commands were also run at phase start. These counts are execution snapshots of repository context, not biological results. Generated Graphify output remains local with the existing repository changes. Raw biological files remain ignored and unchanged.

## Open issues

Exact assay provenance, spatial units/registration, donor and section hierarchy, annotation releases, feature mappings across modalities, paired/unpaired design, and the suitability of any cost, metric, prior or likelihood for the six datasets remain unresolved. These must be verified before a later fitting or comparison phase. Readiness for Phase 2C is a handoff state, not authorization to begin it.

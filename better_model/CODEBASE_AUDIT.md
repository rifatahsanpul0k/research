# Model and codebase audit — 2026-09-25

The user's highest-ARI model is the authoritative starting point. Its reported superiority is user-provided information; there are no saved outputs in the supplied file to independently verify the score. `hello.py` is byte-identical to the initially inspected `hello.ipynb`, with SHA-256 `c2ec5c2172b3f3f8e762ff89abe8f4173f508d3444490a104e437268142593fa`. It contains 11 notebook cells and is retained intact.

## Scope and evidence

The review used the repository-wide Repomix context and Graphify structure, then original model, benchmark, result and knowledge files. Python definitions were inventoried across `code/` and the locally available `external_study/` implementations. Architectural source inspection focused on the supplied model, ARISE, SMART, SpatialGlue, SpaBalance and SCIGMA. SIVA, PRESENT, COSMOS and SpaAlign were reviewed for component/input compatibility using local code inventories and targeted documentation. This is not a new reproduction of those papers or an exhaustive scientific validation of every external repository.

| Area | Relevant evidence | Decision |
|---|---|---|
| User reference | `hello.py`, cells 3–8 | Preserve architecture, objective, bridge and schedule before testing scientific changes |
| Prior ARISE/SMART ablation | `code/run_smart_arise_ablation.py`, `results_smart_arise_exact_A1_D1/all_runs_results.csv` | Topology changes alone do not establish universal improvement; do not replace the preferred encoder on intuition |
| Prior failure analysis | `code/benchmarks/run_phase4a_diagnostics.py`, `run_phase4b_benchmark.py`, `RESEARCH_LOG.md` entries 28–30 | Include modality-only/space-only controls and partition-size diagnostics |
| Existing infrastructure | `code/benchmarks/common/{h5ad,validation,preprocessing,provenance,evaluation}.py` | Follow barcode, provenance and failure-record conventions; avoid reusing historical preprocessing/K-from-label defaults as if identical |
| ARISE/SMART | `external_study/ARISE/ARISE/{model,process,train}.py`, `SMART-main/smart/{model,train}.py` | Retain RNA dual GCN, consensus auxiliary graph and reconstruction objective; do not add a triplet loss without an ablation |
| SpatialGlue/SpaBalance | Local `model.py` implementations | Independent auxiliary graphs and modality balancing are plausible future ablations, not verified replacements |
| SCIGMA/SpaAlign | Local model/loss definitions | Contrastive/uncertainty modules alter the objective and need controlled comparisons |
| SIVA/PRESENT/COSMOS | Local interfaces and documentation | Likelihoods, anchor requirements, WNN/cooperative graphs are materially different protocols; no wholesale code merging |
| Knowledge base | `02_omics/.../28_DATA_LEAKAGE.md`, `06_representations/.../{43_ARISE,56_OVERSMOOTHING,58_GRAPH_CONSTRUCTION_SENSITIVITY}.md`, `ASTRA_OPERATING_RULES.md` | Declare transductive scope, preserve raw inputs, keep GPU training remote, distinguish computational scores from biological validation |

## Concrete problems in the reference

| Finding | Original behavior | Working implementation |
|---|---|---|
| Misnamed input | Notebook JSON has a `.py` extension | Executable module CLI and portable notebook; original preserved |
| Annotation/pairing | Assigns `gt_values.values` without barcode alignment | Exact ID-set validation and deterministic reindexing; missing annotations are masked before string conversion |
| Source semantics | `uns['log1p']` used as a proxy for normalization state | Explicit RNA input and modality settings; no silent HVG-method fallback |
| Preprocessing memory | Scales all RNA genes densely; densifies all ATAC peaks for PCA | Densify only selected RNA HVGs; centered sparse ARPACK PCA for ATAC |
| Graph memory | Dense cosine matrix and binary adjacency | Blocked neighbor queries and edge-only cosine calculations |
| Graph edge cases | Assumes first neighbor is self; unshaped empty intersection | Remove self by ID, cap k, deterministic edges, valid `(2,0)` empty graph; GCN self-loops support isolated nodes |
| Spatial weights | Greater Euclidean distance means greater GCN weight | Preserve in reference; decreasing RBF affinities only in separately named candidate |
| Cosine signs | Negative weights can make GCN degrees nonpositive | Reference fails clearly for nonpositive degrees; candidate removes nonpositive cosine edges |
| Spatial loss memory | Dense n×n adjacency, cosine, negatives and gradients | Algebraically equivalent blockwise BCE with activation checkpointing; verified loss and gradient agreement |
| DEC consensus | Dense n×n normalized adjacency | Sparse row-normalized adjacency and sparse matrix multiplication |
| Failure behavior | Broad exceptions mask HVG/clustering failures | Explicit KMeans protocol and actionable errors; no unlabeled mclust-to-KMeans substitution |
| Selection | Silhouette can favor degenerate partitions | Reference selection preserved; candidate requires K occupied clusters, minimum size 2 and largest fraction ≤0.95 |
| Exports | H5AD written after seed loop, retaining only last seed | Checkpoint, embedding, gates, labels and metrics for every seed |
| Marker claims | Wilcoxon on reconstructed standardized values | Preserve observed log-normalized expression; do not run marker tests on reconstruction |
| Plotting | Uses residual variables from last dataset/seed | Notebook explicitly selects dataset and seed |
| Reproducibility | No trained state, resolved defaults or complete source checksums | State dict, selected labels, resolved config, input/code hashes, exact code snapshot and environment per run |

The successful default KMeans path is supported directly. The reference's optional R/mclust path is intentionally not reproduced; it was not enabled in the supplied execution configuration. Switching cluster backends must be treated as a separate experiment.

## What actually remains the same

Both RNA branches are two GCN layers (input → 512 → 64); the auxiliary branch is one GCN layer (input → 64) on the RNA/spatial intersection. Feature-wise sigmoid gates combine the two RNA branches and then RNA with auxiliary latent features, each followed by a linear projection. The shared decoder hidden layer and all four reconstruction terms remain unchanged. Parameter L1/L2 penalties include DEC centers exactly as in the reference. Stage 2 multiplies beta by 0.2, lowers the learning rate tenfold, and updates the detached DEC target every five epochs. Best-stage-1 restoration and aligned KMeans prototype initialization are retained.

The reference's all-pairs spatial term is

`L = [sum_ij softplus(cos_ij) - sum_(i,j in spatial edges) cos_ij] / (2 n²)`,

with diagonal cosine set to zero. Blocking changes peak activation storage, not which positive or negative pairs contribute. Floating-point summation order, sparse graph ordering, RNA preprocessing precision and ATAC PCA solver can still change numerical trajectories; exact full-run ARI equivalence is not asserted. With nonzero dropout, target updates use evaluation mode for stable targets; the supplied default is dropout=0.

## Observed local results

Read-only input validation and default preprocessing succeeded for A1 (3,484 paired spots) and D1 (3,359 paired spots), with 3,000 RNA HVGs and 31 ADT features. Input checksums are frozen in the A1/D1 configs and recorded in [validation/local_checks.json](validation/local_checks.json). A 96-spot, 128-RNA-feature A1 subset completed 3+2 training epochs with finite embeddings. This deliberately small run is an engineering smoke test; its ARI was not evaluated.

| Default reference graph | A1 | D1 |
|---|---:|---:|
| Directed symmetric RNA edges | 88,520 | 70,328 |
| Directed symmetric spatial edges | 58,444 | 56,304 |
| Intersection edges | 2,388 | 1,538 |
| Spots isolated in intersection before GCN self-loops | 2,488 / 3,484 (71.4%) | 2,523 / 3,359 (75.1%) |
| Negative cosine edges observed | 0 | 0 |

**Interpretation:** much of the auxiliary branch behaves as a self-loop feature projection under this graph. This does not prove the intersection is harmful: the user's model may benefit from that behavior. A future isolated-spot fallback or auxiliary-specific graph should be tested separately with matched seeds and budgets. The current affinity candidate intentionally retains the consensus topology.

## External checks used

- [DEC, Xie et al. (ICML 2016)](https://proceedings.mlr.press/v48/xieb16.html): primary source for embedding/clustering refinement. The spatially modulated target is the user's extension; the DEC paper does not validate it.
- [PyG GCNConv documentation](https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.nn.conv.GCNConv.html): weighted adjacency, degree normalization and self-loops. The nonpositive-degree check follows this formula.
- [Scanpy HVG documentation](https://scanpy.readthedocs.io/en/stable/generated/scanpy.pp.highly_variable_genes.html): Seurat v3 expects count input; other supported flavor expects logged data.
- [Scanpy rank_genes_groups documentation](https://scanpy.readthedocs.io/en/stable/generated/scanpy.tl.rank_genes_groups.html): expects logarithmized expression, supporting removal of the reference's reconstructed-z-score marker test.

These sources were checked on 2026-09-25. They support implementation/input semantics, not an ARI improvement or biological mechanism claim.

## Remaining empirical work

The missing comparison target is the user's actual ASTRA ARI record: dataset, seeds, input version, exclusion policy, selected epochs and scores. The prior `ARISE_EXACT` result CSV is a different architecture and cannot substitute for that record. The new full 400-epoch, three-seed GPU runs and Colab dependency installation are not yet verified. E18 ATAC remains unavailable locally. A1/D1 and mouse sections must be analyzed separately; no donor-level generalization, causal gate interpretation, automatic boundary preservation or SOTA claim follows from this implementation.

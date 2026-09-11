# Phase 3D configuration freeze

Frozen before any Phase 3D scientific result on 2026-09-12. This phase evaluates only the two authorized classical integration/alignment methods, within dataset and within developmental stage. A changed parameter, software source, seed or input contract requires a new experiment series and experiment IDs.

## Starting checkpoint

- Starting repository commit: `951a61ca15239a7f644b60ec56dd1a463cd5570f` (`origin/main`), containing the Phase 3C checkpoint and committed compute-environment policy.
- Phase 3C remains committed and its 84-run registry/results are the comparison reference.
- The user-owned modified `hello.ipynb` and generated Graphify state are preserved; they are not scientific inputs.
- Source files are read-only. Phase 1D SHA-256 records are rechecked before and after each scientific series.

## Scope and eligibility

| Method | Eligible datasets | Views used for fitting | Excluded datasets/views |
|---|---|---|---|
| MOFA+ (`MOFAPLUS`) | `LN_A1`, `LN_D1`, `MB_E11`, `MB_E13`, `MB_E15` | RNA + ADT for lymph node; RNA + ATAC for each mouse stage | `MB_E18`: no ATAC integration; spatial coordinates are not treated as a MOFA view in this series |
| SCOT v1 (`SCOT`) | `LN_A1`, `LN_D1`, `MB_E11`, `MB_E13`, `MB_E15` | Same paired two-view contracts; fit is unsupervised over view relationships | `MB_E18`: no ATAC integration; no cross-stage alignment or spatial-coordinate view |

E18 remains RNA + spatial only with `E18_ATAC_VERIFIED = false`; no E18 MOFA+, SCOT, ATAC or RNA+ATAC run is allowed. Mouse stages are never pooled, and stage-specific ATAC feature spaces are retained independently.

## Source and environment freeze

| Method | Implementation | Immutable source | Version/environment | Compute class |
|---|---|---|---|---|
| MOFA+ | official author-linked Python `mofapy2` implementation | `external/mofapy2`, commit `90418e5021b3ae735ebf1fea5d7e07cae71c8bb7` | `mofapy2 0.7.5`; isolated `phase3d-mofa` environment | `COLAB_CPU` |
| SCOT | official author-linked SCOT v1 source `src/scotv1.py` | `external/SCOT`, commit `14649be6e14017dcfe7ba619091b33d1df55f6a9` | isolated `phase3d-scot` environment; POT version captured at execution | `COLAB_HIGH_MEMORY` |

Colab is the scientific execution environment for R3 workloads under the persisted compute policy. A fresh runtime must check out the exact repository commit, install the frozen environment, verify source checksums, load the frozen configuration and call repository code. Runtime type, Python version, GPU/CUDA fields where relevant, package versions, memory class, logs and output checksums are captured. No paid or additional external compute is used.

## Frozen input preprocessing

Source H5AD `X` is treated as source-provided processed values. Count/fragment semantics remain `UNKNOWN`; no library-size renormalization, filtering, imputation or cross-stage harmonization is performed. Observation IDs are joined explicitly and paired views must have identical ordered IDs. Labels are withheld from fitting and used only for the common evaluation cluster count and ARI/NMI.

### MOFA+ input track

Each view is a dense continuous matrix prepared independently:

- RNA: Phase 3C `log1p` on stored nonzero values, top 2,000 population-variance features with stable position ties, population z-score; selected feature IDs retained.
- ADT: Phase 3C per-observation CLR (`log1p` geometric-mean ratio), then feature population z-score; all panel features retained.
- ATAC: `log1p` on stored nonzero values, top 2,000 population-variance features with stable position ties, population z-score; stage-native peak IDs retained. This is a declared continuous Gaussian-compatible track, not a claim that source values are raw fragments.

MOFA+ uses a Gaussian likelihood for each transformed continuous view. Two views remain separate even when observations are paired. No Phase 3C PCA embedding is used as a MOFA input. The model is:

\[
X^{(m)} \approx ZW^{(m)} + \epsilon^{(m)}.
\]

The observation representation is the fitted factor score matrix `Z`; feature loadings `W^(m)`, variance-explained summaries and training statistics are saved separately. Factor count is fixed at 10. `scale_views=true`, `scale_groups=false`, centered groups, sparse weights enabled, sparse factors disabled, ARD weights enabled, ARD factors disabled, and no label-based selection are frozen. Training uses 1,000 iterations, fast convergence mode, `startELBO=1`, `freqELBO=5`, `startSparsity=50`, `startDrop=1`, `freqDrop=1`, no GPU mode, and the declared experiment seed.

### SCOT input track

SCOT receives two independently prepared view matrices:

- RNA: the frozen Phase 3C RNA representation (2,000 selected, z-scored features).
- ADT: the frozen Phase 3C ADT CLR/z-score representation.
- ATAC: the frozen Phase 3C TF-IDF → randomized 31-component LSI with component 1 dropped and the remaining 30 components population-z-scored.

The official v1 implementation applies its frozen per-sample L2 normalization, builds undirected connectivity kNN graphs using correlation distance, computes shortest-path distance matrices with finite caps for disconnected pairs, normalizes distances, and solves entropic Gromov–Wasserstein alignment. `k=50`, `epsilon=1e-3`, square loss, solver `POT.entropic_gromov_wasserstein`, `max_iter=1000`, `tol=1e-9`, and no self-tuning or label-based parameter search are frozen. A fixed seed-0 permutation of the second view prevents paired row positions from entering the fit; the coupling and its original IDs are retained.

SCOT's native coupling is primary. For common evaluation only, the declared barycentric projection of the second view onto the RNA feature space is used as an observation representation. It is not described as a learned neural embedding.

## Clustering, seeds and metrics

- Common clustering is the Phase 3C KMeans contract: `init="k-means++"`, `n_init=20`, `max_iter=300`, `tol=1e-4`, `algorithm="lloyd"`.
- Seeds are exactly `1729`, `2718`, and `31415`; method, representation and clustering seeds are recorded separately where applicable.
- `K` equals the number of nonmissing reference annotation categories for that dataset and is explicitly recorded as privileged `reference_annotation_count` information.
- Approved common metrics are ARI, arithmetic NMI and Euclidean silhouette with the Phase 3C sample-size and metric-subsample policy. No new headline metric is added after results.
- Every run saves representation variance, finite-value and duplicate-row checks, observation identity coverage, cluster-size distribution, singleton count, dominant-cluster flags and execution/scientific QC status separately.

## Run matrix and IDs

The planned matrix is 5 datasets × 2 methods × 3 seeds = 30 scientific runs, subject to per-run eligibility and failure preservation. IDs are immutable:

`EXP-{DATASET}-{MOFAPLUS|SCOT}-KMEANS-S{SEED}`

R0, R1 and R2 engineering checks are recorded separately from `experiments.csv`. Only completed project-data R3 runs enter that registry. No tuning, winner selection, biological factor interpretation, disease association, deep method, graph-neural method or novelty claim is permitted in this series.

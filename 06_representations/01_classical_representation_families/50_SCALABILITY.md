# Storage and computational scaling

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Output size is not fitting cost

Use n observations, p features, k retained components/neighbors where stated, v views and m target observations. Counts below are algebraic estimates for stated dense or sparse operations, not measured runtimes. A float64 number is 8 bytes before container/index overhead.

| Object/operation | Approximate storage or arithmetic |
|---|---|
| Raw dense X | np numbers |
| CSR X | O(nnz(X)+n) indices/values, with shape metadata |
| k latent scores and loadings | O(k(n+p)) numbers, excluding input/residuals |
| Dense exact SVD | O(np min(n,p)) arithmetic |
| All-pair Euclidean relations | O(n²p) direct work, O(n²) storage |
| Dense kernel eigensystem | O(n²) matrix storage, O(n³) full eigendecomposition |
| Stored KNN relationships | O(nk); discovery can still be O(n²p) |
| Dense graph / edge list | O(n²) / O(n+|E|), plus attributes |
| Dense OT plan | O(nm); dense Sinkhorn pass O(nm) |
| Hypergraph incidence | O(Σ_e|e|) sparse memberships plus dictionaries |
| Full Gaussian summaries | O(nk²), versus O(nk) diagonal summaries |
| Three-way tensor | O(npv) dense; factor storage depends on CP/Tucker ranks |

These estimates follow matrix dimensions and basic dense products; sources describe relevant linear-algebra, neighbor, OT and tensor operations.[^1][^2][^3][^4]

## Concrete size arithmetic

For n=100,000, a full n×n float64 matrix requires 10¹⁰×8=80,000,000,000 bytes, or 80 GB decimal, before overhead. A sparse top-30 list has 3,000,000 directed entries, but this is not the cost of finding them. A1's raw dense dimensions likewise do not predict sparse matrix memory without nonzero counts and index dtypes.

Approximate neighbors, randomized SVD, low-rank kernels, batching and sparse solvers alter computational behavior and potentially the represented information. Their existence does not authorize selection or benchmarking here. Reproducibility requires versions, seeds, stopping criteria and numerical tolerances when fitting is eventually authorized.

For each family, the registry records a conditional cost and failure modes. No laptop feasibility, actual runtime or winning method is inferred from Big-O. Large memory savings can accompany substantial information loss; biological and statistical evaluation remain separate from computational scaling.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).
[^2]: Official project maintainers (2026). [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html). See [access record](SOURCES.md#sk_neighbors).
[^3]: Official project maintainers (2026). [POT user guide](https://pythonot.github.io/). See [access record](SOURCES.md#pot_doc).
[^4]: Kolda TG; Bader BW (2009). [Tensor Decompositions and Applications](https://www.math.ucdavis.edu/~saito/data/tensor/kolda-bader_tensor-decomp-siamrev.pdf). See [access record](SOURCES.md#tensor).

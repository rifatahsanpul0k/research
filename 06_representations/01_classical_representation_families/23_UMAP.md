# UMAP

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Local relationships and a low-dimensional layout

UMAP constructs local neighbor relationships under a selected metric and combines directed local memberships into a fuzzy relationship structure. A useful expression for a directed membership is
\[
u_{j|i}=\exp[-\max(0,d(x_i,x_j)-\rho_i)/\sigma_i],
\]
for neighbors of i, with local connectivity adjustment ρ_i and local scale σ_i>0. Symmetric union weights are \(u_{ij}=u_{j|i}+u_{i|j}-u_{j|i}u_{i|j}\). These n×n memberships are not the final coordinates. A low-dimensional affinity, often written \(v_{ij}=(1+a\|y_i-y_j\|^{2b})^{-1}\), is optimized to approximate them, with a,b>0 determined by layout settings and Y:n×d.[^1][^2]

The conceptual objective has attractive and repulsive cross-entropy terms; practical negative sampling and optimization are implementation details that affect the fitted layout. The fuzzy simplicial interpretation motivates the construction, but the neighbor graph and its coordinate visualization are distinct representation stages.[^2]

## What a plot does and does not establish

The neighborhood size changes scale; min_dist changes how tightly points can be arranged; the metric and input preprocessing change the initial relationships. Initialization and stochastic optimization affect reproducibility. Neither local emphasis nor a method's stated global aims guarantee accurate all-pair distances, tissue boundaries or developmental trajectories for this project.

Using UMAP as a visualization asks for a display. Using its coordinates as model features commits to the layout's distortions and requires future task-specific validation. Similar clusters in a plot are not biologically equivalent; axes have no direct assay units. A transform for new points, where supported, is an algorithmic extension of a fitted representation, not a measured mapping.

Input feature/missingness choices remain external. Neighbor storage is roughly O(nk_neighbor); brute-force exact neighbor search can still cost O(n²p), and approximate search changes the cost/accuracy trade-off. Coordinates use O(nd); epoch and negative-sampling settings affect optimization work. No parameter values or dataset embeddings were tested.

## Evidence

[^1]: McInnes L; Healy J; Melville J (2018). [UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction](https://arxiv.org/abs/1802.03426). See [access record](SOURCES.md#umap).
[^2]: Official project maintainers (2026). [How UMAP Works](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html). See [access record](SOURCES.md#umap_doc).

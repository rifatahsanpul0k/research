# Graph construction families

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Each construction defines a different relation

Let R:n×d be a declared feature representation, D/B:n×n its dissimilarity/similarity, S:n×d_s spatial coordinates and A:n×n an observation adjacency unless otherwise stated. Every rule needs self-loop, direction, weight, tie and missingness conventions. Neighbor search and graph storage are separate operations.[^1][^2]

| Family | Example defining rule | Main assumption or failure mode |
|---|---|---|
| KNN | A_ij=1 if j∈N_k(i) | Fixed k may bridge large gaps; directed by default |
| Mutual KNN | Both neighbor selections required | Can isolate rare/sparse observations |
| Radius | A_ij=1 if D_ij≤r, i≠j | Units and density determine degree |
| Similarity threshold | A_ij=1 if B_ij≥τ | Threshold discontinuity and density shifts |
| Spatial | Apply distance/radius rule to S | Proximity is not signaling or contact |
| Correlation | Threshold correlations across replicates/observations | Correlation is not regulation; nodes may be genes, giving p×p A |
| Kernel weighted | A_ij=K_ij on a declared support | Dense kernel and sparse graph encode different information |
| Adaptive/learned | Optimize weights under a stated objective | Objective can encode unwanted assumptions; no fitting here |
| Biological knowledge | Edge from a curated assertion | Evidence/context and absent-annotation uncertainty |
| Hybrid | Union, intersection or weighted combination of relation types | Must retain provenance and incompatible edge semantics |

## Information and computational consequences

Union and intersection symmetrizations of KNN differ. A weighted sum of spatial and molecular adjacencies can obscure which relation caused a connection; retaining typed edges or separate layers preserves that distinction. A thresholded signed correlation graph needs an explicit treatment of negative relations, not silent deletion.

Sparse O(nk) final adjacency does not imply cheap discovery: naive all-pair search is O(n²d). Graphs from knowledge databases cost according to supplied entities/relations and mapping steps. Adaptive graph fitting can add a full optimization problem. No construction is ranked by these properties.

For project spots, input features and coordinate frames remain part of every graph's provenance. Biological priors require evidence distinctions, not automatic ground truth. Only the synthetic adjacency in the toy is constructed; all ten families are a conceptual survey. No real graph, hybrid rule or learned adjacency is selected.

## Evidence

[^1]: Official project maintainers (2026). [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html). See [access record](SOURCES.md#sk_neighbors).
[^2]: Official project maintainers (2026). [NetworkX graph types](https://networkx.org/documentation/stable/reference/classes/index.html). See [access record](SOURCES.md#networkx).

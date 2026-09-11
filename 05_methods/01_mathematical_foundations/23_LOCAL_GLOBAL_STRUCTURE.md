# 23. Local versus global structure

Let $d_X(i,j)$ be a chosen distance between observations in input space and $d_Z(i,j)$ their distance after a map to $Z\in\mathbb R^{n\times d}$. Local structure concerns relationships among nearby observations; global structure concerns broad relative placement, separation and overall organization. Neither has a unique definition without a metric, scale and sampling context. [Geometry foundations](SOURCES.md#bhk)

Preserving all pairwise distances preserves more than preserving the identity of each nearest neighbor. A map can keep adjacent points close while changing long-range separation. Toy example: points at 0, 1, 10 and 11 on a line form two pairs. Moving the second pair to 100 and 101 preserves each point's nearest-neighbor identity and within-pair distance, but changes separation between pairs greatly. Conversely, a small perturbation around nearly tied nearest distances can change local neighbors with little effect on global spread.

In omics, a locally coherent group may reflect a cell state, a spatial compartment, a batch or a depth range. A global axis might reflect development or preparation. These are candidate interpretations requiring evidence, not consequences of geometry. Spatial locality in $S$ differs from locality in RNA features, and both can matter.

A future evaluation must specify what preservation means: distances, ranks, neighbor membership, densities or relationships between known groups. Uniform visual gaps in a low-dimensional display cannot be assumed to correspond to original separation. This note defines the goals without comparing embedding algorithms or constructing graphs.

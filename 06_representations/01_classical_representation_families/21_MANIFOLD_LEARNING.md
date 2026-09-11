# The manifold hypothesis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## A conditional geometric model

The manifold hypothesis proposes that high-dimensional observations lie near a lower-dimensional structure. Formally, a local smooth parameterization \(g:U\subset\mathbb R^d\to\mathbb R^p\), d<p, can describe a d-dimensional manifold patch when its derivative has rank d. Local neighborhoods may then carry information about intrinsic geometry even when a single linear subspace does not describe the entire set. Manifold methods differ in which neighborhoods and geometry they estimate.[^1][^2]

This is an assumption to assess, not a theorem about RNA, ADT or ATAC. A union of populations, branches, boundaries, sparse observations and technical noise need not form one well-sampled smooth manifold. A visible curve after dimensional reduction is not independent evidence that the assumption held: the plotting algorithm helped create that curve.

## Representation choices and failure modes

A manifold-inspired representation may be coordinates \(Z:n\times d\), an affinity matrix n×n, or a neighborhood structure. These objects are not interchangeable. Local distances, geodesic/path relationships and global Euclidean distances answer different questions. Choosing d, neighborhood scale, a metric and a sampling model affects what can be retained. Disconnected populations cannot acquire a defensible biological bridge solely through a computational connection.

For this project, stage labels, spatial sampling and observation mixtures can shape neighborhoods without expressing a single developmental degree of freedom. Spatial coordinates are physical information with units; manifold coordinates are inferred. Missing views do not automatically become identifiable through a manifold assumption.

Storage ranges from O(nd) for coordinates to O(n²) for dense relationships, plus fitting state. Reconstruction into original named features generally needs a separate inverse model. Later validation would examine sensitivity to sampling, parameters and input preparation, alongside biological evidence. No manifold dimension, embedding or geometry is selected here. t-SNE and UMAP are studied next as particular mechanisms, not as proof of the hypothesis.

## Evidence

[^1]: Coifman RR; Lafon S (2006). [Diffusion maps](https://www.math.ucdavis.edu/~strohmer/courses/270/diffusion_maps.pdf). See [access record](SOURCES.md#diffusion).
[^2]: Official project maintainers (2026). [How UMAP Works](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html). See [access record](SOURCES.md#umap_doc).

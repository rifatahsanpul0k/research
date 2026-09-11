# Prototype-based representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Distances to reference profiles

Let \(c_1,\ldots,c_k\in\mathbb R^p\) be named prototypes and define
\[
R_{ij}=d(x_i,c_j),\qquad X:n\times p,\quad R:n\times k.
\]
A prototype may be an actual reference observation, a mean of a declared group, or an externally specified profile. A centroid is an arithmetic mean and need not correspond to any measured observation. K-means is one mechanism for choosing centroids, not part of the definition of a prototype-distance representation.[^1]

A distance vector preserves relative position to selected references. Its interpretability depends on the metric and prototype provenance. It can lose distinctions if prototypes are few or poorly placed. For example, distances to a single point cannot identify direction. With a sufficient affinely spanning set of known Euclidean prototypes, squared-distance differences can determine coordinates; loss therefore depends on the actual reference configuration, not the label “prototype.”

## Project relevance and cost

A mean RNA profile over mixed spots is a numerical summary; it is not automatically a representative single cell. A reference atlas or hand-selected marker profile would introduce biological priors and possible domain shift. Choosing prototypes using test labels would leak evaluation information.

Computing dense distances to k fixed p-dimensional prototypes costs O(nkp); storing prototypes and distances costs O(kp+nk). Finding prototypes can add iterative optimization, and a stochastic selection algorithm adds seed/initialization sensitivity. Missing entries require a metric policy; a missing assay does not define a zero prototype distance.

The toy defines two centroids from explicitly chosen synthetic groups and computes all distances manually. These groups are explanatory choices, not fitted clusters or biological discoveries. No prototypes, cluster count or assignment rule is selected for the real datasets.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).

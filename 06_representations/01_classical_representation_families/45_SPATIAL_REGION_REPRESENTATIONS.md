# Spatial regions, boundaries and gradients

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Region information can be discrete or continuous

For n observation locations, a region label \(c_i\in\{1,\ldots,r\}\) provides categorical membership. One-hot codes have shape n×r. A probabilistic assignment Q:n×r has nonnegative rows summing to one but requires a model/calibration interpretation; normalized scores are not automatically probabilities.

With coordinates \(s_i\in\mathbb R^{d_s}\) and a specified boundary set B in the same frame, distance-to-boundary is \(b_i=\inf_{s\in B}\|s_i-s\|\). A signed distance requires a declared inside/outside orientation. Continuous gradients can be stored as n×g measurements or inferred values, but their provenance differs. These are possible constructions, not computed project annotations.

Spatial transcriptomics alignment work distinguishes molecular information, measured locations and downstream tissue analysis; a registered slice or region is not automatically a cell-type map.[^1]

## Information loss and ambiguity

A discrete region label makes within-region positions equivalent **in the code**, while actual positions and molecular profiles may differ. Boundary distances lose angular and along-boundary position. A soft region membership can preserve uncertainty about a boundary, but in a mixed spot it must not be confused with cell-type proportions without an explicit model.

For project data, numerical coordinates need verified units/frame before physical distances can be assigned. Region names require an annotation source, species, stage and level of anatomical granularity. A thresholded expression gradient is not independently measured anatomy. Missing labels remain unannotated, not a biological “other” class unless defined.

Labels cost O(n), soft memberships O(nr), raw coordinates O(nd_s); boundary-search cost depends on boundary complexity and indexing. Separate sections cannot share boundary distances without a defined registration. No region delineation, boundary inference, atlas transfer or spatial smoothing is performed. Discrete and continuous representations remain unranked options.

## Evidence

[^1]: Zeira R; Land M; Strzalkowski A; Raphael BJ (2022). [Alignment and integration of spatial transcriptomics data](https://www.nature.com/articles/s41592-022-01459-6). See [access record](SOURCES.md#paste).

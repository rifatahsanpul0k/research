# Representing spatial information

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Several objects from coordinates

Let \(S\in\mathbb R^{n\times d_s}\), usually d_s=2 or 3, contain coordinates with observation identifiers. A coordinate frame, units, section identity and registration status are part of the representation. Possibilities include:

| Object | Shape | Information encoded |
|---|---|---|
| Raw coordinates | n×d_s | Position in one declared frame |
| Spatial distances | n×n | Pairwise separation; loses absolute origin/orientation |
| Spatial neighbor sets | n lists | Selected local proximity relationships |
| Spatial kernel | n×n or sparse | Scale-dependent spatial affinity |
| Region labels | n categories, or n×r one-hot | Membership in a defined region vocabulary |
| Relative coordinates | n×d_s | Position relative to a stated landmark or local frame |

These are definitional constructions. Spatial alignment methods such as PASTE explicitly use spatial relationships and molecular information, illustrating that the two inputs have distinct roles.[^1]

## Interpretation and preservation

Translation of coordinates preserves Euclidean distances; scaling changes their units. Rotation can preserve pairwise distances while changing biologically oriented axes. Coordinates from separate sections cannot be compared merely because both have two columns. Array row/column indices are not automatically micrometers. A distance-to-landmark summary is many-to-one and loses angular information.

Spatial proximity is not proof of physical cell contact or signaling. For spots or capture bins, proximity relates measurement locations rather than verified single-cell boundaries. Mixed expression and a shared region label do not establish equivalent cell types. Existing project units and section/embryo provenance remain partly unresolved; no registration is inferred.

Raw coordinate storage is O(nd_s); full spatial distances/kernels O(n²); sparse neighbor lists O(nk). Choosing a radius without known physical units changes the meaning of the resulting relations. Missing coordinates should remain missing, not become (0,0). Coordinates, molecules and metadata may coexist as separate representations; spatial edges are optional. No spatial graph, distance matrix or region assignment was generated from project data.

## Evidence

[^1]: Zeira R; Land M; Strzalkowski A; Raphael BJ (2022). [Alignment and integration of spatial transcriptomics data](https://www.nature.com/articles/s41592-022-01459-6). See [access record](SOURCES.md#paste).

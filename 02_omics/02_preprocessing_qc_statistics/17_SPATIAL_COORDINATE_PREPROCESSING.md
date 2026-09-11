# Spatial coordinate preprocessing

Coordinates are observation-linked positions in an assay-specific frame. Their origin, axis orientation, units, scale, pixel/array conversion and registration determine whether Euclidean distance (d_{ij}=\sqrt{(x_i-x_j)^2+(y_i-y_j)^2}) has physical meaning [S11,S21]. A translation leaves distances unchanged; anisotropic scaling changes them; axis reflection changes orientation but not pairwise Euclidean distances.

Our H5AD objects expose `obsm/spatial` arrays with shape (n\times2), but local metadata do not establish physical units or image registration. Keep coordinates separate from molecular matrices, retain the original frame, and record any transform as a lineage operation. Do not build a spatial graph in this phase. Nearby spots can share tissue or contain mixtures; coordinate proximity does not prove molecular equivalence. Evidence: Ståhl et al. [S11], 10x spatial outputs [S21], AnnData [S22].

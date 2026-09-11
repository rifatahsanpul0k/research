# 16. Spatial coordinate systems

Coordinates are ordered pairs associated with observations. They may be array row/column, bead/spot position, pixels, micrometres, bins, or capture locations. Space Ranger exposes barcode inclusion, array coordinates, and full-resolution pixel coordinates as separate fields [S21].

A coordinate system has units, origin, orientation, scale, and sometimes a transform to another frame. (S_i=(x_i,y_i)) is metadata, not an image feature. Two assays can use the same numeric pair for different physical distances or orientations; Euclidean distance is meaningful only after these conventions are known.

Registration across modalities or sections can be exact, approximate, or unavailable. Do not create spatial neighbors, interpret distances, or call aligned rows equivalent until coordinate provenance and observation units are verified.

**Evidence:** [S11], [S13], [S21].

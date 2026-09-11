# 9. Spatial transcriptomics

Spatial transcriptomics assigns molecular observations to positions in a tissue section. Sequencing-based capture uses spatially indexed oligos or beads; imaging-based families detect selected transcripts in place. The biological quantity is RNA location and abundance at the assay’s resolution [S11][S12].

An observation may be a spot, bead, bin, cell segmentation, or pixel-defined location. (X\in\mathbb R^{n\times p}) is linked to (S\in\mathbb R^{n\times2}), (S_i=(x_i,y_i)). Coordinates are assay metadata; this project’s computational scope uses molecular matrices and coordinates, not image-derived features.

Spots can contain multiple cells, and a coordinate does not prove a cell identity. Tissue permeabilization, diffusion, capture area, sequencing depth, and registration introduce distortion. Spatial proximity is useful context but does not establish molecular equivalence or communication [S11][S13].

**Evidence:** [S11], [S12], [S13], [S21].

# 10. Spatial protein

Spatial protein assays measure a selected panel of epitopes and attach each measurement to a tissue location. Depending on the family, detection is sequenceable oligo tags or imaging signals; panel membership and spatial indexing define what is measured [S07][S13].

For sequenceable spatial protein data, (X_{protein}\in\mathbb R^{n\times q}) is paired with (S\in\mathbb R^{n\times2}). Rows can be spots, pixels, bins, or segmented cells. Measurements may be fully paired with spatial RNA, approximately aligned across serial sections, or unpaired; the design must be documented.

Protein panels are targeted, antibody affinity varies, and background/saturation affect values. Coordinates can share a tissue frame while molecular capture footprints differ. Do not treat a protein intensity/count as protein activity or assume spatial alignment means same molecules were measured.

**Evidence:** [S06], [S07], [S13], [S21].

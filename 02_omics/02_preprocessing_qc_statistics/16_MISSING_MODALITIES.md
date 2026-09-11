# Missing modalities

Structural missingness means a modality was never designed or supplied for an observation; technical missingness means it was intended but failed; a value-level zero means the modality has a recorded zero. They are different data-generating states. A modality mask (M_{im}\in\{0,1\}) records whether observation (i) has modality (m); it should accompany any downstream table [S14,S43].

RNA and ATAC are paired by identical barcodes and order in local E11/E13/E15 files. E18 RNA is present, but E18 ATAC has no complete local copy and is therefore unavailable, not zero and not imputed from another stage. Imputation would add assumptions and could manufacture cross-modality agreement. Missingness can be biology, protocol design, transfer failure or quality failure; inspect provenance before modeling. Evidence: Argelaguet et al. [S14], Stuart & Satija [S43], local manifests.

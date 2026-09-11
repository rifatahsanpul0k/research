# 17. Donor, specimen, sample, assay, and batch

A useful bookkeeping hierarchy is `organism/donor → specimen → tissue/sample → assay/library → batch → observation`. Actual designs can cross batches, share a specimen across assays, or use serial sections; the hierarchy is a design record rather than a universal law [S17].

Metadata should preserve each level and identifiers. Replicate observations from one donor do not equal independent biological replicates. If cells from one donor appear in training and test sets, apparent generalization can be inflated because cells share genetic and environmental background [S17].

For spatial data, section and coordinate-frame identifiers are additional levels. For multimodal data, assay/library IDs establish whether rows are paired. No splitting or leakage algorithm is implemented here; the hierarchy is a prerequisite for later study design.

**Evidence:** [S17], [S14].

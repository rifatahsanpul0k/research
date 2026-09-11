# Confounders and nuisance variables

A confounder is associated with both a measured feature and the comparison of interest, making an apparent association ambiguous. Candidate variables include batch, donor/embryo, stage, region, cell cycle, library size, quality, disease state and tissue composition. A variable called “nuisance” statistically may still be biological; removing it can erase the question of interest [S16,S17,S43].

Use a design table with observation ID, sample, donor/embryo, stage, section/region, modality and QC fields. Distinguish covariate adjustment from normalization and from correction of measurement error. Single-cell observations nested in donors are subsamples, so treating thousands of cells as independent biological replicates creates pseudoreplication [S17]. This phase inventories fields and does not fit a model or declare any confounder resolved.

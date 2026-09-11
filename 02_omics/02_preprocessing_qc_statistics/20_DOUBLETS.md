# Doublets

A doublet occurs when two cells or nuclei enter one capture unit and produce a mixed molecular profile. It can look like a high-depth observation expressing markers from otherwise separated populations, but similar cell types can be difficult to distinguish. Doublets arise during loading and are assay- and loading-dependent [S46].

Computational detection concepts include simulated pair profiles, nearest-neighbor scores, genotype/hash evidence and multimodal disagreement. These produce suspicion scores, not a perfect ground truth; thresholds depend on expected loading and cell composition. A rare real transitional state can resemble a doublet, and filtering it can remove biology. We do not run DoubletFinder or any detector. Evidence: McGinnis et al. [S46] and local RNA/ATAC QC columns. The correct record is a flag with method, score, threshold and review status.

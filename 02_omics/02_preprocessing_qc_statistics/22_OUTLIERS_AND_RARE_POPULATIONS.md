# Outliers and rare populations

An outlier is an observation extreme relative to a chosen statistical reference; it is not synonymous with an erroneous observation. Technical outliers include low-quality libraries, malformed coordinates or failed capture. Biological outliers include rare cell states, unusual anatomy and transitional populations. A robust summary, replicate evidence and assay metadata are needed before removal [S16,S17].

Filtering on total counts can remove rare cells; filtering on marker expression can remove the population being sought. In spatial data, a rare region may be spatially coherent. In multimodal data, discordance can reflect biology, modality failure or doublet. We retain all source rows and report extrema, with no automatic filtering. Evidence: Luecken & Theis [S16], Zimmerman et al. [S17], and local annotation/QC reconnaissance.

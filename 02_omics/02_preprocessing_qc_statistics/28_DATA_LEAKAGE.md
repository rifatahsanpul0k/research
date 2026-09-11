# Data leakage in preprocessing

Leakage occurs when information from held-out predictive observations influences preprocessing parameters or feature decisions. Examples include choosing genes from all folds, estimating normalization parameters from test cells, selecting peaks using outcome labels, or using a spatial section’s held-out labels to set a threshold. Even unsupervised transforms can leak distributional information when evaluation is meant to represent unseen data.

For a predictive pipeline, split at the biological replicate or other declared unit first, fit (mu,sigma), feature prevalence rules, HVG lists or model parameters on training data, then apply them to validation/test data with identical feature identifiers. This is a design principle, not a train/test experiment; none is run here. In descriptive atlas work, the scope and reuse of all observations must be stated. Evidence: Stuart et al. [S43], Luecken & Theis [S16], Zimmerman et al. [S17].

# Sparse and regularized autoencoders

Phase 2C · method study · studied_not_fitted · not_reproduced.

For \(Z=f_\phi(X)\in\mathbb R^{n\times d}\), one possible teaching objective is
\[
J=J_{\mathrm{rec}}+\lambda_z\frac1n\sum_{i=1}^n\sum_{k=1}^d |z_{ik}|
+\lambda_W\sum_\ell\|W^{(\ell)}\|_F^2 .
\]
The nonnegative \(\lambda_z,\lambda_W\) are penalty weights, not probabilities. Activity sparsity penalizes latent activations; weight decay penalizes parameters. These are distinct constraints. A contractive AE instead penalizes encoder sensitivity, for example \(\|\partial f(x)/\partial x\|_F^2\), a \(d\times p\) Jacobian norm.[^1]

A sparse vector need not select a biological pathway. Consider a decoder \(g(z)=Wz\). Scaling \(z'=az,\ W'=W/a\) leaves reconstruction unchanged for \(a>0\) while changing an L1 activity penalty. Thus activity constraints interact with weight constraints and decoder scale; the penalty alone is not a semantic definition.

If two genes always vary together in a training set, several latent decompositions may explain them. Sparsity chooses among coordinate descriptions under an objective; it does not establish regulatory direction. Identifiability requires extra assumptions or evidence.[^2]

**Project interpretation:** sparsity can mean few active latent units even when the original count matrix is sparse for entirely different measurement reasons. A dense latent code can arise from a sparse input and vice versa. Pathway-based masks are a separate [biological prior](59_BIOLOGICAL_PRIOR_NEURAL_MODELS.md). Reconstruction, interpretability and task utility must remain separate questions.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | AE with activity, weight or sensitivity constraints |
| Training objective | Reconstruction plus explicitly weighted penalties |
| Biological prior | Sparsity/smoothness; biological prior only if separately encoded |
| Downstream model | Separate clustering or prediction |
| Evaluation | Constraint behavior and biological interpretation require distinct evidence |

## Evidence

[^1]: [AE_BOOK: original source and access notes](SOURCES.md#ae_book).
[^2]: [DISENTANGLE: original source and access notes](SOURCES.md#disentangle).


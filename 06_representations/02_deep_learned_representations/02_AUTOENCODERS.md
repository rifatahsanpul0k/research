# Autoencoders

Phase 2C · method study · studied_not_fitted · not_reproduced.

An ordinary deterministic autoencoder uses \(f_\phi:\mathbb R^p\to\mathbb R^d\) and \(g_\theta:\mathbb R^d\to\mathbb R^p\):
\[
Z=f_\phi(X)\in\mathbb R^{n\times d},\quad
\widehat X=g_\theta(Z)\in\mathbb R^{n\times p},\quad
J=\frac1n\sum_i d_x(x_i,\widehat x_i).
\]
Here rowwise evaluation of \(f,g\) is understood and \(d_x\) is a specified reconstruction loss, not necessarily a distance metric. An undercomplete bottleneck has \(d<p\); an overcomplete code has \(d\ge p\) and needs other restrictions to avoid trivial copying. Nonlinear compression need not recover PCA coordinates or an identifiable biological manifold.[^1]

A decoder produces reconstructed values; \(Z\) is the representation. Low training error alone may reflect memorization or reconstruction of technical variation. An especially clear counterexample is an overcomplete identity encoder/decoder: every input is perfectly reconstructed, yet nothing has been compressed or made biologically interpretable.

For squared error \(d_x=\|x-\widehat x\|_2^2\), a feature with a larger numeric scale contributes more unless preprocessing or loss weights compensate. The mathematical objective concerns values in the supplied coordinate system. **Project interpretation:** RNA and ADT cannot be called balanced just because they occur in the same input. A future audit would need their units and transformations.

The ordinary AE in this note does not supply a normalized generative density or a posterior over \(z\). Adding noise or a sparsity penalty does not by itself make it a VAE. See [VAE](05_VARIATIONAL_AUTOENCODERS.md) and [count-aware losses](06_COUNT_AWARE_VAES.md).

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Deterministic encoder and decoder |
| Training objective | Reconstruction loss |
| Biological prior | Compression/regularity assumption; no pathway prior inherent |
| Downstream model | Clustering or prediction on Z; decoder reconstruction is a different output |
| Evaluation | Generalization of reconstruction plus task/biological validity |

## Evidence

[^1]: [AE_BOOK: original source and access notes](SOURCES.md#ae_book).


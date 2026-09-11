# Denoising autoencoders and DCA

Phase 2C · method study · studied_not_fitted · not_reproduced.

A denoising AE draws a corrupted input \(\tilde x\sim c(\tilde x\mid x)\), but uses \(x\) as the target:
\[
J=\mathbb E_{x}\mathbb E_{c(\tilde x\mid x)}
[d_x(x,g_\theta(f_\phi(\tilde x)))].
\]
The corruption law \(c\) is specified, such as feature masking. This differs from an ordinary AE that receives and reconstructs the same vector. Robustness is relative to the corruption chosen; it is not robustness to every source of measurement error.[^1]

**DCA (Eraslan et al., 2019)** is a count autoencoder with neural outputs for negative-binomial mean/dispersion and optional zero-inflation. Its principal denoised output is the fitted NB mean, with a bottleneck available as a representation. DCA's denoising formulation uses observed counts and a statistical noise model; do not describe it as necessarily training on artificially masked counts paired with experimentally known clean counts. The official paper links theislab/dca.[^2]

Synthetic illustration: corrupt \((2,1)\) to \((2,0)\) but train toward \((2,1)\). The target is known because the example created the corruption. With an observed omics zero, the unobserved molecule abundance is not known. Consequently a predicted positive value is an estimate, not a recovered measurement.

**Project interpretation:** denoising can alter pairwise similarities and downstream clustering even when the output looks smoother. Preserve the raw matrix and distinguish \(Z\), reconstructed means, and original counts. A likelihood and a bottleneck do not prove that rare variation is noise. DCA is not a variational posterior encoder merely because its decoder predicts distribution parameters.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | DCA deterministic count AE; generic denoising AE takes corrupted inputs |
| Training objective | DCA NB/ZINB negative log likelihood; generic corruption reconstruction |
| Biological prior | Assumed noise process and shared feature structure |
| Downstream model | Denoised means or separate embedding-based tasks |
| Evaluation | Held-out predictive behavior and preservation of relevant signal |

## Evidence

[^1]: [DAE: original source and access notes](SOURCES.md#dae).
[^2]: [DCA: original source and access notes](SOURCES.md#dca).


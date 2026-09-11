# MultiVI

Phase 2C · method study · studied_not_fitted · not_reproduced.

MultiVI (Ashuach et al., 2023) learns from paired RNA–ATAC observations alongside RNA-only and ATAC-only observations. It has modality-specific encoders, a shared latent representation and modality-specific generative outputs. Paired observations constrain alignment; missing modalities are handled without treating their unmeasured entries as observed zeros.[^1]

For \(G\) genes and \(P\) peaks, \(x_i\in\mathbb N_0^G\) and \(a_i\in\{0,1\}^P\) have different feature meanings. The RNA observation model is count based; the ATAC model targets detection using
\[
a_{ij}\sim\operatorname{Bernoulli}(p_{ij}d_i r_j).
\]
Here \(p_{ij},d_i,r_j\in[0,1]\) are a decoded accessibility term and cell/region scaling factors. Denote RNA depth by \(\ell_i\), **not** \(d_i\), to avoid confusing two kinds of scaling. Modality encoder posteriors have \(d\)-dimensional latent variables; for paired inputs the documented construction averages the two modality representations, and for a single modality bypasses that average.[^2]

**Original teaching point:** two Gaussian latent variables averaged remain Gaussian, but their variance is not the arithmetic mean of variances: for independent \(u,v\), \(\operatorname{Var}[(u+v)/2]=(\Sigma_u+\Sigma_v)/4\). Any implementation's posterior-combination rule must therefore be inspected rather than guessed from the phrase “average latent.”

**Project interpretation:** mouse RNA/ATAC motivates learning this missing-modality design; it does not authorize imputing E18 ATAC. Peak definitions, assembly, feature order and observation matching remain necessary. A zero in a measured ATAC panel is a detection outcome; an absent panel contributes no direct measurement. Predicted accessibility is not an experimentally observed open chromatin state. Integration also needs shared biological support: a modality-only population absent from the paired data can be underconstrained.

Official maintained code is [scvi-tools](https://github.com/scverse/scvi-tools). Paper and documentation are distinguished; current likelihood defaults are not presumed identical to the 2023 analysis.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Modality-specific variational encoders and RNA/ATAC decoders |
| Training objective | Variational likelihood plus modality alignment in the published model |
| Biological prior | Shared state and assay-specific sampling assumptions |
| Downstream model | Joint Z; separate expression/accessibility prediction or differential queries |
| Evaluation | Paired alignment and predictive validity; not measured here |

## Evidence

[^1]: [MULTIVI: original source and access notes](SOURCES.md#multivi).
[^2]: [MULTIVI_DOC: original source and access notes](SOURCES.md#multivi_doc).


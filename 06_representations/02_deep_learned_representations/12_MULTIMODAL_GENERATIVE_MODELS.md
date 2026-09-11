# Other multimodal generative designs

Phase 2C · method study · studied_not_fitted · not_reproduced.

For observed modalities \(O_i\), a shared-latent generative template is
\[
p(z_i)\prod_{m\in O_i}p_{\theta_m}(x_i^{(m)}\mid z_i).
\]
Here \(z_i\in\mathbb R^d\), \(x_i^{(m)}\in\mathbb R^{p_m}\), and each decoder has its own output dimension and distribution. A product-of-experts combines evidence multiplicatively; a mixture-of-experts averages alternative densities. Neither expression means simply averaging feature matrices.[^1][^2]

**scVAEIT (Du, Cai and Roeder, 2022)** studies mosaic integration/imputation with a conditional variational approach and missingness masking. Its model is intended to predict missing features/modalities while accounting for batch. Publication and author repository are verified; this note does not assign an uninspected exact likelihood or parameter count. The original jaydu1/scVAEIT repository redirects to JinHongDu-Lab/scVAEIT.[^3]

**sciPENN (Lakkis et al., 2022)** is a neural framework for CITE-seq/RNA integration and protein prediction/imputation. It illustrates that multimodal prediction need not be classified as a VAE: no VAE prior or ELBO is inferred from its name. The primary abstract and author implementation identify predictive uncertainty as part of its purpose; precise uncertainty calibration is not established by code availability.[^4]

**Project interpretation:** these examples motivate separate fields for integration, prediction and missingness support. A system predicting a protein panel from RNA may be useful for a task even when it supplies no joint likelihood over all possible assays. Conversely, a normalized joint density does not guarantee accurate predictions outside its training support.

See [fusion](49_MULTIMODAL_FUSION.md) for the actual expert-combination equations. No additional family is proposed for this project.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | scVAEIT: conditional VAE; sciPENN: predictive neural model; expert inference is another design axis |
| Training objective | Masked variational prediction versus supervised/predictive objectives; exact sciPENN loss not asserted here |
| Biological prior | Shared support and missingness/assay assumptions |
| Downstream model | scVAEIT latent integration/imputation; sciPENN protein prediction and integrated analysis |
| Evaluation | Prediction and uncertainty need held-out biological evidence |

## Evidence

[^1]: [MVAE: original source and access notes](SOURCES.md#mvae).
[^2]: [MMVAE: original source and access notes](SOURCES.md#mmvae).
[^3]: [SCVAEIT: original source and access notes](SOURCES.md#scvaeit).
[^4]: [SCIPENN: original source and access notes](SOURCES.md#scipenn).


# Cobolt

Phase 2C · method study · studied_not_fitted · not_reproduced.

Cobolt (Gong, Zhou and Purdom, 2021) uses a hierarchical latent count model and multimodal variational inference to integrate jointly and singly measured observations. Its latent categories have modality-specific feature distributions, not guaranteed one-to-one biological-process identities.[^1]

A simplified dimension-explicit generative core is
\[
z_i\in\mathbb R^K,\quad \theta_i=\operatorname{softmax}(z_i)\in\Delta^{K-1},
\quad B^{(m)}\in\mathbb R^{p_m\times K},\quad
\pi_i^{(m)}=\operatorname{softmax}_{\rm column}(B^{(m)})\theta_i,
\quad x_i^{(m)}\sim\operatorname{Multinomial}(N_i^{(m)},\pi_i^{(m)}).
\]
\(N_i^{(m)}\) is the modality count total; each feature-distribution column sums to one, so \(\pi_i^{(m)}\in\Delta^{p_m-1}\). This is a multinomial conditional likelihood, not an independent NB for every feature. The paper also models batch effects and uses jointly measured observations to relate latent estimates from single modalities.[^1]

**Synthetic dimension check:** with three RNA genes, four peaks and two categories, the feature maps have shapes \(3\times2\) and \(4\times2\). Both can map the same two-vector \(\theta_i\) into different feature spaces. Shared dimension does not require a peak-to-gene conversion or equal RNA/ATAC vectors.

**Project interpretation:** conditional totals discard information about absolute modality abundance. Meaningful shared support and correctly recorded pairing are essential. Access to one modality does not make its missing partner known; transferring a latent mapping can fail for a novel biological population.

The representation is a posterior summary of \(z_i\), distinct from feature probabilities, multinomial count draws or downstream clusters. Official publication-linked code: [epurdom/cobolt](https://github.com/epurdom/cobolt); identity checked, not cloned or reproduced.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Multimodal VAE inference for hierarchical latent count model |
| Training objective | Variational objective with modality-specific multinomial likelihoods |
| Biological prior | Shared latent categories and count-composition assumptions |
| Downstream model | Joint clustering/visualization on latent summaries |
| Evaluation | Alignment and biological support require evidence; none generated |

## Evidence

[^1]: [COBOLT: original source and access notes](SOURCES.md#cobolt).


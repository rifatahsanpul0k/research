# Probability distributions as representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## More than a point estimate

An observation can be represented by a distribution over a k-dimensional latent quantity, for example
\[
z_i\sim\mathcal N(\mu_i,\Sigma_i),\quad
\mu_i\in\mathbb R^k,\quad\Sigma_i\in\mathbb R^{k\times k},\quad\Sigma_i\succeq0.
\]
The mean gives a location; diagonal variances give marginal spread; off-diagonal terms give dependence. A degenerate PSD covariance is allowed as a Gaussian measure, while a full-dimensional density requires positive definiteness. This is a representation form, not a VAE architecture.[^1]

For a scalar, N(2,0.01) and N(2,4) share their mean but express different uncertainty. Storing only 2 erases that distinction. Conversely, two non-Gaussian distributions can have the same mean/covariance yet differ in modality or tail probabilities; a Gaussian approximation may lose those properties.

## Interpretation and project boundary

State whether the distribution describes measurement error, a posterior over latent coordinates, a population distribution or a predictive distribution. Posterior uncertainty is conditional on priors, likelihood and fitted parameters; it is not an independent verification that a latent factor is biological. Model misspecification and unmodeled batch effects can produce narrow but misleading uncertainty intervals.

Dense storage for n full Gaussian summaries is O(nk²), or O(nk) for diagonal covariance, which assumes away latent covariance. Inference cost is method-specific. A multimodal posterior requires a likelihood and correspondence assumptions; labeling an object probabilistic does not solve an absent view. Spatial dependence may require a joint model rather than separate per-observation marginals.

The project currently has no fitted probabilistic representation. Such an object could later accompany scores to expose model-based uncertainty, but it cannot convert missing E18 ATAC into a measured assay. Deep generative models remain outside this phase.

## Evidence

[^1]: Blitzstein JK; Hwang J (2019). [Introduction to Probability, second edition](https://stat110.hsites.harvard.edu/). See [access record](SOURCES.md#prob).

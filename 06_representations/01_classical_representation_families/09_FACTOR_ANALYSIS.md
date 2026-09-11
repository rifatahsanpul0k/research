# Classical factor analysis

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## A probabilistic measurement model

For one p-dimensional observation,
\[
x_i=\mu+\Lambda z_i+\epsilon_i,
\quad z_i\sim\mathcal N(0,I_k),\quad
\epsilon_i\sim\mathcal N(0,\Psi),
\]
with \(\mu:p\), \(\Lambda:p\times k\), \(z_i:k\) and diagonal \(\Psi:p\times p\) with positive diagonal entries. Assume z and noise independent. Then
\[
\operatorname{Cov}(x_i)=\Lambda\Lambda^T+\Psi.
\]
The common factors explain cross-feature covariance while Ψ represents feature-specific variance. Estimated latent scores give an n×k representation; their uncertainty is part of the probabilistic model.[^1]

## Difference from PCA

PCA directly optimizes retained variance/reconstruction in a chosen metric. Factor analysis specifies a latent distribution and feature-specific noise. Probabilistic PCA is the special isotropic-noise model \(\Psi=\sigma^2I\); it must not be confused with unconstrained diagonal-noise factor analysis. Gaussian assumptions are modeling assumptions, not facts about raw RNA counts.[^1]

For an orthogonal \(Q:k\times k\), \(\Lambda Q(\Lambda Q)^T=\Lambda\Lambda^T\). Thus covariance alone cannot determine a unique factor orientation. Calling factor 1 a developmental mechanism requires evidence beyond likelihood or loading magnitude. Technical variables can also produce covariance.

## Project use and limits

A fitted loading model could later provide observation coordinates and residual variance estimates on a defined processed assay; no such fit occurs now. Complete-case vanilla implementations and model-based handling of missing values are different capabilities: missing-data support must be checked for a particular estimator, not inferred from the word probabilistic. Multi-view and spatial dependencies need additional structure.

Storage for Λ and n score vectors is O(pk+nk), plus p noise variances. Iterative likelihood estimation and matrix factorizations add solver-dependent costs.[^2] The output preserves modeled covariance approximately and discards residual detail when only scores are retained. A posterior variance quantifies uncertainty under the model; misspecification can leave it overconfident.

## Evidence

[^1]: Official project maintainers (2026). [Decomposing signals in components](https://scikit-learn.org/stable/modules/decomposition.html). See [access record](SOURCES.md#sk_decomp).
[^2]: Deisenroth MP; Faisal AA; Ong CS (2020). [Mathematics for Machine Learning](https://mml-book.github.io/). See [access record](SOURCES.md#mml).

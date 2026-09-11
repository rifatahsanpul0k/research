# scVI

Phase 2C · method study · studied_not_fitted · not_reproduced.

**FACT:** scVI (Lopez et al., 2018) models single-cell RNA counts with a variational encoder and count decoder, accounting for depth and batch. Its latent observation representation supports later clustering and visualization; its generative model also supports differential-expression queries. These are distinct capabilities.[^1]

## Generative and inference objects

Let \(X\in\mathbb N_0^{n\times G}\), \(s_i\in\{0,1\}^B\) a one-hot batch vector, \(z_i\in\mathbb R^d\), and \(\ell_i>0\) RNA depth. A compact version is
\[
z_i\sim N(0,I_d),\quad
\ell_i\sim\operatorname{LogNormal}(a_{s_i},b_{s_i}^2),\quad
\rho_i=f_\theta(z_i,s_i)\in\Delta^{G-1},\quad
x_{ig}\sim\operatorname{NB}(\ell_i\rho_{ig},\theta_g),
\]
with a ZINB alternative adding gene-wise zero-inflation probabilities. \(\Delta^{G-1}\) means nonnegative \(G\)-vectors summing to one, \(\theta_g>0\) is inverse dispersion, and \(a,b^2\) are batch-specific log-depth prior parameters. The original paper uses a zero-inflated generative construction. Current documentation also describes NB alternatives and an observed-library-size option; do not conflate a paper model with a software default.[^1][^2]

A neural encoder approximates \(q_\phi(z_i,\ell_i\mid x_i,s_i)\). Training jointly estimates encoder, decoder and distribution parameters by stochastic variational optimization. The standard fitting does not infer a posterior over every network weight. Extracting posterior means gives \(Z\in\mathbb R^{n\times d}\); drawing samples retains model-conditional latent variation. \(\rho_i\in\mathbb R^G\) is a decoded expression quantity, not the embedding.[^2]

## Biological interpretation and limits

**Project interpretation:** sharing fitted parameters across observations allows statistical information sharing, but does not establish that rows are independent donors or equivalent cells. The decoder's batch input permits different observation distributions at a common latent state. That mechanism alone cannot identify which batch-associated variation is technical when stage and batch are confounded.

A gene-expression contrast asks about decoded distributions between specified groups under stated batch handling. It is not the difference between two latent coordinates. Posterior probabilities/Bayes factors or model-derived DE summaries require their own interpretation; they do not replace biological replication or establish regulation.

A hypothetical decoder with \(\ell=100,\rho=(0.2,0.8)\) predicts means \((20,80)\). Doubling \(\ell\) doubles these means while keeping relative expression fixed. If total RNA changes biologically, deciding which quantity to compare matters. The existing project matrix scale and observation-unit uncertainties therefore remain prerequisites, not automatically solved by scVI.

Official implementation is now maintained in [scvi-tools](https://github.com/scverse/scvi-tools); the original publication links YosefLab/scVI. Code identity is verified, no environment prepared or model run.[^1][^2]

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | RNA encoder and NB/ZINB decoder; separate depth and batch inputs |
| Training objective | ELBO with count likelihood and latent KL |
| Biological prior | Count sampling and low-dimensional structure; no regulatory graph required |
| Downstream model | Z-based clustering/classification; model-based DE is a separate query |
| Evaluation | Predictive fit, DE assumptions and biological validation; not run |

## Evidence

[^1]: [SCVI: original source and access notes](SOURCES.md#scvi).
[^2]: [SCVI_DOC: original source and access notes](SOURCES.md#scvi_doc).


# Count-aware likelihoods

Phase 2C · method study · studied_not_fitted · not_reproduced.

For a nonnegative integer count \(x\), Poisson with mean \(\mu>0\) has variance \(\mu\). A negative binomial parameterized by mean \(\mu\) and inverse dispersion \(\theta>0\) has variance \(\mu+\mu^2/\theta\):
\[
p(x\mid\mu,\theta)=
\frac{\Gamma(x+\theta)}{\Gamma(\theta)\Gamma(x+1)}
\left(\frac{\theta}{\theta+\mu}\right)^\theta
\left(\frac{\mu}{\theta+\mu}\right)^x.
\]
Here \(\Gamma\) extends the factorial, and \(x,\mu,\theta\) are feature/observation-level scalars. DCA and scVI illustrate neural parameterizations of these count models.[^1][^2]

Define zero-inflation probability \(\pi\in[0,1]\) explicitly:
\(p_{\rm ZINB}(0)=\pi+(1-\pi)p_{\rm NB}(0)\);
\(p_{\rm ZINB}(x>0)=(1-\pi)p_{\rm NB}(x)\).
An NB already generates zeros. Extra zero inflation is a hypothesis about the distribution, not a conclusion from sparsity. Technical controls show that droplet UMI data can be consistent with sampling models without an added zero-inflation component.[^3]

Synthetic calculation: \(\mu=2,\theta=2\) gives variance \(4\) and \(p_{\rm NB}(0)=(2/4)^2=1/4\). With \(\pi=0.2\), \(p(0)=0.2+0.8(0.25)=0.4\). No particular observed zero is classified as biologically absent by this arithmetic.

A decoder might set \(\mu_{ig}=\ell_i\rho_{ig}\), with depth \(\ell_i>0\) and proportions \(\rho_i\) summing to one. Library scaling enters the likelihood rather than requiring a Gaussian error on logged values.[^2]

**Project interpretation:** a floating-point storage type does not establish raw-count status. Our prior preprocessing records retain uncertainty about matrix scale. A count likelihood requires verified count provenance, not rounding an already transformed matrix. A missing modality requires an observation mask and absent likelihood contribution; it is not an all-zero measured panel.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | VAE or deterministic AE with count-parameter decoder |
| Training objective | Count negative log likelihood, plus KL only for a VAE |
| Biological prior | Assay-motivated count support/dispersion/depth assumptions |
| Downstream model | Embedding tasks or explicitly defined predictive quantities |
| Evaluation | Distributional fit and biological validity; neither tested here |

## Evidence

[^1]: [DCA: original source and access notes](SOURCES.md#dca).
[^2]: [SCVI: original source and access notes](SOURCES.md#scvi).
[^3]: [UMI_ZERO: original source and access notes](SOURCES.md#umi_zero).


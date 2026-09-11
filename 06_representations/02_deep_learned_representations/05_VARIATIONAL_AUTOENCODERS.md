# Variational autoencoders

Phase 2C · method study · studied_not_fitted · not_reproduced.

A VAE combines a probabilistic generative model \(p_\theta(x,z)=p(z)p_\theta(x\mid z)\) with an approximate posterior \(q_\phi(z\mid x)\). Take \(x\in\mathbb R^p\) (or discrete counts) and \(z\in\mathbb R^d\). The encoder outputs distribution parameters; the decoder outputs likelihood parameters, not necessarily a single reconstruction. A usual prior is \(p(z)=\mathcal N(0,I_d)\).[^1]

## Bound and optimization

For any normalized \(q\) whose support permits these expectations,
\[
\begin{aligned}
\log p_\theta(x)
&=\log \int q_\phi(z\mid x)
 \frac{p_\theta(x,z)}{q_\phi(z\mid x)}\,dz\\
&\ge \mathbb E_q[\log p_\theta(x,z)-\log q_\phi(z\mid x)]\\
&=\underbrace{\mathbb E_q[\log p_\theta(x\mid z)]
-D_{\rm KL}(q_\phi(z\mid x)\|p(z))}_{\mathcal L_{\rm ELBO}}.
\end{aligned}
\]
The inequality uses concavity of log (Jensen). Equivalently,
\(\log p_\theta(x)-\mathcal L_{\rm ELBO}
=D_{\rm KL}(q_\phi(z\mid x)\|p_\theta(z\mid x))\ge0\).
**Maximize** the ELBO or minimize its negative. The prior KL and the posterior approximation gap are different divergences. Reconstruction likelihood is not necessarily MSE.[^1]

For a diagonal Gaussian encoder,
\[
q_\phi=\mathcal N(\mu_\phi(x),\operatorname{diag}(e^{v_\phi(x)})),
\quad \mu,v\in\mathbb R^d,\quad
z=\mu+e^{v/2}\odot\epsilon,\quad\epsilon\sim\mathcal N(0,I_d).
\]
Here \(v\) is **log variance**, so standard deviation is \(e^{v/2}\), not \(e^v\). The sampling transformation allows gradients through \(\mu,v\) while drawing parameter-independent \(\epsilon\). With this prior,
\[
D_{\rm KL}=\tfrac12\sum_{k=1}^d
(\mu_k^2+e^{v_k}-1-v_k).
\]
All terms are scalars after summation. A minibatch objective averages observations; Monte Carlo samples approximate the expected log likelihood.[^1]

## Original teaching derivations and limits

If one dimension has \(\mu=0,v=0\), its KL is zero. If \(\mu=1,v=0\), KL is \(1/2\). Moving the mean away from the prior has a cost even before reconstruction is considered. In the [toy](TOY_DEEP_REPRESENTATIONS.md), a full two-dimensional example distinguishes the posterior mean from a sample.

For a Gaussian decoder with fixed variance \(s^2\),
\(-\log p(x\mid z)=\|x-m_\theta(z)\|^2/(2s^2)+(p/2)\log(2\pi s^2)\).
Only with fixed \(s^2\) and a consistent reduction is optimizing this likelihood equivalent to squared-error reconstruction. Learning variance changes the objective.

Posterior variance describes uncertainty **under the fitted model**. A point estimate \(\theta\) does not integrate uncertainty in its own learned weights. Sampling \(z\) is not evidence of calibrated epistemic uncertainty. Prior sampling generates synthetic \(x\); posterior sampling conditions on a specific observation. Neither generates new experimental evidence.[^2]

**Project interpretation:** low-dimensional uncertainty cannot repair unknown assay units, donor structure, or spot mixtures. A strong decoder may ignore \(z\), producing posterior collapse; a high-dimensional encoder may retain unwanted variation. No coordinate is automatically a cell type, pathway or regulator. The next note connects the likelihood to data support.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Encoder q_phi and likelihood decoder p_theta with a prior |
| Training objective | ELBO, expected reconstruction log likelihood minus prior KL |
| Biological prior | Distributional/conditional-independence assumptions; no biological semantics inherent |
| Downstream model | Separate tasks on posterior mean/samples or posterior predictive quantities |
| Evaluation | Predictive adequacy, calibration and biological checks are distinct |

## Evidence

[^1]: [AEVB: original source and access notes](SOURCES.md#aevb).
[^2]: [UNCERTAINTY: original source and access notes](SOURCES.md#uncertainty).


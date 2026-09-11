# 09. Important distributions

Let $T$ be a random variable, $t$ its realized value, $\pi$ a success probability, $m$ a fixed trial count, $\lambda$ a positive rate, $\mu$ a mean, and $\sigma^2$ a positive Gaussian variance. Probability mass functions (PMFs) apply to discrete values; densities apply to continuous ones. These are candidate measurement models, not proven descriptions of our assays. [Probability](SOURCES.md#probability)

| Family | Support and formula | Mean; variance | Possible modeling use and assumption |
|---|---|---|---|
| Bernoulli($\pi$) | $t\in\{0,1\}$; $\pi^t(1-\pi)^{1-t}$ | $\pi$; $\pi(1-\pi)$ | Detection flag; detection differs from biological presence |
| Binomial($m,\pi$) | $0,\ldots,m$; $\binom mt\pi^t(1-\pi)^{m-t}$ | $m\pi$; $m\pi(1-\pi)$ | Successes in fixed independent trials with common probability |
| Poisson($\lambda$) | $t=0,1,\ldots$; $e^{-\lambda}\lambda^t/t!$ | $\lambda$; $\lambda$ | Idealized count sampling at fixed rate |
| Negative binomial($\mu,\kappa$) | $t\ge0$ integer; formula below | $\mu$; $\mu+\mu^2/\kappa$ | Overdispersed counts; $\kappa>0$ is inverse dispersion |
| Gaussian($\mu,\sigma^2$) | $t\in\mathbb R$; $\frac1{\sqrt{2\pi\sigma^2}}e^{-(t-\mu)^2/(2\sigma^2)}$ | $\mu$; $\sigma^2$ | Continuous errors or transformed values; allows negatives |
| Multinomial($m,\boldsymbol\pi$) | $\boldsymbol t\in\mathbb N_0^p$, $\sum_jt_j=m$; $\frac{m!}{\prod_jt_j!}\prod_j\pi_j^{t_j}$ | $E[T_j]=m\pi_j$; $\operatorname{Var}(T_j)=m\pi_j(1-\pi_j)$ | Category counts at fixed total, $\sum_j\pi_j=1$ |

For the mean/inverse-dispersion NB convention,
$$
P(T=t)=\frac{\Gamma(t+\kappa)}{\Gamma(\kappa)t!}
\left(\frac{\kappa}{\kappa+\mu}\right)^\kappa
\left(\frac{\mu}{\kappa+\mu}\right)^t .
$$
$\Gamma$ extends factorials with $\Gamma(t+1)=t!$ for nonnegative integers. As $\kappa\to\infty$ at fixed $\mu$, NB approaches Poisson. For $\mu=2,\kappa=2$, variance is 4 versus Poisson's 2. Other texts parameterize NB as failures before a fixed number of successes; state the convention.

Multinomial components are not independent: for $j\ne k$, covariance is $-m\pi_j\pi_k$ due to the fixed total. This helps explain how compositional constraints can create negative associations without biological inhibition. A Poisson mixture with varying rate can also have overdispersion.

RNA count models may use NB to address depth and extra-Poisson variability, but protocol, covariates and residual checks matter. [Hafemeister–Satija](SOURCES.md#bio) Integer-looking float32 values alone cannot prove UMI counts. ATAC binarization and ADT background demand their own observation assumptions; no family is selected or fitted.

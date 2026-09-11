# 11. Bayesian foundations

Bayes' rule updates uncertainty over parameter $\theta$ after observations $X$:
$$
p(\theta\mid X)=\frac{p(X\mid\theta)p(\theta)}{p(X)},\qquad
p(X)=\int p(X\mid\theta)p(\theta)\,d\theta .
$$
Use a sum for a discrete parameter. The prior $p(\theta)$ describes pre-data assumptions; likelihood connects parameters to observations; posterior describes conditional uncertainty. Evidence $p(X)$ normalizes the posterior. Density notation is used for continuous parameters. [Probability](SOURCES.md#probability), [MML, probability and distributions](SOURCES.md#mml)

For Bernoulli data $(1,1,0)$, use a uniform prior on $[0,1]$, also Beta(1,1). The posterior is proportional to $\theta^2(1-\theta)$:
$$
\int_0^1(\theta^2-\theta^3)\,d\theta=1/3-1/4=1/12,
\qquad p(\theta\mid X)=12\theta^2(1-\theta).
$$
This is Beta(3,2). The posterior mean is $3/(3+2)=0.6$, mode $2/3$, and variance $3\cdot2/(5^2\cdot6)=0.04$. Mean and mode answer different questions. The result is a distribution, not a guaranteed true probability.

A posterior predictive distribution integrates over parameter uncertainty: $p(x_{\rm new}\mid X)=\int p(x_{\rm new}\mid\theta)p(\theta\mid X)d\theta$, with $x_{\rm new}$ a future observation. A credible interval summarizes posterior mass; it differs in interpretation from a frequentist confidence interval.

Future probabilistic representations can place distributions over latent coordinates or loadings. These express uncertainty under their model and prior, not direct measurement of a biological mechanism. Prior sensitivity, unmodeled batch effects and identifiability remain concerns. No specific VAE or research model is studied here.

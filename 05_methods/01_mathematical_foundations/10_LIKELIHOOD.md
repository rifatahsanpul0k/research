# 10. Likelihood

A model specifies a distribution $p_\theta$ indexed by parameter $\theta$ (or a parameter vector). Data are observed; parameters are the unknown values within that model. Likelihood treats the observed data as fixed and varies $\theta$:
$$
L(\theta\mid X)=p_\theta(X),\qquad \ell(\theta)=\log L(\theta\mid X).
$$
For continuous data this is a density, not the probability of observing an exact point. Likelihood is not a distribution over parameters and need not integrate to one over $\theta$. [Statistical estimation, Convex Optimization §7.1](SOURCES.md#convex)

Toy independent Bernoulli observations are $(1,1,0)$, with success probability $\theta\in[0,1]$. The ordered sample has
$$
L(\theta)=\theta^2(1-\theta),\quad
\ell(\theta)=2\log\theta+\log(1-\theta).
$$
For $0<\theta<1$,
$$
\ell'(\theta)=2/\theta-1/(1-\theta)=0
\ \Rightarrow\ 2(1-\theta)=\theta
\ \Rightarrow\ \hat\theta=2/3.
$$
The second derivative $-2/\theta^2-1/(1-\theta)^2$ is negative, confirming a maximum. If the data were only the count “2 successes out of 3,” the likelihood includes $\binom32=3$; this constant does not change the maximizer. Maximum likelihood estimation is choosing a maximizer, not proving the model correct.

A future RNA likelihood could condition on depth and latent state. Its factorization into independent terms is an assumption requiring review for paired measurements and shared specimens. Large likelihoods across different units or transformed supports are not automatically comparable. Here only a three-value teaching example is solved.

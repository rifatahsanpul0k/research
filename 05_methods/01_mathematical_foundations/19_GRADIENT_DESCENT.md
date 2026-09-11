# 19. Gradient descent

For differentiable objective $\mathcal L$ and parameter $\theta_t\in\mathbb R^d$ at iteration $t$, gradient descent updates
$$
\theta_{t+1}=\theta_t-\eta\nabla\mathcal L(\theta_t),
$$
where $\eta>0$ is the learning rate. Compute the gradient at the current point, multiply by the step size, subtract, and reevaluate. [Convex Optimization, chapter 9](SOURCES.md#convex)

Toy $\mathcal L(\theta)=(\theta-3)^2$, $\theta_0=1$, $\eta=0.1$:
1. Gradient $2(1-3)=-4$.
2. Update $\theta_1=1-0.1(-4)=1.4$.
3. Loss changes from 4 to $(1.4-3)^2=2.56$.
4. Next gradient is $-3.2$, giving $\theta_2=1.72$ and loss 1.6384.

Let error $e_t=\theta_t-3$. Here $e_{t+1}=(1-2\eta)e_t$, so convergence requires $|1-2\eta|<1$, equivalently $0<\eta<1$. At $\eta=1$ the error oscillates without shrinking; at $\eta>1$ it grows. This bound is specific to this quadratic and its units, not a recommended research learning rate.

Gradient descent can be slow, unstable, or converge to a local solution depending on objective and step rule. A full-data gradient differs from a stochastic estimate, but advanced optimizers are deferred. If constraints are present, an unconstrained step can leave the feasible set.

Parameter units, feature scaling and objective scaling affect gradient magnitudes. A successful toy update is arithmetic validation, not model training, convergence evidence for a research model or biological validation.

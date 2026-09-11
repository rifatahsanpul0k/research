# 18. Derivatives and gradients

The derivative $f'(t)=df/dt$ is the limit $\lim_{h\to0}[f(t+h)-f(t)]/h$, when it exists. Here $t$ is a scalar input and $h$ a nonzero increment. It describes local change, not a finite biological effect or causal response. [VMLS, Taylor approximation](SOURCES.md#vmls), [Convex Optimization](SOURCES.md#convex)

For $f(t)=(t-3)^2$ at $t=1$:
$$
f(1)=4,\quad f(1+h)=4-4h+h^2,\quad
\frac{f(1+h)-f(1)}h=-4+h\to-4.
$$
At $h=0.01$, the forward difference is $-3.99$, approximating $f'(1)=-4$. Smaller numerical steps are not always better in finite precision because subtraction can lose precision.

For $\theta=(\theta_1,\ldots,\theta_d)^\top\in\mathbb R^d$, the gradient is $\nabla_\theta\mathcal L=(\partial\mathcal L/\partial\theta_1,\ldots,\partial\mathcal L/\partial\theta_d)^\top\in\mathbb R^d$. The first-order expansion is $\mathcal L(\theta+\Delta)\approx\mathcal L(\theta)+\nabla\mathcal L(\theta)^\top\Delta$, with $\Delta\in\mathbb R^d$.

In Euclidean coordinates, the gradient points in the steepest local ascent direction among unit steps; its negative points toward descent. Other norms give other steepest directions. For $\mathcal L(a,b)=(a-3)^2+2b^2$, gradient is $(2(a-3),4b)^\top$; at $(1,1)$ it is $(-4,4)^\top$.

The chain rule connects composite maps: if $z=W\theta$ with $W\in\mathbb R^{k\times d}$ and loss $g(z)$, then $\nabla_\theta g(W\theta)=W^\top\nabla_zg(z)$. A zero gradient may describe a minimum, maximum or saddle. L1 penalties are nondifferentiable at zero and need a suitable generalized derivative or algorithm.

# 20. Regularization

For a data-fit objective $\mathcal L_{\rm data}(\theta)$, regularization minimizes $\mathcal L_{\rm data}(\theta)+\lambda R(\theta)$ with $\lambda\ge0$ controlling the penalty weight. L1 uses $R=\|\theta\|_1=\sum_j|\theta_j|$; L2 uses $R=\|\theta\|_2^2=\sum_j\theta_j^2$. The convention on factors such as $1/2$ changes the numerical interpretation of $\lambda$. [Convex Optimization, §6.3](SOURCES.md#convex)

In one coordinate, fit target $a\in\mathbb R$ with $\tfrac12(\theta-a)^2$.
- L2 objective $\tfrac12(\theta-a)^2+\lambda\theta^2$ has derivative $(1+2\lambda)\theta-a$, so $\theta^*=a/(1+2\lambda)$.
- L1 objective $\tfrac12(\theta-a)^2+\lambda|\theta|$ gives $\theta^*=\operatorname{sign}(a)\max(|a|-\lambda,0)$.

For $a=3,\lambda=1$, L2 gives 1 and L1 gives 2; for $a=0.5,\lambda=1$, L1 gives exactly 0 while L2 gives $1/6$. Exact L1 zeros arise from the corner at zero; L2 typically shrinks without exact zeros. These are scalar demonstrations, not general sparsity guarantees for arbitrary nonconvex objectives.

In high-dimensional omics, many coefficient settings may fit the same observations. Regularization can control instability and overfitting by favoring smaller or sparser parameters, at the cost of bias. It does not make the preferred solution a biological mechanism. Correlated features can make the selected subset unstable.

Scale features and define which parameters are penalized before interpreting the penalty; an intercept need not be penalized. A penalty on model weights differs from sparsity in the input count matrix. Later selection of $\lambda$ must respect validation boundaries. No research value is chosen here.

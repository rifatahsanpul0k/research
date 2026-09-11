# 22. Geometry in high dimension

Distance concentration and near-orthogonality are conditional results about distributions, not universal rules for omics. As an illustrative model, take independent random vectors $u,v\sim N(0,I_p)$, where $I_p$ is identity and each coordinate is independent standard Gaussian. Then $u-v\sim N(0,2I_p)$:
$$
E[\|u-v\|_2^2]=2p,\qquad
\operatorname{Var}(\|u-v\|_2^2)=8p.
$$
The coefficient of variation of squared distance is $\sqrt{8p}/(2p)=\sqrt{2/p}$, shrinking as $p$ increases. Absolute distances grow while relative fluctuations shrink. This is not a proof that all distances are equal or that maximum/minimum ratios concentrate for any growing sample size. [BHK, chapter 2](SOURCES.md#bhk)

For independent uniform unit directions $a,b$ on the sphere in $\mathbb R^p$, $E[a^\top b]=0$ and $\operatorname{Var}(a^\top b)=1/p$. For $\epsilon>0$, Chebyshev gives $P(|a^\top b|\ge\epsilon)\le1/(p\epsilon^2)$. Random directions tend toward right angles under these assumptions. Nonnegative sparse RNA/ATAC vectors with shared depth and correlated features do not meet that model directly.

Boundary intuition also changes. In the unit ball, the fraction of volume inside radius $1-\epsilon$ is $(1-\epsilon)^p$ for $0<\epsilon<1$. With $\epsilon=0.1$, this is $0.9^2=0.81$ in 2D but about $0.00515$ in 50D. Most volume can sit near the outer shell.

A neighborhood's reliability depends on signal, noise and effective dimension. Local geometry can remain useful even when global distances are affected by batch or composition. No distance concentration is claimed to have been measured in our datasets, and no nearest-neighbor structure is built.

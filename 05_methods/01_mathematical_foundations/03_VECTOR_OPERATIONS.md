# 03. Vector operations

Let $x,y\in\mathbb R^p$ and $a\in\mathbb R$. Addition $(x+y)_j=x_j+y_j$ and scalar multiplication $(ax)_j=ax_j$ preserve the number of coordinates, not generally the norm. The dot product $x^\top y=\sum_{j=1}^p x_jy_j$ is a scalar: $(1\times p)(p\times1)$. Element-wise multiplication $x\odot y$ is a $p$-vector. It is not a dot product or matrix multiplication. [VMLS](SOURCES.md#vmls)

For $x=(2,1,0)^\top$, $y=(3,0,1)^\top$:
- $x+y=(5,1,1)^\top$; $2x=(4,2,0)^\top$.
- $x^\top y=2\cdot3+1\cdot0+0\cdot1=6$.
- $x\odot y=(6,0,0)^\top$.

A norm measures vector size. $\|x\|_1=\sum_j|x_j|=3$; $\|x\|_2=(\sum_jx_j^2)^{1/2}=\sqrt5$. A norm is nonnegative, zero only for the zero vector, absolutely homogeneous, and satisfies the triangle inequality. $\|x\|_1$ equals library size only for nonnegative entries on a suitable count scale. It is not library size after centering.

Distances are norms of differences. L1 accumulates absolute changes; L2 weights large differences more strongly through squares. For differences $(3,0)$ and $(2,2)$, L1 prefers the first (3 versus 4) while L2 prefers the second (3 versus $\sqrt8$). Thus a nearest observation can change with the norm. Later L1/L2 penalties also prefer different parameter structures; see [regularization](20_REGULARIZATION.md).

Adding aligned count vectors produces an aggregate assay vector, not a new measured cell. Multiplication across RNA and ADT requires compatible feature definitions, not just matching vector lengths. Units multiply in a dot product unless values are made dimensionless.

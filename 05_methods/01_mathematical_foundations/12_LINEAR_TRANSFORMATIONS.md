# 12. Linear and affine transformations

For $x\in\mathbb R^p$ and $W\in\mathbb R^{k\times p}$, $z=Wx\in\mathbb R^k$ has entry $z_a=\sum_{j=1}^pW_{aj}x_j$, with output index $a=1,\ldots,k$. Adding $b\in\mathbb R^k$ gives $z=Wx+b$, an **affine** map; it is linear only if $b=0$. A linear map preserves addition and scalar multiplication. [VMLS](SOURCES.md#vmls)

Take
$$
W=\begin{bmatrix}1&0&1\\0&2&0\end{bmatrix}_{2\times3},
\quad x=\begin{bmatrix}2\\1\\0\end{bmatrix}_{3\times1},
\quad b=\begin{bmatrix}1\\-1\end{bmatrix}_{2\times1}.
$$
Then $Wx=(2,2)^\top$ and $Wx+b=(3,1)^\top$. For all observations, $Z=XW^\top+\mathbf1_nb^\top$ has shape $(n\times p)(p\times k)+(n\times1)(1\times k)=n\times k$.

| Map | Matrix and behavior |
|---|---|
| Scaling | $D=\operatorname{diag}(2,1)$ doubles the first coordinate |
| Rotation | $R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ sends $(1,0)^\top$ to $(0,1)^\top$ and preserves Euclidean distance |
| Orthogonal projection | $P=\operatorname{diag}(1,0)$ keeps the first axis; $P^2=P=P^\top$ |
| Change of basis | With invertible $B\in\mathbb R^{p\times p}$ whose columns are basis vectors, coordinates $c=B^{-1}x$ reconstruct $x=Bc$ |

A general dimension-reducing $W$ is not necessarily an orthogonal projection. A change of basis is invertible; a map with $k<p$ cannot be injective on all of $\mathbb R^p$. Rotation and orthonormal basis changes preserve Euclidean geometry; arbitrary scaling does not.

Weighted molecular features become constructed quantities, with units and meaning inherited from the weights. They do not automatically become measured pathways. No projection is fitted to real observations.

# 02. Scalars, vectors, matrices and tensors

A scalar is one number, such as one stored RNA value $x_{ij}=2$. A vector is an ordered list, such as one observation's $p$ features or one gene's values across $n$ observations. A matrix is a two-axis array; order matters, because position $j$ must keep its feature identity. Dimensions specify each axis length: $X\in\mathbb R^{n\times p}$. For the synthetic matrix in [toy calculations](TOY_CALCULATIONS.md), $n=4,p=3$, $x_{12}=1$, the first row is $(2,1,0)$, and the first column is $(2,3,8,9)^\top$. [VMLS](SOURCES.md#vmls)

An order-three tensor is an array $T\in\mathbb R^{a\times b\times c}$ with three indices. An illustrative gene-by-region-by-time tensor would have $a$ genes, $b$ defined regions and $c$ time points. Our specimens do not automatically form that tensor: missing combinations, unmatched regions and repeated specimens must be represented explicitly. Tensor order (number of axes) differs from matrix rank. No tensor is constructed here.

| Operation/object | Definition and dimensions | Omics meaning |
|---|---|---|
| Transpose | $(X^\top)_{ji}=x_{ij}$; $p\times n$ | Exchanges observation and feature axes without changing measurements |
| Identity | $I_p$ has ones on its diagonal, zeros elsewhere; $p\times p$ | $XI_p=X$ |
| Diagonal | $D=\operatorname{diag}(d_1,\ldots,d_p)$; $p\times p$ | $XD$ scales feature $j$ by $d_j$ |
| Symmetric | $A=A^\top$; square $p\times p$ | Covariance is symmetric |
| Sparse | Most entries are zero; stored compactly | CSR storage does not alter mathematical shape |

Transposition is not feature alignment. Equal shapes do not imply matching identifiers. In particular, $X^\top X$ is $p\times p$, whereas $XX^\top$ is $n\times n$; the first relates features, the second observations. A sparse input can have a dense product, so mathematical validity and memory feasibility are separate checks.

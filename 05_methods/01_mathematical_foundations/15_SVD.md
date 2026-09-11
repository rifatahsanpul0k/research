# 15. Singular value decomposition

For any real $X\in\mathbb R^{n\times p}$, singular value decomposition writes $X=UDV^\top$. $D$ is also conventionally written $\Sigma$; here $D$ prevents confusion with covariance. Singular values $d_1\ge\cdots\ge d_h\ge0$, where $h=\min(n,p)$, lie on its diagonal. [BHK, chapter 3](SOURCES.md#bhk)

| Form | $U$ | $D$ (or $\Sigma$) | $V$ | $V^\top$ |
|---|---|---|---|---|
| Full | $n\times n$ | $n\times p$ | $p\times p$ | $p\times p$ |
| Reduced/thin | $n\times h$ | $h\times h$ | $p\times h$ | $h\times p$ |
| Compact, rank $\rho$ | $n\times\rho$ | $\rho\times\rho$ | $p\times\rho$ | $\rho\times p$ |

Full $U,V$ are orthogonal square matrices; thin/compact factors have orthonormal columns. Reduced SVD can retain zero singular values; compact SVD keeps only nonzero ones. The distinction matters for rank-deficient data. Matrix products in every row above reconstruct $n\times p$.

For right singular direction $v_a\in\mathbb R^p$ and left direction $u_a\in\mathbb R^n$, $Xv_a=d_au_a$. Thus $V$ describes feature directions and $UD$ observation scores. Singular values are square roots of eigenvalues of $X^\top X$, whereas covariance eigenvalues from centered data are $d_a^2/(n-1)$. Centering must be explicit; uncentered SVD also captures the mean signal.

The hand-checkable $2\times3$ example in [toy calculations](TOY_CALCULATIONS.md) reconstructs from two rank-one components. Truncating to $k<\rho$ gives $X_k=U_kD_kV_k^\top$. Retained scores have shape $n\times k$.

PCA later uses centered data and variance directions; LSI uses an accessibility-specific transformed matrix before SVD. Generic factorization need not impose orthogonality or use the same loss. This note makes those mathematical connections only. Signs and bases within repeated singular values are nonunique; they cannot be interpreted as unique biological axes.

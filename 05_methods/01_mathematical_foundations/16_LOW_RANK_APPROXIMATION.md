# 16. Low-rank approximation

For the SVD $X=UDV^\top$ and chosen integer $0\le k<\rho=\operatorname{rank}(X)$, the truncation
$$
X_k=U_kD_kV_k^\top,\quad
U_k:n\times k,\ D_k:k\times k,\ V_k:p\times k
$$
minimizes Frobenius reconstruction error over all rank-at-most-$k$ matrices. The Frobenius norm is $\|A\|_F=(\sum_{ij}a_{ij}^2)^{1/2}$. The minimum squared error is $\|X-X_k\|_F^2=\sum_{a>k}d_a^2$; operator-norm error is $d_{k+1}$. Here $d_a$ denotes singular value $a$, and the operator norm is $\|A\|_{\mathrm{op}}=\max_{\|v\|_2=1}\|Av\|_2$, with $v$ having as many entries as $A$ has columns. Repeated singular values at the cutoff can yield multiple minimizers. [BHK, chapter 3](SOURCES.md#bhk)

Scores $Z=U_kD_k\in\mathbb R^{n\times k}$ with loadings $V_k$ store roughly $k(n+p)$ numbers versus $np$. This is compression only if that storage, plus required metadata, is smaller. A low rank does not guarantee a sparse score matrix.

**Which biological information might be lost when low-variance directions are discarded?** A rare population's marker, a localized spatial boundary or a weak perturbation response may contribute little pooled variance yet answer the biological question. Consider a synthetic binary marker present in fraction $\pi$ of observations: variance is $\pi(1-\pi)$, which is small for small $\pi$ despite perfect marking of that subgroup. This derivation shows why variance alone cannot define biological importance. Measurement noise can also have high variance. [Measurement context](SOURCES.md#bio)

For $\operatorname{diag}(3,1)$ embedded in a $2\times3$ matrix, rank-one truncation discards the second coordinate entirely; error squared is 1. Whether that coordinate encodes nuisance or a rare biological distinction cannot be decided by the theorem.

The theorem optimizes one numerical loss on one scale. It makes no claim about annotation agreement, ancestry, tissue boundaries or generalization. No real-data rank or cutoff is selected.

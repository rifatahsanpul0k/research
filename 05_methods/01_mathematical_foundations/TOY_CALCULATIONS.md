# Phase 2A toy calculations

Everything here is synthetic. No row is a project cell or spot, and the assigned groups are teaching labels. Natural logs are used except where bits are explicitly stated. Sample variance uses denominator $n-1$; empirical population variance uses $n$. Each numbered topic defines its remaining symbols.

Use
$$
X=\begin{bmatrix}
2&1&0\\3&0&1\\8&7&6\\9&8&5
\end{bmatrix}\in\mathbb R^{4\times3},
$$
with rows $x_i^\top$, $i=1,\ldots,4$, and feature columns $j=1,2,3$. Verification code is [check_phase2a_toys.py](../../code/data_inspection/check_phase2a_toys.py); it checks arithmetic and edge cases using synthetic inputs only.

## 1. Means and centering

Column sums are $(2+3+8+9,\ 1+0+7+8,\ 0+1+6+5)=(22,16,12)$. Divide by $n=4$:
$$
\mu=(5.5,4,3)^\top,\qquad
X_c=X-\mathbf1_4\mu^\top=
\begin{bmatrix}
-3.5&-3&-3\\-2.5&-4&-2\\2.5&3&3\\3.5&4&2
\end{bmatrix}.
$$
$\mathbf1_4\mu^\top$ has shape $(4\times1)(1\times3)=4\times3$. Every centered column sums to zero.

## 2. Variance and covariance

Centered column squared sums are:
$$
12.25+6.25+6.25+12.25=37,\quad
9+16+9+16=50,\quad
9+4+9+4=26.
$$
Sample variances are $(37/3,50/3,26/3)$; population moments would be $(37/4,50/4,26/4)$. Sample standard deviations are their positive square roots.

Cross-products:
$$
X_{c,1}^\top X_{c,2}=10.5+10+7.5+14=42,
$$
$$
X_{c,1}^\top X_{c,3}=10.5+5+7.5+7=30,
$$
$$
X_{c,2}^\top X_{c,3}=9+8+9+8=34.
$$
Here $X_{c,j}$ denotes centered column $j$. Thus
$$
\widehat\Sigma=\frac{X_c^\top X_c}{3}
=\frac13\begin{bmatrix}37&42&30\\42&50&34\\30&34&26\end{bmatrix}.
$$
The first-two-feature Pearson correlation is $42/\sqrt{37\cdot50}\approx0.976480$. It says nothing about whether either synthetic feature regulates the other.

## 3. Distances and norms

$x_1-x_2=(-1,1,-1)^\top$. Therefore $d_2(1,2)=\sqrt{1+1+1}=\sqrt3\approx1.732051$ and $d_1(1,2)=1+1+1=3$. Also $\|x_1\|_1=3$, $\|x_1\|_2=\sqrt5$.

The squared-distance table, obtained by summing three squared coordinate differences, is
$$
D^{(2)}=\begin{bmatrix}
0&3&108&123\\3&0&99&116\\108&99&0&3\\123&116&3&0
\end{bmatrix}.
$$
For example, $x_1-x_3=(-6,-6,-6)$ gives $36+36+36=108$; $x_2-x_4=(-6,-8,-4)$ gives $36+64+16=116$. Euclidean distances take square roots entrywise; superscript $(2)$ denotes squared distance here, not matrix multiplication.

## 4. Cosine and profile correlation

$x_1^\top x_2=2\cdot3+1\cdot0+0\cdot1=6$, $\|x_1\|_2=\sqrt5$, $\|x_2\|_2=\sqrt{10}$:
$$
\cos(x_1,x_2)=6/\sqrt{50}\approx0.848528.
$$
For profile Pearson, mean of $x_1$ across features is 1, mean of $x_2$ is $4/3$. Centered profiles are $(1,0,-1)$ and $(5/3,-4/3,-1/3)$; dot product is 2 and squared norms are 2 and $14/3$. Therefore
$$
\rho(x_1,x_2)=2/\sqrt{28/3}=3/\sqrt{21}\approx0.654654.
$$
This differs from feature correlation in section 2 because the axes differ. Cosine with zero vector and Pearson with constant vector are undefined.

## 5. Standardization

Define $Z_{ij}=(x_{ij}-\mu_j)/s_j$ using sample standard deviations:
$$
Z=\begin{bmatrix}
-3.5/\sqrt{37/3}&-3/\sqrt{50/3}&-3/\sqrt{26/3}\\
-2.5/\sqrt{37/3}&-4/\sqrt{50/3}&-2/\sqrt{26/3}\\
2.5/\sqrt{37/3}&3/\sqrt{50/3}&3/\sqrt{26/3}\\
3.5/\sqrt{37/3}&4/\sqrt{50/3}&2/\sqrt{26/3}
\end{bmatrix}.
$$
First row is approximately $(-0.996616,-0.734847,-1.019049)$. Each column has mean zero and sample variance one. Original zero $x_{13}=0$ becomes about $-1.019049$: centering does not preserve sparse zeros. $Z$ specifically means standardized values in this section.

## 6. Matrix multiplication and affine maps

Let $W=\begin{bmatrix}1&0&1\\0&2&0\end{bmatrix}\in\mathbb R^{2\times3}$. Each output row contains feature 1 plus feature 3, and twice feature 2:
$$
XW^\top=
\begin{bmatrix}2+0&2\cdot1\\3+1&2\cdot0\\8+6&2\cdot7\\9+5&2\cdot8\end{bmatrix}
=\begin{bmatrix}2&2\\4&0\\14&14\\14&16\end{bmatrix}\in\mathbb R^{4\times2}.
$$
For $b=(1,-1)^\top$, add $\mathbf1_4b^\top$ to obtain
$\begin{bmatrix}3&1\\5&-1\\15&13\\15&15\end{bmatrix}$. This is affine because zero input maps to nonzero $b$. The feature sum is constructed, not an observed new gene.

## 7. Eigenvalues and eigenvectors

For $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$,
$$
\det(A-\lambda I_2)=(2-\lambda)^2-1
=\lambda^2-4\lambda+3=(\lambda-3)(\lambda-1).
$$
Hence eigenvalues are 3 and 1. Check $A(1,1)^\top=(3,3)^\top$ and $A(1,-1)^\top=(1,-1)^\top$.
Normalize by $\sqrt2$ to obtain an orthonormal basis. With $Q=\frac1{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, $Q^\top Q=I_2$ and $A=Q\operatorname{diag}(3,1)Q^\top$. This $A$ is separate from the covariance of $X$.

## 8. SVD and low-rank reconstruction

Use separate $B=\begin{bmatrix}3&0&0\\0&1&0\end{bmatrix}\in\mathbb R^{2\times3}$. Since $B^\top B=\operatorname{diag}(9,1,0)$, singular values are 3 and 1.

Full factors: $U=I_2$ ($2\times2$), $D=B$ ($2\times3$), $V=I_3$ ($3\times3$). Thin factors: $U_h=I_2$, $D_h=\operatorname{diag}(3,1)$ and
$V_h=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$ ($3\times2$). Both multiply to $B$.

Rank-one components are
$$
3\begin{bmatrix}1\\0\end{bmatrix}\begin{bmatrix}1&0&0\end{bmatrix}
+
1\begin{bmatrix}0\\1\end{bmatrix}\begin{bmatrix}0&1&0\end{bmatrix}.
$$
Keeping only the first gives $B_1=\begin{bmatrix}3&0&0\\0&0&0\end{bmatrix}$. Residual has only one nonzero, 1, so $\|B-B_1\|_F^2=1$. Retained squared-singular-value fraction is $9/(9+1)=0.9$. It is an energy fraction here, not an explained centered-variance claim.

If the second coordinate marked a rare biological state, this optimum would still erase it. The objective cannot decide its relevance.

## 9. Derivative and gradient descent

For $f(\theta)=(\theta-3)^2$,
$$
\frac{f(1+h)-f(1)}h=-4+h\to-4.
$$
Take $\eta=0.1$, $\theta_0=1$: $\theta_1=1-0.1(-4)=1.4$. Loss drops from 4 to 2.56. Next update gives $1.72$ and loss 1.6384. These are scalar updates, not research model training.

## 10. RBF similarity

For toy rows 1 and 2, squared distance is 3. With bandwidth $\sigma=1$:
$$
K(x_1,x_2)=\exp[-3/(2\cdot1^2)]=e^{-1.5}\approx0.223130.
$$
At $\sigma=2$, $K=e^{-3/8}\approx0.687289$. Same observations, different bandwidth, different similarity.

## 11. Entropy, cross-entropy and KL

Let $P=(3/4,1/4)$ and $Q=(1/2,1/2)$ on the same two outcomes:
$$
H(P)=-\tfrac34\log(\tfrac34)-\tfrac14\log(\tfrac14)
\approx0.562335\text{ nats}=0.811278\text{ bits}.
$$
$$
H(P,Q)=-\tfrac34\log(\tfrac12)-\tfrac14\log(\tfrac12)=\log2\approx0.693147.
$$
$$
D_{\rm KL}(P\|Q)=\tfrac34\log(1.5)+\tfrac14\log(0.5)
\approx0.304099-0.173287=0.130812.
$$
Check $H(P,Q)-H(P)=0.130812$. Reversing arguments gives $\tfrac12\log(2/3)+\tfrac12\log2=\tfrac12\log(4/3)\approx0.143841$, so KL is asymmetric. If $Q=(1,0)$, divergence is infinite because $P$ puts positive mass on its second outcome.

## 12. ARI by pairs

Reference $Y=(A,A,B,B)$ and crossed partition $C=(u,v,u,v)$ are fixed by hand.

| Pair | Same in $Y$? | Same in $C$? | Agreement? |
|---|---|---|---|
| 12 | yes | no | no |
| 13 | no | yes | no |
| 14 | no | no | yes |
| 23 | no | no | yes |
| 24 | no | yes | no |
| 34 | yes | no | no |

Contingency table is $\begin{bmatrix}1&1\\1&1\end{bmatrix}$, margins $(2,2)$. There are $T=\binom42=6$ pairs. Together-in-both count $J=4\binom12=0$; together totals $A=B=2\binom22=2$. Expected together agreement under fixed margins is $E=AB/T=2/3$:
$$
ARI=\frac{0-2/3}{(2+2)/2-2/3}=-1/2.
$$
Rand Index is $2/6=1/3$. For matching partition $C=(u,u,v,v)$, $J=2$ and ARI=1. For partial partition $C=(u,u,u,v)$, $J=1,A=3,B=2,E=1$, so ARI=0. A zero score does not prove the labels were generated randomly.

## 13. NMI from contingency probabilities

Use arithmetic normalization $2I/[H(C)+H(Y)]$. Matching equal groups give $H(C)=H(Y)=\log2$, $I=\log2$, NMI=1. Crossed groups have joint probabilities $1/4$ and marginal products $1/4$: $I=4(1/4)\log1=0$, NMI=0.

For $Y=(A,A,B,B)$ and $C=(u,u,u,v)$:
$$
P_{CY}=\begin{bmatrix}1/2&1/4\\0&1/4\end{bmatrix},
\quad P_C=(3/4,1/4),\quad P_Y=(1/2,1/2).
$$
Zero cells contribute zero. The remaining terms give
$$
I=\tfrac12\log(4/3)+\tfrac14\log(2/3)+\tfrac14\log2
\approx0.215762.
$$
$H(C)=0.562335$, $H(Y)=0.693147$, hence
$$
NMI=\frac{2(0.215762)}{0.562335+0.693147}\approx0.343711.
$$
The same partial partition had ARI=0. The metrics answer different questions.

## 14. Silhouette with assigned groups

Use raw toy $X$, Euclidean distances and hand-assigned groups $\{1,2\}$, $\{3,4\}$. Within-group distance is $\sqrt3$ for every observation.

| $i$ | $a(i)$ | $b(i)$, mean distance to the only other group | $s(i)=1-a(i)/b(i)$ |
|---|---:|---|---:|
| 1 | $\sqrt3$ | $(\sqrt{108}+\sqrt{123})/2=10.741421$ | 0.838750 |
| 2 | $\sqrt3$ | $(\sqrt{99}+\sqrt{116})/2=10.360102$ | 0.832815 |
| 3 | $\sqrt3$ | $(\sqrt{108}+\sqrt{99})/2=10.171090$ | 0.829708 |
| 4 | $\sqrt3$ | $(\sqrt{123}+\sqrt{116})/2=10.930433$ | 0.841539 |

All $b>a$, so the simplified form in the last column is valid. Mean silhouette is approximately 0.835703. It measures this space and grouping only. Singleton contributions and $a=b=0$ use the zero convention; an all-one-cluster partition is ineligible.

## 15. Additional consistency checks

Bernoulli outcomes $(1,1,0)$ give MLE $2/3$ from $2/\theta-1/(1-\theta)=0$. A uniform prior gives posterior density $12\theta^2(1-\theta)$, mean 0.6 and variance 0.04. Likelihood and posterior are different objects.

Binary confusion counts TP=3, FP=1, TN=4, FN=2 give accuracy $7/10$, precision $3/4$, recall $3/5$, specificity $4/5$, F1 $6/9$.

For missing row $(2,\text{missing},0)$, averaging measured entries gives 1; replacing the missing entry by zero gives $2/3$. Missingness and observed zero have different semantics.

Definitions come from [sources](SOURCES.md). Intermediate numbers are derived here, not copied benchmark results.

# 13. Rank, span and basis

For vectors $v_1,\ldots,v_m\in\mathbb R^p$, a linear combination is $\sum_{a=1}^m c_av_a$, where coefficients $c_a\in\mathbb R$. Their span is the set of all such combinations. They are linearly independent if $\sum_ac_av_a=0$ implies every $c_a=0$. A basis is an independent spanning set for a specified space; the number of basis vectors is that space's dimension. [VMLS, chapter 5](SOURCES.md#vmls)

The rank of $X\in\mathbb R^{n\times p}$ is the dimension of its column space, equal to that of its row space. It obeys $\operatorname{rank}(X)\le\min(n,p)$. For
$$
A=\begin{bmatrix}1&2&0\\0&0&1\\1&2&1\end{bmatrix},
$$
column 2 equals twice column 1, while columns 1 and 3 are independent. Rank is 2. They form a basis of the column space in $\mathbb R^3$, but not a basis of all of $\mathbb R^3$.

Redundant columns mean there are nonzero $v$ with $Xv=0$. If a coefficient vector $\beta$ fits $X\beta$, then $\beta+v$ fits the same values. This is one reason high-dimensional inverse problems can be nonunique. Approximate dependence differs from exact dependence; a numerical rank needs a tolerance and scale.

Biological features can share programs, but correlated genes are not necessarily algebraically duplicate columns. Duplicate display names likewise do not prove identical values or biological features. High count sparsity does not imply low rank: the identity matrix is sparse and full rank.

For A1 RNA, rank is at most 3,484; after column centering it is at most 3,483. This is a shape-derived upper bound, not a measured rank. Selecting a basis or low-rank subspace must later distinguish numerical redundancy from biologically meaningful distinctions.

# 05. Similarity

For nonzero $x,y\in\mathbb R^p$, cosine similarity is
$$
c(x,y)=\frac{x^\top y}{\|x\|_2\|y\|_2}.
$$
It lies in $[-1,1]$, and in $[0,1]$ for nonnegative vectors. It measures direction and ignores positive whole-vector rescaling. A zero vector has no defined cosine; a software replacement must be declared. For toy rows 1 and 2, $c=6/(\sqrt5\sqrt{10})\approx0.848528$. [VMLS](SOURCES.md#vmls)

Pearson similarity between two observation profiles first centers each profile over its features:
$$
\rho(x,y)=\frac{(x-\bar x\mathbf1_p)^\top(y-\bar y\mathbf1_p)}
{\|x-\bar x\mathbf1_p\|_2\|y-\bar y\mathbf1_p\|_2},
\quad \bar x=p^{-1}\sum_jx_j.
$$
$\mathbf1_p$ is the $p$-vector of ones. Both centered norms must be nonzero. This is cosine after centering, so it removes constant offsets as well as positive scale. Toy rows give $\rho=3/\sqrt{21}\approx0.654654$, unlike the uncentered cosine. For $y=2x$, cosine is one while Euclidean distance is $\|x\|_2$.

| Term | What it describes | What it does not establish |
|---|---|---|
| Distance | Separation under specified metric | Biological difference |
| Similarity | Chosen numerical agreement | A calibrated probability |
| Correlation | Linear or rank association | Causation |
| Biological relatedness | A specified biological relation supported by evidence | One universal score |

The axis matters: comparing two cells across genes differs from correlating two genes across observations. Feature scaling, shared technical effects and zero patterns affect similarity. A constant profile has undefined Pearson correlation. $1-c$ is often called cosine distance, but generally fails the triangle inequality. None of these scores alone certifies equal molecular states.

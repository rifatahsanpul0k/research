# 08. Probability foundations

A random variable assigns a numerical value to an outcome of a defined random process. Let $A$ be detection of a particular RNA feature (0 or 1), $B$ a library-quality category, and $N$ its captured count. The probability distribution describes uncertainty under a model of that process. An observed number is one realization, not its distribution. [Harvard probability materials](SOURCES.md#probability)

For events $A=a$ and $B=b$:
- Joint probability: $P(A=a,B=b)$.
- Marginal: $P(A=a)=\sum_bP(A=a,B=b)$.
- Conditional: $P(A=a\mid B=b)=P(A=a,B=b)/P(B=b)$ for positive denominator.
- Independence: $P(A=a,B=b)=P(A=a)P(B=b)$ for all values.

Synthetic table:

| | $B=$high | $B=$low | Marginal |
|---|---:|---:|---:|
| $A=1$ | 0.4 | 0.1 | 0.5 |
| $A=0$ | 0.1 | 0.4 | 0.5 |
| Marginal | 0.5 | 0.5 | 1 |

Then $P(A=1\mid B=\text{high})=0.8$, while $P(A=1)=0.5$, so independence fails. The table does not establish that quality causes biological expression.

For discrete random variable $N$ with mass function $p_N(t)$, expectation is $E[N]=\sum_t t\,p_N(t)$ and variance is $\operatorname{Var}(N)=E[(N-E[N])^2]$. Continuous variables use density integrals. A probability density can exceed one; probabilities are areas under it, and a single exact continuous value generally has probability zero.

A statistical model of cells is not automatically a sampling model of donors. Multiple spots from one section share context. Treating them as independent biological replicates needs justification. [Replication evidence](SOURCES.md#bio) Conditional modeling may explain measured covariates while leaving unmeasured confounding unresolved.

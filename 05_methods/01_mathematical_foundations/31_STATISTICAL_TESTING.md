# 31. Statistical testing

A null hypothesis $H_0$ specifies a reference claim (for example, a mean difference $\delta=0$); an alternative $H_1$ describes a competing claim (such as $\delta\ne0$). A test statistic $T(X)$ is a chosen numerical summary. A p-value is the probability, under the null sampling model, of a statistic at least as extreme as the observed value according to the declared test. It is not $P(H_0\mid X)$, effect magnitude or biological importance. [Shalizi](SOURCES.md#testing)

A confidence interval procedure has a repeated-sampling coverage rate under its assumptions. A 95% interval does not mean a fixed frequentist parameter has 95% posterior probability of lying in the realized interval. An effect size, such as an RNA mean difference in declared units, conveys magnitude; uncertainty and meaningful biological scale accompany it.

Synthetic known-Gaussian-error example: estimate $\hat\delta=0.4$ with standard error 0.1. Under $H_0$, $T=\hat\delta/0.1=4$ has a standard normal reference. A two-sided p-value is $2[1-\Phi(4)]\approx0.00006334$, where $\Phi$ is the standard normal CDF. The approximate 95% interval is $0.4\pm1.96(0.1)=[0.204,0.596]$. Whether 0.4 matters biologically cannot be read from that p-value.

For $m=10000$ true null tests, each with type-I error probability 0.05, the expected number of false rejections is $500$ by linearity of expectation. Independence is not needed for this expectation. This motivates multiple-testing control. Define $V$ as false discoveries and $R$ as total discoveries; FDR is $E[V/\max(R,1)]$. It controls an expected proportion, not the probability that each selected gene is false. [Benjamini–Hochberg](SOURCES.md#bh)

The BH step-up rule sorts p-values $p_{(1)}\le\cdots\le p_{(m)}$ and chooses largest $k$ with $p_{(k)}\le kq/m$ for target $q$. If none meets the rule, reject none. Its guarantee requires valid p-values and suitable dependence assumptions; the original result treats independent tests.

Cells/spots within donors or sections are not automatically independent biological replicates. [Replication](SOURCES.md#bio) No actual gene testing or differential-expression analysis occurs here.

# 06. Mean, variance and covariance

For column $j$ of $X\in\mathbb R^{n\times p}$, its empirical mean is $\mu_j=n^{-1}\sum_ix_{ij}$. For $n>1$ the sample variance is
$$
s_j^2=\frac1{n-1}\sum_i(x_{ij}-\mu_j)^2.
$$
We use $s_j^2$ for the prompt's sample estimate $\sigma_j^2$ to distinguish it from a population parameter. Dividing by $n$ instead describes the finite table's population moment. Prior Phase 1E JSON summaries used that population convention. Unbiasedness of the $n-1$ estimator concerns independent, identically distributed observations with finite variance; it does not create independent biological replicates. [Probability](SOURCES.md#probability), [replication](SOURCES.md#bio)

Sample covariance between features $j,k$ is
$$
s_{jk}=\frac1{n-1}\sum_i(x_{ij}-\mu_j)(x_{ik}-\mu_k).
$$
Positive covariance means deviations tend to share sign; negative covariance means they tend to oppose. Units are the product of feature units. Constant features have zero covariance. Neither direction implies regulatory interaction.

Let $\mu\in\mathbb R^p$ collect means, $\mathbf1_n\in\mathbb R^n$ be all ones, and $X_c=X-\mathbf1_n\mu^\top\in\mathbb R^{n\times p}$. Then the empirical covariance matrix is
$$
\widehat\Sigma=\frac{X_c^\top X_c}{n-1}\in\mathbb R^{p\times p}.
$$
It is symmetric positive semidefinite: $v^\top\widehat\Sigma v=\|X_cv\|_2^2/(n-1)\ge0$ for $v\in\mathbb R^p$. Diagonal entries are sample variances; off-diagonal entries are covariances. Rank is at most $\min(p,n-1)$, so $p>n-1$ implies singular covariance. [Linear algebra](SOURCES.md#vmls)

For the shared toy, means are $(5.5,4,3)$; variances are $(37/3,50/3,26/3)$; covariance of features 1 and 2 is $42/3=14$. Intermediate products appear in [toy calculations](TOY_CALCULATIONS.md). Gene covariance can also reflect composition, depth or shared regulators; interpretation requires Phase 1B evidence.

# 17. Optimization foundations

Let $\theta\in\Theta\subseteq\mathbb R^d$ be a parameter vector, $\Theta$ the feasible set, and $\mathcal L:\Theta\to\mathbb R$ an objective. Then
$$
\theta^*\in\arg\min_{\theta\in\Theta}\mathcal L(\theta)
$$
means a parameter choice attaining the smallest objective. The argmin is a set if multiple choices tie; it can be empty when an infimum is not attained. $\min\mathcal L$ is a value, unlike $\arg\min\mathcal L$. Maximization is minimization of the negative objective. [Convex Optimization, chapters 1–4](SOURCES.md#convex)

A global minimum is no worse than every feasible point. A local minimum is no worse than nearby feasible points; it need not be global. Constraints restrict permissible solutions, for example $0\le\theta\le1$ for a probability or nonnegative coefficients for a specified interpretation. Constraints must be justified by the variable's meaning.

Toy objective $\mathcal L(\theta)=(\theta-3)^2$ has global minimum at $\theta=3$ with value 0. Under $\Theta=[0,2]$, the constrained minimum is $\theta=2$ with value 1. For $\mathcal L(\theta)=\theta$ on $\Theta=(0,1)$, infimum 0 is never attained. These examples explain why domains cannot be omitted.

For a convex objective over a convex feasible set, every local minimum is global; strict convexity ensures at most one minimizer, but existence still needs conditions. General representation objectives need not be convex. A converged computation need not establish global optimality.

Optimizing reconstruction, label agreement or regularized likelihood can target different things. Low objective value is numerical success under assumptions; it does not establish correct biology. This phase solves only tiny scalar teaching problems.

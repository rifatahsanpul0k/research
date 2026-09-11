# Entropic optimal transport

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Regularized coupling

Use the measures, cost and marginal constraints from [OT](26_OPTIMAL_TRANSPORT.md). For \(\Pi:n\times m\), define \(H(\Pi)=-\sum_{ij}\Pi_{ij}(\log\Pi_{ij}-1)\), with 0 log 0=0. Entropic OT minimizes
\[
\langle\Pi,C\rangle-\varepsilon H(\Pi),\quad\varepsilon>0.
\]
The entropy encourages spreading mass and makes the balanced finite-cost objective strictly convex over the feasible plan. For positive marginals, the solution has the scaling form
\[
\Pi=\operatorname{diag}(u)K\operatorname{diag}(v),\quad
K_{ij}=e^{-C_{ij}/\varepsilon},\quad
u=a/(Kv),\quad v=b/(K^Tu).
\]
Here u:n, v:m; divisions are elementwise. Alternating these scalings enforces marginals in the Sinkhorn procedure. K is a cost-exponential matrix, not necessarily a PSD kernel, particularly when rectangular.[^1][^2]

## Bias, smoothness and interpretation

Regularization changes the coupling, not just execution time. As ε decreases, solutions approach unregularized optimizers under suitable finite discrete conditions but numerical conditioning can worsen. Larger ε favors diffuse mass. Stable log-domain implementations avoid underflow in extreme exponentials. Raw entropic objectives should not automatically be called true metrics; self-cost and regularization bias require care.

In the two-by-two toy from note 26, finite positive K and marginals give positive off-diagonal coupling, unlike the unregularized diagonal optimum. That mass spreading follows the regularizer; it does not show a transitional cell population. Entropic uncertainty is not necessarily calibrated uncertainty about biological matching.

One dense scaling iteration costs O(nm) and storage is O(nm), excluding cost construction. Convergence tolerance, ε and stabilization affect actual work; no runtime comparison was performed. Missing observations, unequal features and absent populations still need appropriate modeling. A smooth-looking stage alignment would not establish chronological dynamics or lineage. No project Sinkhorn optimization was executed.

## Evidence

[^1]: Cuturi M (2013). [Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances](https://arxiv.org/abs/1306.0895). See [access record](SOURCES.md#sinkhorn).
[^2]: Official project maintainers (2026). [POT user guide](https://pythonot.github.io/). See [access record](SOURCES.md#pot_doc).

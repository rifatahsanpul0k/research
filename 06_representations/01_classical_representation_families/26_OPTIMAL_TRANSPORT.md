# Optimal transport couplings

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Measures, costs and marginal constraints

Let \(\mu=\sum_{i=1}^n a_i\delta_{x_i}\) and \(\nu=\sum_{j=1}^m b_j\delta_{y_j}\), with a:n, b:m, nonnegative masses each summing to one; δ is a unit point mass. A cost \(C:n\times m\) gives the cost per mass assigned between each pair. Balanced discrete OT solves
\[
\min_{\Pi\ge0}\langle\Pi,C\rangle
=\min_{\Pi\ge0}\sum_{ij}\Pi_{ij}C_{ij},
\quad \Pi\mathbf1_m=a,\quad\Pi^T\mathbf1_n=b.
\]
The plan Π:n×m is a coupling with prescribed marginals. It is not an n×d feature embedding, and its entries are not automatically probabilities of biological ancestry.[^1][^2]

## A concrete coupling and an optional map

For a=b=(1/2,1/2) and C=[[0,2],[2,0]], Π=diag(1/2,1/2) has cost 0. The independent plan abᵀ has four entries 1/4 and cost 1. Both satisfy the marginals, but only the first is optimal here. This is hand arithmetic, not biological matching.

If target features \(Y:m\times q\) are meaningful, the barycentric map \(\widehat Y=\operatorname{diag}(a)^{-1}\Pi Y:n\times q\) is another representation for a_i>0. It averages target features according to conditional transported mass; it is an inferred summary and can mix distinct target observations.

## Assumptions and project limits

OT needs a defensible cost. Direct cross-feature Euclidean cost requires comparable axes; RNA and unrelated peak features cannot simply be subtracted. Balanced mass constraints force allocation, which may be unsuitable if populations are absent or abundances differ; unbalanced/partial variants change the problem. Coupling ambiguity can persist under symmetries or flat costs.

Dense C and Π require O(nm) storage; exact linear-programming cost depends on the solver. Spatial positions may define costs, but coordinate units/frame matter. No transport plan, matching or stage transition was inferred for the project. Foundational OT and PASTE provide the authorized classical alignment coverage without studying uniPort's deep architecture.

## Evidence

[^1]: Peyré G; Cuturi M (2019). [Computational Optimal Transport](https://arxiv.org/abs/1803.00567). See [access record](SOURCES.md#ot).
[^2]: Official project maintainers (2026). [POT user guide](https://pythonot.github.io/). See [access record](SOURCES.md#pot_doc).

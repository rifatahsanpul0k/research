# t-SNE

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Neighborhood distributions and optimization

For input \(X:n\times p\), define for j≠i
\[
p_{j|i}=\frac{\exp(-\|x_i-x_j\|^2/(2\sigma_i^2))}
{\sum_{\ell\ne i}\exp(-\|x_i-x_\ell\|^2/(2\sigma_i^2))},
\quad p_{ij}=\frac{p_{j|i}+p_{i|j}}{2n}.
\]
Set diagonal probabilities to zero. Local bandwidths σ_i are chosen to match a target perplexity, \(2^{-\sum_jp_{j|i}\log_2p_{j|i}}\). For low-dimensional \(Y:n\times d\), typically d=2 for a display,
\[
q_{ij}=\frac{(1+\|y_i-y_j\|^2)^{-1}}{\sum_{a\ne b}(1+\|y_a-y_b\|^2)^{-1}},
\qquad L=\sum_{i\ne j}p_{ij}\log(p_{ij}/q_{ij}).
\]
The heavy-tailed low-dimensional affinity and asymmetric KL objective target neighborhood distribution agreement. Both pairwise distributions sum to one over ordered off-diagonal pairs.[^1]

## Visualization is not quantitative biological validation

The objective does not promise faithful global intercluster distances, cluster areas or axis meanings. A gap between islands is not a measured developmental interval. Coordinates may be used in a downstream model only as an explicit additional modeling choice with validation; a visually convincing plot is insufficient. Random initialization, perplexity, learning rate and optimization settings can change the map. Even deterministic initialization does not establish scientific reproducibility.

For project spots, an island is not automatically a cell type, and spatial contiguity is absent unless specifically encoded upstream. Missing data require a suitable input representation; t-SNE does not measure an absent assay. Adding new observations is not simply appending rows to an unchanged coordinate map in the baseline algorithm.

Dense exact pairwise work/storage is quadratic in n; approximations change scaling and the numerical objective evaluation. The final n×d coordinates are much smaller than fitting state. No project t-SNE was fitted. The cited author's code distribution and library alternatives are recorded without installation or performance comparison.

## Evidence

[^1]: van der Maaten L; Hinton G (2008). [Visualizing Data using t-SNE](https://www.jmlr.org/papers/v9/vandermaaten08a.html). See [access record](SOURCES.md#tsne).

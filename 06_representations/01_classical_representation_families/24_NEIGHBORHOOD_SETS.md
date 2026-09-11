# Neighborhood sets

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Relationships without compulsory graph encoding

For observation i and a specified dissimilarity on an input representation, \(N_k(i)\subseteq\{1,\ldots,n\}\setminus\{i\}\) contains k closest reference observations. Declare the self-exclusion rule and tie policy. A radius set is \(N_r(i)=\{j\ne i:d(x_i,x_j)\le r\}\). Mutual KNN retains j only when both j∈N_k(i) and i∈N_k(j). KNN is generally asymmetric even for a symmetric metric.[^1]

The result may be stored as identifier sets or ordered lists. Turning them into a graph adds a vertex set and an explicit edge, direction, symmetrization and weighting rule. A neighborhood set therefore need not be called a graph; a directed KNN adjacency is one encoding of the same selected relationships.

## Sensitivity and project meaning

A neighbor depends on preprocessing, retained features, initial representation, metric, k/r and the reference population. Changing any of these can change membership. KNN fixes neighbor count, so it may connect across a large gap in a sparse region. A radius rule fixes distance but allows isolated observations and varying degree. Mutual filtering changes connectivity; it does not automatically identify biological boundaries.

The toy uses Euclidean distances, self-exclusion and an ID tie-break rule; no real neighborhood sets are built. Molecular neighbors are not necessarily spatial neighbors. Spot-to-spot relationships are not direct cell contacts or signaling evidence.

Stored KNN IDs take O(nk) entries; naive exact discovery costs O(n²p), while indexes and approximate searches have data-dependent behavior. Keeping only IDs discards absolute distances and unused feature detail. Weighted lists preserve more but remain thresholded. Missing modalities need a legitimate comparison rule before search, not artificial zero vectors. The official neighbor implementation is recorded as a library mechanism, without fitting project data.

Official implementation context: [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html).[^2]

## Evidence

[^1]: Blum A; Hopcroft J; Kannan R (2020). [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). See [access record](SOURCES.md#bhk).

[^2]: Official documentation. [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html); [access record](SOURCES.md#sk_neighbors).

# Graphs as one representation family

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Formal object and encodings

A graph \(G=(V,E)\) has N=|V| vertices and edges E. For a directed graph, edges are ordered vertex pairs; an undirected graph identifies the two orders. A binary adjacency \(A:N\times N\) records presence, while weighted adjacency stores declared edge weights. A weight of zero may require a separate edge-presence mask if zero-weight edges are allowed. Optional node features \(F:N\times p\) and edge features \(Q:|E|\times q\) carry additional measurements.[^1]

An edge list stores endpoint identifiers, with optional type/weight/provenance columns. Sparse adjacency stores nonzeros and index structures. Dense adjacency costs O(N²); an edge list or sparse adjacency is O(N+|E|) before attributes. These storage choices can encode the same graph exactly when vertex ordering, directions and multiedge semantics are preserved.

## What an edge means

An edge can encode a selected numerical neighbor, physical relationship, correlation or database assertion. Those meanings are not interchangeable. A KNN observation edge is a result of a declared construction rule, not a measured regulatory interaction. A gene–gene correlation graph has different node entities from a spot–spot proximity graph. Node IDs and relation provenance are necessary for interpretation.

A graph created from a feature table generally discards unselected pairwise relations and feature values unless attributes are retained. A graph object with full F may retain the original table too; “graph representation” therefore does not imply a fixed amount of compression. An adjacency matrix is not automatically a PSD kernel or a probability transition matrix.

For this project, graphs are one branch beside vectors, kernels, sets, tensors and couplings. No GNN or real-data graph is built. The only adjacency calculation is the explicitly authorized five-observation synthetic example. Graphify's code graph describes repository structure and is unrelated to a biological observation graph. Missing measurements and uncertain interactions must remain explicit rather than being interpreted as verified nonedges.

## Evidence

[^1]: Official project maintainers (2026). [NetworkX graph types](https://networkx.org/documentation/stable/reference/classes/index.html). See [access record](SOURCES.md#networkx).

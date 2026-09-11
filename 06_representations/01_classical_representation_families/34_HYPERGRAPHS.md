# Hypergraphs

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Group relations and incidence

A hypergraph \(\mathcal H=(V,\mathcal E)\) allows a hyperedge e∈𝓔 to contain more than two vertices. For N=|V|, h=|𝓔|, incidence \(H\in\{0,1\}^{N\times h}\) has H_ie=1 exactly when vertex i belongs to hyperedge e. Here H is incidence, not an NMF loading matrix. Optional hyperedge weights have length h.[^1][^2]

For V={a,b,c,d} and hyperedges {a,b,c}, {c,d},
\[
H=\begin{bmatrix}1&0\\1&0\\1&1\\0&1\end{bmatrix}.
\]
The first column records one three-member relationship. Replacing it by a triangle of pairwise edges loses whether the group was one assertion or three separate assertions. Conversely, observing all three pairwise associations does not establish a collective interaction.

## Biological possibilities and caution

Pathway membership, a gene program or a proposed multicell niche can be represented as groups, provided the entity and membership definitions are explicit. Membership alone does not prove cooperative function or simultaneous activity. A hyperedge may encode annotation membership rather than a measured higher-order interaction. This is a biological interpretation boundary, not evidence that such group effects occur in our datasets.

A hypergraph differs from a heterogeneous graph: the former changes edge arity; the latter changes entity/relation types. Both properties can coexist. A bipartite incidence encoding uses hyperedge-nodes and membership edges and can preserve H; clique expansion generally loses information.

Dense incidence costs O(Nh); sparse storage is O(N+h+Σ_e|e|). Enumerating candidate groups can grow combinatorially and needs a justified restriction. Missing observations/annotations remain uncertain membership, not verified zeros. HyperNetX is a verified official library, not an implementation of a selected biological model. No project hyperedges are constructed and no superiority claim is made.

## Evidence

[^1]: Battiston F; Cencetti G; Iacopini I; Latora V; Lucas M; Patania A; Young JG; Petri G (2020). [Networks beyond pairwise interactions: Structure and dynamics](https://arxiv.org/abs/2006.01764). See [access record](SOURCES.md#higher).
[^2]: Official project maintainers (2026). [HyperNetX documentation](https://hypernetx.readthedocs.io/en/latest/). See [access record](SOURCES.md#hypernetx).

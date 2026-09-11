# Higher-order representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## What exceeds pairwise description

A motif is a specified small pattern of edges; a triangle motif can exist entirely within an ordinary pairwise graph. A group interaction is a different statement: the group contributes information that is not represented by independently listed pairs. Higher-order frameworks distinguish these possibilities.[^1]

An abstract simplicial complex is a collection of vertex subsets closed under taking subsets. If {a,b,c} is a simplex, then its pairs and singletons must also belong. A hypergraph need not obey this closure rule. A filled triangle simplex therefore encodes more than the boundary formed by three pairwise edges. This formal difference does not prove a three-way biological mechanism.[^1][^2]

## A direct information-loss example

Consider a hypergraph containing one edge {a,b,c}, versus one containing three edges {a,b}, {a,c}, {b,c}. Their clique-expanded pairwise graph is identical. Thus any procedure retaining only that graph cannot distinguish which group system generated it. An incidence table can. A simplex construction would impose additional closure; that is a modeling commitment, not a neutral reformatting.

For this project, a “niche” group could be defined by a spatial rule or external annotation, but its members' presence does not establish a collective signaling mechanism. Molecular similarity, co-location and functional interaction remain separate evidence classes. No higher-order biological relationships are inferred.

Storage depends on the represented groups/simplices and their membership sizes. Enumerating all groups of size r among N entities requires up to \(\binom Nr\) candidates; storing all subsets can be exponential. Sparsity and a maximum order are assumptions with information consequences. This note remains introductory; no topological pipeline, hypergraph neural method or comparison experiment is begun.

## Evidence

[^1]: Battiston F; Cencetti G; Iacopini I; Latora V; Lucas M; Patania A; Young JG; Petri G (2020). [Networks beyond pairwise interactions: Structure and dynamics](https://arxiv.org/abs/2006.01764). See [access record](SOURCES.md#higher).
[^2]: Official project maintainers (2026). [HyperNetX documentation](https://hypernetx.readthedocs.io/en/latest/). See [access record](SOURCES.md#hypernetx).

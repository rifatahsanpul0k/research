# Heterogeneous graphs

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Typed entities and relations

A heterogeneous information network has an entity-type map \(\tau:V\to\mathcal T\) and relation-type map \(\rho:E\to\mathcal R\). Cell/spot, gene, protein and pathway vertices have different meanings and feature schemas. A typed adjacency block \(A^{(r)}:n_s\times n_t\) links source entities of one type to target entities of another. A full N×N matrix alone does not express those semantics unless type maps are retained.[^1]

| Relation | Possible data source | What it does not automatically mean |
|---|---|---|
| observation–expresses–gene | Assay value with threshold/weight rule | Causal effect of that gene |
| gene–encodes–protein | Sequence annotation with IDs/versions | Measured protein abundance |
| protein–participates-in–pathway | Curated/inferred database annotation | Active pathway in this tissue |
| gene–associated-with–disease | Explicit association evidence | Disease causation |

A meta-path is a sequence of entity/relation types; the original PathSim paper shows why similarity depends on this typed relational context. This phase studies that schema, not a PathSim search implementation or a neural model.[^1]

## Preservation and limitations

A spot–gene–pathway path has a different interpretation from a spot–spot distance edge. Treating both as untyped adjacency loses their meaning. Multiple database assertions may have different evidence strengths and dates. Graph structure cannot turn an inferred annotation into ground truth.[^2]

Sparse storage scales with the total entities and typed edges, plus attributes; a dense full adjacency costs O(N²) even when many type-pair blocks are invalid. Uncertain/absent assertions are not confirmed nonrelations. Identifier mismatches can create false joins, and gene-to-protein mapping is not generally one symbol to one unique isoform.

For this project, all entity identities, observation units and annotation releases would require verification before construction. Generic NetworkX can store typed attributes, but is not author code for PathSim. No heterogeneous biological graph or downstream model is built.

## Evidence

[^1]: Sun Y; Han J; Yan X; Yu PS; Wu T (2011). [PathSim: Meta Path-Based Top-K Similarity Search in Heterogeneous Information Networks](https://www.vldb.org/pvldb/vol4/p992-sun.pdf). See [access record](SOURCES.md#pathsim).
[^2]: Official project maintainers (2026). [Guide to GO evidence codes](https://geneontology.org/docs/guide-go-evidence-codes/). See [access record](SOURCES.md#go).

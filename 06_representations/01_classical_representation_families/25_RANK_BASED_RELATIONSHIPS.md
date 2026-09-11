# Ranks of relationships

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Ordered proximity

Let \(r_i(j)\in\{1,\ldots,n-1\}\) be j's rank among the other observations sorted by d(x_i,x_j). Ties require a convention: tied ranks, average ranks, or a stable deterministic ordering. Full ranks form n×n information with an excluded diagonal; top-k rankings use O(nk) entries. A rank is relative to a reference population, not an absolute quantity.[^1]

For a fixed row, applying any strictly increasing function h to all its distances preserves their ordering. Thus distances (1,2,10) and (1,100,101) yield the same neighbor order, although their gaps differ. This directly demonstrates both a robustness property and an information loss. Strictly increasing transformation of every distance need not preserve metric axioms, even when it preserves ranks.

## Consequences

Rank-based similarity can avoid dependence on particular monotone scale choices, but it does not fix a poorly chosen metric. A tiny change near a tie can swap ranks, while a large change far from a boundary may preserve them. Rankings across reference sets are not directly comparable when sampling density or population composition differs.

For this project, selecting the same nearest spot in RNA and space means agreement of selected orderings, not equal physical and molecular distances. A stage absent from the sampled reference cannot appear as a neighbor. Missing-feature handling still determines the original comparisons.

Full sorting costs O(n² log n) after pairwise distances in a straightforward implementation; top-k selection or indexed searches change the cost. Rank representations remove distance magnitudes and cannot generally reconstruct X. They make ordinal relationships easier to use but hide whether the nearest candidate was actually close. No ranking of representation families is made here: ranking observations by a declared metric is a different concept from ranking methods by performance.

## Evidence

[^1]: Blum A; Hopcroft J; Kannan R (2020). [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). See [access record](SOURCES.md#bhk).

# Multilayer and multiplex relationships

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Layers retain relationship provenance

A multiplex can represent separate RNA, ADT and spatial relations over corresponding observations. If all n observations exist in each of v layers, layer adjacencies \(A^{(m)}:n\times n\) may be kept as a tuple. A supra-adjacency has shape nv×nv: diagonal blocks are within-layer edges, and off-diagonal blocks encode explicitly defined cross-layer relations. General multilayer networks need not have identical node sets in all layers.[^1]

An identity correspondence between a spot's RNA-layer and ADT-layer node says they share an observation ID; it is not a measured molecular interaction. An absent layer for an observation must be recorded separately from a present node with degree zero. In a partially overlapping system, use an entity/layer membership table rather than inventing missing nodes' measurements.

## Project meaning and trade-offs

Keeping layers separate lets a future analysis distinguish molecular proximity from physical proximity. Collapsing them to a weighted sum can remove that provenance unless retained elsewhere. It also introduces weights with units and assumptions. A shared node set does not imply equal edge density or reliability in all modalities.

For A1, paired spot IDs could support node correspondence, but no RNA/ADT/spatial adjacency is computed. Mouse stages do not share physical cells merely because feature IDs or stage categories can be related. Inter-stage edges would require a separate inference and evidence trail.

Layer storage is O(vn²) if dense or proportional to total within- and cross-layer edges if sparse; storing a fully dense supra-matrix can require O(v²n²). Ordinary graph tools can store explicit layer attributes, but a generic library is not the original review's official model implementation. The registry states this distinction. No fusion strategy, cross-layer weight or biological network was selected.

## Evidence

[^1]: Kivelä M; Arenas A; Barthelemy M; Gleeson JP; Moreno Y; Porter MA (2014). [Multilayer networks](https://arxiv.org/abs/1309.7233). See [access record](SOURCES.md#multilayer).

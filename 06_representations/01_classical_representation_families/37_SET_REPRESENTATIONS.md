# Sets of detected features or events

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Membership instead of amounts

Given \(X:n\times p\) and a declared threshold τ_g for each feature, define \(F_i=\{g:x_{ig}>\tau_g\}\). Each F_i is a subset of the feature universe. An equivalent binary incidence representation is \(B:n\times p\), B_ig=1 when g∈F_i. Permuting the order in which set members are stored does not change the set; changing feature identifiers does.[^1]

Synthetic vectors (1,0,3) and (8,0,1) become the same set {1,3} under τ=0, although their amounts differ. Membership preserves detected support and loses count magnitude. A multiset or weighted set retains multiplicity or weights and is a different object.

Jaccard similarity is \(|F_i\cap F_j|/|F_i\cup F_j|\) when the union is nonempty; the empty-empty case needs a stated convention. It assesses overlap, not equivalence of cells. Threshold decisions near measurement limits can alter membership abruptly.

## Project interpretation

Possible sets include detected genes, accessible regions or detected antibody features. Their universes are different, so a common integer index is not a common biological feature. “Not in the set” means below the chosen detection/selection rule, not necessarily biologically absent. Missing features must be tracked separately from observed nonmembership.

Storage is proportional to total retained memberships plus observation/feature dictionaries, or O(np) as dense incidence. Deriving sets costs a pass over the input representation; threshold choice changes information. Set descriptions can incorporate curated membership but inherit annotation uncertainty. Spatial positions can be retained as metadata rather than encoded as edges. No neural Deep Sets model, threshold selection or project set extraction occurs in this phase.

## Evidence

[^1]: Blum A; Hopcroft J; Kannan R (2020). [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). See [access record](SOURCES.md#bhk).

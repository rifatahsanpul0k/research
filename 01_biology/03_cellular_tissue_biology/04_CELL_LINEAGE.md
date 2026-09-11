# Cell lineage and ancestry

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Lineage is a history of descent through cell divisions. An ancestor–descendant relationship is directional; sister cells share a parent. A developmental trajectory describes change in state and may be inferred rather than observed. These are different meanings of developmental relationship.[^LINE]

## B. Mechanism

Division produces descendants that may maintain or change phenotype. Differentiation can branch into different fates; a state transition can also occur without a division. Thus a branch in a state description is not necessarily a mitosis, and similarity cannot identify an ancestor.[^LINE]

## C. Relationship to prior concepts

Topic 3 concerns changing properties and possible outputs; lineage asks which outputs actually descended from which cells. Genetic history, regulatory state and present function should not be compressed into one relation.

## D. Experimental observation/measurement

Time-resolved observation or inherited labels can support descent. Each has limits of observation duration, labeling specificity and incomplete recovery.[^LINE] In mice, fate mapping linked adult microglia to primitive macrophages, providing developmental evidence beyond the shared word “glia”; it does not identify ancestry of any row in our datasets.[^MICRO]

## E. Computational representation

A fictional lineage record:

| parent | child | division_time_hours | evidence |
|---|---|---:|---|
| P | A | 12 | directly_tracked |
| P | B | 12 | directly_tracked |
| unknown | C | unknown | not_observed |

A and B are sisters in this example. Even if A and C share the same RNA vector, C's parent remains unknown. Tables, lineage trees/networks, descendant sets and probabilistic ancestry descriptions are possible forms; no lineage graph is constructed here.

## F. Relevance to our project

E11 and E18 specimens need not contain the same tracked cells or embryos. Cross-stage molecular correspondence must therefore remain a correspondence of states unless independent historical evidence is supplied. The distinction matters to future representation and evaluation targets.

## G. Common misconceptions

Similarity is not ancestry; label-sharing is not automatically a fully resolved division tree; chronological stage is not lineage. Answered check: a cell can change state without producing a descendant, and two descendants of one parent can become dissimilar. Unresolved: no lineage-tracing metadata have been verified for the project.

## H. Evidence

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). Nature Reviews Genetics. DOI: 10.1038/s41576-020-0223-2. Supporting location/access: [source LINE](SOURCES.md#line).

[^MICRO]: Ginhoux F; Greter M; Leboeuf M; Nandi S; See P; Gokhan S; Mehler MF; Conway SJ; Ng LG; Stanley ER; Samokhvalov IM; Merad M (2010). [Fate mapping analysis reveals that adult microglia derive from primitive macrophages](https://pubmed.ncbi.nlm.nih.gov/20966214/). Science. DOI: 10.1126/science.1194637. Supporting location/access: [source MICRO](SOURCES.md#micro).


# Tissue biology to data: preserving the meaning of each field

All numerical examples are synthetic. These are prospective schemas and arithmetic demonstrations, not processed project data. The six dataset folders have not been accessed. Observation units, modalities, pairing and annotations remain unknown.

## From tissue to a record

```text
biological specimen in a state and anatomical context
 -> sampled cell, nucleus or spatial footprint
 -> measurement of selected molecules/properties
 -> identifiers and values with units
 -> molecular table + geometry + specimen metadata + evidence-backed interpretations
```

Sampling an entire cell versus a nucleus changes which compartment contributes; aggregation can combine different cells.[^NUCLEUS][^TECH] Detailed measurement chemistry and technology are deferred to Phase 1D. The present requirement is to avoid assigning a biological meaning that the observation unit cannot support.

## Molecular matrix

Let \(X\in\mathbb R^{n\times p}\), where ℝ denotes real numbers, n is the number of observations, and p is the number of molecular features. X_ig is the recorded value for observation i and feature g. An untransformed count matrix occupies nonnegative integers within this general real-valued space; an intensity or derived abundance matrix uses another value definition.

| observation | gene A | gene B | gene C |
|---|---:|---:|---:|
| C1 | 8 | 0 | 3 |
| C2 | 1 | 6 | 2 |
| C3 | 7 | 0 | 4 |

For this example alone assume each row is a separately measured cell and each entry counts detected molecules assigned to that gene. In the actual project, neither assumption is established. Columns need stable feature IDs, organism and annotation provenance. A zero is a recorded non-detection under the stated measurement, not proof of no biological expression; `not_measured` must remain distinguishable from zero.[^TECH]

Numerical resemblance between C1 and C3 leaves their ancestry, function, location and unmeasured regulatory/protein properties unresolved. Different values in C2 do not alone establish a different type. This is the logical consequence of limited observations; it does not depend on choosing a similarity metric.

## Spatial coordinates

Let \(S\in\mathbb R^{n\times2}\) contain positions in one declared two-dimensional frame. Row s_i=(a_i,b_i) gives the two coordinate components of observation i. This coordinate matrix S is distinct from a superscripted similarity symbol \(S^{molecular}_{ij}\).

| observation | a_µm | b_µm | frame | position_meaning |
|---|---:|---:|---|---|
| C1 | 0 | 0 | section_1 | hypothetical cell centroid |
| C2 | 5 | 0 | section_1 | hypothetical cell centroid |
| C3 | 100 | 0 | section_1 | hypothetical cell centroid |

C1 and C3 are molecularly similar in the displayed table but 100 µm apart, while the different vector C2 is 5 µm from C1. These values are not cell-contact measurements. A common frame, units and observation IDs are prerequisites for joining X and S. Coordinates from different sections cannot be directly compared merely because both are two-dimensional. Two-dimensional separation also omits separation normal to the section.

## Annotations and hierarchy

Let \(y=(y_1,\ldots,y_n)\), where y_i is an annotation attached to observation i. “Cell annotations” is appropriate only when the unit is actually a cell; a mixed footprint may need a composition description. Labels are interpretations and should retain source, granularity, reference version, conflicting evidence and uncertainty.[^ONTO][^TYPE]

| observation | broad_label | finer_label | state | annotation_source |
|---|---|---|---|---|
| C1 | T cell candidate | unknown | unknown | synthetic illustration |
| C2 | unknown | unknown | unknown | not assigned |
| C3 | T cell candidate | unknown | unknown | synthetic illustration |

These fictional labels are not deduced from the invented gene counts. A label used to interpret a matrix is not automatically independent validation if it was inferred from that matrix. Similarity at a broad lineage label and similarity at a fine subtype label ask different questions.

## Developmental stage and specimen

Let t_i denote the developmental stage of observation i. Use an ordered category until an age convention is verified; measured ages also need units. Store embryo, litter, region, section and collection time separately. Stage and row identity do not establish ancestry.[^LINE][^STAGE]

For the four supplied labels, intended order is E11 < E13 < E15 < E18. Their exact definitions and replicate relationships remain unknown. They motivate studying a developing system but do not license treating every row as a repeat measurement of a previous cell.

**Composition versus within-population change.** In an invented two-population example, each P cell has a feature value 2 and each N cell a value 8. A sample with three P cells and one N cell has mean (3×2+1×8)/4=3.5. A sample with one P and three N cells has mean (1×2+3×8)/4=6.5. The average changes although neither population's per-cell value changes. In real development, changing composition and changing cellular programs can both occur.[^DEV] These possibilities require separate evidence.

## Interaction table

| sender | receiver | ligand | receptor | evidence |
|---|---|---|---|---|
| C1 | C2 | L1 | R1 | hypothetical compatible expression; delivery and response unknown |

L1/R1 are invented symbols. Sender and receiver may be cells, populations or sampled regions; their entity type must be explicit. Add species, specimen, time, contact evidence, protein evidence, response evidence, intervention evidence and source. An inferred candidate must not be promoted to an observed event. Ligand/receptor expression does not establish the complete signaling chain.[^SIGNAL]

## Region annotation

| observation | region | biological_system | evidence |
|---|---|---|---|
| i | cortex | lymph node | hypothetical histological assignment |
| j | medulla | lymph node | hypothetical histological assignment |

Here i and j are generic observation identifiers, not actual dataset rows. LN cortex is anatomically different from cerebral cortex. Region annotation records location in a tissue vocabulary, not a molecular type. Textbook LN anatomy does not verify either row or region in A1/D1.[^HIST]

## Mixtures and missingness

The conceptual expression \(x_{spot}\approx\sum_{k=1}^{m}w_kx_k\) uses x_spot for a p-feature footprint profile, m for the number of contributing cells, x_k for a contributor profile and w_k for its nonnegative effective contribution. For relative profiles, one may impose \(\sum_k w_k=1\); that convention is not required for absolute contributions and is not established for the project. Weights need not equal cell fractions. Background and capture effects are omitted here.

Different decompositions can explain one vector. Therefore neither cell count nor contributor identity is identified by writing the equation. See [observation units](16_OBSERVATION_UNITS.md) for a numerical example. Record a separate availability indicator for each missing modality/feature/metadata field; blank region, unmeasured RNA and measured zero should not collapse into one value.

## Representation-neutral inventory

| Biological relationship | Possible computational forms | Meaning that must survive |
|---|---|---|
| Molecular | vectors, matrices, kernels, latent variables | measured features, units, missingness and uncertainty |
| Spatial | coordinate matrices, distance matrices, spatial fields | frame, scale, sampling footprint and dimension |
| Functional | sets, categories, continuous scores, distributions | specified function and evidence, not expression alone |
| Regulatory | feature matrices, evidence tables, networks | activity versus inferred program, context and direction |
| Lineage | descendant sets, parent–child tables, lineage networks, ancestry distributions | historical support versus current similarity |
| Interaction | event tables, directed networks, hypergraphs for group relations | entities, direction, time and evidence strength |
| Developmental | ordered labels, trajectories as hypotheses, time-indexed tensors | stage versus measured time versus ancestry |
| Anatomical hierarchy | nested labels, region sets, ontology relations | is-a versus part-of; specimen-specific annotation |

A tensor is an array with explicitly named axes. A latent variable is inferred rather than directly measured. A hypergraph can encode a group relation without asserting every pair interacts. A kernel requires its mathematical definition and applicable properties; naming it does not verify biology. These forms are encountered only as possible ways of recording information. No graphs, kernels, embeddings or models are constructed or ranked.

The practical invariant is semantic: molecular measurements, positions, labels, stage, anatomy and interaction evidence are different information. Combining them later must not erase their provenance or pretend they are one interchangeable notion of similarity.

## Evidence

[^NUCLEUS]: Bakken TE; Hodge RD; Miller JA; Yao Z; Nguyen TN; et al. (2018). [Single-nucleus and single-cell transcriptomes compared in matched cortical cell types](https://pubmed.ncbi.nlm.nih.gov/30586455/). See [source NUCLEUS](SOURCES.md#nucleus) for identifiers and access depth.

[^TECH]: Laehnemann D; Koester J; Szczurek E; McCarthy DJ; Hicks SC; Robinson MD; Vallejos CA; Campbell KR; Beerenwinkel N; Mahfouz A; Pinello L; Skums P; Stamatakis A; Stephan-Otto Attolini C; Aparicio S; Baaijens J; Balvert M; Dutilh BE; Guryev V; Marioni JC; Stegle O; Theis FJ; McHardy AC; Raphael BJ; Shah SP; Schoenhuth A; et al. (2020). [Eleven grand challenges in single-cell data science](https://link.springer.com/article/10.1186/s13059-020-1926-6). See [source TECH](SOURCES.md#tech) for identifiers and access depth.

[^ONTO]: Osumi-Sutherland D; Xu C; Keays M; Levine AP; Kharchenko PV; Regev A; Lein E; Teichmann SA (2021). [Cell type ontologies of the Human Cell Atlas](https://pubmed.ncbi.nlm.nih.gov/34750578/). See [source ONTO](SOURCES.md#onto) for identifiers and access depth.

[^TYPE]: Zeng H (2022). [What is a cell type and how to define it?](https://pubmed.ncbi.nlm.nih.gov/35868277/). See [source TYPE](SOURCES.md#type) for identifiers and access depth.

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). See [source LINE](SOURCES.md#line) for identifiers and access depth.

[^STAGE]: eMouseAtlas / EMAP (unknown). [Staging Criteria](https://www.emouseatlas.org/emap/ema/staging_criteria/staging_criteria.html). See [source STAGE](SOURCES.md#stage) for identifiers and access depth.

[^DEV]: Jabaudon D (2017). [Fate and freedom in developing neocortical circuits](https://www.nature.com/articles/ncomms16042). See [source DEV](SOURCES.md#dev) for identifiers and access depth.

[^SIGNAL]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [General Principles of Cell Communication](https://www.ncbi.nlm.nih.gov/books/NBK26813/). See [source SIGNAL](SOURCES.md#signal) for identifiers and access depth.

[^HIST]: Mercadante AA; Tadi P (2023). [Histology, Lymph Nodes](https://www.ncbi.nlm.nih.gov/books/NBK559053/). See [source HIST](SOURCES.md#hist) for identifiers and access depth.


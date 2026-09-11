# 36. Biological versus computational evaluation

**Permanent research principle:** mathematically compact clusters are not automatically correct biological populations. Every future representation assessment must distinguish computational properties, statistical evidence and biological interpretation. This principle applies to all representation families.

| Layer | Questions | Evidence that is insufficient alone |
|---|---|---|
| Computational | What distances, ranks, neighborhoods or reconstructions are preserved? What memory/time is required? | A visually clean embedding |
| Statistical | Are uncertainty, sampling hierarchy, held-out generalization and multiple testing handled? | A small p-value or a single metric |
| Biological | Are cell/region units, marker context, stage, anatomy and independent evidence consistent? | Agreement with one supplied label set |

ARI/NMI assess partition agreement; silhouette assesses geometry under a metric. Reconstruction measures a chosen numerical loss. None alone establishes a developmental lineage, cell type, regulatory interaction or spatial communication. [Metric definitions](SOURCES.md#cluster-metrics), [Phase 1B evidence distinctions](../../01_biology/02_gene_regulation/11_ENHANCER_PROMOTER_INTERACTIONS.md)

Future evaluation should preserve provenance of reference labels and distinguish anatomy/region labels from cell-type or state labels. Inspect failures for rare populations and continuous transitions rather than letting dominant classes decide all conclusions. A method may preserve a legitimate signal that disagrees with coarse labels; that disagreement also needs evidence before being called an improvement. [Biological annotation foundations](../../01_biology/03_cellular_tissue_biology/17_BIOLOGICAL_ANNOTATION.md)

Technical signal can be strong and reproducible within one preparation. Independent biological replication and meaningful held-out units remain necessary for broader claims; repeated cells from one donor cannot replace donors. [Zimmerman et al.](SOURCES.md#bio)

Phase 2A establishes definitions and synthetic calculations. It provides no ranking, preferred family, fitted graph, research model or new biological conclusion. Phase 2B remains unstarted. Mathematical readiness is a reviewed learning artifact, not proof that the human learner has mastered the material.

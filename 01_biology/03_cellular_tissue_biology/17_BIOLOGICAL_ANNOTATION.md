# Biological annotation and marker evidence

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Annotation assigns an interpretation to observations using evidence and a naming convention. Marker genes and proteins are features informative about a category in context. A positive marker supports a candidate when detected appropriately; a negative marker is an expected absence/exclusion criterion, not simply a recorded zero. “Canonical” means established usage, not universal specificity.[^TYPE][^TECH]

Manual annotation involves expert interpretation; reference-based annotation compares with a labeled reference. Both inherit assumptions about species, tissue, developmental stage, observation unit and label granularity.[^ONTO]

## B. Mechanism

Regulatory programs produce combinations of features, while state and development alter expression. For example, developing T cells change CD3/TCR and CD4/CD8 expression across maturation; therefore context matters even for familiar marker proteins.[^TDEV] RNA of a marker gene and abundance/activity of its protein need not match exactly.[^PROT]

## C. Relationship to prior concepts

Type/state distinctions prevent naming every activation program as a type. Hierarchical definitions permit a broad supported label when finer identity is unresolved. A molecule's biological role is separate from its usefulness as a marker.

## D. Experimental observation/measurement

Combine marker patterns with morphology, location or relevant functional evidence. Independent observations strengthen a claim more than repeating a label derived from the same matrix.[^TYPE] Negative evidence requires adequate detection and coverage; non-detection cannot automatically exclude the candidate.[^TECH]

## E. Computational representation

Hypothetical marker table; M1–M3 are invented features, not real annotation rules:

| observation | M1 | M2 | M3 | interpretation |
|---|---:|---:|---|---|
| A | detected | detected | not_measured | candidate Q; exclusion evidence missing |
| B | detected | not_detected | detected | ambiguous; review context |

A gene marker table should retain gene identifier, species and feature meaning; a protein marker table should retain protein/epitope and observation definition. A label table should record candidate, accepted label, parent category, reference/version, evidence, conflicts and uncertainty.

Categorical labels, marker sets, continuous evidence scores and probability distributions are possible forms. A numeric confidence value must not be called a calibrated probability without evidence of calibration.

## F. Relevance to our project

No marker panel or atlas labels are applied to A1/D1 or the four brain datasets. Future human LN annotation and embryonic mouse annotation need appropriate references. Mixed spatial observations may need population/composition descriptions rather than one cell identity.

## G. Common misconceptions

One marker rarely settles identity conclusively; multiple markers are stronger only if informative in context, not merely numerous. Reference agreement is not guaranteed truth; absence is not automatically negative evidence; a marker-associated function is not a demonstrated functional assay. Check: a missing exclusion marker measurement leaves uncertainty rather than establishing its absence.

## H. Evidence

[^TYPE]: Zeng H (2022). [What is a cell type and how to define it?](https://pubmed.ncbi.nlm.nih.gov/35868277/). Cell. DOI: 10.1016/j.cell.2022.06.031. Supporting location/access: [source TYPE](SOURCES.md#type).

[^TECH]: Laehnemann D; Koester J; Szczurek E; McCarthy DJ; Hicks SC; Robinson MD; Vallejos CA; Campbell KR; Beerenwinkel N; Mahfouz A; Pinello L; Skums P; Stamatakis A; Stephan-Otto Attolini C; Aparicio S; Baaijens J; Balvert M; Dutilh BE; Guryev V; Marioni JC; Stegle O; Theis FJ; McHardy AC; Raphael BJ; Shah SP; Schoenhuth A; et al. (2020). [Eleven grand challenges in single-cell data science](https://link.springer.com/article/10.1186/s13059-020-1926-6). Genome Biology. DOI: 10.1186/s13059-020-1926-6. Supporting location/access: [source TECH](SOURCES.md#tech).

[^ONTO]: Osumi-Sutherland D; Xu C; Keays M; Levine AP; Kharchenko PV; Regev A; Lein E; Teichmann SA (2021). [Cell type ontologies of the Human Cell Atlas](https://pubmed.ncbi.nlm.nih.gov/34750578/). Nature Cell Biology. DOI: 10.1038/s41556-021-00787-7. Supporting location/access: [source ONTO](SOURCES.md#onto).

[^TDEV]: Janeway CA Jr; Travers P; Walport M; Shlomchik MJ (2001). [Generation of lymphocytes in bone marrow and thymus](https://www.ncbi.nlm.nih.gov/books/NBK27123/). Immunobiology: The Immune System in Health and Disease, 5th edition. DOI: unknown. Supporting location/access: [source TDEV](SOURCES.md#tdev).

[^PROT]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source PROT](SOURCES.md#prot).


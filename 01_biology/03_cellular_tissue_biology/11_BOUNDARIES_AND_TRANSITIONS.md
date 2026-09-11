# Tissue boundaries, gradients and transitional states

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

An anatomical boundary separates defined tissue domains; a gradient is a spatially varying quantity; a transition zone spans changing properties. Molecular state variation may be continuous, categorical or a mixture. A computational partition is a chosen description, not proof that biology has abrupt divisions.[^GRAD][^HET]

## B. Mechanism

Graded developmental cues can produce different expression responses depending on the receiving cells. Regulatory interpretation can generate distinct domains from a continuous input.[^GRAD] Adhesion structures can support interfaces; ongoing movement can bring cells across some compartment boundaries.[^JUNCTION][^MIGLN] Thus “boundary” does not always mean impermeable wall.

## C. Relationship to prior concepts

Cell differentiation supplies temporal transitions and tissue organization supplies spatial ones. They should not be conflated: a spatial gradient in one section is not a directly observed sequence of cell-state changes over time.

## D. Experimental observation/measurement

Morphological continuity, localized proteins and expression patterns can reveal different kinds of interface. Movement requires temporal observations. Molecularly mixed observations can reflect either cell-intrinsic properties or more than one contributor; observation-unit evidence must decide which interpretation is tenable.[^MIGLN][^TECH]

## E. Computational representation

Synthetic ordered positions and an arbitrary signal:

| position_µm | signal_relative_units | region_annotation |
|---:|---:|---|
| 0 | 1 | R1 |
| 10 | 3 | transition |
| 20 | 6 | R2 |

This is not a measured morphogen profile, nor proof of a particular threshold response. Continuous fields, boundary polygons, uncertain categorical labels and transition membership scores are possible forms. A distance to an annotated boundary requires declaring which boundary and coordinate frame.

## F. Relevance to our project

B/T-region interfaces in lymph node and developing brain domains motivate retaining both boundaries and gradients. Future evaluation may need to respect transitional observations; forcing every case into a crisp reference category could obscure genuine uncertainty. This is an interpretation constraint, not a clustering recommendation.

## G. Common misconceptions

A gradient is not necessarily a lineage; a mixed marker pattern is not necessarily a new type; a cluster boundary is not automatically anatomical. Conversely, continuous signal input does not prove the absence of distinct cell types. Check: two neighboring observations on opposite sides of a functional interface can be spatially close and biologically distinct.

## H. Evidence

[^GRAD]: Ashe HL; Briscoe J (2006). [The interpretation of morphogen gradients](https://pubmed.ncbi.nlm.nih.gov/16410409/). Development. DOI: 10.1242/dev.02238. Supporting location/access: [source GRAD](SOURCES.md#grad).

[^HET]: Wagner A; Regev A; Yosef N (2016). [Revealing the vectors of cellular identity with single-cell genomics](https://pmc.ncbi.nlm.nih.gov/articles/PMC5465644/). Nature Biotechnology. DOI: 10.1038/nbt.3711. Supporting location/access: [source HET](SOURCES.md#het).

[^JUNCTION]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Cell Junctions](https://www.ncbi.nlm.nih.gov/books/NBK26857/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source JUNCTION](SOURCES.md#junction).

[^MIGLN]: Bajénoff M; Egen JG; Koo LY; Laugier JP; Brau F; Glaichenhaus N; Germain RN (2006). [Stromal cell networks regulate lymphocyte entry, migration, and territoriality in lymph nodes](https://pubmed.ncbi.nlm.nih.gov/17112751/). Immunity. DOI: 10.1016/j.immuni.2006.10.011. Supporting location/access: [source MIGLN](SOURCES.md#migln).

[^TECH]: Laehnemann D; Koester J; Szczurek E; McCarthy DJ; Hicks SC; Robinson MD; Vallejos CA; Campbell KR; Beerenwinkel N; Mahfouz A; Pinello L; Skums P; Stamatakis A; Stephan-Otto Attolini C; Aparicio S; Baaijens J; Balvert M; Dutilh BE; Guryev V; Marioni JC; Stegle O; Theis FJ; McHardy AC; Raphael BJ; Shah SP; Schoenhuth A; et al. (2020). [Eleven grand challenges in single-cell data science](https://link.springer.com/article/10.1186/s13059-020-1926-6). Genome Biology. DOI: 10.1186/s13059-020-1926-6. Supporting location/access: [source TECH](SOURCES.md#tech).


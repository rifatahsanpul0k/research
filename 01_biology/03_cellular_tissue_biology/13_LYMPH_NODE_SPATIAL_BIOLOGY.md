# Why lymph-node spatial structure matters

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Spatial organization affects which cells and antigens can encounter one another. B-rich and T-rich territories, stromal structures, vascular entry points and lymphatic spaces are distinct biological features.[^STROMA] They are expected structures to inspect, not guaranteed labels or complete regions in A1 or D1.

## B. Mechanism

In mouse lymph nodes, microscopy showed T-cell movement associated with fibroblastic reticular structures and B-cell movement with follicular dendritic structures. Supporting anatomy helped organize movement and territoriality.[^MIGLN] Stromal signals also support cell positioning and maintenance.[^STROMA]

Tissue lymph enters through afferent vessels and sinuses, while blood vascular entry supplies another route for cells. Consequently, two equally close locations can differ in access to flowing material and in the structures they contact.[^ANATOMY][^STROMA]

## C. Relationship to prior concepts

Identity helps determine response competence; environment supplies cues; position affects access. The requested “identity + local environment + physical position → observed state” is a conceptual combination with feedback and dependencies, not a sum of three measured independent causes.

## D. Experimental observation/measurement

Fixed sections show location at collection; time-resolved imaging addresses movement. The mouse stromal study combined confocal, electron and intravital observations, illustrating why structural and dynamic evidence complement one another.[^MIGLN] A new specimen still needs its own anatomy and annotation evidence.

## E. Computational representation

Synthetic compartment observations:

| observation | type_candidate | region | proximity_to_vessel_µm | interaction_evidence |
|---|---|---|---:|---|
| A | T cell | R1 | 5 | unknown |
| B | T cell | R2 | 50 | unknown |
| C | endothelial | R1 | 0 | unknown |

A and B share a proposed type but occupy different contexts; A and C share a region but differ in proposed type. Distances, labels, region memberships and interaction records should remain separately interpretable. A vessel-distance field is not a measure of exposure or a probability of communication.

## F. Relevance to our project

For A1/D1, future molecular-state differences could reflect local exposure, cell composition or sampling. These alternatives must remain open. Cross-sample coordinate comparison requires common anatomical/frame information; A1/D1 names do not establish matched regions or sections.

## G. Common misconceptions

B-cell-rich does not mean B-cell-only; stromal structure is not an inert backdrop; proximity to a vessel does not prove recent entry. Molecular similarity need not reproduce anatomy. Check: different type labels near a sinus need not be an annotation mistake if the region normally contains different constituents.

## H. Evidence

[^STROMA]: Mueller SN; Germain RN (2009). [Stromal cell contributions to the homeostasis and functionality of the immune system](https://www.nature.com/articles/nri2588). Nature Reviews Immunology. DOI: 10.1038/nri2588. Supporting location/access: [source STROMA](SOURCES.md#stroma).

[^MIGLN]: Bajénoff M; Egen JG; Koo LY; Laugier JP; Brau F; Glaichenhaus N; Germain RN (2006). [Stromal cell networks regulate lymphocyte entry, migration, and territoriality in lymph nodes](https://pubmed.ncbi.nlm.nih.gov/17112751/). Immunity. DOI: 10.1016/j.immuni.2006.10.011. Supporting location/access: [source MIGLN](SOURCES.md#migln).

[^ANATOMY]: University of Leeds (unknown). [Lymph nodes: The Histology Guide](https://histology.leeds.ac.uk/home/lymphoid/lymphnodes/). The Histology Guide. DOI: not_applicable. Supporting location/access: [source ANATOMY](SOURCES.md#anatomy).


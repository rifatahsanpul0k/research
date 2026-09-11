# Extracellular matrix, stroma and microenvironment

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Microenvironment denotes local extracellular conditions and surrounding cells. Extracellular matrix (ECM) is organized extracellular material, including structural and adhesive macromolecules; stroma refers to supporting tissue components and cells, not a single cell type. A niche is an environment functionally supporting a particular cellular process; a stem-cell niche regulates maintenance and output.[^ECM][^STROMA][^NICHE]

## B. Mechanism

ECM proteins bind adhesion receptors and can retain or present growth factors. Therefore signal availability depends on local organization as well as secretion.[^ECM] Mechanical coupling through adhesion structures and the cytoskeleton can transmit forces and influence cellular responses; stiffness and applied force are not the same quantity.[^MECH]

A cell's response also depends on its own competence. Two neighbors may face different surfaces, signals or mechanical conditions, and may respond differently to a shared signal.[^SIGNAL]

## C. Relationship to prior concepts

Regulation and signaling give mechanisms for environment-dependent states. Adhesion connects cells to one another and to matrix; cell activity can in turn remodel the environment. This feedback prevents treating spatial context as an independent additive explanation.

## D. Experimental observation/measurement

Matrix labeling and microscopy address composition and organization. Mechanical probing addresses physical properties, while local ligand or response observations address biochemical effects.[^ECM][^MECH] Demonstrating a niche requires evidence concerning the supported cell function, not just a region name.[^NICHE]

## E. Computational representation

Proposed synthetic metadata:

| observation | compartment | matrix_contact | local_stiffness_Pa | survival_support |
|---|---|---|---|---|
| A | region R | observed | unknown | untested |

Pa means pascals. Unknown stiffness must not become zero. Possible forms: environmental feature vectors, spatial fields, continuous mechanical measurements, sets of neighboring entities and uncertain niche labels. These are alternatives with different semantics.

## F. Relevance to our project

LN stroma and neural developmental environments motivate recording context. Future paired molecular measurements could help connect response with state, but proximity alone does not measure the environment. No niche annotation or mechanical estimate is assigned to project observations.

## G. Common misconceptions

ECM ≠ inert filler; stroma ≠ all one lineage; niche ≠ any nearby group. A region with many progenitors does not by itself demonstrate that the region maintains stem-cell capacity. More detailed mechanobiology remains future depth, not a prerequisite for assigning hypothetical stiffness values.

## H. Evidence

[^ECM]: Hynes RO (2009). [The extracellular matrix: not just pretty fibrils](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536535/). Science. DOI: 10.1126/science.1176009. Supporting location/access: [source ECM](SOURCES.md#ecm).

[^STROMA]: Mueller SN; Germain RN (2009). [Stromal cell contributions to the homeostasis and functionality of the immune system](https://www.nature.com/articles/nri2588). Nature Reviews Immunology. DOI: 10.1038/nri2588. Supporting location/access: [source STROMA](SOURCES.md#stroma).

[^NICHE]: Scadden DT (2006). [The stem-cell niche as an entity of action](https://pubmed.ncbi.nlm.nih.gov/16810242/). Nature. DOI: 10.1038/nature04957. Supporting location/access: [source NICHE](SOURCES.md#niche).

[^MECH]: Wang N; Tytell JD; Ingber DE (2009). [Mechanotransduction at a distance: mechanically coupling the extracellular matrix with the nucleus](https://pubmed.ncbi.nlm.nih.gov/19197334/). Nature Reviews Molecular Cell Biology. DOI: 10.1038/nrm2594. Supporting location/access: [source MECH](SOURCES.md#mech).

[^SIGNAL]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [General Principles of Cell Communication](https://www.ncbi.nlm.nih.gov/books/NBK26813/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source SIGNAL](SOURCES.md#signal).


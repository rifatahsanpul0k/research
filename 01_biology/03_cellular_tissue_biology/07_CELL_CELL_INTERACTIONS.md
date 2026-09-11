# Cell–cell interactions

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

An interaction is a specified influence or physical relationship between cells. Contact, adhesion, molecular communication and a functional outcome are distinguishable observations. Two cells can be adjacent without engaging the signaling mechanism of interest; extracellular signals can act without persistent cell contact.[^SIGNAL]

## B. Mechanism

Cadherin-containing junctions connect adjacent cells and couple to intracellular structures; gap junctions permit exchange of small signals. Adhesion is therefore a molecularly organized process, not merely short centroid distance.[^JUNCTION]

In immune tissue, antigen-presenting cells and lymphocytes participate in recognition and response; stromal cells help arrange the encounters. These are relationships between potentially dissimilar cells, rather than a requirement for equal molecular profiles.[^IMMUNE][^STROMA]

## C. Relationship to prior concepts

Signaling is one form of interaction. Interactions can modify the local environment, which feeds back on cell behavior. A contact diagram would encode a different claim from a molecular-similarity diagram.

## D. Experimental observation/measurement

Imaging can establish contact and duration; labeling molecular partners can identify structures at interfaces. In mouse lymph nodes, combined microscopy connected lymphocyte movements with supporting stromal structures.[^MIGLN] This is direct spatial observation in a reported system, not proof that every close pair in a new sample communicates.

## E. Computational representation

Synthetic records with separate evidence dimensions:

| pair | centroid_distance_µm | membrane_contact | ligand_delivery | response |
|---|---:|---|---|---|
| A,B | 8 | observed | unknown | unknown |
| A,C | 80 | not_observed | unknown | unknown |

Observation time, image dimension and confidence would also be needed. A table can preserve heterogeneous evidence; a network could encode pair relations; a hypergraph could describe a multicellular group. Group membership alone would not establish all pairwise interactions.

## F. Relevance to our project

LN immune encounters and developing tissue coordination require more than proximity. For future single-cell/spatial multi-omics interpretation, keep the sampled entities and molecular evidence explicit. A dissimilar pair may be functionally complementary; this is not a reason to rank a representation now.

## G. Common misconceptions

Proximity ≠ contact; contact ≠ adhesion mechanism; adhesion ≠ particular signaling response; shared pathway expression ≠ interaction. Negative evidence requires an observation capable of detecting the event, not merely an empty field. Open question: are any contact or response measurements present in the project? Unknown.

## H. Evidence

[^SIGNAL]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [General Principles of Cell Communication](https://www.ncbi.nlm.nih.gov/books/NBK26813/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source SIGNAL](SOURCES.md#signal).

[^JUNCTION]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Cell Junctions](https://www.ncbi.nlm.nih.gov/books/NBK26857/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source JUNCTION](SOURCES.md#junction).

[^IMMUNE]: Janeway CA Jr; Travers P; Walport M; Shlomchik MJ (2001). [The components of the immune system](https://www.ncbi.nlm.nih.gov/books/NBK27092/). Immunobiology: The Immune System in Health and Disease, 5th edition. DOI: unknown. Supporting location/access: [source IMMUNE](SOURCES.md#immune).

[^STROMA]: Mueller SN; Germain RN (2009). [Stromal cell contributions to the homeostasis and functionality of the immune system](https://www.nature.com/articles/nri2588). Nature Reviews Immunology. DOI: 10.1038/nri2588. Supporting location/access: [source STROMA](SOURCES.md#stroma).

[^MIGLN]: Bajénoff M; Egen JG; Koo LY; Laugier JP; Brau F; Glaichenhaus N; Germain RN (2006). [Stromal cell networks regulate lymphocyte entry, migration, and territoriality in lymph nodes](https://pubmed.ncbi.nlm.nih.gov/17112751/). Immunity. DOI: 10.1016/j.immuni.2006.10.011. Supporting location/access: [source MIGLN](SOURCES.md#migln).


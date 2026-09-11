# Tissue organization

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

A tissue contains organized cells and extracellular components. A layer is a spatial arrangement; a region is a delimited anatomical area; a compartment implies organizational separation; a functional unit supports a biological operation. A niche adds a functionally specified local environment. These descriptions can overlap without being synonymous.[^JUNCTION][^NICHE]

## B. Mechanism

Cell adhesion, migration and local signals contribute to organization. Junctions can maintain tissue continuity and selective boundaries.[^JUNCTION] In lymph nodes, anatomical zones organize antigen encounters; in developing cortex, production and migration of neurons generate laminar organization.[^IMMUNE][^MIG] Thus tissue architecture is produced and maintained by cellular processes.

## C. Relationship to prior concepts

Microenvironment emphasizes what a cell experiences locally. Tissue organization asks how such environments and populations are arranged across a larger structure. A cell-type class is an “is-a” relation; a region inside an organ is a “part-of” relation.

## D. Experimental observation/measurement

Histological sections reveal morphology and compartments. Multiple sections or volumetric observations are needed to address three-dimensional continuity; a single plane gives a particular view. Developmental staging criteria supply anatomical reference context rather than labels for an unexamined specimen.[^HIST][^STAGE]

## E. Computational representation

Synthetic location table:

| observation | type_label | region_label | section | coordinate_frame | region_evidence |
|---|---|---|---|---|---|
| A | type T | R1 | s1 | frame_s1 | manual_morphology |
| B | type B | R1 | s1 | frame_s1 | manual_morphology |
| C | type T | R2 | s1 | frame_s1 | manual_morphology |

This logically permits different types in one region and the same type in different regions. Region masks, polygons, categorical tables, sets and spatial tensors could store organizational evidence. A polygon is an annotation boundary, not itself a proven biological barrier.

## F. Relevance to our project

The LN cortex and brain cortex share a word, not an anatomical identity. Preserve organism, organ and region vocabulary. Future representation evaluation should distinguish type recovery from anatomical recovery; a single label would conflate those tasks.

## G. Common misconceptions

Nearby cells need not be the same type; the same type need not be nearby. One two-dimensional section does not guarantee complete coverage of an organ. Regions are not necessarily homogeneous. Check: cells with identical type labels in separate follicles are not required to have adjacent positions.

## H. Evidence

[^JUNCTION]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Cell Junctions](https://www.ncbi.nlm.nih.gov/books/NBK26857/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source JUNCTION](SOURCES.md#junction).

[^NICHE]: Scadden DT (2006). [The stem-cell niche as an entity of action](https://pubmed.ncbi.nlm.nih.gov/16810242/). Nature. DOI: 10.1038/nature04957. Supporting location/access: [source NICHE](SOURCES.md#niche).

[^IMMUNE]: Janeway CA Jr; Travers P; Walport M; Shlomchik MJ (2001). [The components of the immune system](https://www.ncbi.nlm.nih.gov/books/NBK27092/). Immunobiology: The Immune System in Health and Disease, 5th edition. DOI: unknown. Supporting location/access: [source IMMUNE](SOURCES.md#immune).

[^MIG]: Nadarajah B; Parnavelas JG (2002). [Modes of neuronal migration in the developing cerebral cortex](https://www.nature.com/articles/nrn845). Nature Reviews Neuroscience. DOI: 10.1038/nrn845. Supporting location/access: [source MIG](SOURCES.md#mig).

[^HIST]: Mercadante AA; Tadi P (2023). [Histology, Lymph Nodes](https://www.ncbi.nlm.nih.gov/books/NBK559053/). StatPearls. DOI: unknown. Supporting location/access: [source HIST](SOURCES.md#hist).

[^STAGE]: eMouseAtlas / EMAP (unknown). [Staging Criteria](https://www.emouseatlas.org/emap/ema/staging_criteria/staging_criteria.html). eMouseAtlas. DOI: not_applicable. Supporting location/access: [source STAGE](SOURCES.md#stage).


# Six distinct biological relationships

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Molecular resemblance, physical proximity, functional resemblance, regulatory resemblance, ancestry and interaction answer different questions. Identity has multiple biological aspects, and historical evidence adds information absent from a snapshot.[^IDENT][^LINE] The following notation declares intended meanings; it does not specify a model.

## B. Mechanism

Coordinated regulation can support similar outputs, while signaling can connect cells with different outputs. Migration can change position without making a new lineage. These mechanisms allow relationships to correlate, diverge or change with time.[^TF][^SIGNAL][^MIG]

## C. Relationship to prior concepts

Identity/state (1), lineage (4), interactions (7) and organization (9) supply the biological distinctions. A relationship should be selected by the biological question, not silently inherited from whichever table is easiest to compute.

## D. Experimental observation/measurement

Molecular assays, functional observations, regulatory evidence, spatial imaging and lineage observations support different relation types. A particular modality may be missing; an inferred label is not independent evidence if it comes from the same measured profile.[^TYPE][^LINE]

## E. Computational representation

Let i and j index observations, not necessarily cells. Define:

| Symbol | Meaning | Possible forms, without preference |
|---|---|---|
| Sᵐᵒˡᵉᶜᵘˡᵃʳᵢⱼ | Similarity of specified measured molecular features | vectors; similarity matrices; kernels; latent variables |
| Dˢᵖᵃᵗⁱᵃˡᵢⱼ | Physical separation in a common coordinate frame | coordinate arrays; distance matrices |
| Sᶠᵘⁿᶜᵗⁱᵒⁿᵃˡᵢⱼ | Resemblance of specified functions | functional scores; membership sets; distributions |
| Sʳᵉᵍᵘˡᵃᵗᵒʳʸᵢⱼ | Resemblance of supported regulatory programs | feature matrices; evidence tables; networks |
| Lᵢⱼ | Declared ancestry relation, possibly unknown | lineage tables/trees; ancestry distributions |
| Eᵢⱼ | Evidence for a specified interaction | directed event tables; networks; group hypergraphs |

Equivalently the requested notation is \(S^{molecular}_{ij}, D^{spatial}_{ij}, S^{functional}_{ij}, S^{regulatory}_{ij}\). No numerical scale is fixed for S, L or E. Smaller D means closer spatially; a larger S would mean more similar only after choosing a convention. E may be directed. A kernel is a specified pairwise function; it is not automatically biological evidence or a valid positive-semidefinite kernel merely because it is called similarity.

For two-dimensional positions s_i=(a_i,b_i) measured in µm, one illustrative geometric distance is \(D^{spatial}_{ij}=\sqrt{(a_i-a_j)^2+(b_i-b_j)^2}\). Here a and b are coordinate components. This says nothing about traversable paths or communication.

## F. Relevance to our project

In future representation research, each relation needs its own target, evidence and uncertainty. Across stages, comparable function need not mean equal expression or shared immediate ancestry. No candidate computational form is ranked or constructed.

## G. Common misconceptions

Same coordinates in different unregistered sections do not imply proximity. Shared ancestry does not require matching state. Complementary interacting cells need not be similar. Undefined interaction evidence must not become a zero-valued molecular similarity. Answered counterexample: a T cell beside a stromal cell can be close, different in type and potentially interacting, with ancestry unresolved.

## H. Evidence

[^IDENT]: Morris SA (2019). [The evolving concept of cell identity in the single cell era](https://pubmed.ncbi.nlm.nih.gov/31249002/). Development. DOI: 10.1242/dev.169748. Supporting location/access: [source IDENT](SOURCES.md#ident).

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). Nature Reviews Genetics. DOI: 10.1038/s41576-020-0223-2. Supporting location/access: [source LINE](SOURCES.md#line).

[^TF]: Spitz F; Furlong EEM (2012). [Transcription factors: from enhancer binding to developmental control](https://www.nature.com/articles/nrg3207). Nature Reviews Genetics. DOI: 10.1038/nrg3207. Supporting location/access: [source TF](SOURCES.md#tf).

[^SIGNAL]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [General Principles of Cell Communication](https://www.ncbi.nlm.nih.gov/books/NBK26813/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source SIGNAL](SOURCES.md#signal).

[^MIG]: Nadarajah B; Parnavelas JG (2002). [Modes of neuronal migration in the developing cerebral cortex](https://www.nature.com/articles/nrn845). Nature Reviews Neuroscience. DOI: 10.1038/nrn845. Supporting location/access: [source MIG](SOURCES.md#mig).

[^TYPE]: Zeng H (2022). [What is a cell type and how to define it?](https://pubmed.ncbi.nlm.nih.gov/35868277/). Cell. DOI: 10.1016/j.cell.2022.06.031. Supporting location/access: [source TYPE](SOURCES.md#type).


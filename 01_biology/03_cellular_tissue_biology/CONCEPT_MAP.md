# From molecular programs to cells and tissues

This is a biological teaching map. Arrows indicate influence or a conceptual connection; they are not chemical conversions, proven dataset edges or a computational representation selected for the project.

```text
DNA / regulation
      |
      v
molecular program (RNA; protein abundance, location and activity)
      |
      v
cell identity / state
      |                         |
      v                         v
signaling <--------------> differentiation
      |                         |
      +-------------+-----------+
                    v
             cell interactions
                    |
                    v
             microenvironment
                    |
                    v
             tissue organization
                    |
                    v
       spatial biological structure
```

Regulation controls molecular output; protein activity feeds back on regulation.[^REG][^PROT] Signaling changes responses and can affect developmental decisions.[^SIGNAL][^TF] Cell adhesion and extracellular organization support tissue structure, while tissue context feeds back on cells.[^JUNCTION][^ECM] Therefore the downward teaching order is not a one-way biological pipeline. Differentiation does not require every preceding event in this diagram to occur as a discrete step.

Developmental time adds:

```text
state of a cell at t -> state of that cell at t+Δt
         or division -> states of descendants at t+Δt
```

Here t denotes observation time and Δt a later positive interval. These arrows are conceptual possibilities. Cross-sectional samples at E11/E13/E15/E18 do not demonstrate that the same cell, its descendants or the same embryo was tracked.[^LINE] They can instead sample different populations while development changes composition and architecture.[^DEV]

| Connection | What it permits us to ask | What it does not establish |
|---|---|---|
| Regulation → phenotype | Which programs support a property? | RNA is identical to protein function |
| Identity + context → state | How does this type respond here? | Every state is a new type |
| Signaling → response | Is delivery and response supported? | Ligand/receptor expression proves communication |
| Differentiation → lineage question | What outputs arise from a precursor? | Molecular resemblance is ancestry |
| Organization → spatial relationships | Which cells/regions are arranged together? | Nearby means the same type |
| Stage → changing populations | What changes across development? | A later row is an earlier row's descendant |

The two systems instantiate different portions of this map. LN follicles, T-cell territories, stroma and vascular/sinus routes organize encounters.[^STROMA] Embryonic brain progenitor compartments, cell birth and migration organize developing tissue.[^NEURO][^MIG] Neither example supplies verified dataset labels.

## Ordered reading route
1. [Cell Identity](01_CELL_IDENTITY.md)
2. [Cellular Heterogeneity](02_CELLULAR_HETEROGENEITY.md)
3. [Differentiation](03_DIFFERENTIATION.md)
4. [Cell Lineage](04_CELL_LINEAGE.md)
5. [Cell Cycle](05_CELL_CYCLE.md)
6. [Cell Signaling](06_CELL_SIGNALING.md)
7. [Cell Cell Interactions](07_CELL_CELL_INTERACTIONS.md)
8. [Microenvironment](08_MICROENVIRONMENT.md)
9. [Tissue Organization](09_TISSUE_ORGANIZATION.md)
10. [Spatial Biological Relationships](10_SPATIAL_BIOLOGICAL_RELATIONSHIPS.md)
11. [Boundaries And Transitions](11_BOUNDARIES_AND_TRANSITIONS.md)
12. [Lymph Node Foundations](12_LYMPH_NODE_FOUNDATIONS.md)
13. [Lymph Node Spatial Biology](13_LYMPH_NODE_SPATIAL_BIOLOGY.md)
14. [Embryonic Mouse Brain](14_EMBRYONIC_MOUSE_BRAIN.md)
15. [Developmental Time](15_DEVELOPMENTAL_TIME.md)
16. [Observation Units](16_OBSERVATION_UNITS.md)
17. [Biological Annotation](17_BIOLOGICAL_ANNOTATION.md)
18. [Biological Hierarchy](18_BIOLOGICAL_HIERARCHY.md)

End with [biology to data](BIOLOGY_TO_DATA.md), then the [conceptual checks and readiness record](VALIDATION.md). The molecular, spatial, functional, regulatory, lineage and interaction distinctions must survive every transition in this map.

## Evidence

[^REG]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [An Overview of Gene Control](https://www.ncbi.nlm.nih.gov/books/NBK26885/). See [source REG](SOURCES.md#reg) for identifiers and access depth.

[^PROT]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/). See [source PROT](SOURCES.md#prot) for identifiers and access depth.

[^SIGNAL]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [General Principles of Cell Communication](https://www.ncbi.nlm.nih.gov/books/NBK26813/). See [source SIGNAL](SOURCES.md#signal) for identifiers and access depth.

[^TF]: Spitz F; Furlong EEM (2012). [Transcription factors: from enhancer binding to developmental control](https://www.nature.com/articles/nrg3207). See [source TF](SOURCES.md#tf) for identifiers and access depth.

[^JUNCTION]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Cell Junctions](https://www.ncbi.nlm.nih.gov/books/NBK26857/). See [source JUNCTION](SOURCES.md#junction) for identifiers and access depth.

[^ECM]: Hynes RO (2009). [The extracellular matrix: not just pretty fibrils](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536535/). See [source ECM](SOURCES.md#ecm) for identifiers and access depth.

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). See [source LINE](SOURCES.md#line) for identifiers and access depth.

[^DEV]: Jabaudon D (2017). [Fate and freedom in developing neocortical circuits](https://www.nature.com/articles/ncomms16042). See [source DEV](SOURCES.md#dev) for identifiers and access depth.

[^STROMA]: Mueller SN; Germain RN (2009). [Stromal cell contributions to the homeostasis and functionality of the immune system](https://www.nature.com/articles/nri2588). See [source STROMA](SOURCES.md#stroma) for identifiers and access depth.

[^NEURO]: Götz M; Huttner WB (2005). [The cell biology of neurogenesis](https://www.nature.com/articles/nrm1739). See [source NEURO](SOURCES.md#neuro) for identifiers and access depth.

[^MIG]: Nadarajah B; Parnavelas JG (2002). [Modes of neuronal migration in the developing cerebral cortex](https://www.nature.com/articles/nrn845). See [source MIG](SOURCES.md#mig) for identifiers and access depth.


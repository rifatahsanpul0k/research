# Embryonic mouse-brain foundations

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Embryonic brain development involves production, specification, movement and maturation of cells within a changing structure. Neural tube formation establishes an early epithelial organization from which central nervous system development proceeds.[^TUBE] Embryonic tissue is not an adult brain scaled down: progenitor compartments and ongoing cell production are central to its interpretation.[^NEURO]

## B. Mechanism

| Process | Biological meaning and mechanism |
|---|---|
| Proliferation | Divisions expand progenitor numbers; division outcome determines whether the pool is maintained or produces differentiating descendants |
| Neurogenesis | Neural progenitors generate neurons, directly or through intermediate progenitors |
| Differentiation | Regulatory and expression changes establish specialized neuronal or glial properties |
| Migration | Cells move from sites of production toward other tissue locations |
| Gliogenesis | Production of macroglial lineages, including astrocytes and oligodendrocytes, with timing and competence dependent on region and development |

Neuroepithelial cells, radial glia and basal/intermediate progenitors are foundational progenitor categories. Radial glia are both progenitors and part of the structural context for migration.[^NEURO][^GLIA]

In the developing cortex, projection neurons largely migrate radially; cortical interneurons can originate in ventral telencephalic regions and migrate tangentially. The inside-out sequence for layers II–VI means that later-born neurons generally settle more superficially than earlier-born ones; this is not a rule for every brain region or all cortical cells.[^MIG]

A cortical wall can contain ventricular zone (VZ), subventricular zone (SVZ), migrating cells and cortical plate. Their composition and extent change as direct and indirect neurogenesis proceed.[^DEV] Spatially graded signals can influence regional regulatory responses.[^GRAD] Gliogenesis overlaps developmental changes rather than obeying one brain-wide switch. Traced radial glial cells can produce neurons and subsequently differentiate into astroglial cells, demonstrating a temporal change of output within at least some progenitor lineages; this is not a claim that every progenitor has identical potential.[^GLIA] Microglia require a distinct ancestry: mouse fate mapping supports primitive macrophage origin, so “glia” does not mean one neural-progenitor lineage.[^GLIA][^MICRO]

## C. Relationship to prior concepts

This joins proliferation (5), differentiation (3), ancestry (4), movement and organization (9). A changing transcriptional program can reflect progenitor competence, newly differentiated function or maturation; a current location need not be the birthplace.[^DEV][^MIG]

## D. Experimental observation/measurement

Staged histology observes developing compartments. DNA-synthesis labeling provides birthdating-related information; lineage studies address ancestry; live observation addresses migration. Molecular labeling identifies expression domains, but a marker or position alone does not establish a complete developmental history.[^CYCLE][^LINE][^MIG] No protocols or dataset-specific annotation are developed.

## E. Computational representation

A hypothetical metadata schema:

| observation | stage_label | anatomical_domain | developmental_role | lineage_evidence |
|---|---|---|---|---|
| A | E13 | unknown | progenitor_candidate | unknown |
| B | E15 | unknown | differentiating_candidate | unknown |

These invented rows do not annotate the supplied mouse datasets. Stage-by-region tables, categorical roles, molecular matrices, trajectory hypotheses and spatiotemporal tensors are possible forms. A tensor needs explicit axes and missingness; it does not imply that the same cell was followed.

## F. Relevance to our project

Mouse_Brain_E11_S1, E13_S1, E15_S1 and E18_S1 motivate studying changing progenitor output and tissue pattern. Cortical examples explain principles without assuming those folders contain cortex, a particular cutting plane or the same embryo. S1 remains a supplied label, not an inferred “somatosensory cortex” annotation.

## G. Common misconceptions

Proliferation ≠ neurogenesis; migration ≠ differentiation; postmitotic ≠ fully mature; radial glia ≠ only passive guides; all glia ≠ one ancestry. E18 does not imply adult organization. Check: a neuron farther from a germinal zone may have migrated; distance alone cannot establish its age or parent.[^MIG][^DEV]

## H. Evidence

[^TUBE]: Gilbert SF (2000). [Formation of the Neural Tube](https://www.ncbi.nlm.nih.gov/books/NBK10080/). Developmental Biology, 6th edition. DOI: unknown. Supporting location/access: [source TUBE](SOURCES.md#tube).

[^NEURO]: Götz M; Huttner WB (2005). [The cell biology of neurogenesis](https://www.nature.com/articles/nrm1739). Nature Reviews Molecular Cell Biology. DOI: 10.1038/nrm1739. Supporting location/access: [source NEURO](SOURCES.md#neuro).

[^GLIA]: Kriegstein A; Alvarez-Buylla A (2009). [The glial nature of embryonic and adult neural stem cells](https://pubmed.ncbi.nlm.nih.gov/19555289/). Annual Review of Neuroscience. DOI: 10.1146/annurev.neuro.051508.135600. Supporting location/access: [source GLIA](SOURCES.md#glia).

[^MIG]: Nadarajah B; Parnavelas JG (2002). [Modes of neuronal migration in the developing cerebral cortex](https://www.nature.com/articles/nrn845). Nature Reviews Neuroscience. DOI: 10.1038/nrn845. Supporting location/access: [source MIG](SOURCES.md#mig).

[^DEV]: Jabaudon D (2017). [Fate and freedom in developing neocortical circuits](https://www.nature.com/articles/ncomms16042). Nature Communications. DOI: 10.1038/ncomms16042. Supporting location/access: [source DEV](SOURCES.md#dev).

[^GRAD]: Ashe HL; Briscoe J (2006). [The interpretation of morphogen gradients](https://pubmed.ncbi.nlm.nih.gov/16410409/). Development. DOI: 10.1242/dev.02238. Supporting location/access: [source GRAD](SOURCES.md#grad).

[^MICRO]: Ginhoux F; Greter M; Leboeuf M; Nandi S; See P; Gokhan S; Mehler MF; Conway SJ; Ng LG; Stanley ER; Samokhvalov IM; Merad M (2010). [Fate mapping analysis reveals that adult microglia derive from primitive macrophages](https://pubmed.ncbi.nlm.nih.gov/20966214/). Science. DOI: 10.1126/science.1194637. Supporting location/access: [source MICRO](SOURCES.md#micro).

[^CYCLE]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [An Overview of the Cell Cycle](https://www.ncbi.nlm.nih.gov/books/NBK26869/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source CYCLE](SOURCES.md#cycle).

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). Nature Reviews Genetics. DOI: 10.1038/s41576-020-0223-2. Supporting location/access: [source LINE](SOURCES.md#line).


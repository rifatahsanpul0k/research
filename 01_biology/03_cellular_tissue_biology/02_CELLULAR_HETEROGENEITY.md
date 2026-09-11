# Cellular heterogeneity

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Heterogeneity is variation among cells, including within a named population. A useful explanatory inventory separates biological variation from variation introduced by observation. These sources can covary and need not be recoverable independently from one table.[^HET]

## B. Mechanism

| Source | Biological mechanism or origin |
|---|---|
| Genetic | Somatic mutations can generate different genomes within an individual[^MOSAIC] |
| Epigenetic | Persistent regulatory differences can maintain different responses[^EPI] |
| Transcriptional | Differences in RNA production and removal change RNA abundance[^REG] |
| Protein | Synthesis, degradation, modification and localization distinguish abundance from activity[^PROT] |
| Signaling | Exposure and response competence vary[^SIGNAL] |
| Developmental history | Descendants inherit histories not specified by current similarity[^LINE] |
| Cell cycle | DNA replication and division require regulated molecular programs[^CYCREG] |
| Metabolic | Mitochondrial content and physiological variation contribute to differences between cells[^METAB] |
| Environment | Matrix-associated signals differ locally[^ECM] |
| Technical | Sampling and measurement introduce incomplete detection and other variability[^TECH] |

This is an inventory, not a fitted decomposition of the project data.

## C. Relationship to prior concepts

Type is one part of the variation described in topic 1. Differentiation and signaling can change multiple components together; one cannot conclude that correlated columns represent independent mechanisms.[^HET]

## D. Experimental observation/measurement

DNA observations address genetic variation; RNA and protein measurements address different outputs; mitochondrial functional observations address physiology. An RNA-based metabolic label is not a measurement of metabolic flux.[^MOSAIC][^METAB][^PROT] Replicate and measurement-control information is needed to assess technical explanations.[^TECH]

## E. Computational representation

Synthetic counts, with type known independently only for this example:

| cell | type | gene A | gene B | cycle_context |
|---|---|---:|---:|---|
| C1 | type T | 8 | 2 | noncycling |
| C2 | type T | 2 | 8 | cycling |

Numerical difference does not logically contradict shared type. Conversely, observing `(8,2)` in two cells cannot determine unmeasured proteins, genotype or history. The example does not claim that these invented genes are cycle markers.

Possible forms include covariate tables, measurement vectors, uncertainty distributions and modality-indexed tensors; no form uniquely identifies a cause.

## F. Relevance to our project

In lymph node and embryonic brain, preserve specimen, stage and observation-unit metadata before interpreting variation. Future biological similarity must name the relevant variation; removing all differences could erase biology, while treating every difference as identity could exaggerate diversity. Neither action is performed here.

## G. Common misconceptions

Technical variability is not always negligible and biological variability is not always a new subtype. Equal measurements mean equality only of those recorded values under that measurement definition. Open question: which sources actually dominate our datasets? It cannot be answered without verified assays and specimens.

## H. Evidence

[^HET]: Wagner A; Regev A; Yosef N (2016). [Revealing the vectors of cellular identity with single-cell genomics](https://pmc.ncbi.nlm.nih.gov/articles/PMC5465644/). Nature Biotechnology. DOI: 10.1038/nbt.3711. Supporting location/access: [source HET](SOURCES.md#het).

[^MOSAIC]: Freed D; Stevens EL; Pevsner J (2014). [Somatic mosaicism in the human genome](https://pubmed.ncbi.nlm.nih.gov/25513881/). Genes. DOI: 10.3390/genes5041064. Supporting location/access: [source MOSAIC](SOURCES.md#mosaic).

[^EPI]: Berger SL; Kouzarides T; Shiekhattar R; Shilatifard A (2009). [An operational definition of epigenetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3959995/). Genes & Development. DOI: 10.1101/gad.1787609. Supporting location/access: [source EPI](SOURCES.md#epi).

[^REG]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [An Overview of Gene Control](https://www.ncbi.nlm.nih.gov/books/NBK26885/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source REG](SOURCES.md#reg).

[^PROT]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source PROT](SOURCES.md#prot).

[^SIGNAL]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [General Principles of Cell Communication](https://www.ncbi.nlm.nih.gov/books/NBK26813/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source SIGNAL](SOURCES.md#signal).

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). Nature Reviews Genetics. DOI: 10.1038/s41576-020-0223-2. Supporting location/access: [source LINE](SOURCES.md#line).

[^CYCREG]: Bertoli C; Skotheim JM; de Bruin RAM (2013). [Control of cell cycle transcription during G1 and S phases](https://pmc.ncbi.nlm.nih.gov/articles/PMC4569015/). Nature Reviews Molecular Cell Biology. DOI: 10.1038/nrm3629. Supporting location/access: [source CYCREG](SOURCES.md#cycreg).

[^METAB]: Aryaman J; Johnston IG; Jones NS (2019). [Mitochondrial Heterogeneity](https://pubmed.ncbi.nlm.nih.gov/30740126/). Frontiers in Genetics. DOI: 10.3389/fgene.2018.00718. Supporting location/access: [source METAB](SOURCES.md#metab).

[^ECM]: Hynes RO (2009). [The extracellular matrix: not just pretty fibrils](https://pmc.ncbi.nlm.nih.gov/articles/PMC3536535/). Science. DOI: 10.1126/science.1176009. Supporting location/access: [source ECM](SOURCES.md#ecm).

[^TECH]: Laehnemann D; Koester J; Szczurek E; McCarthy DJ; Hicks SC; Robinson MD; Vallejos CA; Campbell KR; Beerenwinkel N; Mahfouz A; Pinello L; Skums P; Stamatakis A; Stephan-Otto Attolini C; Aparicio S; Baaijens J; Balvert M; Dutilh BE; Guryev V; Marioni JC; Stegle O; Theis FJ; McHardy AC; Raphael BJ; Shah SP; Schoenhuth A; et al. (2020). [Eleven grand challenges in single-cell data science](https://link.springer.com/article/10.1186/s13059-020-1926-6). Genome Biology. DOI: 10.1186/s13059-020-1926-6. Supporting location/access: [source TECH](SOURCES.md#tech).


# Sources used in Phase 1E

Existing Phase 1D sources S01–S35 remain applicable; this phase adds:

- **S36** Brennecke P, Anders S, Kim JK, et al. *Accounting for technical noise in single-cell RNA-seq experiments*. Nature Methods 10, 1093–1095 (2013). DOI: [10.1038/nmeth.2645](https://www.nature.com/articles/nmeth.2645). Mean–variance technical noise and HVG rationale.
- **S37** Hafemeister C, Satija R. *Normalization and variance stabilization of single-cell RNA-seq data using regularized negative binomial regression*. Genome Biology 20, 296 (2019). DOI: [10.1186/s13059-019-1874-1](https://link.springer.com/article/10.1186/s13059-019-1874-1). Count modeling and variance stabilization.
- **S38** Bioconductor OSCA Basic, “Normalization”. [Official chapter](https://www.bioconductor.org/books/3.19/OSCA.basic/normalization.html). Size-factor assumptions and alternatives.
- **S39** Bioconductor OSCA Basic, “Data infrastructure”. [Official chapter](https://bioconductor.org/books/3.12/OSCA/data-infrastructure.html). Size-factor semantics.
- **S40** Bacher R, Chu LF, Leng N, et al. *SCnorm: robust normalization of single-cell RNA-seq data*. Nature Methods 14, 584–586 (2017). DOI: [10.1038/nmeth.4263](https://www.nature.com/articles/nmeth.4263).
- **S41** Lun ATL, McCarthy DJ, Marioni JC. *A step-by-step workflow for low-level analysis of single-cell RNA-seq data with Bioconductor*. Genome Biology 17, 74 (2016). DOI: [10.1186/s13059-016-0947-7](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0947-7). scran pooling.
- **S42** Brennecke et al. [S36] is also the primary source for abundance-dependent technical variance and variable-gene selection.
- **S43** Stuart T, Satija R. *Integrative single-cell analysis*. Nature Reviews Genetics 20, 257–272 (2019). DOI: [10.1038/s41576-019-0093-7](https://www.nature.com/articles/s41576-019-0093-7). Integration, batch and modality context.
- **S44** Cusanovich DA, Daza R, Adey A, et al. *Multiplex single cell profiling of chromatin accessibility by combinatorial cellular indexing*. Science 348, 910–914 (2015). DOI: [10.1126/science.aab1601](https://pmc.ncbi.nlm.nih.gov/articles/PMC4836442/). scATAC features and TF-IDF/LSI context.
- **S45** Stuart T, Butler A, Hoffman P, et al. *Comprehensive integration of single-cell data*. Cell 177, 1888–1902 (2019). DOI: [10.1016/j.cell.2019.05.031](https://pubmed.ncbi.nlm.nih.gov/31178118/). Modality-aware preprocessing context.
- **S46** McGinnis CS, Murrow LM, Gartner ZJ. *DoubletFinder: Doublet detection in single-cell RNA sequencing data using artificial nearest neighbors*. Cell Systems 8, 329–337 (2019). DOI: [10.1016/j.cels.2019.03.003](https://pmc.ncbi.nlm.nih.gov/articles/PMC6853612/).
- **S47** Young MD, Behjati S. *SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data*. GigaScience 9, giaa151 (2020). DOI: [10.1093/gigascience/giaa151](https://pmc.ncbi.nlm.nih.gov/articles/PMC7763177/).
- **S48** Yang S, Corbett SE, Koga Y, et al. *Decontamination of ambient RNA in single-cell RNA-seq with DecontX*. Genome Biology 21, 57 (2020). DOI: [10.1186/s13059-020-1950-6](https://link.springer.com/article/10.1186/s13059-020-1950-6).

Technical documentation and local source studies used: AnnData format [S22], 10x HDF5 matrix [S20], GEO/MISAR/SMART [S27,S29,S33,S34], and lymph-node ADT background [S07]. Sources are used for biological/statistical rationale or documented file semantics; software defaults are not treated as universal biological rules.

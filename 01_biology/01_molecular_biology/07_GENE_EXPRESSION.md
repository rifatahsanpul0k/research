# 07. Gene Expression

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

Gene expression is the production of a functional gene product from genetic information. For protein-coding genes this includes transcription into RNA and translation into protein; for non-coding RNA genes, expression can mean production of the functional RNA itself [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK21050/).

## B. Biological mechanism

Expression level depends on transcription initiation and elongation, RNA processing, RNA export, RNA stability, translation efficiency, protein folding, protein modification, and protein degradation. Cells regulate these steps to control molecular programs in different cell types and states [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26829/); [Shine et al. 2024](https://pubmed.ncbi.nlm.nih.gov/38509203/).

## C. Relationships

Expression integrates DNA, genes, transcription, RNA, translation, and proteins. It is the biological idea behind many matrix values, but the matrix value is a measurement proxy whose meaning depends on assay design.

## D. Experimental measurement

Expression can be measured at RNA level by RNA-seq or in situ methods and at protein level by antibody, mass spectrometry, reporter, or other protein assays. Single-cell RNA-seq produces noisy, sparse molecular count data in which zeros can have biological or technical causes [Luecken and Theis 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6582955/); [Amezquita et al. 2020](https://link.springer.com/article/10.1186/s13059-020-1926-6).

## E. Numerical/computational representation

Common matrix form:

| cell_id | GeneA | GeneB | GeneC |
|---|---:|---:|---:|
| C1 | 8 | 0 | 3 |
| C2 | 1 | 6 | 2 |
| C3 | 7 | 0 | 4 |

Rows are observations, columns are gene features, and values are molecule counts or processed expression values. A metadata table may store batch, sample, tissue, coordinate, or quality fields.

## F. Relevance to our project

Expression is central to single-cell and spatial omics because it can reflect cell identity, activity, differentiation, and response. Multi-omics can compare RNA expression with protein abundance or regulatory signals. Biological similarity often starts from expression patterns, but representation learning must preserve the distinction between measurement similarity and biological equivalence.

## G. Misconceptions

- Treating normalized expression as raw molecular counts.
- Treating expression similarity as proof of same cell type.
- Ignoring sampling depth, capture efficiency, cell cycle, stress, and batch effects when comparing expression vectors.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6.
- Luecken and Theis, 2019, *Molecular Systems Biology*, single-cell RNA-seq best practices.
- Amezquita et al., 2020, *Genome Biology*, single-cell data challenges.


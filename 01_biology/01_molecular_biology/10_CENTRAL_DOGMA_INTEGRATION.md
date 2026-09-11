# 10. Relationship Between DNA -> RNA -> Protein

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

The DNA -> RNA -> protein relationship describes the core flow of genetic information: DNA stores sequence information, transcription copies selected DNA regions into RNA, and translation decodes protein-coding RNA into amino acid sequence. The framework is central, but it is not a claim that every gene produces a protein or that RNA and protein levels are identical [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK21050/).

## B. Biological mechanism

The central dogma specifically concerns transfer of residue-by-residue sequence information, rather than every causal influence within a cell. Protein-mediated feedback on transcription does not copy protein sequence into nucleic acid. RNA-to-DNA sequence transfer is compatible with this distinction; describing all departures from a simple DNA -> RNA -> protein diagram as exceptions to the dogma is misleading [Crick 1970](https://www.nature.com/articles/227561a0).

For a protein-coding gene, regulatory DNA helps determine transcription; RNA polymerase produces a transcript; eukaryotic RNA processing can alter transcript structure; ribosomes translate coding sequence; the protein folds and may be modified. For non-coding RNA genes, the RNA product can function without translation [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26887/); [Mattick et al. 2023](https://www.nature.com/articles/s41580-022-00566-8).

## C. Relationships

The complete Phase 1A chain is:

DNA -> chromosome/genome organization -> gene and regulatory context -> transcription -> RNA -> gene expression -> translation -> protein -> cellular function.

This is a study sequence, not a literal sequence of molecular conversions: chromosome organization is a property of DNA, and gene expression encompasses multiple processes rather than an extra reaction between RNA and translation. Later measurements can capture different points in this system, and those points are not interchangeable.

## D. Experimental measurement

Different assays observe different levels: DNA sequencing observes sequence; annotation maps genes and regions; RNA-seq observes RNA molecules or derived abundance; protein assays observe protein abundance or state; spatial assays attach measurements to tissue coordinates; multimodal assays combine levels [Baysoy et al. 2023](https://www.nature.com/articles/s41580-023-00615-w); [Argelaguet et al. 2021](https://www.nature.com/articles/s41587-021-00895-7).

## E. Numerical/computational representation

A compact multi-table representation:

| cell_id | GeneA_RNA | GeneB_RNA | ProteinA |
|---|---:|---:|---:|
| C1 | 8 | 0 | 12 |
| C2 | 1 | 6 | 0 |

| feature_id | molecule_level | source_gene | chromosome |
|---|---|---|---|
| GeneA_RNA | RNA | GeneA | chr1 |
| ProteinA | protein | GeneA | chr1 |

The two tables say that RNA and protein features can share a gene relationship while measuring different biological molecules.

## F. Relevance to our project

Single-cell and spatial multi-omics data turn parts of this biological chain into tabular measurements. Biological similarity may arise from shared genome-derived programs, but observed similarity depends on the measured molecule, timing, assay chemistry, normalization, and metadata. Representation learning can help organize high-dimensional data, but biological interpretation must return to the DNA -> RNA -> protein mechanism and the evidence level of each feature.

## G. Misconceptions

- Treating central dogma as a one-to-one deterministic mapping from gene to mRNA to protein.
- Treating RNA counts as direct cellular function.
- Treating all cells with similar vectors as biologically equivalent without checking cell identity, tissue context, state, technical covariates, and modality.

## H. Evidence

- Crick F. (1970), [Central Dogma of Molecular Biology](https://www.nature.com/articles/227561a0), *Nature* 227:561-563. DOI: 10.1038/227561a0.

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6.
- Mattick et al., 2023, *Nature Reviews Molecular Cell Biology*.
- Argelaguet et al., 2021, *Nature Biotechnology*.
- Baysoy et al., 2023, *Nature Reviews Molecular Cell Biology*.

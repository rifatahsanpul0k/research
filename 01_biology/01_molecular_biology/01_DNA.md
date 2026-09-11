# 01. DNA

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

DNA, deoxyribonucleic acid, is the stable molecular store of inherited cellular information. It is a polymer made from four nucleotide bases, A, C, G, and T, arranged in sequence along two complementary strands. Biological information is carried by nucleotide order, while complementary base pairing allows the information to be copied and read [Alberts 2002, Ch. 4](https://www.ncbi.nlm.nih.gov/books/NBK26821/).

## B. Biological mechanism

Inside cells, DNA is chemically stable enough to preserve information across cell divisions but accessible enough to be copied and transcribed. The two strands pair through base complementarity, so one strand can guide synthesis of a complementary strand during replication or RNA synthesis. In eukaryotes, DNA is packaged with proteins into chromatin, which affects which regions can be read by transcription machinery [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK21050/); [Oudelaar and Higgs 2021](https://www.nature.com/articles/s41576-020-00303-x).

## C. Relationships

DNA is the substrate for chromosomes and genome organization. Specific genomic regions can be genes, regulatory elements, repeats, or other sequence classes. DNA is transcribed into RNA for many genes, and protein-coding RNAs can later be translated into proteins [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK21050/).

## D. Experimental measurement

DNA can be observed by sequencing, which reports nucleotide strings aligned to reference genomes; by cytogenetic and imaging methods that observe chromosome-scale structure; and by molecular assays that infer accessibility or contacts. This phase records DNA conceptually only; it does not inspect our dataset files.

## E. Numerical/computational representation

DNA can become:

| representation | example | biological meaning |
|---|---|---|
| sequence string | `ACGTG...` | nucleotide order in a region |
| genomic interval | `chr1:1000-1200` | location on a reference assembly |
| feature table | `gene_id, chr, start, end, strand` | annotation of biological features |

A small genes x features table:

| gene_id | chromosome | start | end | strand |
|---|---:|---:|---:|---|
| GeneA | chr1 | 1000 | 1800 | + |
| GeneB | chr1 | 5000 | 7200 | - |

## F. Relevance to our project

Single-cell and spatial omics matrices usually use gene or genomic-region identifiers that ultimately refer back to DNA coordinates or annotations. Multi-omics integration depends on matching molecular measurements to shared genomic references. Biological similarity cannot be interpreted correctly unless feature identity, reference genome version, and gene/region annotation are known. Representation learning and downstream ML may use numerical matrices, but the columns represent biological features grounded in DNA annotations.

## G. Misconceptions

- Treating a gene symbol as a timeless biological object; symbols and coordinates depend on annotation release and reference genome.
- Assuming every DNA region has an obvious protein-coding interpretation.
- Assuming absence of a DNA-derived feature in a table means absence from the genome rather than absence from the assay, annotation, or preprocessing.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, 4th ed., Chapter 4, DNA structure and genome information.
- Alberts et al., *Molecular Biology of the Cell*, 4th ed., Chapter 6, DNA as source of transcribed information.
- Oudelaar and Higgs, 2021, *Nature Reviews Genetics*, genome structure and gene regulation.


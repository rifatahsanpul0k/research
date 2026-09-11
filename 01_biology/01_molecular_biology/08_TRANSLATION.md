# 08. Translation

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

Translation is the process by which ribosomes decode mRNA nucleotide sequence into a polypeptide amino acid sequence. It converts information from the RNA alphabet into the protein alphabet using the genetic code [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26829/).

## B. Biological mechanism

Ribosomes read mRNA in three-nucleotide codons. tRNAs carry amino acids and pair their anticodons with codons. Translation begins at a start codon, elongates by adding amino acids, and stops at termination codons. The new polypeptide must then fold and may undergo processing or modification [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26829/); [de la Torre and Chin 2021](https://www.nature.com/articles/s41576-020-00307-7).

## C. Relationships

Translation follows transcription and RNA processing for protein-coding genes. It produces proteins, which execute many cellular functions and feed back into regulation by acting as enzymes, structural molecules, receptors, or transcription factors.

## D. Experimental measurement

Translation can be studied by ribosome profiling, reporter assays, pulse labeling, proteomics, and protein abundance assays. RNA-seq alone does not directly measure translation; it measures RNA molecules or derived abundance.

## E. Numerical/computational representation

Translation-related data can be stored as:

| gene_id | coding_sequence_length | protein_id | ribosome_signal | protein_abundance |
|---|---:|---|---:|---:|
| GeneA | 900 | ProtA | 42 | 12 |
| GeneB | 1500 | ProtB | 5 | 0 |

This separates RNA-level evidence from protein-level evidence.

## F. Relevance to our project

Single-cell RNA data may suggest which proteins could be produced, but translation and protein stability can break a simple RNA-to-protein mapping. Spatial omics can show where transcripts are located, while protein assays may show functional molecules. Multi-omics can expose discordance between RNA and protein. Downstream ML should not interpret transcript abundance as guaranteed protein activity.

## G. Misconceptions

- Assuming every detected mRNA is being actively translated.
- Assuming one codon maps to one amino acid in a non-redundant way; the genetic code has multiple codons for many amino acids.
- Treating predicted protein presence from RNA as measured protein evidence.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6, From RNA to Protein.
- de la Torre and Chin, 2021, *Nature Reviews Genetics*, genetic code and translation context.


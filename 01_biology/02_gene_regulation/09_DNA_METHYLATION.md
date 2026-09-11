# DNA methylation

## A. Biological meaning

In the mammalian CpG context, methylation commonly refers to addition of a methyl group at cytosine carbon 5, producing 5-methylcytosine (5mC). CpG means neighboring cytosine and guanine linked along a DNA strand; it is not the C-G base pair across strands. Methylation can also occur outside CpGs, so CpG-only data are not the entire methylome.[^METH]

## B. Mechanism

DNMT3A and DNMT3B establish methylation patterns, while DNMT1 participates in their maintenance after replication. TET enzymes oxidize 5mC, contributing to pathways of methylation remodeling. Loss of maintenance during replication can also dilute a pattern.[^METH]

Methylation can affect protein binding or recruitment of repressive complexes. However, its interpretation depends on genomic context and can reflect an existing regulatory state rather than initiate it.[^INFO]

| Genomic context | Interpretation to consider |
|---|---|
| CpG-rich promoter | Methylation is often associated with repression, but lack of methylation is not sufficient for expression |
| Gene body | Methylation can coexist with active transcription; effects differ from promoter methylation |
| Distal regulatory element | Relationship depends on TF binding, activity and local sequence |
| Repetitive sequence | Methylation can participate in suppression of transposable elements |

These are contextual associations and mechanisms, not a monotonic formula from methylation to RNA abundance.[^CONTEXT][^METH]

## C. Relationship to previous concepts

DNA methylation changes a property of DNA that TFs and other proteins encounter. It interacts with chromatin regulation but is not measured by a standard accessibility count. It can contribute to memory while still being dynamic during development.[^METH][^INFO]

## D. Measurement

Bisulfite-based assays exploit differential conversion of cytosines. Conventional bisulfite measurements do not distinguish 5mC from 5-hydroxymethylcytosine (5hmC); specialized chemistry is required for that distinction.[^BS] Coverage and conversion controls matter. A regional average also combines sites, alleles and potentially cells.[^METH]

Methylated-DNA immunoprecipitation provides enrichment of modified DNA regions, and array-based approaches interrogate selected genomic features; their signals and coverage differ from base-resolution sequencing.[^METH] This is a measurement interpretation overview, not a protocol or methylome analysis.

## E. Computational representation

Let K and C be n x s tables, where n is observations, s is assayed sites, K contains modified-cytosine-supporting reads and C contains total informative coverage. Define M_ab=K_ab/C_ab when C_ab>0; otherwise M_ab is missing. M is a fraction matrix in [0,1] with a missingness mask. Here a indexes observations and b sites.

Synthetic example:

| observation | CpG_site | modified_support K | coverage C | fraction M |
|---|---|---:|---:|---|
| C1 | site1 | 8 | 10 | 0.8 |
| C2 | site1 | 1 | 2 | 0.5 |
| C3 | site1 | 0 | 0 | NA |

The larger number of reads does not create more genomic copies in the cell; duplicates and independent-molecule support require assay-specific interpretation. Fractions 0.8 and 0.5 have different coverage support. An uncovered site is not 0% methylated.

For region summaries, define whether to pool support/coverage or average site fractions; these operations can differ. Keep CpG coordinates, reference build, strand policy and whether the assay reports 5mC or combined modified-cytosine signal.

## F. Relevance to our research

Do not substitute ATAC accessibility for methylation. If methylation is eventually available, preserve promoter versus gene-body context and coverage. In spatial data, intermediate fractions may reflect mixtures; in multimodal data, correlations need not establish direction. These are interpretation constraints for future work, not evidence that our datasets include methylation.

## G. Common misconceptions

More methylation does not unconditionally mean less expression. A regional fraction is not automatically a fraction of methylated cells. NA is not an unmethylated call. Bisulfite-retained cytosine is not always uniquely 5mC.[^CONTEXT][^METH][^INFO]

## H. Evidence

[^METH]: Li E; Zhang Y (2014). [DNA Methylation in Mammals](https://pmc.ncbi.nlm.nih.gov/articles/PMC3996472/). Cold Spring Harbor Perspectives in Biology; review. Locator: Overview; DNMT and TET mechanisms; methylation measurement discussion.

[^INFO]: Schubeler D (2015). [Function and information content of DNA methylation](https://pubmed.ncbi.nlm.nih.gov/25592537/). Nature; review. Locator: Abstract.

[^CONTEXT]: Jones PA (2012). [Functions of DNA methylation: islands, start sites, gene bodies and beyond](https://www.nature.com/articles/nrg3230). Nature Reviews Genetics; review. Locator: Abstract and promoter versus gene-body discussion.


[^BS]: Huang Y; Pastor WA; Shen Y; Tahiliani M; Liu DR; Rao A (2010). [The behaviour of 5-hydroxymethylcytosine in bisulfite sequencing](https://pubmed.ncbi.nlm.nih.gov/20126651/). PLOS ONE; primary_research. DOI: 10.1371/journal.pone.0008888. Locator: Abstract and Figure 1: differential cytosine conversion.

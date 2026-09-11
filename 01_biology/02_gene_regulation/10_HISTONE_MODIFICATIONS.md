# Histone modifications

## A. Biological meaning

Histones can be chemically modified at specific amino-acid residues. In H3K4me3, H3 names the histone, K4 is lysine at position 4, and me3 denotes trimethylation. In H3K27ac, ac denotes acetylation at lysine 27. These are protein modifications, distinct from cytosine methylation in DNA.[^HIST]

## B. Mechanism

Enzymes install or remove modifications, while binding proteins recognize particular modified contexts. The terms writer, eraser and reader summarize these roles. Acetyltransferases can add acetyl groups and deacetylases remove them; methyltransferases and demethylases act on specific methylated contexts. Acetylation changes lysine charge, while methylation affects recognition without the same charge-neutralizing effect. Modifications can affect physical interactions or recruit regulatory complexes; consequences depend on residue, modification and neighboring molecular context.[^HIST]

| Mark | Common association | Interpretation limit |
|---|---|---|
| H3K4me3 | Promoter-associated chromatin, often at active promoters | Does not alone prove productive transcription |
| H3K27ac | Active promoter/enhancer-associated chromatin | Does not specify an enhancer's target |
| H3K4me1 | Enhancer-associated chromatin | Can occur without current enhancer activity |
| H3K27me3 | Polycomb-associated repression | Contextual state, not permanent inability to activate |

The active-promoter associations and candidate annotations have empirical support; they remain descriptions of enrichment rather than deterministic definitions.[^ENC][^HIST] Landmark H3K27ac work explicitly compared activity states among H3K4me1-associated enhancer candidates.[^AC]

In human embryonic stem cells, Rada-Iglesias and colleagues described poised enhancer candidates with H3K4me1 and H3K27me3, little H3K27ac, and low nucleosomal density; a subset acquired active signatures on differentiation. That experimentally described context must not be generalized to every H3K4me1-only interval.[^POISE]

A poised regulatory label requires its definition: inactive but prepared for possible activation is a functional interpretation, not a guaranteed future. Some developmental promoter regions show H3K4me3 together with H3K27me3, often called bivalent. A population measurement showing both signals need not prove both modifications occur in the same cell or nucleosome.[^HIST]

## C. Relationship to previous concepts

TFs and cofactors can recruit chromatin-modifying activities. Histone modifications characterize a different aspect of chromatin from accessibility or DNA methylation. Their co-occurrence with RNA output cannot alone determine whether the mark caused, maintained or followed transcription.[^HIST][^ENC]

## D. Measurement

Histone-directed chromatin enrichment with sequencing, such as ChIP-seq, associates genomic intervals with antibody-selected chromatin. The result depends on antibody specificity, background, sampling and normalization. Measuring several marks usually means separate measurements; their apparent overlap is not direct molecular co-occupancy evidence.[^HIST][^ENC]

## E. Computational representation

Synthetic region-by-mark matrix with illustrative enrichment ratios, not molecule counts:

| region | H3K4me3 | H3K27ac | H3K4me1 | H3K27me3 |
|---|---:|---:|---:|---:|
| P1 | 8 | 6 | 1 | 1 |
| E1 | 1 | 7 | 5 | 1 |
| P2 | 5 | 1 | 1 | 6 |

P1 is consistent with an active-promoter-associated pattern; E1 with an active-enhancer-associated pattern; P2 needs investigation of mixed or bivalent signal. These are hypothetical interpretations, not classifications applied to a dataset. Ratios across marks are not automatically comparable because antibodies and backgrounds differ.

For n observations, q regions and h measured marks, a tensor H in real n x q x h space is one possible bookkeeping object. Define units per mark and retain missing measurements; alternatively use a long table with observation, region, mark and value.

## F. Relevance to our research

Histone annotations may contextualize accessible regions, but annotation transfer requires species, stage, tissue and assay provenance. A mark-based feature remains evidence about chromatin, not measured TF activity or protein function. Matrix, tensor and table storage are all plausible; this phase ranks none.

## G. Common misconceptions

- H3K4me1 proves enhancer activity.
- H3K27ac proves a causal enhancer-gene link.
- H3K27me3 means irreversible repression.
- H3K4me3 guarantees high RNA.
- Population overlap proves same-cell bivalency.
- Histone methylation and DNA methylation are the same measurement.[^HIST][^AC][^ENC]

## H. Evidence

[^HIST]: Bannister AJ; Kouzarides T (2011). [Regulation of chromatin by histone modifications](https://pmc.ncbi.nlm.nih.gov/articles/PMC3193420/). Cell Research; review. Locator: Acetylation; lysine methylation; euchromatin and heterochromatin.

[^ENC]: ENCODE Project Consortium; Moore JE; Purcaro MJ; Pratt HE; Epstein CB; Shoresh N; Adrian J; Kawli T; Davis CA; et al. (2020). [Expanded encyclopaedias of DNA elements in the human and mouse genomes](https://www.nature.com/articles/s41586-020-2493-4). Nature; database_resource_paper. Locator: Abstract; Figure 2 and candidate CRE registry description.

[^AC]: Creyghton MP; Cheng AW; Welstead GG; Kooistra T; Carey BW; Steine EJ; Hanna J; Lodato MA; Frampton GM; Sharp PA; Boyer LA; Young RA; Jaenisch R (2010). [Histone H3K27ac separates active from poised enhancers and predicts developmental state](https://pmc.ncbi.nlm.nih.gov/articles/PMC3003124/). Proceedings of the National Academy of Sciences USA; primary_research. Locator: Abstract and H3K27ac/H3K4me1 comparison.


[^POISE]: Rada-Iglesias A; Bajpai R; Swigut T; Brugmann SA; Flynn RA; Wysocka J (2011). [A unique chromatin signature uncovers early developmental enhancers in humans](https://www.nature.com/articles/nature09692). Nature; primary_research. DOI: 10.1038/nature09692. Locator: Abstract; Figure 1 description.

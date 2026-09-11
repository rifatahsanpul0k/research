# Individual cells, nuclei, spots, bins and populations

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

An individual cell is a biological entity; a nucleus is one subcellular compartment. A spot is a spatial sampling footprint and a bin is a chosen spatial aggregation unit. Either can include contributions from multiple cells. A cell population is a collection defined by stated criteria; a population average is not an individual member.[^MEM][^NUCLEUS][^TECH]

These are biological and sampling definitions only. No sequencing or spatial technology is studied here.

## B. Mechanism

Compartment selection changes which molecules can contribute. In a matched adult mouse cortical comparison, nuclear and whole-cell RNA profiles differed while retaining information about type; this supports distinguishing compartments, not applying adult labels to embryonic tissue.[^NUCLEUS]

Aggregation combines signals before interpretation. A blended profile can have features of several cell types without any constituent cell having that combined state. This follows from summing different contributions, not from a particular assay.

## C. Relationship to prior concepts

Earlier notes described biology at cell level; actual rows may represent different units. A spatial coordinate may locate a spot center, bin or nucleus rather than an entire cell. Annotation granularity must respect this distinction.

## D. Experimental observation/measurement

Specimen metadata, sampling geometry and images are needed to establish the unit. Dimensions alone are insufficient: one row per identifier does not tell whether the identifier names a cell, nucleus or region. Missing metadata must stay unknown. Nuclear/whole-cell differences are supported by biological comparison, not resolved by renaming rows.[^NUCLEUS]

## E. Computational representation

Conceptual mixture:

\[x_{spot}pprox\sum_{k=1}^{m}w_kx_k.\]

Here x_spot is a p-feature observation vector; x_k is a p-feature molecular profile of contributing cell k; m is the number of contributors; w_k is its nonnegative effective contribution weight. This expression is illustrative, not an identified measurement model. For relative profiles one may choose weights summing to one. Absolute contributions need not use that convention. Capture, geometry and background can make the real relation different.

Synthetic example: x_1=(8,0), x_2=(0,6), w_1=w_2=1/2 gives x_spot=(4,3). Both features are positive although neither contributor has both positive. The fractional result is a weighted relative profile, not a claim that raw molecule counts are fractional.

Possible forms: unit metadata, observation-by-feature matrices, population summaries, contributor sets and uncertain composition distributions. Contribution weight ≠ cell fraction unless additional assumptions justify it.

## F. Relevance to our project

All six datasets have unverified observation units. Until metadata are checked, use “observation,” not “cell,” for their rows. This prevents future similarity or annotation work from mistaking a mixture for a hybrid biological cell.

## G. Common misconceptions

One row ≠ one cell; one nucleus ≠ a full cytoplasmic profile; a spot mixture ≠ a novel type; bin size ≠ biological resolution. Check: (4,3) in the example supports a combined observation, not a proof that one cell co-expresses both features.

## H. Evidence

[^MEM]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Membrane Structure](https://www.ncbi.nlm.nih.gov/books/NBK21055/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source MEM](SOURCES.md#mem).

[^NUCLEUS]: Bakken TE; Hodge RD; Miller JA; Yao Z; Nguyen TN; et al. (2018). [Single-nucleus and single-cell transcriptomes compared in matched cortical cell types](https://pubmed.ncbi.nlm.nih.gov/30586455/). PLOS ONE. DOI: 10.1371/journal.pone.0209648. Supporting location/access: [source NUCLEUS](SOURCES.md#nucleus).

[^TECH]: Laehnemann D; Koester J; Szczurek E; McCarthy DJ; Hicks SC; Robinson MD; Vallejos CA; Campbell KR; Beerenwinkel N; Mahfouz A; Pinello L; Skums P; Stamatakis A; Stephan-Otto Attolini C; Aparicio S; Baaijens J; Balvert M; Dutilh BE; Guryev V; Marioni JC; Stegle O; Theis FJ; McHardy AC; Raphael BJ; Shah SP; Schoenhuth A; et al. (2020). [Eleven grand challenges in single-cell data science](https://link.springer.com/article/10.1186/s13059-020-1926-6). Genome Biology. DOI: 10.1186/s13059-020-1926-6. Supporting location/access: [source TECH](SOURCES.md#tech).


# Cell cycle

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

The cell cycle coordinates replication of cellular material with division. G0 denotes a noncycling condition; G1 precedes DNA synthesis, S is replication, G2 follows replication, and M comprises mitosis with cell division. G0 is not absence of cellular function.[^CYCLE]

## B. Mechanism

Cyclin-dependent regulation coordinates transitions and expression of products needed for subsequent events. Checkpoints can delay progression when conditions are inappropriate. Cycle phase therefore affects a molecular profile, even when the broad cell type stays the same.[^CYCREG]

For an ordinary diploid cycle, DNA content rises from 2C to 4C during S, remains 4C in G2 before segregation, and returns to 2C per daughter after division. Here C denotes one haploid genome's DNA amount; doubling DNA content is not a change from diploid to tetraploid chromosome complement before chromatid segregation.[^CYCLE]

## C. Relationship to prior concepts

Proliferation increases cell number; differentiation changes specialized properties. They can occur in the same developing population but are distinct processes. Stage and cycle are also separate clocks: one embryo contains cells in different phases.

## D. Experimental observation/measurement

Microscopy observes mitosis; DNA-binding signals quantify DNA amount; incorporation of a labeled DNA precursor identifies synthesis during the labeling interval. DNA content alone cannot resolve G0 versus G1 or G2 versus M.[^CYCLE] The observation and its interpreted phase should remain separate fields.

## E. Computational representation

Synthetic relative transcript units:

| cell | independent_type | replication_program | other_program | independently_assessed_phase |
|---|---|---:|---:|---|
| A | progenitor Q | 1 | 6 | G1 |
| B | progenitor Q | 9 | 6 | S |

The replication difference could separate these profiles numerically without requiring different types. A phase category, continuous DNA-content value or distribution over possible phases carries different certainty. Program values are invented, not inferred scores from project data.

## F. Relevance to our project

Both proliferating immune populations and developing neural progenitors motivate cycle awareness. Later preprocessing must ask whether proliferation is relevant signal before attempting adjustment. No algorithm, phase scoring or removal of cycle effects is performed.

## G. Common misconceptions

G0 ≠ dead; S ≠ a developmental stage; a proliferation-associated marker ≠ an exact phase. A measured 4C amount requires context and does not by itself identify mitosis. Same-type numerical separation can reflect cycle biology.[^CYCLE][^CYCREG]

## H. Evidence

[^CYCLE]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [An Overview of the Cell Cycle](https://www.ncbi.nlm.nih.gov/books/NBK26869/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source CYCLE](SOURCES.md#cycle).

[^CYCREG]: Bertoli C; Skotheim JM; de Bruin RAM (2013). [Control of cell cycle transcription during G1 and S phases](https://pmc.ncbi.nlm.nih.gov/articles/PMC4569015/). Nature Reviews Molecular Cell Biology. DOI: 10.1038/nrm3629. Supporting location/access: [source CYCREG](SOURCES.md#cycreg).


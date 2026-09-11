# Developmental time and cross-stage interpretation

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

E11, E13, E15 and E18 are supplied embryonic-stage labels. Their intended ordering matters: \(t_1<t_2<t_3<t_4\), where t_k is the ordered stage associated with label k in that sequence. This order does not verify exact elapsed time, specimen pairing or a staging convention.

Chronological age and morphological developmental stage are related but distinct. Theiler staging uses observed anatomical features, including somites or external structures depending on age.[^STAGE]

## B. Mechanism

During cortical development, progenitor output, expression programs, migrating populations and laminar organization change. An embryo contains cells of different birthdates and maturation states at the same chronological age.[^DEV] Developmental stage can therefore change cell composition, cell states, regulatory programs, spatial organization and tissue architecture together; it is not merely a batch name.

## C. Relationship to prior concepts

Lineage concerns historical descent; stage concerns when a specimen was obtained. A state ordering inferred from snapshots is neither an observed lineage nor automatically a calibrated developmental clock.[^LINE] Migration also prevents interpreting fixed position as fixed identity through time.

## D. Experimental observation/measurement

Record age convention, morphological stage, embryo/litter identity, region and collection conditions when available. Repeated population sampling provides cross-sectional time information; observation of the same tracked cell provides a different design.[^STAGE][^LINE] The project's records do not yet identify either design fully.

## E. Computational representation

User-input provenance, not verified developmental metadata:

| dataset | supplied stage | intended rank | exact convention / embryo / region |
|---|---|---:|---|
| Mouse_Brain_E11_S1 | E11 | 1 | unknown |
| Mouse_Brain_E13_S1 | E13 | 2 | unknown |
| Mouse_Brain_E15_S1 | E15 | 3 | unknown |
| Mouse_Brain_E18_S1 | E18 | 4 | unknown |

Source: [datasets.csv](../../datasets.csv). Rank is ordinal: gaps of one rank are not equal durations. Store t_i for the stage of observation i, together with its specimen; repeating stage values across rows does not create independent embryos.

Possible forms include ordered categories, measured ages with units, age-uncertainty distributions and stage-indexed population tensors. Within-stage resemblance and across-stage correspondence should have separate declared meanings.

## F. Relevance to our project

The four stages describe snapshots of an evolving system, not four biologically unrelated inputs. Yet their samples must not be assumed longitudinally paired. Across stages, similar broad identity may coexist with changed maturation; within one stage, differences may reflect regions or birthdates. Future representation research must preserve this distinction without ranking methods now.

## G. Common misconceptions

E15 is not the parent of E18. A rank is not a day interval; a stage label is not exact morphology. Similar vectors across stages do not prove unchanged function. Check: two mature-looking rows at different stages may reflect comparable states in different cells; actual ancestry remains unknown.

## H. Evidence

[^STAGE]: eMouseAtlas / EMAP (unknown). [Staging Criteria](https://www.emouseatlas.org/emap/ema/staging_criteria/staging_criteria.html). eMouseAtlas. DOI: not_applicable. Supporting location/access: [source STAGE](SOURCES.md#stage).

[^DEV]: Jabaudon D (2017). [Fate and freedom in developing neocortical circuits](https://www.nature.com/articles/ncomms16042). Nature Communications. DOI: 10.1038/ncomms16042. Supporting location/access: [source DEV](SOURCES.md#dev).

[^LINE]: Wagner DE; Klein AM (2020). [Lineage tracing meets single-cell omics: opportunities and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC7307462/). Nature Reviews Genetics. DOI: 10.1038/s41576-020-0223-2. Supporting location/access: [source LINE](SOURCES.md#line).


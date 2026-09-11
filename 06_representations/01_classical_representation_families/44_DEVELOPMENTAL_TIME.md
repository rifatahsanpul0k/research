# Chronological stage and inferred pseudotime

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Different time representations

| Object | Example shape | Meaning |
|---|---|---|
| Categorical stage | n labels or n×4 one-hot | Membership in E11/E13/E15/E18 categories |
| Ordinal stage | n ordered values | Known stage order, without assuming equal gaps |
| Nominal embryonic-day number | n values | Numeric meaning of the supplied stage label; exact timing still needs provenance |
| Pseudotime | n inferred real scores | Relative position under a computational trajectory model |
| Trajectory relationship | Branch labels/relations plus scores | Model-dependent ordering and branching |

For the user-supplied mouse stages, **E11 < E13 < E15 < E18** is chronological stage order. Coding them as 1,2,3,4 preserves order but imposes equal numerical gaps if used with Euclidean distance. Coding 11,13,15,18 retains nominal day-label gaps but does not verify exact sampling times, staging protocol or embryo identity.

## Pseudotime is inferred

The original Monocle study orders single-cell expression profiles by a computational measure of progression, distinct from collection time.[^1] A pseudotime t_i∈R is not automatically hours, embryonic days, or a lineage record. Root choice, feature selection, branch topology, sampling and method assumptions affect the quantity. A continuous coordinate can interpolate numerical states without observing an actual transition.

For this project, cross-sectional capture locations at different stages are not repeated measurements of the same cells. Similar vectors across E11 and E18 do not show ancestry. A stage-specific region or assay difference may confound inferred ordering. Exact section/embryo hierarchy and missing E18 ATAC remain unresolved; no time-specific biology is inferred from filenames.

Categories and scalar scores use O(n) storage; fitting a trajectory has method-dependent relationship and optimization costs. A single pseudotime loses branching information unless branch identifiers are retained. Unknown stages and unavailable measurements remain missing, not time zero. Monocle's original paper and official release repository are recorded as classical literature context only; no trajectory, graph or pseudotime is fitted.

## Evidence

[^1]: Trapnell C; Cacchiarelli D; Grimsby J; Pokharel P; Li S; Morse M; Lennon NJ; Livak KJ; Mikkelsen TS; Rinn JL (2014). [The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells](https://cole-trapnell-lab.github.io/pdfs/papers/trapnell-cacchiarelli-monocle.pdf). See [access record](SOURCES.md#pseudotime).

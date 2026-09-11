# Peak construction and feature alignment

A peak is a called genomic interval; the feature set depends on genome build, caller, thresholds, sample composition and whether peaks are stage-specific or a consensus. Union retains every interval from a collection; intersection retains only shared intervals. Either can discard rare but real regulatory elements and changes the matrix dimension. Peak identifiers must include coordinates and reference context [S08,S09].

Read-only comparison finds E11/E13/E15 ATAC counts of 69,370/123,840/141,420, pairwise overlaps of 3, 4 and 16 unique IDs, and no common ID across all three; unions are 193,207, 210,786 and 265,244 pairwise, with all-feature union 334,607. RNA files share order and unique IDs after accounting for duplicates (40 repeated IDs per mouse RNA file); A1/D1 RNA and ADT likewise have repeated IDs. These are facts about supplied feature labels, not evidence to harmonize. Evidence: 10x/AnnData formats [S20,S22], MISAR-seq [S27].

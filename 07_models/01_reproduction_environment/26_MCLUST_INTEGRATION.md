# MClust integration

Plan an isolated R environment with the mclust package, pinned version and sessionInfo(). The input is n×d with observations in rows. The adapter passes G=K, a modelName policy and a seed via set.seed, then returns labels aligned to observation IDs.

R and mclust are unavailable locally now, so status is BLOCKED_FOR_R1. No clustering smoke test or benchmark was run.

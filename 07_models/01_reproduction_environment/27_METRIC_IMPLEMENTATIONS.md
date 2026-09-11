# Metric implementations

ARI, NMI and silhouette use pinned scikit-learn functions with explicit averaging/metric parameters. Retrieval metrics use deterministic rank/tie policies. FOSCTTM records direction and candidate pool. Spatial metrics consume coordinates/graphs only when required. scIB-derived metrics use a pinned implementation rather than copied formulas.

Each metric has direction, valid range, required labels/pairing/space, missing-input behavior and toy tests. No project metric is computed in Phase 3B.

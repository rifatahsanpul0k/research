# Seed implementation

A run stores Python, NumPy, PyTorch, CUDA, R, method-specific and clustering seeds separately. Uniform defaults are allowed only when recorded. CUDA and framework determinism flags are captured when relevant.

The common SeedPlan applies Python's seed now; optional libraries are seeded inside their isolated adapters. Multiple-run seed sets are chosen before observing results.

# Provenance-aware preprocessing cache

A cache key hashes input checksums, operation, parameters, software version and training subset. Reuse is allowed only when all fields match. Assets fitted with test observations cannot be reused in a training-only pipeline.

Cache entries are derived and ignored by Git; manifests retain their metadata. Similar names do not imply identical preprocessing.

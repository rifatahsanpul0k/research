# Immutable raw-data policy

Files under each 04_datasets/<dataset>/raw directory are read-only inputs. Adapters must never normalize, overwrite or add files there. Derived assets belong under a separate ignored derived/cache location with input checksums, operation, parameters and environment recorded.

Existing Phase 1D checksums remain the provenance baseline. A future preflight compares them before and after a run. Large outputs remain Git-ignored; metadata and schemas are versioned.

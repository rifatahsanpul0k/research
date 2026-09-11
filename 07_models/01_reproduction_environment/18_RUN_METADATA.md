# Run metadata

Every future run records experiment ID, UTC timestamp, canonical/original dataset, method, repository commit/tag, environment digest, preprocessing, seed plan, parameters, hardware class, input checksums, outputs, runtime, exit status and log locations. The provenance validator rejects missing required fields.

Metadata are written before execution as PLANNED/PREPARING and finalized without deleting failure evidence.

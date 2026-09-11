# Run metadata

Every future run records experiment ID, UTC timestamp, canonical/original dataset, method, repository commit/tag, compute classification, environment digest, preprocessing, seed plan, parameters, hardware, input checksums, outputs, runtime, exit status and log locations. The provenance validator rejects missing required fields.

For Colab, environment and hardware records also include Colab runtime type, Python version, package versions, GPU model and CUDA version where relevant. The selected repository commit and frozen configuration must be recorded before execution.

Metadata are written before execution as PLANNED/PREPARING and finalized without deleting failure evidence.

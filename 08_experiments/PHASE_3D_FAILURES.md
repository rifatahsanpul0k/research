# Phase 3D failures and blockers

No scientific R3 failure has occurred because no project-data R3 run has been started.

The current blockers are execution access and source synchronization: MOFA+ R3 runs require the frozen `COLAB_CPU` classification and SCOT R3 runs require `COLAB_HIGH_MEMORY`; no active Colab runtime is attached to this session, so local execution would violate the frozen compute policy. In addition, the exact checkpoint commit does not yet contain the uncommitted Phase 3D configs, adapters and runner. The controller must be used only after a reviewed commit containing these files, or after an explicitly checksummed working-tree sync is recorded. It must never silently run a different source snapshot. The generic controller and 30 immutable configs are otherwise ready.

The engineering checks passed and are not failures: MOFA+ official entry-point build, SCOT v1 import/initialization and fixed-parameter API alignment. If a Colab run fails, its experiment directory must retain `failure.json`, stdout/stderr, STATUS, configuration, source checksums and the failure category.

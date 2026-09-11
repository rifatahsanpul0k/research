# Configuration system

Canonical runs use checked configuration files with experiment_id, dataset, method, seeds, inputs, preprocessing, method parameters, clustering and output directory. Paths are workspace-relative or explicitly external; credentials are forbidden.

The historical machine-readable contract is `schemas/run-config.schema.json`. Configurations authorized after Phase 3C use `schemas/run-config-v2.schema.json`, which requires a compute classification. Three deliberately unresolved examples are stored under `examples/`: a transparent PCA plan, a paired RNA+ADT totalVI plan, and an E18 MultiVI plan that demonstrates the hard ATAC gate. Hundreds of speculative configs are intentionally absent.

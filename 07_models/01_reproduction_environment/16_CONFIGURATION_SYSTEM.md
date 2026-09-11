# Configuration system

Canonical runs use checked configuration files with experiment_id, dataset, method, seeds, inputs, preprocessing, method parameters, clustering and output directory. Paths are workspace-relative or explicitly external; credentials are forbidden.

The machine-readable contract is `schemas/run-config.schema.json`, and three deliberately unresolved examples are stored under `examples/`: a transparent PCA plan, a paired RNA+ADT totalVI plan, and an E18 MultiVI plan that demonstrates the hard ATAC gate. Phase 3C may add resolved configs one run at a time; hundreds of speculative configs are intentionally absent.

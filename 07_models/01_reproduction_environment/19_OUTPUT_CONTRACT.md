# Output contract

Each 08_experiments/EXP-... directory contains config.yaml, environment.json, provenance.json, stdout.log, stderr.log, embedding with observation-ID sidecar, native_output/, metrics.json and STATUS. Large outputs are ignored; compact metadata may be versioned after review.

Embedding rows must map exactly to input observations. Metrics consume declared artifacts and cannot infer hidden labels.

# Resource planning

Phase 3A · 2026-09-12 · proposed design; no local performance results.

Qualitative classes below are **planning estimates**, not measured runtimes. LOW: simple matrix transforms/reductions at current observation counts; MODERATE: iterative factors, relational matrices or ordinary neural fitting; HIGH: documented large-memory reference setup; UNKNOWN: insufficient transferable evidence. Exact CPU count, RAM, GPU model/VRAM and runtime required on our hardware are UNKNOWN for every candidate until a future feasibility check. Available project hardware was not inventoried.

| Candidate | Planning class | CPU/GPU and memory mechanism | Dependency burden |
|---|---|---|---|
| RNA separate | LOW | CPU plausible; sparse input/dense reductions; hardware untested | LOW: numerical library |
| Second modality separate | LOW | CPU plausible; sparse input/dense reductions; hardware untested | LOW: numerical library |
| Scaled concatenation | LOW | CPU plausible; sparse input/dense reductions; hardware untested | LOW: numerical library |
| Coordinates only | LOW | CPU plausible; sparse input/dense reductions; hardware untested | LOW: numerical library |
| Spatial kernel control | MODERATE | pairwise/coupling arrays grow quadratically; CPU possible, memory depends on dense intermediates | MODERATE: iterative numerical/framework stack |
| PCA | LOW | CPU plausible; sparse input/dense reductions; hardware untested | LOW: numerical library |
| NMF | MODERATE | CPU plausible; sparse input/dense reductions; hardware untested | MODERATE: iterative numerical/framework stack |
| CCA | MODERATE | CPU plausible; sparse input/dense reductions; hardware untested | MODERATE: iterative numerical/framework stack |
| MOFA+ | MODERATE | CPU BLAS; optional CuPy GPU documented; avoid dense full peak matrices without budget | MODERATE: iterative numerical/framework stack |
| Kernel PCA | MODERATE | pairwise/coupling arrays grow quadratically; CPU possible, memory depends on dense intermediates | MODERATE: iterative numerical/framework stack |
| Diffusion maps | MODERATE | CPU plausible; sparse input/dense reductions; hardware untested | MODERATE: iterative numerical/framework stack |
| WNN | MODERATE | CPU plausible; sparse input/dense reductions; hardware untested | MODERATE: iterative numerical/framework stack |
| SCOT | MODERATE | pairwise/coupling arrays grow quadratically; CPU possible, memory depends on dense intermediates | MODERATE: iterative numerical/framework stack |
| totalVI | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | MODERATE: iterative numerical/framework stack |
| MultiVI | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | MODERATE: iterative numerical/framework stack |
| Cobolt | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | MODERATE: iterative numerical/framework stack |
| MIDAS | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | MODERATE: iterative numerical/framework stack |
| scGLUE | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | MODERATE: iterative numerical/framework stack |
| SpatialGlue | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | HIGH: Python/PyTorch plus optional R/PyG bridges |
| SpaMI | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | HIGH: Python/PyTorch plus optional R/PyG bridges |
| Garfield | UNKNOWN | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | HIGH: Python/PyTorch plus optional R/PyG bridges |
| SCIGMA | HIGH | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | HIGH: Python/PyTorch plus optional R/PyG bridges |
| ARISE | UNKNOWN | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | HIGH: Python/PyTorch plus optional R/PyG bridges |
| SMART | MODERATE | CPU/GPU support depends on implementation; GPU desirable for neural fitting; activation and graph memory require measurement | HIGH: Python/PyTorch plus optional R/PyG bridges |
| PASTE | MODERATE | pairwise/coupling arrays grow quadratically; CPU possible, memory depends on dense intermediates | MODERATE: iterative numerical/framework stack |

Source anchors: [code/environment audit](31_CODEBASE_VERIFICATION.md), [MOFA FAQ](SOURCES.md#DOC_MOFA). [Garfield paper](SOURCES.md#GARFIELD_2026) reports an A800-SXM4-80GB experimental setup. [SCIGMA repository](https://github.com/YMa-lab/SCIGMA) reports a 24GB-GPU/100GB-RAM setup or a 24-CPU/400GB-RAM setup. These are authors' reported configurations, **not minimum requirements**, and are not our measurements.

Derived storage example, not runtime measurement: a dense float32 n×n array at n=3484 requires 3484²×4 = 48,553,024 bytes. Multiple affinities, gradients and copies multiply memory. E15 dense ATAC alone is 1949×141420×4 = 1,102,510,320 bytes, before models. Sparse storage does not guarantee a package avoids internal densification. Any future pilot must record peak resident RAM/VRAM, preprocessing/fitting/downstream wall time separately, thread count, failures and timeout limits. A failed run is reported, never omitted from timing summaries.

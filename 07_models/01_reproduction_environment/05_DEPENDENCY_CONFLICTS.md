# Dependency conflict matrix

| Group | Python | PyTorch/CUDA | R | Isolation |
|---|---|---|---|---|
| Baselines | 3.11 target | none | none | uv/venv baseline |
| MOFA+ | Python optional | CuPy optional | required for MOFA2 route | R environment or Docker |
| SCOT | repository-pinned | none/POT | none | dedicated venv |
| scvi-tools | supported release to be locked | PyTorch; CUDA optional | none | dedicated venv/container |
| SpatialGlue | repository documents Python 3.8 | torch/PyG; CUDA optional | R 4.0.3/rpy2/MClust | legacy container preferred |
| Garfield | repository-defined | torch/PyG; CUDA-oriented | none unless downstream needs R | dedicated GPU-capable environment |

The groups must not share one mutable environment. Version changes require an explicit compatibility record.

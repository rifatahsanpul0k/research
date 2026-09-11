# Dependency audit

| CORE group | Principal requirements | Difficulty | Main blocker |
|---|---|---|---|
| scikit baselines | Python 3.11.8, NumPy 2.4.4, SciPy 1.17.1, scikit-learn 1.9.1 | LOW | isolated uv environment installed and smoke-tested; scientific adapters remain unexecuted |
| MOFA+ | R MOFA2 or Python mofapy2; BLAS; optional CuPy | MODERATE | R absent; arm64 compatibility must be tested |
| SCOT | Python, POT and repository requirements | MODERATE | old dependency constraints require isolated solve |
| totalVI/MultiVI | Python, PyTorch, scvi-tools, AnnData/Scanpy | MODERATE | no CUDA; MPS support/version must be tested |
| SpatialGlue | Python 3.8-era stack, PyTorch/PyG, R/rpy2/MClust | HIGH | R absent and mixed-language legacy dependencies |
| Garfield | Python, PyTorch/PyG and graph stack | HIGH | CUDA-oriented evidence; Apple MPS support unknown |

Compiled extensions, PyTorch wheels and R bridges must be solved per environment. Installation difficulty is engineering status, not scientific quality.

The baseline environment resolved seven packages: the three direct pins plus cloudpickle 3.1.2, joblib 1.6.0, narwhals 2.26.0 and threadpoolctl 3.6.0. This resolution applies only to the transparent baselines/PCA group and does not establish compatibility with the remaining CORE methods.

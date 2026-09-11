# Local environment

Phase 3B engineering inventory, captured 2026-09-12. Secrets, serial numbers, hardware UUIDs and credentials are intentionally excluded.

| Resource | Observed value |
|---|---|
| OS | macOS 26.6.2 (Darwin 25.6.0) |
| Architecture | arm64 |
| Machine | Apple M2 MacBook Air |
| CPU | Apple M2, 8 cores (4 performance, 4 efficiency) |
| RAM | 16 GB |
| GPU | Integrated Apple M2, 8 cores, Metal support |
| CUDA | Unavailable; Apple GPU is not CUDA |
| Python | CPython 3.11.8 |
| R | Unavailable on PATH |
| Java | OpenJDK 25.0.2 |
| Docker CLI | 29.7.2; daemon availability not established |
| Conda/Mamba | Unavailable on PATH |
| uv | 0.12.7 |
| pip | 25.3 |
| Homebrew | 6.0.22 |
| Free disk | Approximately 25 GiB at capture time |

The base Python has NumPy 2.4.4 and pandas 3.0.2; SciPy, scikit-learn, PyYAML, AnnData, Scanpy and PyTorch were not importable there. A separate ignored `baseline_py311` uv environment was then created with NumPy 2.4.4, SciPy 1.17.1 and scikit-learn 1.9.1. All three imported, and a synthetic 3 × 2 matrix produced a finite 3 × 1 PCA output. This is an `ENGINEERING_SMOKE_TEST`, not a project-data run or performance result. See [ENVIRONMENT.md](ENVIRONMENT.md) and the pinned [requirements](environments/baseline-py311.requirements.txt).

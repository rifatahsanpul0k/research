# Phase 3B environment record

The available host is an arm64 Apple M2 MacBook Air with 16 GB RAM, integrated Metal GPU, no CUDA device, macOS 26.6.2, Python 3.11.8, uv/pip/Homebrew and Docker CLI. R, Conda and Mamba are not available on PATH. Roughly 25 GiB free disk was observed.

This host supports infrastructure tests and modest CPU baselines. CUDA-specific upstream environments cannot run natively. Apple Metal support does not imply that a repository supports MPS. Exact Docker daemon availability and external GPU resources remain UNKNOWN. No credentials or device identifiers are recorded.

The ignored `baseline_py311` uv environment uses CPython 3.11.8 with NumPy 2.4.4, SciPy 1.17.1 and scikit-learn 1.9.1. Imports and a finite synthetic PCA calculation passed on 2026-09-12. The reusable pins are in `environments/baseline-py311.requirements.txt`; the environment directory itself is intentionally excluded from Git.

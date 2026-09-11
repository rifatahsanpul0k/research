# Determinism policy

Exact reproducibility targets identical outputs under the same software, hardware and deterministic kernels. Statistical reproducibility expects stable distributions across declared seeds when exact determinism is unavailable.

GPU kernels, multithreading, BLAS, PyTorch/PyG scatter operations and stochastic clustering may remain nondeterministic. Each run records deterministic flags, thread counts and known exceptions.

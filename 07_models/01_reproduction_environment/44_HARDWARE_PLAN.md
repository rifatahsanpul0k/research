# Hardware-aware plan

Use `LOCAL_LIGHT` for repository work, validation, inspection, smoke tests and lightweight classical algorithms. Use the user's Google Colab environment for substantial compute: `COLAB_CPU` for remote CPU workloads, `COLAB_GPU` for neural/GPU-beneficial methods and `COLAB_HIGH_MEMORY` for memory-intensive factorization or optimal transport. Use `UNRESOLVED` only until evidence supports an executable selection; do not begin a scientific run in that state.

Current manifest defaults are `LOCAL_LIGHT` for the transparent controls/PCA, `COLAB_CPU` for MOFA+, `COLAB_HIGH_MEMORY` for SCOT, and `COLAB_GPU` for totalVI, MultiVI, SpatialGlue and Garfield. These are resource selections, not scientific rankings. The frozen experiment configuration must confirm availability and may revise a default before execution with a recorded reason.

No paid or additional external compute is authorized. Runtime, memory, accelerator identity and CUDA availability are captured from the selected runtime rather than inferred.

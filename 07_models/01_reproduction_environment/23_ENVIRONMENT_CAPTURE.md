# Environment capture

Python runs capture python --version, interpreter path, pip freeze or uv lock, OS/architecture, framework versions and GPU/CUDA/MPS visibility. Conda uses an explicit export when used. R runs save sessionInfo() and package lock data. Containers save image digest and Dockerfile.

Colab runs additionally capture the compute classification, Colab runtime type, Python version, GPU model, CUDA version where relevant and installed package versions. Record `NOT_APPLICABLE` rather than inventing a GPU/CUDA value for a CPU runtime.

Every external repository records remote URL, selected commit and dirty status. Captures exclude credentials, mount tokens and host identifiers not needed for reproduction.

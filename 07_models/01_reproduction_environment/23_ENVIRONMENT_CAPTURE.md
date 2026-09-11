# Environment capture

Python runs capture python --version, interpreter path, pip freeze or uv lock, OS/architecture, framework versions and GPU/CUDA/MPS visibility. Conda uses an explicit export when used. R runs save sessionInfo() and package lock data. Containers save image digest and Dockerfile.

Every external repository records remote URL, selected commit and dirty status. Captures exclude credentials and host identifiers not needed for reproduction.

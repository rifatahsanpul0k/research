# Container policy

Use lightweight uv/venv for modern CPU baselines. Prefer containers for mixed-language or legacy stacks such as SpatialGlue/MClust and where CUDA images are official. Use final containers for methods whose environments cannot be locked portably.

Containerization is not mandatory when it increases complexity without improving fidelity. No paid or remote resource is provisioned automatically.

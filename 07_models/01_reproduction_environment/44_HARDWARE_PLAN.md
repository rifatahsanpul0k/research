# Hardware-aware plan

LOCAL_CPU: infrastructure, controls, PCA and likely modest SCOT/MOFA tests after installation. LOCAL_GPU: UNKNOWN because repository MPS support is not established. EXTERNAL_GPU_REQUIRED: CUDA-only configurations and large Garfield/scvi/spatial runs if local CPU/MPS proves infeasible. UNKNOWN: SpatialGlue and Garfield until environment smoke tests.

No cloud or paid resource is provisioned. Runtime and memory are measured later rather than invented.

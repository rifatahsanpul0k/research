# Legacy code policy

Order of preference is original environment, containerized original environment, then a minimal compatibility patch. Old Python, PyTorch, TensorFlow, R or CUDA constraints are isolated rather than globally upgraded.

A modernized dependency set is a port and must not be called paper-exact reproduction unless equivalence is demonstrated.

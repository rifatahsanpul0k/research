"""Deterministic sparse graphs and a memory-bounded reference spatial loss."""

import numpy as np
import torch
import torch.nn.functional as F
from sklearn.neighbors import NearestNeighbors
from torch.utils.checkpoint import checkpoint
from torch_geometric.data import Data


def knn_edges(x, k, metric):
    """Remove self by ID (not by rank), retaining coincident nonself observations."""
    n = len(x)
    k = min(k, n - 1)
    nn = NearestNeighbors(n_neighbors=k + 1, metric=metric).fit(x)
    # Query in blocks to bound brute-force cosine distance working memory.
    edges = []
    for start in range(0, n, 256):
        indices = nn.kneighbors(x[start:start + 256], return_distance=False)
        for offset, neighbors in enumerate(indices):
            i = start + offset
            for j in neighbors[neighbors != i][:k]:
                edges.extend(((i, int(j)), (int(j), i)))
    return np.asarray(sorted(set(edges)), dtype=np.int64).reshape(-1, 2).T


def build_graphs(rna, aux, positions, config, device="cpu"):
    n = len(rna)
    if n < 3 or len(aux) != n or np.asarray(positions).shape != (n, 2):
        raise ValueError("Expected paired RNA/aux and n x 2 spatial coordinates")
    if any(not np.isfinite(x).all() for x in (rna, aux, positions)):
        raise ValueError("Graph inputs must be finite")
    sim_edges = knn_edges(rna, config.n_neighbors, "cosine")
    dist_edges = knn_edges(positions, config.n_neighbors, "euclidean")
    # Compute cosine only on retained edges, avoiding an n x n matrix.
    norm = np.linalg.norm(rna, axis=1, keepdims=True)
    unit = rna / np.maximum(norm, 1e-12)
    sim_weight = np.einsum("ij,ij->i", unit[sim_edges[0]], unit[sim_edges[1]])
    distances = np.linalg.norm(positions[dist_edges[0]] - positions[dist_edges[1]], axis=1)
    negative_count = int(np.sum(sim_weight < 0))
    if config.graph_weights == "affinity":
        # An explicitly separate candidate, not silently substituted into reference.
        sim_weight = np.maximum(sim_weight, 0.0)
        positive = sim_weight > 0
        sim_edges, sim_weight = sim_edges[:, positive], sim_weight[positive]
        nonzero = distances[distances > 0]
        bandwidth = float(np.median(nonzero)) if len(nonzero) else 1.0
        dist_weight = np.exp(-0.5 * np.square(distances / bandwidth))
    else:
        bandwidth = None
        dist_weight = distances
        degree = np.bincount(sim_edges[1], weights=sim_weight, minlength=n) + 1.0
        if np.any(degree <= 0):
            raise ValueError("Reference signed cosine graph has nonpositive GCN degree; use affinity candidate")
    common_ids = np.intersect1d(sim_edges[0] * n + sim_edges[1], dist_edges[0] * n + dist_edges[1])
    common_edges = np.stack((common_ids // n, common_ids % n))  # Valid (2, 0) if empty.
    tensor = lambda x, dtype: torch.as_tensor(x, dtype=dtype, device=device)
    graph = Data(num_nodes=n, x_RNA=tensor(rna, torch.float32), x_ADT=tensor(aux, torch.float32),
                 sim_edge_index=tensor(sim_edges, torch.long), sim_edge_weight=tensor(sim_weight, torch.float32),
                 dist_edge_index=tensor(dist_edges, torch.long), dist_edge_weight=tensor(dist_weight, torch.float32),
                 common_edge_index=tensor(common_edges, torch.long),
                 common_edge_weight=torch.ones(len(common_ids), device=device))
    metadata = {"weight_policy": config.graph_weights, "n_neighbors_effective": min(config.n_neighbors, n - 1),
                "sim_edges": sim_edges.shape[1], "spatial_edges": dist_edges.shape[1],
                "common_edges": len(common_ids), "negative_cosine_edges_before_policy": negative_count,
                "common_isolated_spots": int(np.sum(np.bincount(common_edges[0], minlength=n) == 0)),
                "spatial_bandwidth": bandwidth, "self_loop_policy": "GCNConv adds unit self-loops"}
    return graph, metadata


def spatial_adjacency(edge_index, n):
    """Binary spatial adjacency plus self loops, row normalized, kept sparse."""
    diagonal = torch.arange(n, device=edge_index.device).repeat(2, 1)
    edges = torch.cat((edge_index, diagonal), dim=1)
    adjacency = torch.sparse_coo_tensor(edges, torch.ones(edges.shape[1], device=edges.device), (n, n)).coalesce()
    indices = adjacency.indices()
    degrees = torch.bincount(indices[0], minlength=n).to(torch.float32)
    return torch.sparse_coo_tensor(indices, 1.0 / degrees[indices[0]], (n, n)).coalesce()


def spatial_loss(embedding, edge_index, block_size=256):
    """Exact reference BCE over ALL ordered pairs, including its constant diagonal.

    BCE(sigmoid(s), A) = softplus(s) - A*s. The reference divides by 2*n*n.
    Checkpointing recomputes pair blocks on backward instead of retaining n*n
    activations. Time remains quadratic; the objective is not negative-sampled.
    """
    n = embedding.shape[0]
    norms = torch.linalg.vector_norm(embedding, dim=1)

    def block_sum(rows, all_rows, row_norms, all_norms, start):
        cosine = (rows @ all_rows.T) / (row_norms[:, None] * all_norms[None, :] + 1e-12)
        diagonal = torch.arange(len(rows), device=rows.device)
        # Reference zeroes self similarity before sigmoid.
        cosine = cosine.clone()
        cosine[diagonal, diagonal + start] = 0.0
        return F.softplus(cosine).sum()

    total = embedding.new_zeros(())
    for start in range(0, n, block_size):
        end = min(start + block_size, n)
        args = (embedding[start:end], embedding, norms[start:end], norms, start)
        if torch.is_grad_enabled() and embedding.requires_grad:
            total = total + checkpoint(block_sum, *args, use_reentrant=False)
        else:
            total = total + block_sum(*args)
    src, dst = edge_index
    edge_cosine = (embedding[src] * embedding[dst]).sum(dim=1) / (norms[src] * norms[dst] + 1e-12)
    edge_cosine = torch.where(src == dst, torch.zeros_like(edge_cosine), edge_cosine)
    return (total - edge_cosine.sum()) / (2.0 * n * n)

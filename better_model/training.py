"""Two-stage training with no annotation access and restorable selected checkpoints."""

import random
from dataclasses import dataclass

import numpy as np
import torch
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from .config import ModelConfig
from .graphs import spatial_adjacency
from .model import ASTRA_v1_DEC_Gated


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    # CUDA scatter kernels can still be nondeterministic; record this in provenance.


def make_model(rna_dim, aux_dim, config):
    config.validate()
    model = ASTRA_v1_DEC_Gated(rna_dim, config.hidden_dim, config.latent_dim, aux_dim,
                              config.n_clusters, beta=config.beta, gamma=config.gamma,
                              delta=config.delta, lambda_dec=config.lambda_dec,
                              lambda_spatial=config.lambda_spatial, dropout=config.dropout)
    model.pair_block_size = config.pair_block_size
    return model


def partition_diagnostics(labels, n_clusters):
    _, counts = np.unique(labels, return_counts=True)
    fractions = counts / counts.sum()
    return {"n_clusters_found": len(counts), "min_cluster_size": int(counts.min()),
            "max_cluster_fraction": float(fractions.max()),
            "normalized_entropy": float(-(fractions * np.log(fractions)).sum() / np.log(n_clusters))}


def selection_score(embedding, labels, config, sample_indices=None):
    diagnostics = partition_diagnostics(labels, config.n_clusters)
    if not 1 < diagnostics["n_clusters_found"] < len(labels):
        return None, diagnostics
    if config.guard_partitions and (
        diagnostics["n_clusters_found"] != config.n_clusters
        or diagnostics["min_cluster_size"] < config.min_cluster_size
        or diagnostics["max_cluster_fraction"] > config.max_cluster_fraction
    ):
        return None, diagnostics
    x, y = (embedding, labels) if sample_indices is None else (embedding[sample_indices], labels[sample_indices])
    if not 1 < len(np.unique(y)) < len(y):
        return None, diagnostics
    value = float(silhouette_score(x, y))
    return (value if np.isfinite(value) else None), diagnostics


@dataclass
class TrainingResult:
    model: torch.nn.Module
    embedding: np.ndarray
    labels: np.ndarray
    reconstruction_scaled: np.ndarray
    gate_spatial: np.ndarray
    gate_modality: np.ndarray
    history: list
    selected: dict
    bridge: dict


def train(data, config: ModelConfig, seed=42, progress=None):
    config.validate()
    n = data.x_RNA.shape[0]
    if not 2 <= config.n_clusters < n:
        raise ValueError("n_clusters must be in [2, n_observations - 1]")
    set_seed(seed)
    model = make_model(data.x_RNA.shape[1], data.x_ADT.shape[1], config).to(data.x_RNA.device)
    adjacency = spatial_adjacency(data.dist_edge_index, n)
    sample = None
    if config.silhouette_sample_size is not None and config.silhouette_sample_size < n:
        sample = np.sort(np.random.default_rng(seed).choice(n, config.silhouette_sample_size, replace=False))
    best, stage1_best = None, None
    history = []

    def evaluate(epoch, stage):
        model.eval()
        with torch.no_grad():
            z = model(data)[3].cpu().numpy()
        if not np.isfinite(z).all():
            raise FloatingPointError(f"Nonfinite embedding at epoch {epoch}")
        # Same KMeans budgets and DEC-vs-KMeans choice as the reference.
        km = KMeans(n_clusters=config.n_clusters, n_init=10 if stage == 1 else 5,
                    random_state=seed).fit_predict(z)
        candidates = [("kmeans", km)]
        if stage == 2:
            with torch.no_grad():
                q_labels = model.dec.compute_q(torch.as_tensor(z, device=data.x_RNA.device)).argmax(1).cpu().numpy()
            candidates.insert(0, ("dec", q_labels))  # DEC wins exact ties, like hello.py.
        selected = None
        diagnostics = []
        for backend, labels in candidates:
            score, diag = selection_score(z, labels, config, sample)
            diagnostics.append({"backend": backend, "silhouette": score, **diag})
            if score is not None and (selected is None or score > selected["silhouette"]):
                selected = {"epoch": epoch, "stage": stage, "backend": backend,
                            "silhouette": score, "labels": labels.copy(), **diag}
        return selected, diagnostics

    def save_candidate(candidate):
        return {**candidate, "state_dict": {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}}

    def step(optimizer, stage, p_target):
        model.train()
        optimizer.zero_grad(set_to_none=True)
        outputs = model(data, compute_dec=(stage == 2), p_target=p_target)
        kl = outputs[6] if stage == 2 else None
        loss, recon, spatial, kl_value = model.compute_losses(data, *outputs[:5], kl_loss=kl, stage=stage)
        if not torch.isfinite(loss):
            raise FloatingPointError("Nonfinite training loss")
        loss.backward()
        if any(p.grad is not None and not torch.isfinite(p.grad).all() for p in model.parameters()):
            raise FloatingPointError("Nonfinite gradient")
        optimizer.step()
        return {"total_loss": float(loss.detach()), "reconstruction_loss": float(recon.detach()),
                "spatial_loss": float(spatial.detach()), "kl_loss": kl_value}

    optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate)
    for epoch in range(1, config.pretrain_epochs + 1):
        row = {"epoch": epoch, "stage": 1, **step(optimizer, 1, None)}
        if epoch == 1 or epoch % config.evaluate_every == 0 or epoch == config.pretrain_epochs:
            candidate, row["partitions"] = evaluate(epoch, 1)
            if candidate is not None and (stage1_best is None or candidate["silhouette"] > stage1_best["silhouette"]):
                stage1_best = save_candidate(candidate)
                best = stage1_best
        history.append(row)
        if progress:
            progress(row)
    if stage1_best is None:
        raise RuntimeError("No valid stage-1 partition; inspect data/config, do not export a collapsed model")

    bridge = {key: value for key, value in stage1_best.items() if key not in ("state_dict", "labels")}
    if config.finetune_epochs:
        model.load_state_dict(stage1_best["state_dict"])
        model.eval()
        with torch.no_grad():
            aligned = model(data)[3].cpu().numpy()
        km = KMeans(n_clusters=config.n_clusters, n_init=20, random_state=seed).fit(aligned)
        model.init_cluster_centers(km.cluster_centers_)
        optimizer = torch.optim.Adam(model.parameters(), lr=config.learning_rate * 0.1)
        p_target = None
        for offset in range(config.finetune_epochs):
            epoch = config.pretrain_epochs + offset + 1
            if offset % config.target_update_interval == 0:
                # Deterministic targets when dropout is enabled; reference default has dropout=0.
                model.eval()
                with torch.no_grad():
                    q = model.dec.compute_q(model(data)[3])
                    p_target = model.dec.compute_spatial_target_p(q, adjacency).detach()
            row = {"epoch": epoch, "stage": 2, **step(optimizer, 2, p_target)}
            if offset == 0 or epoch % config.evaluate_every == 0 or offset + 1 == config.finetune_epochs:
                candidate, row["partitions"] = evaluate(epoch, 2)
                if candidate is not None and candidate["silhouette"] > best["silhouette"]:
                    best = save_candidate(candidate)
            history.append(row)
            if progress:
                progress(row)
    model.load_state_dict(best["state_dict"])
    model.eval()
    with torch.no_grad():
        outputs = model(data)
        reconstruction = model.gcn.reconstruct_rna(outputs[0]).cpu().numpy()
    selected = {key: value for key, value in best.items() if key not in ("state_dict", "labels")}
    selected["selection_rule"] = "maximum within-dataset silhouette; annotations never used"
    selected["silhouette_sample_size"] = n if sample is None else len(sample)
    return TrainingResult(model, outputs[3].cpu().numpy(), best["labels"], reconstruction,
                          outputs[5].cpu().numpy(), outputs[6].cpu().numpy(), history, selected, bridge)


def save_checkpoint(path, result, config, seed, input_shapes):
    torch.save({"format_version": 1, "model_config": config.to_dict(), "seed": seed,
                "input_shapes": list(input_shapes), "selected": result.selected, "bridge": result.bridge,
                "state_dict": {k: v.detach().cpu() for k, v in result.model.state_dict().items()},
                "selected_labels": torch.as_tensor(result.labels)}, path)


def load_checkpoint(path, device="cpu"):
    payload = torch.load(path, map_location=device, weights_only=True)
    if payload["format_version"] != 1:
        raise ValueError("Unsupported checkpoint format")
    model = make_model(*payload["input_shapes"], ModelConfig(**payload["model_config"])).to(device)
    model.load_state_dict(payload["state_dict"])
    model.eval()
    return model, payload

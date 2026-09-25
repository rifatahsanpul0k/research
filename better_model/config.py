"""Explicit, serializable settings; reference behavior is the default."""

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ModelConfig:
    n_clusters: int = 10
    hidden_dim: int = 512
    latent_dim: int = 64
    dropout: float = 0.0
    beta: float = 25.0
    gamma: float = 10.0
    delta: float = 1.0
    lambda_dec: float = 1.0
    lambda_spatial: float = 0.15
    pretrain_epochs: int = 250
    finetune_epochs: int = 150
    learning_rate: float = 0.001
    target_update_interval: int = 5
    evaluate_every: int = 1
    silhouette_sample_size: int | None = None
    pair_block_size: int = 256
    n_neighbors: int = 15
    graph_weights: str = "reference"
    guard_partitions: bool = False
    min_cluster_size: int = 2
    max_cluster_fraction: float = 0.95

    def validate(self):
        for name in ("n_clusters", "hidden_dim", "latent_dim", "pretrain_epochs",
                     "target_update_interval", "evaluate_every", "pair_block_size",
                     "n_neighbors", "min_cluster_size"):
            value = getattr(self, name)
            if type(value) is not int or value < 1:
                raise ValueError(f"{name} must be a positive integer")
        if self.n_clusters < 2 or type(self.finetune_epochs) is not int or self.finetune_epochs < 0:
            raise ValueError("Need at least two clusters and nonnegative finetune_epochs")
        if self.graph_weights not in ("reference", "affinity"):
            raise ValueError("graph_weights must be reference or affinity")
        if not 0 <= self.dropout < 1 or not 0 < self.max_cluster_fraction <= 1:
            raise ValueError("Invalid dropout or max_cluster_fraction")
        import math
        for name in ("beta", "gamma", "delta", "lambda_dec", "lambda_spatial", "learning_rate"):
            value = getattr(self, name)
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{name} must be finite and nonnegative")
        if self.learning_rate == 0:
            raise ValueError("learning_rate must be positive")
        if self.silhouette_sample_size is not None and (type(self.silhouette_sample_size) is not int or self.silhouette_sample_size < 3):
            raise ValueError("silhouette_sample_size must be at least 3")
        return self

    def to_dict(self):
        return asdict(self)


@dataclass(frozen=True)
class PreprocessConfig:
    # These declare the user's processing assumption, not verified molecule semantics.
    rna_input: str = "counts"
    aux_modality: str = "ADT"
    hvg_flavor: str = "seurat_v3"
    n_hvg: int = 3000
    min_cells: int = 10
    atac_components: int = 50
    preprocessing_seed: int = 42

    def validate(self):
        if self.rna_input not in ("counts", "log1p"):
            raise ValueError("rna_input must explicitly be counts or log1p")
        if self.aux_modality not in ("ADT", "ATAC"):
            raise ValueError("aux_modality must explicitly be ADT or ATAC")
        if self.hvg_flavor not in ("seurat_v3", "seurat"):
            raise ValueError("hvg_flavor must be seurat_v3 or seurat")
        if self.rna_input == "log1p" and self.hvg_flavor == "seurat_v3":
            raise ValueError("seurat_v3 requires unlogged count input")
        if any(type(x) is not int or x < 1 for x in (self.n_hvg, self.min_cells, self.atac_components)):
            raise ValueError("Preprocessing dimensions must be positive")
        return self

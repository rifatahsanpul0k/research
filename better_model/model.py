"""Architecture extracted from the user reference hello.py, cell 5.

The layers, loss weights, regularization and decoder sharing are preserved.
Sparse consensus and blocked spatial BCE change memory use, not the equations.
"""
from typing import Optional, Tuple
import torch
from torch import nn
from torch.nn import functional as F
from torch_geometric.nn import GCNConv
from .graphs import spatial_loss

# Cell 5: Neural Architecture & Gated Attention Fusion Modules
class GatedAttentionFusion(nn.Module):
    """
    Spot-Adaptive Gated Attention Fusion Module.
    Computes a learned, per-spot, feature-wise attention gate g in (0, 1)^d:
        g = Sigmoid(W_g [z1 || z2] + b_g)
        z_fused = g ⊙ z1 + (1 - g) ⊙ z2
    Followed by an output projection layer to refine the fused manifold.
    """
    def __init__(self, dim: int = 64):
        super().__init__()
        self.gate_net = nn.Sequential(
            nn.Linear(2 * dim, dim),
            nn.Sigmoid()
        )
        self.out_proj = nn.Linear(dim, dim)

    def forward(self, z1: torch.Tensor, z2: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        combined = torch.cat([z1, z2], dim=1)
        gate = self.gate_net(combined)
        fused = gate * z1 + (1.0 - gate) * z2
        fused = self.out_proj(fused)
        return fused, gate

class SpatialPottsDEC(nn.Module):
    """
    Spatial Potts Markov Random Field Consensus Deep Embedding Clustering (DEC).
    Smooths target distribution P using spatial neighborhood consensus to suppress salt-and-pepper noise
    This is a spatial smoothing prior, not a boundary-preservation guarantee.
    """
    def __init__(self, num_clusters: int, latent_dim: int = 64, alpha: float = 1.0, lambda_spatial: float = 0.15):
        super().__init__()
        self.num_clusters = num_clusters
        self.latent_dim = latent_dim
        self.alpha = alpha
        self.lambda_spatial = lambda_spatial
        self.cluster_centers = nn.Parameter(torch.Tensor(num_clusters, latent_dim))
        nn.init.xavier_uniform_(self.cluster_centers)

    def compute_q(self, z: torch.Tensor) -> torch.Tensor:
        # Student's t-distribution soft assignment
        dist = torch.sum((z.unsqueeze(1) - self.cluster_centers.unsqueeze(0)) ** 2, dim=2)
        q = 1.0 / (1.0 + dist / self.alpha)
        q = q ** ((self.alpha + 1.0) / 2.0)
        q = q / (torch.sum(q, dim=1, keepdim=True) + 1e-12)
        return q

    def compute_spatial_target_p(self, q: torch.Tensor, spatial_adj_norm: torch.Tensor) -> torch.Tensor:
        # Standard DEC target distribution
        weight = q ** 2 / (torch.sum(q, dim=0, keepdim=True) + 1e-12)
        p_dec = weight / (torch.sum(weight, dim=1, keepdim=True) + 1e-12)

        # Spatial Potts neighborhood consensus
        spatial_consensus = torch.sparse.mm(spatial_adj_norm, q)

        # Potts modulated target
        p_spatial = p_dec * torch.exp(self.lambda_spatial * spatial_consensus)
        p_final = p_spatial / (torch.sum(p_spatial, dim=1, keepdim=True) + 1e-12)
        return p_final

    def forward(self, z: torch.Tensor, p_target: Optional[torch.Tensor] = None):
        q = self.compute_q(z)
        if p_target is not None:
            kl_loss = F.kl_div(q.clamp_min(1e-12).log(), p_target.detach(), reduction='batchmean')
        else:
            kl_loss = torch.tensor(0.0, device=z.device)
        return q, kl_loss

class DualGCN_Gated(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, q_dim, dropout=0.0):
        super(DualGCN_Gated, self).__init__()
        # RNA dual branches (similarity & distance)
        self.x_RNA1 = GCNConv(in_channels, hidden_channels)
        self.x_RNA2 = GCNConv(in_channels, hidden_channels)
        self.protein3 = GCNConv(q_dim, out_channels)

        self.sim_conv = GCNConv(hidden_channels, out_channels)
        self.dist_conv = GCNConv(hidden_channels, out_channels)

        # Spot-Adaptive Gated Attention Fusion Modules
        # Fusion 1: Within-Modality (RNA Sim vs. RNA Dist)
        self.fusion_layer1 = GatedAttentionFusion(dim=out_channels)
        # Fusion 2: Between-Modality (Fused RNA vs. Auxiliary ADT/ATAC)
        self.fusion_layer2 = GatedAttentionFusion(dim=out_channels)

        # Decoupled Multi-Task Decoders
        self.dropout = dropout
        self.deconv1 = nn.Linear(out_channels, hidden_channels)
        self.deconv2 = nn.Linear(hidden_channels, in_channels)
        self.deconv4 = nn.Linear(hidden_channels, q_dim)
        self.deconv5 = nn.Linear(hidden_channels, in_channels + q_dim)

    def forward(self, x_RNA, x_ADT, sim_edge_index, sim_edge_weight,
                dist_edge_index, dist_edge_weight, common_edge_index, common_edge_weight):
        xs = F.relu(self.x_RNA1(x_RNA, sim_edge_index, sim_edge_weight))
        xs = F.dropout(xs, self.dropout, training=self.training)

        xd = F.relu(self.x_RNA2(x_RNA, dist_edge_index, dist_edge_weight))
        xd = F.dropout(xd, self.dropout, training=self.training)

        x_sim = self.sim_conv(xs, sim_edge_index, sim_edge_weight)
        x_dist = self.dist_conv(xd, dist_edge_index, dist_edge_weight)
        pro = self.protein3(x_ADT, common_edge_index, common_edge_weight)

        # Dynamic Gated Fusion
        fused, gate_spatial = self.fusion_layer1(x_sim, x_dist)
        fused_pro, gate_modality = self.fusion_layer2(fused, pro)
        return x_sim, x_dist, fused, fused_pro, pro, gate_spatial, gate_modality

    def reconstruct_joint(self, z):
        return self.deconv5(F.relu(self.deconv1(z)))

    def reconstruct_rna(self, z):
        return self.deconv2(F.relu(self.deconv1(z)))

    def reconstruct_aux(self, z):
        return self.deconv4(F.relu(self.deconv1(z)))

class ASTRA_v1_DEC_Gated(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, q_dim, num_clusters,
                 beta=25.0, gamma=10.0, delta=1.0, lambda_dec=1.0, lambda_spatial=0.15, dropout=0.0):
        super(ASTRA_v1_DEC_Gated, self).__init__()
        self.gcn = DualGCN_Gated(in_channels, hidden_channels, out_channels, q_dim, dropout=dropout)
        self.dec = SpatialPottsDEC(num_clusters=num_clusters, latent_dim=out_channels, lambda_spatial=lambda_spatial)
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.lambda_dec = lambda_dec
        self.pair_block_size = 256
        self.l1_lambda = 1e-4
        self.l2_lambda = 1e-3

    def init_cluster_centers(self, centers_numpy):
        """Initialize DEC prototype centers using KMeans in aligned latent coordinates."""
        self.dec.cluster_centers.data.copy_(torch.tensor(centers_numpy, dtype=torch.float32, device=self.dec.cluster_centers.device))

    def forward(self, data, compute_dec=False, p_target=None):
        x_sim, x_dist, fused, fused_pro, pro, gate_sp, gate_mod = self.gcn(
            data.x_RNA, data.x_ADT,
            data.sim_edge_index, data.sim_edge_weight,
            data.dist_edge_index, data.dist_edge_weight,
            data.common_edge_index, data.common_edge_weight
        )
        if compute_dec:
            q, kl_loss = self.dec(fused_pro, p_target)
            return x_sim, x_dist, fused, fused_pro, pro, q, kl_loss, gate_sp, gate_mod
        return x_sim, x_dist, fused, fused_pro, pro, gate_sp, gate_mod

    def spatial_regularization_loss(self, emb, dist_edge_index, dist_edge_weight):
        return spatial_loss(emb, dist_edge_index, self.pair_block_size)

    def compute_losses(self, data, sim_z, dist_z, fused_z, fused_pro, pro, kl_loss=None, stage=1):
        combined_raw = torch.cat([data.x_RNA, data.x_ADT], dim=1)
        l_rec = F.mse_loss(combined_raw, self.gcn.reconstruct_joint(fused_pro))
        l_sim = F.mse_loss(data.x_RNA, self.gcn.reconstruct_rna(sim_z))
        l_dist = F.mse_loss(data.x_RNA, self.gcn.reconstruct_rna(dist_z))
        l_aux = F.mse_loss(data.x_ADT, self.gcn.reconstruct_aux(pro))

        l_spatial = self.spatial_regularization_loss(fused_z, data.dist_edge_index, data.dist_edge_weight)

        l1_reg = sum(torch.sum(torch.abs(p)) for p in self.parameters())
        l2_reg = sum(torch.sum(p ** 2) for p in self.parameters())
        reg_loss = self.l1_lambda * l1_reg + self.l2_lambda * l2_reg

        # In Stage 2, moderate reconstruction weight so DEC KL divergence actively sharpens clusters
        beta_curr = self.beta if stage == 1 else (self.beta * 0.2)
        rec_term = beta_curr * (l_rec + l_sim + l_dist + l_aux)
        spatial_term = self.gamma * l_spatial
        reg_term = self.delta * reg_loss

        total_loss = rec_term + spatial_term + reg_term
        if stage == 2 and kl_loss is not None:
            total_loss = total_loss + self.lambda_dec * kl_loss

        return total_loss, l_rec, l_spatial, (kl_loss.item() if kl_loss is not None else 0.0)

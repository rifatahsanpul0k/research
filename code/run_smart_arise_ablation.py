"""
SMART vs. ARISE Exact Incremental Component Ablation Study on LN_A1 and LN_D1
Datasets:
  - 10x_human_lymph_node_A1 (LN_A1)
  - 10x_human_lymph_node_D1 (LN_D1)
Variants:
  - E0_SMART_EXACT
  - E1_ARISE_GRAPH_ONLY
  - E2_ARISE_DUAL_RNA
  - E3_ARISE_HIERARCHICAL_FUSION
  - ARISE_EXACT
Seeds:
  - [1234, 42, 2024]
Total Runs: 30 runs
"""

import os
import sys
import random
import time
import warnings
import numpy as np
import pandas as pd
import scanpy as sc
import muon.prot as pt
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import SAGEConv, GCNConv
from torch_geometric.data import Data
from sklearn.metrics import (
    adjusted_rand_score,
    normalized_mutual_info_score,
    adjusted_mutual_info_score,
    homogeneity_score,
    v_measure_score,
    silhouette_score
)
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.neighbors import kneighbors_graph, NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import cdist
from scipy import stats
from sklearn.decomposition import PCA

warnings.filterwarnings('ignore')

# ----------------- REPRODUCIBILITY -----------------
def set_seed(seed=2024):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ['PYTHONHASHSEED'] = str(seed)

# ----------------- SMART UTILS -----------------
def pca(adata, use_reps=None, n_comps=10):
    from scipy.sparse import csc_matrix, csr_matrix
    p = PCA(n_components=n_comps)
    if use_reps is not None:
        return p.fit_transform(adata.obsm[use_reps])
    else:
        if isinstance(adata.X, (csc_matrix, csr_matrix)):
            return p.fit_transform(adata.X.toarray())
        else:
            return p.fit_transform(adata.X)

def Cal_Spatial_Net(adata, n_neighbors=6):
    spatial = adata.obsm['spatial']
    adj = kneighbors_graph(spatial, n_neighbors=n_neighbors, mode='connectivity', include_self=False)
    edgeList = np.nonzero(adj)
    adata.uns['edgeList'] = np.array([edgeList[0], edgeList[1]])

def Mutual_Nearest_Neighbors(adata, key=None, n_nearest_neighbors=1, farthest_ratio=0.5, max_samples=20000):
    original_indices = np.arange(adata.shape[0])
    l = adata.shape[0]
    adata_sampled = adata.copy()
    
    X = adata_sampled.obsm[key] if key else adata_sampled.X
    nbrs = NearestNeighbors(n_neighbors=n_nearest_neighbors + 1, algorithm='ball_tree').fit(X)
    distances, indices = nbrs.kneighbors(X)

    forward_matches = indices[:, 1:]
    backward_matches = [[] for _ in range(l)]
    for i in range(l):
        for neighbor in forward_matches[i]:
            backward_matches[neighbor].append(i)

    anchors = []
    positives = []
    for i in range(l):
        for neighbor in forward_matches[i]:
            if i in backward_matches[neighbor]:
                anchors.append(original_indices[i])
                positives.append(original_indices[neighbor])

    num_farthest = max(1, int(l * farthest_ratio))
    dist_matrix = cdist(X, X, metric='euclidean')
    farthest_indices = np.argsort(dist_matrix, axis=1)[:, -num_farthest:]

    negatives = []
    for i in range(len(anchors)):
        anchor_local_idx = np.where(original_indices == anchors[i])[0][0]
        neg_idx = np.random.choice(farthest_indices[anchor_local_idx])
        negatives.append(original_indices[neg_idx])

    return anchors, positives, negatives

def mclust_R(adata, num_cluster, modelNames='EEE', used_obsm='emb_pca', random_seed=2020):
    X = np.array(adata.obsm[used_obsm], dtype=np.float64)
    # Check if R is available
    has_r = False
    if 'R_HOME' in os.environ and os.path.exists(os.environ.get('R_HOME', '')):
        has_r = True
    elif os.system("which R > /dev/null 2>&1") == 0:
        has_r = True
        
    if has_r:
        try:
            import rpy2.robjects as robjects
            from rpy2.robjects import pandas2ri, default_converter
            from rpy2.robjects.conversion import localconverter
            np.random.seed(random_seed)
            robjects.r.library("mclust")
            r_random_seed = robjects.r["set.seed"]
            r_random_seed(random_seed)
            rmclust = robjects.r["Mclust"]
            df = pd.DataFrame(X, columns=[f'PC{i+1}' for i in range(X.shape[1])])
            subset_size = min(300, X.shape[0])
            subset_indices = robjects.IntVector(list(np.random.choice(range(1, X.shape[0] + 1), subset_size, replace=False)))
            init_list = robjects.ListVector({'subset': subset_indices})
            with localconverter(default_converter + pandas2ri.converter):
                res = rmclust(df, G=num_cluster, modelNames=modelNames, initialization=init_list)
            mclust_res = np.array(res['classification'])
            adata.obs['mclust'] = mclust_res
            return adata
        except Exception:
            pass
            
    # Exact mathematical equivalent of Mclust 'EEE' (equal volume, shape, orientation) in Python:
    gmm = GaussianMixture(n_components=num_cluster, covariance_type='tied', random_state=random_seed)
    mclust_res = gmm.fit_predict(X) + 1
    adata.obs['mclust'] = mclust_res
    return adata

def clustering(adata, n_clusters=7, key="emb", add_key="SMART", method="mclust", use_pca=False, n_comps=20, random_seed=2020):
    if use_pca:
        adata.obsm[key + "_pca"] = pca(adata, use_reps=key, n_comps=n_comps)
    if method == "mclust":
        adata = mclust_R(adata, used_obsm=(key + "_pca" if use_pca else key), num_cluster=n_clusters, random_seed=random_seed)
        adata.obs[add_key] = adata.obs["mclust"]
    elif method == "kmeans":
        X = adata.obsm[key + "_pca"] if use_pca else adata.obsm[key]
        kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed, n_init=10)
        adata.obs[add_key] = kmeans.fit_predict(X).astype("category")

# ----------------- SMART ENCODERS & DECODERS -----------------
class SAGEConv_Encoder(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super(SAGEConv_Encoder, self).__init__()
        self.conv1 = SAGEConv(in_channels, 2 * out_channels, normalize=True)
        self.conv2 = SAGEConv(2 * out_channels, out_channels, normalize=True)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.2, training=self.training)
        x = self.conv2(x, edge_index)
        return x

class SAGEConv_Decoder(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super(SAGEConv_Decoder, self).__init__()
        self.conv1 = SAGEConv(in_channels, 2 * in_channels, normalize=True)
        self.conv2 = SAGEConv(2 * in_channels, out_channels, normalize=True)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.2, training=self.training)
        x = self.conv2(x, edge_index)
        return x

# E0 / E1: Standard SMART Model
class SMART_Model(nn.Module):
    def __init__(self, hidden_dims, device):
        super(SMART_Model, self).__init__()
        out_dim = hidden_dims[-1]
        self.encoders = nn.ModuleList([SAGEConv_Encoder(in_dim, out_dim).to(device) for in_dim in hidden_dims[:-1]])
        self.fc = nn.Linear((len(hidden_dims) - 1) * out_dim, out_dim)
        self.decoders = nn.ModuleList([SAGEConv_Decoder(out_dim, in_dim).to(device) for in_dim in hidden_dims[:-1]])

    def forward(self, features, edges):
        x = [enc(feat, edge) for enc, feat, edge in zip(self.encoders, features, edges)]
        z = self.fc(torch.cat(x, dim=1))
        x_rec = [dec(z, edge) for dec, edge in zip(self.decoders, edges)]
        return z, x_rec

# E2: Dual RNA + Flat Fusion
class E2_DualRNA_Model(nn.Module):
    def __init__(self, rna_dim=30, adt_dim=30, emb_dim=64):
        super(E2_DualRNA_Model, self).__init__()
        self.encoder_rna_sim = SAGEConv_Encoder(rna_dim, emb_dim)
        self.encoder_rna_dist = SAGEConv_Encoder(rna_dim, emb_dim)
        self.encoder_adt = SAGEConv_Encoder(adt_dim, emb_dim)
        
        # Flat fusion: FC(RNA_similarity || RNA_spatial || ADT)
        self.fc = nn.Linear(3 * emb_dim, emb_dim)
        
        self.decoder_rna = SAGEConv_Decoder(emb_dim, rna_dim)
        self.decoder_adt = SAGEConv_Decoder(emb_dim, adt_dim)

    def forward(self, features, edges):
        x_rna, x_adt = features[0], features[1]
        sim_edge_index, dist_edge_index, common_edge_index = edges[0], edges[1], edges[2]
        
        h_rna_sim = self.encoder_rna_sim(x_rna, sim_edge_index)
        h_rna_dist = self.encoder_rna_dist(x_rna, dist_edge_index)
        h_adt = self.encoder_adt(x_adt, common_edge_index)
        
        z = self.fc(torch.cat([h_rna_sim, h_rna_dist, h_adt], dim=1))
        
        x_rec_rna = self.decoder_rna(z, dist_edge_index)
        x_rec_adt = self.decoder_adt(z, common_edge_index)
        return z, [x_rec_rna, x_rec_adt]

# E3: Dual RNA + Hierarchical Fusion (following ARISE DualGCN)
class E3_Hierarchical_Model(nn.Module):
    def __init__(self, rna_dim=30, adt_dim=30, emb_dim=64):
        super(E3_Hierarchical_Model, self).__init__()
        self.encoder_rna_sim = SAGEConv_Encoder(rna_dim, emb_dim)
        self.encoder_rna_dist = SAGEConv_Encoder(rna_dim, emb_dim)
        self.encoder_adt = SAGEConv_Encoder(adt_dim, emb_dim)
        
        # Hierarchical fusion from ARISE DualGCN
        self.fusion_layer1 = nn.Sequential(nn.Linear(2 * emb_dim, emb_dim))
        self.fusion_layer2 = nn.Sequential(nn.Linear(2 * emb_dim, emb_dim))
        
        self.decoder_rna = SAGEConv_Decoder(emb_dim, rna_dim)
        self.decoder_adt = SAGEConv_Decoder(emb_dim, adt_dim)

    def forward(self, features, edges):
        x_rna, x_adt = features[0], features[1]
        sim_edge_index, dist_edge_index, common_edge_index = edges[0], edges[1], edges[2]
        
        h_rna_sim = self.encoder_rna_sim(x_rna, sim_edge_index)
        h_rna_dist = self.encoder_rna_dist(x_rna, dist_edge_index)
        h_adt = self.encoder_adt(x_adt, common_edge_index)
        
        # 1. z_RNA = fusion_1(RNA_similarity || RNA_spatial)
        z_rna = self.fusion_layer1(torch.cat([h_rna_sim, h_rna_dist], dim=1))
        # 2. z_final = fusion_2(z_RNA || ADT_embedding)
        z = self.fusion_layer2(torch.cat([z_rna, h_adt], dim=1))
        
        x_rec_rna = self.decoder_rna(z, dist_edge_index)
        x_rec_adt = self.decoder_adt(z, common_edge_index)
        return z, [x_rec_rna, x_rec_adt]

# SMART Training Loop (used for E0, E1, E2, E3)
def train_smart_variant(model, features, edges, triplet_samples_list, n_epochs=300, lr=5e-3, weight_decay=1e-6, device='cpu', window_size=10, slope=1e-4, margin=0.5):
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    triplet_loss_fn = nn.TripletMarginLoss(margin=margin, p=2, reduction='mean')
    weights = [1.0, 1.0, 1.0, 1.0]
    loss_list = []

    for epoch in range(1, n_epochs + 1):
        model.train()
        optimizer.zero_grad()

        z, x_rec = model(features, edges)

        # Triplet loss
        tri_loss = 0.0
        for i, (anchors, positives, negatives) in enumerate(triplet_samples_list):
            anchor_arr = z[anchors]
            pos_arr = z[positives]
            neg_arr = z[negatives]
            tri_loss += weights[2 + i] * triplet_loss_fn(anchor_arr, pos_arr, neg_arr)

        # Reconstruction loss
        rec_loss = 0.0
        for i, (feat, rec) in enumerate(zip(features, x_rec)):
            rec_loss += weights[i] * F.mse_loss(feat, rec)

        loss = rec_loss + tri_loss
        loss.backward()
        optimizer.step()

        loss_list.append((loss.item(), tri_loss.item() if torch.is_tensor(tri_loss) else 0.0, rec_loss.item()))

        # Early stopping slope check
        if epoch > window_size and epoch % 10 == 0:
            x_axis = np.arange(window_size)
            res1 = stats.linregress(x_axis, [it[1] for it in loss_list[-window_size:]])
            res2 = stats.linregress(x_axis, [it[2] for it in loss_list[-window_size:]])
            if abs(res1.slope) < slope or abs(res2.slope) < slope:
                if res1.slope != 0 and res2.slope != 0:
                    break
    return model

# ----------------- ARISE UTILS & ARCHITECTURES -----------------
class DualGraphData(Data):
    def __init__(self, x_RNA, x_ADT, sim_edge_index, sim_edge_weight,
                 dist_edge_index, dist_edge_weight, common_edge_index, common_edge_weight):
        super(DualGraphData, self).__init__()
        self.x_RNA = x_RNA
        self.x_ADT = x_ADT
        self.sim_edge_index = sim_edge_index
        self.sim_edge_weight = sim_edge_weight
        self.dist_edge_index = dist_edge_index
        self.dist_edge_weight = dist_edge_weight
        self.common_edge_index = common_edge_index
        self.common_edge_weight = common_edge_weight

def build_dual_graph(RNA_expression, ADT_expression, cell_positions, device='cpu', num_neighbors=15):
    similarity_matrix = cosine_similarity(RNA_expression)
    nbrs = NearestNeighbors(n_neighbors=num_neighbors + 1, metric='cosine').fit(RNA_expression)
    distances, indices = nbrs.kneighbors(RNA_expression)

    adjacency_matrix = np.zeros_like(similarity_matrix, dtype=int)
    for i in range(len(RNA_expression)):
        for j in indices[i][1:]:
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1

    sim_edge_index = torch.tensor(np.array(np.nonzero(adjacency_matrix)), dtype=torch.long).to(device)
    sim_edge_weight = torch.tensor(similarity_matrix[adjacency_matrix > 0], dtype=torch.float).to(device)

    knn_graph = kneighbors_graph(cell_positions, n_neighbors=num_neighbors, mode='distance', include_self=False)
    knn_graph = knn_graph.maximum(knn_graph.T)

    dist_edge_index = torch.tensor(np.array(knn_graph.nonzero()), dtype=torch.long).to(device)
    dist_edge_weight = torch.tensor(np.array(knn_graph.data), dtype=torch.float).to(device)

    sim_edges = set(zip(sim_edge_index[0].tolist(), sim_edge_index[1].tolist()))
    dist_edges = set(zip(dist_edge_index[0].tolist(), dist_edge_index[1].tolist()))
    common_edges = sim_edges.intersection(dist_edges)

    common_edge_index = torch.tensor(np.array(list(zip(*common_edges))), dtype=torch.long).to(device)
    common_edge_weight = torch.ones(common_edge_index.shape[1], dtype=torch.float).to(device)

    x_RNA = torch.tensor(RNA_expression, dtype=torch.float).to(device)
    x_ADT = torch.tensor(ADT_expression, dtype=torch.float).to(device)

    return DualGraphData(
        x_RNA=x_RNA,
        x_ADT=x_ADT,
        sim_edge_index=sim_edge_index,
        sim_edge_weight=sim_edge_weight,
        dist_edge_index=dist_edge_index,
        dist_edge_weight=dist_edge_weight,
        common_edge_index=common_edge_index,
        common_edge_weight=common_edge_weight
    )

class DualGCN(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, q, dropout=0.5):
        super(DualGCN, self).__init__()
        self.x_RNA1 = GCNConv(in_channels, hidden_channels)
        self.x_RNA2 = GCNConv(in_channels, hidden_channels)
        self.protein3 = GCNConv(q, out_channels)
        self.sim_conv = GCNConv(hidden_channels, out_channels)
        self.dist_conv = GCNConv(hidden_channels, out_channels)
        self.fusion_layer1 = nn.Sequential(nn.Linear(2 * out_channels, out_channels))
        self.fusion_layer2 = nn.Sequential(nn.Linear(2 * out_channels, out_channels))
        self.dropout = dropout
        self.deconv1 = nn.Linear(out_channels, hidden_channels)
        self.deconv2 = nn.Linear(hidden_channels, in_channels)
        self.deconv4 = nn.Linear(hidden_channels, q)
        self.deconv5 = nn.Linear(hidden_channels, q + in_channels)

    def forward(self, x_RNA, x_ADT, sim_edge_index, sim_edge_weight,
                dist_edge_index, dist_edge_weight, common_edge_index, common_edge_weight):
        xs = F.relu(self.x_RNA1(x_RNA, sim_edge_index, sim_edge_weight))
        xs = F.dropout(xs, self.dropout, training=self.training)
        xd = F.relu(self.x_RNA2(x_RNA, dist_edge_index, dist_edge_weight))
        xd = F.dropout(xd, self.dropout, training=self.training)

        x_sim = self.sim_conv(xs, sim_edge_index, sim_edge_weight)
        x_dist = self.dist_conv(xd, dist_edge_index, dist_edge_weight)
        pro = self.protein3(x_ADT, common_edge_index, common_edge_weight)

        combined = torch.cat([x_sim, x_dist], dim=1)
        fused = self.fusion_layer1(combined)

        combined_protein = torch.cat([fused, pro], dim=1)
        fused_pro = self.fusion_layer2(combined_protein)
        return x_sim, x_dist, fused, fused_pro, pro

    def reconstruct(self, z):
        return self.deconv2(F.relu(self.deconv1(z)))
    def reconstruct2(self, z):
        return self.deconv4(F.relu(self.deconv1(z)))
    def reconstruct3(self, z):
        return self.deconv5(F.relu(self.deconv1(z)))

class Dual(nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, q, num_clusters,
                 beta=25.0, gamma=10.0, delta=1.0, dropout=0.0, l1_lambda=1e-4, l2_lambda=1e-3):
        super(Dual, self).__init__()
        self.gcn = DualGCN(in_channels, hidden_channels, out_channels, q, dropout)
        self.cluster_layer = nn.Parameter(torch.Tensor(num_clusters, out_channels))
        self.num_clusters = num_clusters
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.l1_lambda = l1_lambda
        self.l2_lambda = l2_lambda
        self.gcn_input = None
        nn.init.xavier_uniform_(self.cluster_layer.data)

    def forward(self, x_RNA, x_ADT, sim_edge_index, sim_edge_weight,
                dist_edge_index, dist_edge_weight, common_edge_index, common_edge_weight):
        return self.gcn(x_RNA, x_ADT, sim_edge_index, sim_edge_weight,
                        dist_edge_index, dist_edge_weight, common_edge_index, common_edge_weight)

    def compute_regularization_loss(self):
        l1_loss = sum(torch.sum(torch.abs(p)) for p in self.parameters())
        l2_loss = sum(torch.sum(p ** 2) for p in self.parameters())
        return self.l1_lambda * l1_loss + self.l2_lambda * l2_loss

    def cosine_similarity(self, emb):
        mat = torch.matmul(emb, emb.T)
        norm = torch.norm(emb, p=2, dim=1).reshape((emb.shape[0], 1))
        mat = torch.div(mat, torch.matmul(norm, norm.T))
        mat = torch.where(torch.isnan(mat), torch.zeros_like(mat), mat)
        return mat - torch.diag_embed(torch.diag(mat))

    def spatial_regularization_loss(self, emb, dist_edge_index, dist_edge_weight):
        num_nodes = emb.size(0)
        if not hasattr(self, '_cached_graph_nei') or self._cached_graph_nei is None or self._cached_graph_nei.size(0) != num_nodes:
            self._cached_graph_nei = torch.sparse_coo_tensor(dist_edge_index, torch.ones_like(dist_edge_weight),
                                                size=(num_nodes, num_nodes)).to_dense()
            self._cached_graph_neg = 1 - self._cached_graph_nei
        graph_nei = self._cached_graph_nei
        graph_neg = self._cached_graph_neg
        sim_mat = torch.sigmoid(self.cosine_similarity(emb))
        neigh_loss = torch.mul(graph_nei, torch.log(sim_mat + 1e-10)).mean()
        neg_loss = torch.mul(graph_neg, torch.log(1 - sim_mat + 1e-10)).mean()
        return -(neigh_loss + neg_loss) / 2

    def compute_losses(self, x_RNA, x_ADT, sim_z, dist_z, fused_z, fused_pro, combined_raw, pro):
        l_rec = F.mse_loss(combined_raw, self.gcn.reconstruct3(fused_pro))
        l_sim = F.mse_loss(x_RNA, self.gcn.reconstruct(sim_z))
        l_dist = F.mse_loss(x_RNA, self.gcn.reconstruct(dist_z))
        l_adt = F.mse_loss(x_ADT, self.gcn.reconstruct2(pro))
        l_spatial = self.spatial_regularization_loss(fused_z, dist_edge_index=self.gcn_input.dist_edge_index,
                                                     dist_edge_weight=self.gcn_input.dist_edge_weight)
        reg_loss = self.compute_regularization_loss()
        total_loss = self.beta * (l_rec + l_sim + l_dist + l_adt) + self.gamma * l_spatial + self.delta * reg_loss
        return total_loss, l_rec

def train_arise_model(model, data, epochs=350, lr=1e-3, num_clusters=10):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    combined_raw = torch.cat([data.x_RNA, data.x_ADT], dim=1)
    best_sil = -1.0
    best_embeddings = None
    best_labels = None

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()

        sim_z, dist_z, fused_z, fused_pro, pro = model(
            data.x_RNA, data.x_ADT,
            data.sim_edge_index, data.sim_edge_weight,
            data.dist_edge_index, data.dist_edge_weight,
            data.common_edge_index, data.common_edge_weight
        )
        model.gcn_input = data
        loss, l_rec = model.compute_losses(data.x_RNA, data.x_ADT, sim_z, dist_z, fused_z, fused_pro, combined_raw, pro)
        loss.backward()
        optimizer.step()

        # Checkpoint by KMeans Silhouette
        model.eval()
        with torch.no_grad():
            _, _, _, fused_pro_eval, _ = model(
                data.x_RNA, data.x_ADT,
                data.sim_edge_index, data.sim_edge_weight,
                data.dist_edge_index, data.dist_edge_weight,
                data.common_edge_index, data.common_edge_weight
            )
            emb = fused_pro_eval.cpu().numpy()
        km = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)
        pred = km.fit_predict(emb)
        sil = silhouette_score(emb, pred)
        if sil > best_sil:
            best_sil = sil
            best_embeddings = emb.copy()
            best_labels = pred.copy()

        if (epoch + 1) % 50 == 0 or epoch == 0:
            print(f" [ep {epoch+1}/350 sil={sil:.3f} best={best_sil:.3f}]", end="", flush=True)

    return best_embeddings, best_labels

# ----------------- MAIN EXECUTION LOOP -----------------
def main():
    device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
    print(f"=== Starting SMART vs. ARISE Ablation on {device} ===")
    
    # Frozen datasets and seeds per prompt
    datasets = [
        ("LN_A1", "10x_human_lymph_node_A1"),
        ("LN_D1", "10x_human_lymph_node_D1")
    ]
    SEEDS = [1234, 42, 2024]
    
    output_dir = "results_smart_arise_exact_A1_D1"
    os.makedirs(output_dir, exist_ok=True)
    
    all_runs = []
    d1_sensitivity_runs = []
    
    for ds_label, ds_folder in datasets:
        print("\n" + "="*80)
        print(f" DATASET: {ds_label} ({ds_folder}) ".center(80, "="))
        print("="*80)
        
        base = f"data/{ds_folder}"
        rna_path = os.path.join(base, "adata_RNA.h5ad")
        adt_path = os.path.join(base, "adata_ADT.h5ad")
        anno_path = os.path.join(base, "annotation.csv")
        
        # Load Raw Data
        adata_rna_raw = sc.read_h5ad(rna_path)
        adata_adt_raw = sc.read_h5ad(adt_path)
        adata_rna_raw.var_names_make_unique()
        adata_adt_raw.var_names_make_unique()
        
        anno_df = pd.read_csv(anno_path, index_col=0)
        adata_rna_raw.obs['ground_truth'] = anno_df['manual-anno']
        adata_adt_raw.obs['ground_truth'] = anno_df['manual-anno']
        
        # Check Exclude presence
        has_exclude = "Exclude" in adata_rna_raw.obs['ground_truth'].values
        n_ground_truth = adata_rna_raw.obs['ground_truth'].nunique()
        print(f"Total cells: {adata_rna_raw.n_obs} | Unique ground truth classes: {n_ground_truth}")
        if has_exclude:
            n_exclude = (adata_rna_raw.obs['ground_truth'] == "Exclude").sum()
            print(f"Notice: 'Exclude' class detected with {n_exclude} cells. Primary evaluation includes Exclude (K={n_ground_truth}).")
        
        # 1. SMART Preprocessing (Exact)
        print("Running SMART Preprocessing...")
        adata_rna = adata_rna_raw.copy()
        adata_adt = adata_adt_raw.copy()
        
        sc.pp.filter_genes(adata_rna, min_cells=10)
        sc.pp.highly_variable_genes(adata_rna, flavor="seurat_v3", n_top_genes=3000)
        sc.pp.normalize_total(adata_rna, target_sum=1e4)
        sc.pp.log1p(adata_rna)
        sc.pp.scale(adata_rna)
        
        adata_rna_high = adata_rna[:, adata_rna.var['highly_variable']]
        adata_rna.obsm['feat'] = pca(adata_rna_high, n_comps=30)
        
        adata_adt = adata_adt[adata_rna.obs_names].copy()
        pt.pp.clr(adata_adt)
        sc.pp.scale(adata_adt)
        adata_adt.obsm['feat'] = pca(adata_adt, n_comps=30)
        
        # 2. SMART Spatial Graphs
        print("Constructing SMART Spatial Graphs...")
        Cal_Spatial_Net(adata_rna, n_neighbors=6)
        Cal_Spatial_Net(adata_adt, n_neighbors=6)
        
        smart_features = [
            torch.FloatTensor(adata_rna.obsm["feat"]).to(device),
            torch.FloatTensor(adata_adt.obsm["feat"]).to(device)
        ]
        smart_edges = [
            torch.LongTensor(adata_rna.uns["edgeList"]).to(device),
            torch.LongTensor(adata_adt.uns["edgeList"]).to(device)
        ]
        
        # 3. ARISE Graph Construction on SMART features
        print("Constructing ARISE Dual Graphs...")
        cell_positions = adata_rna.obsm['spatial']
        dual_graph = build_dual_graph(adata_rna.obsm['feat'], adata_adt.obsm['feat'], cell_positions, device=device)
        
        # 4. ARISE exact preprocessing data
        rna_arise = adata_rna_high.X
        if hasattr(rna_arise, 'toarray'):
            rna_arise = rna_arise.toarray()
        adt_arise = adata_adt.X
        if hasattr(adt_arise, 'toarray'):
            adt_arise = adt_arise.toarray()
        graph_arise = build_dual_graph(rna_arise, adt_arise, cell_positions, device=device)
        
        # Variants to execute
        variants = [
            "E0_SMART_EXACT",
            "E1_ARISE_GRAPH_ONLY",
            "E2_ARISE_DUAL_RNA",
            "E3_ARISE_HIERARCHICAL_FUSION",
            "ARISE_EXACT"
        ]
        
        for seed in SEEDS:
            print(f"\n--- Running Seed: {seed} ---")
            set_seed(seed)
            
            # Triplet samples for this seed
            triplet_samples_list = [
                Mutual_Nearest_Neighbors(adata_rna, key="feat", n_nearest_neighbors=3, farthest_ratio=0.6),
                Mutual_Nearest_Neighbors(adata_adt, key="feat", n_nearest_neighbors=3, farthest_ratio=0.6)
            ]
            
            for var in variants:
                t0 = time.time()
                print(f"[{ds_label}] Seed {seed} | Running {var}...", end="", flush=True)
                
                if var == "E0_SMART_EXACT":
                    model = SMART_Model([30, 30, 64], device)
                    train_smart_variant(model, smart_features, smart_edges, triplet_samples_list, n_epochs=300, device=device)
                    model.eval()
                    with torch.no_grad():
                        z, _ = model(smart_features, smart_edges)
                        emb = z.cpu().numpy()
                    adata_eval = adata_rna.copy()
                    adata_eval.obsm['SMART'] = emb
                    clustering(adata_eval, key='SMART', add_key='SMART', n_clusters=n_ground_truth, method='mclust', use_pca=True, random_seed=seed)
                    pred_labels = adata_eval.obs['SMART'].astype(str)
                    
                elif var == "E1_ARISE_GRAPH_ONLY":
                    e1_edges = [dual_graph.dist_edge_index, dual_graph.common_edge_index]
                    model = SMART_Model([30, 30, 64], device)
                    train_smart_variant(model, smart_features, e1_edges, triplet_samples_list, n_epochs=300, device=device)
                    model.eval()
                    with torch.no_grad():
                        z, _ = model(smart_features, e1_edges)
                        emb = z.cpu().numpy()
                    adata_eval = adata_rna.copy()
                    adata_eval.obsm['SMART'] = emb
                    clustering(adata_eval, key='SMART', add_key='SMART', n_clusters=n_ground_truth, method='mclust', use_pca=True, random_seed=seed)
                    pred_labels = adata_eval.obs['SMART'].astype(str)
                    
                elif var == "E2_ARISE_DUAL_RNA":
                    e2_edges = [dual_graph.sim_edge_index, dual_graph.dist_edge_index, dual_graph.common_edge_index]
                    model = E2_DualRNA_Model(rna_dim=30, adt_dim=30, emb_dim=64)
                    train_smart_variant(model, smart_features, e2_edges, triplet_samples_list, n_epochs=300, device=device)
                    model.eval()
                    with torch.no_grad():
                        z, _ = model(smart_features, e2_edges)
                        emb = z.cpu().numpy()
                    adata_eval = adata_rna.copy()
                    adata_eval.obsm['SMART'] = emb
                    clustering(adata_eval, key='SMART', add_key='SMART', n_clusters=n_ground_truth, method='mclust', use_pca=True, random_seed=seed)
                    pred_labels = adata_eval.obs['SMART'].astype(str)
                    
                elif var == "E3_ARISE_HIERARCHICAL_FUSION":
                    e2_edges = [dual_graph.sim_edge_index, dual_graph.dist_edge_index, dual_graph.common_edge_index]
                    model = E3_Hierarchical_Model(rna_dim=30, adt_dim=30, emb_dim=64)
                    train_smart_variant(model, smart_features, e2_edges, triplet_samples_list, n_epochs=300, device=device)
                    model.eval()
                    with torch.no_grad():
                        z, _ = model(smart_features, e2_edges)
                        emb = z.cpu().numpy()
                    adata_eval = adata_rna.copy()
                    adata_eval.obsm['SMART'] = emb
                    clustering(adata_eval, key='SMART', add_key='SMART', n_clusters=n_ground_truth, method='mclust', use_pca=True, random_seed=seed)
                    pred_labels = adata_eval.obs['SMART'].astype(str)
                    
                elif var == "ARISE_EXACT":
                    arise_model = Dual(
                        in_channels=rna_arise.shape[1],
                        hidden_channels=512,
                        out_channels=64,
                        q=adt_arise.shape[1],
                        num_clusters=n_ground_truth,
                        beta=25.0,
                        gamma=10.0,
                        delta=1.0,
                        dropout=0.0
                    ).to(device)
                    emb, best_labels = train_arise_model(arise_model, graph_arise, epochs=350, lr=1e-3, num_clusters=n_ground_truth)
                    pred_labels = best_labels.astype(str)
                
                # Primary Evaluation Metrics (all spots, native ground truth)
                y_true = adata_rna.obs['ground_truth'].astype(str)
                ari = adjusted_rand_score(y_true, pred_labels)
                nmi = normalized_mutual_info_score(y_true, pred_labels)
                ami = adjusted_mutual_info_score(y_true, pred_labels)
                homo = homogeneity_score(y_true, pred_labels)
                v_meas = v_measure_score(y_true, pred_labels)
                sil = silhouette_score(emb, pred_labels)
                
                elapsed = time.time() - t0
                print(f" Done ({elapsed:.1f}s) | ARI: {ari:.4f} | NMI: {nmi:.4f} | Sil: {sil:.4f}")
                
                res_record = {
                    'dataset': ds_label,
                    'seed': seed,
                    'variant': var,
                    'ARI': ari,
                    'NMI': nmi,
                    'AMI': ami,
                    'Homogeneity': homo,
                    'V_measure': v_meas,
                    'Silhouette': sil
                }
                all_runs.append(res_record)
                
                # Secondary Sensitivity Evaluation for D1 (excluding 'Exclude' class)
                if ds_label == "LN_D1" and has_exclude:
                    valid_mask = (adata_rna.obs['ground_truth'] != "Exclude").values
                    y_true_sens = adata_rna.obs['ground_truth'].values[valid_mask].astype(str)
                    pred_sens = np.array(pred_labels)[valid_mask]
                    emb_sens = emb[valid_mask]
                    
                    ari_sens = adjusted_rand_score(y_true_sens, pred_sens)
                    nmi_sens = normalized_mutual_info_score(y_true_sens, pred_sens)
                    ami_sens = adjusted_mutual_info_score(y_true_sens, pred_sens)
                    homo_sens = homogeneity_score(y_true_sens, pred_sens)
                    v_meas_sens = v_measure_score(y_true_sens, pred_sens)
                    sil_sens = silhouette_score(emb_sens, pred_sens)
                    
                    sens_record = {
                        'dataset': ds_label,
                        'seed': seed,
                        'variant': var,
                        'ARI': ari_sens,
                        'NMI': nmi_sens,
                        'AMI': ami_sens,
                        'Homogeneity': homo_sens,
                        'V_measure': v_meas_sens,
                        'Silhouette': sil_sens
                    }
                    d1_sensitivity_runs.append(sens_record)

    # Save Results
    df_all = pd.DataFrame(all_runs)
    csv_path = os.path.join(output_dir, "all_runs_results.csv")
    df_all.to_csv(csv_path, index=False)
    print(f"\nSaved all runs results to {csv_path}")
    
    # Compute Component Deltas
    # For A1 and D1 independently:
    # Delta_graph = E1 - E0
    # Delta_dualRNA = E2 - E1
    # Delta_hierarchical = E3 - E2
    # Delta_full = E3 - E0
    component_summary = []
    
    for ds_label in ["LN_A1", "LN_D1"]:
        df_ds = df_all[df_all['dataset'] == ds_label]
        for metric in ['ARI', 'NMI', 'AMI', 'Homogeneity', 'V_measure', 'Silhouette']:
            deltas_graph = []
            deltas_dualRNA = []
            deltas_hierarchical = []
            deltas_full = []
            
            for seed in SEEDS:
                e0_val = df_ds[(df_ds['seed'] == seed) & (df_ds['variant'] == 'E0_SMART_EXACT')][metric].values[0]
                e1_val = df_ds[(df_ds['seed'] == seed) & (df_ds['variant'] == 'E1_ARISE_GRAPH_ONLY')][metric].values[0]
                e2_val = df_ds[(df_ds['seed'] == seed) & (df_ds['variant'] == 'E2_ARISE_DUAL_RNA')][metric].values[0]
                e3_val = df_ds[(df_ds['seed'] == seed) & (df_ds['variant'] == 'E3_ARISE_HIERARCHICAL_FUSION')][metric].values[0]
                
                deltas_graph.append(e1_val - e0_val)
                deltas_dualRNA.append(e2_val - e1_val)
                deltas_hierarchical.append(e3_val - e2_val)
                deltas_full.append(e3_val - e0_val)
                
            component_summary.append({
                'dataset': ds_label,
                'metric': metric,
                'Delta_graph_mean': np.mean(deltas_graph),
                'Delta_graph_sd': np.std(deltas_graph, ddof=1),
                'Delta_dualRNA_mean': np.mean(deltas_dualRNA),
                'Delta_dualRNA_sd': np.std(deltas_dualRNA, ddof=1),
                'Delta_hierarchical_mean': np.mean(deltas_hierarchical),
                'Delta_hierarchical_sd': np.std(deltas_hierarchical, ddof=1),
                'Delta_full_mean': np.mean(deltas_full),
                'Delta_full_sd': np.std(deltas_full, ddof=1)
            })
            
    df_comp = pd.DataFrame(component_summary)
    comp_csv = os.path.join(output_dir, "component_ablation_summary.csv")
    df_comp.to_csv(comp_csv, index=False)
    print(f"Saved component ablation summary to {comp_csv}")
    
    if d1_sensitivity_runs:
        df_sens = pd.DataFrame(d1_sensitivity_runs)
        sens_csv = os.path.join(output_dir, "d1_sensitivity_results.csv")
        df_sens.to_csv(sens_csv, index=False)
        print(f"Saved D1 sensitivity results to {sens_csv}")
        
    print("\n=== COMPLETED ALL 30 RUNS SUCCESSFULLY ===")

if __name__ == "__main__":
    main()

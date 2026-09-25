"""Engineering and reference-equivalence checks, not biological benchmarks."""

from dataclasses import replace
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np
import pandas as pd
import torch
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors, kneighbors_graph

from better_model.config import ModelConfig, PreprocessConfig
from better_model.data import align_annotations, align_modalities, preprocess
from better_model.graphs import build_graphs, spatial_adjacency, spatial_loss
from better_model.model import SpatialPottsDEC
from better_model.run import synthetic_inputs, evaluate, run_suite, smoke_config
from better_model.training import train, load_checkpoint, save_checkpoint, selection_score, make_model
from better_model.compare import compare


class AstraTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        torch.set_num_threads(1)

    def fixture(self):
        rna, aux, labels, _ = synthetic_inputs()
        prep = preprocess(rna, aux, PreprocessConfig(hvg_flavor="seurat", n_hvg=30, min_cells=1))
        cfg = ModelConfig(n_clusters=3, hidden_dim=12, latent_dim=6, n_neighbors=4,
                          pretrain_epochs=3, finetune_epochs=2, pair_block_size=16)
        graph, info = build_graphs(prep.rna, prep.aux, prep.positions, cfg)
        return prep, cfg, graph

    def test_spatial_loss_matches_reference_value_and_gradient(self):
        torch.manual_seed(5)
        x = torch.randn(9, 4, dtype=torch.float64, requires_grad=True)
        edges = torch.tensor([[0, 1, 2, 3, 4, 8], [1, 0, 3, 2, 8, 4]])
        norm = x.norm(dim=1, keepdim=True)
        cosine = (x @ x.T) / (norm @ norm.T + 1e-12)
        cosine = cosine - torch.diag_embed(torch.diag(cosine))
        adjacency = torch.zeros(9, 9, dtype=x.dtype)
        adjacency[edges[0], edges[1]] = 1
        sig = cosine.sigmoid()
        expected = -(adjacency * (sig + 1e-10).log() + (1 - adjacency) * (1 - sig + 1e-10).log()).mean() / 2
        expected_gradient = torch.autograd.grad(expected, x)[0]
        actual = spatial_loss(x, edges, block_size=3)
        actual_gradient = torch.autograd.grad(actual, x)[0]
        torch.testing.assert_close(actual, expected, rtol=1e-8, atol=1e-9)
        torch.testing.assert_close(actual_gradient, expected_gradient, rtol=1e-7, atol=1e-9)

    def test_architecture_forward_and_total_loss_match_user_reference(self):
        from typing import Optional, Tuple
        from torch import nn
        from torch.nn import functional as F
        from torch_geometric.nn import GCNConv
        reference_path = Path(__file__).parents[1] / "hello.py"
        notebook = json.loads(reference_path.read_text())
        namespace = dict(torch=torch, nn=nn, F=F, GCNConv=GCNConv, Optional=Optional, Tuple=Tuple)
        exec(compile("".join(notebook["cells"][5]["source"]), str(reference_path), "exec"), namespace)
        prepared, cfg, graph = self.fixture()
        model = make_model(prepared.rna.shape[1], prepared.aux.shape[1], cfg)
        original = namespace["ASTRA_v1_DEC_Gated"](prepared.rna.shape[1], cfg.hidden_dim,
                                                    cfg.latent_dim, prepared.aux.shape[1], cfg.n_clusters)
        original.load_state_dict(model.state_dict())
        actual, expected = model(graph), original(graph)
        for first, second in zip(actual, expected):
            torch.testing.assert_close(first, second, rtol=0, atol=0)
        actual_loss = model.compute_losses(graph, *actual[:5])[0]
        expected_loss = original.compute_losses(graph, *expected[:5])[0]
        torch.testing.assert_close(actual_loss, expected_loss, rtol=1e-6, atol=1e-6)

    def test_rna_adt_preprocessing_matches_reference(self):
        import scanpy as sc
        rna, aux, _, _ = synthetic_inputs()
        # Exercise the same successful seurat_v3 path used by the research configs.
        actual = preprocess(rna, aux, PreprocessConfig(n_hvg=30, min_cells=1))
        sc.pp.filter_genes(rna, min_cells=1)
        sc.pp.highly_variable_genes(rna, flavor="seurat_v3", n_top_genes=30)
        sc.pp.normalize_total(rna, target_sum=1e4)
        sc.pp.log1p(rna)
        sc.pp.scale(rna)
        expected_rna = rna[:, rna.var.highly_variable].X
        expected_rna = expected_rna.toarray() if sparse.issparse(expected_rna) else expected_rna
        x = aux.X.toarray()
        aux.X = np.log1p(x / (np.exp(np.log1p(x).mean(axis=1, keepdims=True)) + 1e-12))
        sc.pp.scale(aux)
        np.testing.assert_allclose(actual.rna, expected_rna, rtol=1e-5, atol=1e-6)
        np.testing.assert_allclose(actual.aux, aux.X, rtol=1e-5, atol=1e-6)

    def test_two_stage_selection_matches_original_training_loop(self):
        import contextlib
        import copy
        import io
        from typing import Optional, Tuple
        from torch import nn
        from torch.nn import functional as F
        from torch_geometric.nn import GCNConv
        from torch_geometric.data import Data
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score
        from better_model.training import set_seed
        notebook = json.loads((Path(__file__).parents[1] / "hello.py").read_text())
        namespace = dict(torch=torch, nn=nn, F=F, GCNConv=GCNConv, Optional=Optional, Tuple=Tuple,
                         np=np, copy=copy, KMeans=KMeans, silhouette_score=silhouette_score, DualGraphData=Data)
        for index in (5, 6):
            exec("".join(notebook["cells"][index]["source"]), namespace)
        prep, cfg, graph = self.fixture()
        actual = train(graph, cfg, 42)
        set_seed(42)
        model = namespace["ASTRA_v1_DEC_Gated"](prep.rna.shape[1], cfg.hidden_dim,
                                               cfg.latent_dim, prep.aux.shape[1], cfg.n_clusters)
        adjacency = spatial_adjacency(graph.dist_edge_index, len(prep.rna)).to_dense()
        with contextlib.redirect_stdout(io.StringIO()):
            expected = namespace["train_model_dec"](model, graph, adjacency, pretrain_epochs=3,
                                                       finetune_epochs=2, num_clusters=3, seed=42)
        np.testing.assert_array_equal(actual.labels, expected[1])
        np.testing.assert_allclose(actual.embedding, expected[0], rtol=1e-4, atol=1e-5)
        self.assertEqual(actual.selected["epoch"], expected[4])

    def test_sparse_target_matches_reference_and_is_probability(self):
        edges = torch.tensor([[0, 1, 1, 2], [1, 0, 2, 1]])
        adj = spatial_adjacency(edges, 4)
        q = torch.softmax(torch.randn(4, 3), dim=1)
        dec = SpatialPottsDEC(3, 5)
        actual = dec.compute_spatial_target_p(q, adj)
        w = q.square() / (q.sum(0, keepdim=True) + 1e-12)
        p = w / (w.sum(1, keepdim=True) + 1e-12)
        p = p * torch.exp(0.15 * (adj.to_dense() @ q))
        p = p / p.sum(1, keepdim=True)
        torch.testing.assert_close(actual, p)
        torch.testing.assert_close(actual.sum(1), torch.ones(4))
        torch.testing.assert_close(adj.to_dense().sum(1), torch.ones(4))

    def test_reference_graph_matches_dense_notebook_graph(self):
        rng = np.random.default_rng(17)
        x, aux, pos = rng.normal(size=(30, 10)), rng.normal(size=(30, 3)), rng.normal(size=(30, 2))
        cfg = ModelConfig(n_neighbors=5)
        actual, _ = build_graphs(x, aux, pos, cfg)
        cosine = cosine_similarity(x)
        inds = NearestNeighbors(n_neighbors=6, metric="cosine").fit(x).kneighbors(x, return_distance=False)
        a = np.zeros((len(x), len(x)), dtype=bool)
        for i in range(len(x)):
            for j in inds[i, 1:]:
                a[i, j] = a[j, i] = True
        np.testing.assert_array_equal(actual.sim_edge_index.numpy(), np.array(a.nonzero()))
        np.testing.assert_allclose(actual.sim_edge_weight.numpy(), cosine[a], atol=1e-7)
        dist = kneighbors_graph(pos, n_neighbors=5, mode="distance", include_self=False)
        dist = dist.maximum(dist.T).tocoo()
        dense = dist.toarray()
        np.testing.assert_array_equal(actual.dist_edge_index.numpy(), np.array(dense.nonzero()))
        np.testing.assert_allclose(actual.dist_edge_weight.numpy(), dense[dense > 0], rtol=1e-6)

    def test_affinity_handles_duplicates_small_n_and_nonpositive_cosine(self):
        x = np.array([[1., 0.], [-1., 0.], [0., 0.], [1., 0.]])
        pos = np.array([[0., 0.], [0., 0.], [2., 0.], [9., 0.]])
        graph, _ = build_graphs(x, x, pos, ModelConfig(n_neighbors=15, graph_weights="affinity"))
        self.assertEqual(graph.common_edge_index.shape[0], 2)
        self.assertTrue(torch.all(graph.sim_edge_weight >= 0))
        self.assertTrue(torch.all(graph.dist_edge_weight > 0))
        model = make_model(2, 2, ModelConfig(n_clusters=2, hidden_dim=4, latent_dim=2))
        self.assertTrue(torch.isfinite(model(graph)[3]).all())
        adj = spatial_adjacency(torch.empty((2, 0), dtype=torch.long), 4)
        torch.testing.assert_close(adj.to_dense(), torch.eye(4))

    def test_empty_consensus_graph_runs(self):
        cfg = ModelConfig(n_clusters=2, hidden_dim=4, latent_dim=2, n_neighbors=1, graph_weights="affinity")
        # Feature pairs (0,1), (2,3); spatial pairs (0,2), (1,3).
        x = np.array([[1., 0.], [1., 0.], [0., 1.], [0., 1.]])
        pos = np.array([[0., 0.], [10., 0.], [0., 1.], [10., 1.]])
        graph, _ = build_graphs(x, x, pos, cfg)
        self.assertEqual(tuple(graph.common_edge_index.shape), (2, 0))
        self.assertTrue(torch.isfinite(make_model(2, 2, cfg)(graph)[3]).all())

    def test_alignment_is_by_barcode_and_preserves_inputs(self):
        rna, aux, labels, _ = synthetic_inputs()
        original = rna.X.copy()
        reordered = aux[::-1].copy()
        _, aligned = align_modalities(rna, reordered)
        np.testing.assert_array_equal(aligned.X.toarray(), aux.X.toarray())
        frame = pd.DataFrame({"annotation": labels}).iloc[::-1]
        pd.testing.assert_series_equal(align_annotations(frame, rna.obs_names, "annotation"), labels.rename("annotation"))
        preprocess(rna, aux, PreprocessConfig(hvg_flavor="seurat", min_cells=1))
        self.assertEqual((rna.X != original).nnz, 0)
        self.assertNotIn("log1p", rna.uns)
        with self.assertRaises(ValueError):
            align_modalities(rna, aux[:-1])
        with self.assertRaises(ValueError):
            align_annotations(frame.iloc[1:], rna.obs_names, "annotation")

    def test_atac_preprocessing_uses_sparse_pca_with_valid_dimensions(self):
        rna, aux, _, _ = synthetic_inputs()
        result = preprocess(rna, aux, PreprocessConfig(aux_modality="ATAC", hvg_flavor="seurat", min_cells=1))
        self.assertEqual(result.aux.shape, (48, 8))
        self.assertTrue(np.isfinite(result.aux).all())
        self.assertIn("atac_pca_components", result.transforms)

    def test_partition_guards_reject_collapse_without_labels(self):
        x = np.random.default_rng(1).normal(size=(100, 3))
        y = np.array([0] * 98 + [1, 2])
        self.assertIsNone(selection_score(x, y, ModelConfig(n_clusters=3, guard_partitions=True))[0])
        self.assertIsNone(selection_score(x, np.zeros(100), ModelConfig(n_clusters=3))[0])
        self.assertIsNotNone(selection_score(x, y, ModelConfig(n_clusters=3))[0])

    def test_missing_annotations_are_not_string_classes(self):
        x = np.array([[0.], [0.1], [10.], [11.]])
        metrics = evaluate(x, np.array([0, 0, 1, 1]), pd.Series(["a", None, "b", "Exclude"]),
                           ModelConfig(n_clusters=2), ["Exclude"])
        self.assertEqual(metrics["n_annotated_evaluated"], 2)
        self.assertEqual(metrics["ari"], 1.0)

    def test_two_stage_training_repeatability_and_checkpoint_reload(self):
        prepared, cfg, graph = self.fixture()
        first = train(graph, cfg, 42)
        second = train(graph, cfg, 42)
        np.testing.assert_array_equal(first.labels, second.labels)
        np.testing.assert_allclose(first.embedding, second.embedding, rtol=0, atol=0)
        self.assertEqual(len(first.history), 5)
        self.assertEqual(first.history[-1]["stage"], 2)
        self.assertTrue(all(np.isfinite(row["total_loss"]) for row in first.history))
        self.assertLessEqual(first.bridge["epoch"], 3)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.pt"
            save_checkpoint(path, first, cfg, 42, (prepared.rna.shape[1], prepared.aux.shape[1]))
            model, payload = load_checkpoint(path)
            with torch.no_grad():
                restored = model(graph)[3].numpy()
            np.testing.assert_array_equal(restored, first.embedding)
            np.testing.assert_array_equal(payload["selected_labels"].numpy(), first.labels)

    def test_every_seed_saved_and_overwrite_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            cfg = smoke_config()
            cfg["seeds"] = [42, 1234]
            output = Path(directory) / "run"
            run_suite(cfg, ".", output, smoke=True)
            for seed in cfg["seeds"]:
                self.assertTrue((output / "SYNTHETIC_SMOKE" / f"seed_{seed}" / "model.pt").exists())
            self.assertEqual(json.loads((output / "status.json").read_text())["status"], "COMPLETED")
            paired, summary = compare(output, output)
            self.assertTrue((paired["delta_ari"] == 0).all())
            self.assertEqual(len(paired), 2)
            with self.assertRaises(FileExistsError):
                run_suite(cfg, ".", output, smoke=True)

    def test_affinity_candidate_trains_both_stages(self):
        prep, cfg, _ = self.fixture()
        cfg = replace(cfg, graph_weights="affinity", guard_partitions=True)
        graph, _ = build_graphs(prep.rna, prep.aux, prep.positions, cfg)
        result = train(graph, cfg, 42)
        self.assertEqual(result.selected["n_clusters_found"], 3)
        self.assertEqual(result.history[-1]["stage"], 2)
        self.assertTrue(np.isfinite(result.embedding).all())


if __name__ == "__main__":
    unittest.main()

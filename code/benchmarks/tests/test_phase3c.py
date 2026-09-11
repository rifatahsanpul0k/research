import csv
import json
import tempfile
import unittest
from pathlib import Path

import h5py
import numpy as np
from scipy import sparse

from code.benchmarks.common.h5ad import load_h5ad, load_labels, sha256
from code.benchmarks.common.failures import write_failure_artifacts
from code.benchmarks.common.evaluation import cluster_and_evaluate
from code.benchmarks.common.preprocessing import (
    adt_representation,
    atac_representation,
    concatenate_equal_blocks,
    coordinate_representation,
    rna_representation,
    row_diagnostics,
)
from code.benchmarks.run_phase3c import FIRST_ID, intended_ids, method_id


def write_fixture(path: Path) -> None:
    with h5py.File(path, "w") as handle:
        x = sparse.csr_matrix(np.asarray([[1, 0, 2], [0, 3, 1], [2, 1, 0]], dtype=np.float32))
        group = handle.create_group("X")
        group.attrs["encoding-type"] = "csr_matrix"
        group.attrs["shape"] = x.shape
        group.create_dataset("data", data=x.data)
        group.create_dataset("indices", data=x.indices)
        group.create_dataset("indptr", data=x.indptr)
        obs = handle.create_group("obs")
        obs.attrs["_index"] = "_index"
        obs.create_dataset("_index", data=np.asarray(["a", "b", "c"], dtype=h5py.string_dtype()))
        var = handle.create_group("var")
        var.attrs["_index"] = "_index"
        var.create_dataset("_index", data=np.asarray(["g", "g", "h"], dtype=h5py.string_dtype()))
        var.create_dataset("gene_ids", data=np.asarray(["id1", "id2", "id3"], dtype=h5py.string_dtype()))
        obsm = handle.create_group("obsm")
        obsm.create_dataset("spatial", data=np.asarray([[0, 0], [1, 0], [0, 1]], dtype=np.int64))


class Phase3CTests(unittest.TestCase):
    def test_read_only_h5ad_and_feature_identity(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "fixture.h5ad"
            write_fixture(path)
            before = sha256(path)
            view = load_h5ad(path, before)
            self.assertEqual(view.observation_ids, ["a", "b", "c"])
            self.assertEqual(view.feature_ids, ["id1", "id2", "id3"])
            self.assertEqual(sha256(path), before)

    def test_annotation_identifier_join(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "labels.csv"
            with path.open("w", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerows([["barcode", "cluster"], ["b", "B"], ["a", "A"]])
            labels, diagnostics = load_labels(path, ["a", "b"], "cluster")
            self.assertEqual(labels.tolist(), ["A", "B"])
            self.assertTrue(diagnostics["joined_by_identifier"])

    def test_preprocessing_shapes_and_finite_values(self):
        matrix = sparse.csr_matrix(np.asarray([[1, 0, 2], [0, 3, 1], [2, 1, 0], [1, 1, 1]], dtype=float))
        rna, _ = rna_representation(matrix, ["a", "b", "c"], n_features=2)
        adt, _ = adt_representation(matrix, ["a", "b", "c"])
        coordinates, _ = coordinate_representation(np.asarray([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=float))
        combined, _ = concatenate_equal_blocks(rna, adt)
        self.assertEqual(rna.shape, (4, 2))
        self.assertEqual(coordinates.shape, (4, 2))
        self.assertEqual(combined.shape, (4, 5))
        self.assertTrue(row_diagnostics(combined)["finite"])

    def test_atac_pipeline_drops_first_lsi_component(self):
        rng = np.random.default_rng(4)
        matrix = sparse.csr_matrix(rng.poisson(0.3, size=(40, 50)))
        result, metadata = atac_representation(matrix, [f"p{i}" for i in range(50)])
        self.assertEqual(result.shape, (40, 30))
        self.assertEqual(metadata["lsi"]["component_dropped"], 1)

    def test_experiment_ids_are_unique_and_mapped(self):
        planned = intended_ids()
        self.assertEqual(len(planned), 84)
        self.assertEqual(len(planned), len(set(planned)))
        self.assertIn(FIRST_ID, planned)
        self.assertEqual(method_id("PCA"), "PCA_CLASSICAL")

    def test_metric_serialization(self):
        values = np.asarray([[0, 0], [0, 1], [10, 10], [10, 11]], dtype=float)
        labels = np.asarray(["a", "a", "b", "b"])
        _, metrics, sizes = cluster_and_evaluate(values, labels, 1729)
        serialized = json.dumps(metrics, allow_nan=False)
        self.assertIn("adjusted_rand_score", serialized)
        self.assertEqual(sum(sizes.values()), 4)

    def test_failed_run_logging(self):
        with tempfile.TemporaryDirectory() as folder:
            record = write_failure_artifacts(folder, "EXP-TEST", ValueError("bad input"), "DATA_ERROR", "load", "trace\n")
            self.assertEqual(record["status"], "FAILED")
            self.assertEqual((Path(folder) / "STATUS").read_text(), "FAILED\n")
            self.assertEqual(json.loads((Path(folder) / "failure.json").read_text())["failure_category"], "DATA_ERROR")


if __name__ == "__main__":
    unittest.main()

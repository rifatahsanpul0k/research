import tempfile
import unittest
from pathlib import Path

from code.benchmarks.common.config import DatasetInput, RunConfig
from code.benchmarks.common.io import load_json, write_json_atomic
from code.benchmarks.common.provenance import REQUIRED_PROVENANCE, sha256, validate_provenance
from code.benchmarks.common.seeds import SeedPlan
from code.benchmarks.common.validation import validate_embedding, validate_row_mapping


class InfrastructureTests(unittest.TestCase):
    def test_config_and_dataset_identity(self):
        item = DatasetInput("LN_A1", "RNA", "matrix", "obs", "var", "processed")
        run = RunConfig(
            "EXP-LN-A1-PCA-0001",
            "LN_A1",
            "PCA",
            7,
            (item,),
            {},
            {},
            {},
            "08_experiments/EXP-LN-A1-PCA-0001",
            compute_classification="LOCAL_LIGHT",
        )
        self.assertEqual(run.to_dict()["dataset"], "LN_A1")
        self.assertEqual(run.to_dict()["compute_classification"], "LOCAL_LIGHT")
        with self.assertRaises(ValueError):
            RunConfig("EXP-LN-A1-PCA-0002", "LN_A1", "PCA", 7, (item,), {}, {}, {}, "08_experiments/EXP-LN-A1-PCA-0002", status="DONE").validate()

    def test_compute_classification_gate(self):
        item = DatasetInput("LN_A1", "RNA", "matrix", "obs", "var", "processed")
        with self.assertRaises(ValueError):
            RunConfig(
                "EXP-LN-A1-PCA-0003",
                "LN_A1",
                "PCA",
                7,
                (item,),
                {},
                {},
                {},
                "08_experiments/EXP-LN-A1-PCA-0003",
                compute_classification="UNRESOLVED",
                status="RUNNING",
            ).validate()

    def test_row_identity_and_embedding(self):
        validate_row_mapping(["a", "b"], ["a", "b"])
        self.assertEqual(validate_embedding([[1.0, 2.0], [3.0, 4.0]], 2), 2)
        with self.assertRaises(ValueError):
            validate_row_mapping(["a", "b"], ["b", "a"])

    def test_seed_plan(self):
        self.assertEqual(SeedPlan.uniform(11).apply_stdlib()["clustering"], 11)

    def test_json_and_checksum(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "record.json"
            write_json_atomic({"ok": True}, path)
            self.assertEqual(load_json(path), {"ok": True})
            self.assertEqual(len(sha256(path)), 64)

    def test_provenance_gate(self):
        record = {key: "recorded" for key in REQUIRED_PROVENANCE}
        record["compute_classification"] = "LOCAL_LIGHT"
        validate_provenance(record)
        record.pop("seed")
        with self.assertRaises(ValueError):
            validate_provenance(record)

    def test_unresolved_provenance_cannot_run(self):
        record = {key: "recorded" for key in REQUIRED_PROVENANCE}
        record["compute_classification"] = "UNRESOLVED"
        record["exit_status"] = "RUNNING"
        with self.assertRaises(ValueError):
            validate_provenance(record)


if __name__ == "__main__":
    unittest.main()

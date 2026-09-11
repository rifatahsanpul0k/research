import json
import os
import tempfile
import unittest
from pathlib import Path

import numpy as np

from code.benchmarks.methods.mofaplus import fit as fit_mofa
from code.benchmarks.methods.scot import validate_coupling
from code.benchmarks.phase3d_protocol import configs, validate_config
from code.benchmarks.run_phase3d import run


class Phase3DTests(unittest.TestCase):
    def test_frozen_matrix_and_ids(self):
        records = list(configs())
        self.assertEqual(len(records), 30)
        self.assertEqual(len({record["experiment_id"] for record in records}), 30)
        self.assertTrue(all(validate_config(record) == record for record in records))
        self.assertEqual({record["compute_classification"] for record in records}, {"COLAB_CPU", "COLAB_HIGH_MEMORY"})

    def test_scot_coupling_marginals(self):
        plan = np.full((4, 4), 1 / 16, dtype=float)
        result = validate_coupling(plan, 4, 4)
        self.assertEqual(result["row_marginal_max_error"], 0.0)
        self.assertEqual(result["column_marginal_max_error"], 0.0)

    def test_mofa_feature_contract(self):
        with self.assertRaises(ValueError):
            fit_mofa(
                [np.ones((3, 2)), np.ones((3, 2))],
                ["c1", "c2", "c3"],
                [["g1"], ["p1", "p2"]],
                {"second_modality": "ADT"},
                Path(tempfile.mkdtemp()),
            )

    def test_runner_requires_verified_colab(self):
        config_path = Path("07_models/02_classical_integration/configs/EXP-LN-A1-MOFAPLUS-KMEANS-S1729.json")
        prior = os.environ.pop("ASTRA_COLAB_CONFIRMED", None)
        try:
            with self.assertRaises(RuntimeError):
                run(config_path)
        finally:
            if prior is not None:
                os.environ["ASTRA_COLAB_CONFIRMED"] = prior


if __name__ == "__main__":
    unittest.main()

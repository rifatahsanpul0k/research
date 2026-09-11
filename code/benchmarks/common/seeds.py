"""Seed plans that do not import optional scientific frameworks."""

from __future__ import annotations

import os
import random
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class SeedPlan:
    python: int
    numpy: int
    pytorch: int
    cuda: int
    r: int
    method: int
    clustering: int

    @classmethod
    def uniform(cls, seed: int) -> "SeedPlan":
        return cls(seed, seed, seed, seed, seed, seed, seed)

    def apply_stdlib(self) -> dict[str, int]:
        random.seed(self.python)
        os.environ["PYTHONHASHSEED"] = str(self.python)
        return asdict(self)

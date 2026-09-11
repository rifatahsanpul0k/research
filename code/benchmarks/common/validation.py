"""Validation helpers for IDs, embeddings and immutable inputs."""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence


def validate_unique_ids(ids: Sequence[str], label: str) -> None:
    if not ids:
        raise ValueError(f"{label} IDs are empty")
    if any(not value for value in ids):
        raise ValueError(f"{label} IDs contain an empty value")
    if len(ids) != len(set(ids)):
        raise ValueError(f"{label} IDs are not unique")


def validate_row_mapping(input_ids: Sequence[str], output_ids: Sequence[str]) -> None:
    validate_unique_ids(input_ids, "input observation")
    validate_unique_ids(output_ids, "output observation")
    if list(input_ids) != list(output_ids):
        raise ValueError("output row order does not match input observation IDs")


def validate_embedding(rows: Iterable[Sequence[float]], expected_rows: int) -> int:
    materialized = [list(row) for row in rows]
    if len(materialized) != expected_rows:
        raise ValueError("embedding row count does not match observations")
    widths = {len(row) for row in materialized}
    if len(widths) != 1 or not widths or next(iter(widths)) == 0:
        raise ValueError("embedding must be a nonempty rectangular matrix")
    if any(not math.isfinite(value) for row in materialized for value in row):
        raise ValueError("embedding contains non-finite values")
    return next(iter(widths))

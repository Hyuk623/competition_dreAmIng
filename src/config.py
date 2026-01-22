from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ExperimentConfig:
    seed: int
    input_dir: Path
    output_dir: Path
    train_file: str
    test_file: str
    id_col: str
    target_col: str
    model: str
    notes: str | None = None


def _normalize_path(value: str | Path) -> Path:
    path = Path(value)
    return path


def load_config(path: str | Path) -> ExperimentConfig:
    with open(path, "r", encoding="utf-8") as handle:
        raw: dict[str, Any] = yaml.safe_load(handle) or {}

    return ExperimentConfig(
        seed=int(raw.get("seed", 42)),
        input_dir=_normalize_path(raw.get("input_dir", "data")),
        output_dir=_normalize_path(raw.get("output_dir", "outputs")),
        train_file=str(raw.get("train_file", "train.csv")),
        test_file=str(raw.get("test_file", "test.csv")),
        id_col=str(raw.get("id_col", "id")),
        target_col=str(raw.get("target_col", "target")),
        model=str(raw.get("model", "logistic_regression")),
        notes=raw.get("notes"),
    )

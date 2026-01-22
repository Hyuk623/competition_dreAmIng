from __future__ import annotations

from pathlib import Path

import pandas as pd


def resolve_path(base_dir: Path, filename: str) -> Path:
    return base_dir / filename


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

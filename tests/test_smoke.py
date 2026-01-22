from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd
import yaml


def test_train_infer_smoke(tmp_path: Path) -> None:
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    train_df = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "feature": [0.1, 0.2, 0.3, 0.4],
            "target": [0, 1, 0, 1],
        }
    )
    test_df = pd.DataFrame(
        {
            "id": [5, 6],
            "feature": [0.5, 0.6],
        }
    )

    train_path = data_dir / "train.csv"
    test_path = data_dir / "test.csv"
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    config_path = tmp_path / "exp_001.yaml"
    output_dir = tmp_path / "outputs"
    config = {
        "seed": 7,
        "input_dir": str(data_dir),
        "output_dir": str(output_dir),
        "train_file": "train.csv",
        "test_file": "test.csv",
        "id_col": "id",
        "target_col": "target",
        "model": "logistic_regression",
        "notes": "smoke test",
    }
    config_path.write_text(yaml.safe_dump(config), encoding="utf-8")

    subprocess.check_call(
        [
            sys.executable,
            "scripts/train.py",
            "--config",
            str(config_path),
        ]
    )

    submission_path = tmp_path / "submission.csv"
    subprocess.check_call(
        [
            sys.executable,
            "scripts/infer.py",
            "--config",
            str(config_path),
            "--out",
            str(submission_path),
        ]
    )

    assert submission_path.exists()
    submission = pd.read_csv(submission_path)
    assert list(submission.columns) == ["id", "prediction"]

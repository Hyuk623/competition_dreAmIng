from __future__ import annotations

import argparse
import pickle
from pathlib import Path

import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.config import load_config
from src.io import save_csv
from src.pipeline import load_data, predict, preprocess


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run inference and create submission.csv")
    parser.add_argument("--config", required=True, help="Path to experiment config YAML")
    parser.add_argument("--out", required=True, help="Output path for submission.csv")
    return parser.parse_args()


def resolve_output_path(out_arg: str) -> Path:
    out_path = Path(out_arg)
    if out_path.suffix.lower() == ".csv":
        return out_path
    return out_path / "submission.csv"


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    output_path = resolve_output_path(args.out)

    model_path = config.output_dir / "model.pkl"
    with open(model_path, "rb") as handle:
        model = pickle.load(handle)

    bundle = load_data(config)
    _, _, test_x = preprocess(bundle.train, bundle.test, config)
    preds = predict(model, test_x)

    submission = pd.DataFrame(
        {config.id_col: bundle.test[config.id_col], "prediction": preds}
    )
    save_csv(submission, output_path)
    print(f"Saved submission to {output_path}")


if __name__ == "__main__":
    main()

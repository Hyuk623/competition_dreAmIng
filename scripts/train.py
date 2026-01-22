from __future__ import annotations

import argparse
import json
import pickle

from src.config import load_config
from src.pipeline import run_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train baseline model")
    parser.add_argument("--config", required=True, help="Path to experiment config YAML")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)

    model, _, _ = run_pipeline(config)

    output_dir = config.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    model_path = output_dir / "model.pkl"
    meta_path = output_dir / "meta.json"

    with open(model_path, "wb") as handle:
        pickle.dump(model, handle)

    with open(meta_path, "w", encoding="utf-8") as handle:
        json.dump({"model": config.model, "notes": config.notes}, handle, indent=2)

    print(f"Saved model to {model_path}")


if __name__ == "__main__":
    main()

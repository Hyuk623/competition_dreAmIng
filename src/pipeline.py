from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from src.config import ExperimentConfig
from src.io import load_csv, resolve_path


@dataclass
class DatasetBundle:
    train: pd.DataFrame
    test: pd.DataFrame


def load_data(config: ExperimentConfig) -> DatasetBundle:
    train_path = resolve_path(config.input_dir, config.train_file)
    test_path = resolve_path(config.input_dir, config.test_file)
    train_df = load_csv(train_path)
    test_df = load_csv(test_path)
    return DatasetBundle(train=train_df, test=test_df)


def preprocess(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    config: ExperimentConfig,
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    train_y = train_df[config.target_col]
    train_x = train_df.drop(columns=[config.target_col])

    combined = pd.concat([train_x, test_df], axis=0, ignore_index=True)
    combined = pd.get_dummies(combined)
    combined = combined.fillna(0)

    train_x_processed = combined.iloc[: len(train_x), :].copy()
    test_x_processed = combined.iloc[len(train_x) :, :].copy()

    return train_x_processed, train_y, test_x_processed


def train_model(train_x: pd.DataFrame, train_y: pd.Series, seed: int) -> LogisticRegression:
    model = LogisticRegression(max_iter=200, random_state=seed)
    model.fit(train_x, train_y)
    return model


def predict(model: LogisticRegression, test_x: pd.DataFrame) -> np.ndarray:
    if hasattr(model, "predict_proba"):
        return model.predict_proba(test_x)[:, 1]
    return model.predict(test_x)


def run_pipeline(config: ExperimentConfig) -> Tuple[LogisticRegression, pd.DataFrame, np.ndarray]:
    bundle = load_data(config)
    train_x, train_y, test_x = preprocess(bundle.train, bundle.test, config)
    model = train_model(train_x, train_y, config.seed)
    predictions = predict(model, test_x)
    return model, bundle.test, predictions

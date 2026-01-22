# Kaggle Competition Team Repo (Single Source of Truth)

This repository is the **single source of truth** for code, configs, and documentation. Kaggle notebooks are only a runtime for execution and submission artifacts.

## Workflow
- **GitHub**: store code/configs/docs, run CI, enforce policy checks.
- **Kaggle**: run `scripts/train.py` or `scripts/infer.py` using configs from `configs/`.

## Quickstart
```bash
pip install -r requirements.txt -r requirements-dev.txt
```

### Train
```bash
python scripts/train.py --config configs/exp_001.yaml
```

### Infer
```bash
python scripts/infer.py --config configs/exp_001.yaml --out /tmp/submission.csv
```

## Rules (Summary)
- Merge targets live in `src/`, `scripts/`, `configs/`, and docs. Notebooks are for exploration only.
- `scripts/train.py` and `scripts/infer.py` are the **only** entrypoints.
- Experiments must be defined in `configs/exp_XXX.yaml` (no hardcoding).
- `infer.py` **must** write `submission.csv` to the `--out` path.
- Large artifacts (`data/`, `models/`, `outputs/`, `runs/`, model binaries) are **not** committed.
- No external network calls in code.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details and [SETUP_GITHUB.md](SETUP_GITHUB.md) for required GitHub settings.

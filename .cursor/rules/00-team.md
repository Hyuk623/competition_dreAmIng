# Team Rules

- GitHub is the source of truth; Kaggle is runtime only.
- Merge targets are `src/`, `scripts/`, `configs/`, and docs.
- Only entrypoints: `scripts/train.py` and `scripts/infer.py`.
- Experiments belong in `configs/exp_XXX.yaml`.
- `infer.py` must write `submission.csv` to the `--out` path.
- No external network calls.
- Do not commit artifacts: `data/`, `models/`, `outputs/`, `runs/`, model binaries, or `submission.csv`.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

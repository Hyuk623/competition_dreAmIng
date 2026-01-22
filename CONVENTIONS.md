# Team Conventions

- GitHub is the single source of truth; Kaggle is a runtime only.
- Merge targets are `src/`, `scripts/`, `configs/`, and docs. Notebooks are exploratory.
- Only entrypoints: `scripts/train.py` and `scripts/infer.py`.
- Experiments are defined only in `configs/exp_XXX.yaml`.
- `infer.py` must write `submission.csv` to the `--out` path.
- No external network calls in code.
- Do not commit artifacts: `data/`, `models/`, `outputs/`, `runs/`, model binaries, or `submission.csv`.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

# Team Rules (Agents)

These rules apply to the entire repository.

## Core Principles
- **GitHub is the source of truth**; Kaggle is a runtime only.
- Only merge code/configs/docs in `src/`, `scripts/`, `configs/`, and documentation.
- **Only two entrypoints**: `scripts/train.py` and `scripts/infer.py`.
- All experiment parameters must live in `configs/exp_XXX.yaml`.
- `infer.py` must write `submission.csv` to the `--out` path.
- **No external network calls** (HTTP requests, downloads, etc.).
- Do not commit artifacts: `data/`, `models/`, `outputs/`, `runs/`, or model binaries.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

These rules must be enforced by CI/policy checks and followed by all tools/agents.

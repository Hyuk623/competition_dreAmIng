# Contributing

## Branch Naming
Use `feature/<topic>`, `fix/<topic>`, or `chore/<topic>`.

## Pull Request Requirements
- PR body **must** include sections:
  - `## Goal`
  - `## Changes`
  - `## Result`
  - `## Reproduce`
- Only entrypoints are `scripts/train.py` and `scripts/infer.py`.
- Add experiment parameters only via `configs/exp_XXX.yaml`.
- Do not commit artifacts in `data/`, `models/`, `outputs/`, `runs/`, or model binaries.
- No external network calls.

## Merge Criteria
- Required checks pass: `ci`, `pr_policy`, `codex_review`.
- P0 policy violations are **not** allowed (merge blocked).
- Optional: at least one human approval (configurable by repo admins).

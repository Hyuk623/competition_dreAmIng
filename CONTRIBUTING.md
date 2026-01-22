# Contributing / 기여 가이드

## Branch Naming / 브랜치 네이밍
`feature/<topic>`, `fix/<topic>`, `chore/<topic>` 형식을 사용합니다.

Use `feature/<topic>`, `fix/<topic>`, or `chore/<topic>`.

## Pull Request Requirements / PR 필수 요건
- PR 본문에 반드시 다음 섹션이 포함되어야 합니다:
  - `## Goal`
  - `## Changes`
  - `## Result`
  - `## Reproduce`
- 엔트리포인트는 `scripts/train.py`와 `scripts/infer.py`만 허용됩니다.
- 실험 파라미터는 `configs/exp_XXX.yaml`로만 추가합니다.
- `data/`, `models/`, `outputs/`, `runs/` 및 모델 바이너리 파일은 커밋 금지입니다.
- 외부 네트워크 호출은 금지됩니다.

- PR body **must** include sections:
  - `## Goal`
  - `## Changes`
  - `## Result`
  - `## Reproduce`
- Only entrypoints are `scripts/train.py` and `scripts/infer.py`.
- Add experiment parameters only via `configs/exp_XXX.yaml`.
- Do not commit artifacts in `data/`, `models/`, `outputs/`, `runs/`, or model binaries.
- No external network calls.

## Merge Criteria / 머지 기준
- 필수 체크(`ci`, `pr_policy`, `codex_review`)가 통과되어야 합니다.
- P0 정책 위반은 **허용되지 않습니다**.
- (선택) 최소 1명의 리뷰 승인이 필요하도록 설정할 수 있습니다.

- Required checks pass: `ci`, `pr_policy`, `codex_review`.
- P0 policy violations are **not** allowed (merge blocked).
- Optional: at least one human approval (configurable by repo admins).

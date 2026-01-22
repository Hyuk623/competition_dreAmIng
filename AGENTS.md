# Team Rules (Agents) / 팀 규칙 (에이전트)

이 규칙은 전체 레포지토리에 적용됩니다.

These rules apply to the entire repository.

## Core Principles / 핵심 원칙
- **GitHub는 단일 원본**이며, Kaggle은 실행 런타임입니다.
- 머지 대상은 `src/`, `scripts/`, `configs/`, 문서입니다.
- **엔트리포인트는 두 개**: `scripts/train.py`, `scripts/infer.py`.
- 실험 파라미터는 `configs/exp_XXX.yaml`에만 둡니다.
- `infer.py`는 `--out` 경로에 `submission.csv`를 생성해야 합니다.
- **외부 네트워크 호출 금지** (HTTP 요청/다운로드 등).
- `data/`, `models/`, `outputs/`, `runs/`, 모델 바이너리 커밋 금지.
- PR 본문에 **Goal / Changes / Result / Reproduce** 섹션이 필수입니다.

- **GitHub is the source of truth**; Kaggle is a runtime only.
- Only merge code/configs/docs in `src/`, `scripts/`, `configs/`, and documentation.
- **Only two entrypoints**: `scripts/train.py` and `scripts/infer.py`.
- All experiment parameters must live in `configs/exp_XXX.yaml`.
- `infer.py` must write `submission.csv` to the `--out` path.
- **No external network calls** (HTTP requests, downloads, etc.).
- Do not commit artifacts: `data/`, `models/`, `outputs/`, `runs/`, or model binaries.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

These rules must be enforced by CI/policy checks and followed by all tools/agents.

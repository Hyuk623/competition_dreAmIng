# Team Rules / 팀 규칙

- GitHub는 단일 원본 저장소이며, Kaggle은 런타임입니다.
- 머지 대상은 `src/`, `scripts/`, `configs/`, 문서입니다.
- 엔트리포인트는 `scripts/train.py`와 `scripts/infer.py`만 허용됩니다.
- 실험은 `configs/exp_XXX.yaml`에만 정의합니다.
- `infer.py`는 `--out` 경로에 `submission.csv`를 생성해야 합니다.
- 외부 네트워크 호출 금지.
- `data/`, `models/`, `outputs/`, `runs/`, 모델 바이너리 및 `submission.csv` 커밋 금지.
- PR 본문에 **Goal / Changes / Result / Reproduce** 섹션 필수.

- GitHub is the source of truth; Kaggle is runtime only.
- Merge targets are `src/`, `scripts/`, `configs/`, and docs.
- Only entrypoints: `scripts/train.py` and `scripts/infer.py`.
- Experiments belong in `configs/exp_XXX.yaml`.
- `infer.py` must write `submission.csv` to the `--out` path.
- No external network calls.
- Do not commit artifacts: `data/`, `models/`, `outputs/`, `runs/`, model binaries, or `submission.csv`.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

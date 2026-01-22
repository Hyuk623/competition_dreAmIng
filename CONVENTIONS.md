# Team Conventions / 팀 규칙

- GitHub는 단일 원본 저장소이며, Kaggle은 실행 런타임입니다.
- 머지 대상은 `src/`, `scripts/`, `configs/`, 문서이며 노트북은 탐색용입니다.
- 엔트리포인트는 `scripts/train.py`와 `scripts/infer.py`만 허용됩니다.
- 실험은 `configs/exp_XXX.yaml`로만 정의합니다.
- `infer.py`는 `--out` 경로에 `submission.csv`를 반드시 생성해야 합니다.
- 외부 네트워크 호출은 금지됩니다.
- `data/`, `models/`, `outputs/`, `runs/`, 모델 바이너리 및 `submission.csv` 커밋 금지.
- PR 본문에 **Goal / Changes / Result / Reproduce** 섹션이 필수입니다.

- GitHub is the single source of truth; Kaggle is a runtime only.
- Merge targets are `src/`, `scripts/`, `configs/`, and docs. Notebooks are exploratory.
- Only entrypoints: `scripts/train.py` and `scripts/infer.py`.
- Experiments are defined only in `configs/exp_XXX.yaml`.
- `infer.py` must write `submission.csv` to the `--out` path.
- No external network calls in code.
- Do not commit artifacts: `data/`, `models/`, `outputs/`, `runs/`, model binaries, or `submission.csv`.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

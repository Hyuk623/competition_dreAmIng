# Kaggle Competition Team Repo (Single Source of Truth)

이 레포지토리는 코드/설정/문서의 **단일 원본 저장소**입니다. Kaggle 노트북은 실행 및 제출 산출물 생성을 위한 **런타임**으로만 사용합니다.

This repository is the **single source of truth** for code, configs, and documentation. Kaggle notebooks are only a runtime for execution and submission artifacts.

## Workflow / 워크플로우
- **GitHub**: 코드/설정/문서를 저장하고, CI와 정책 체크를 실행합니다.
- **Kaggle**: `configs/`의 설정을 사용해 `scripts/train.py` 또는 `scripts/infer.py`를 실행합니다.

- **GitHub**: store code/configs/docs, run CI, enforce policy checks.
- **Kaggle**: run `scripts/train.py` or `scripts/infer.py` using configs from `configs/`.

## Quickstart / 빠른 시작
```bash
pip install -r requirements.txt -r requirements-dev.txt
```

### Train / 학습
```bash
python scripts/train.py --config configs/exp_001.yaml
```

### Infer / 추론
```bash
python scripts/infer.py --config configs/exp_001.yaml --out /tmp/submission.csv
```

## Rules (Summary) / 규칙 요약
- 머지 대상은 `src/`, `scripts/`, `configs/`, 문서이며, 노트북은 탐색 용도입니다.
- `scripts/train.py`와 `scripts/infer.py`만 **엔트리포인트**로 허용됩니다.
- 실험 파라미터는 `configs/exp_XXX.yaml`로만 관리합니다(하드코딩 금지).
- `infer.py`는 반드시 `--out` 경로에 `submission.csv`를 생성해야 합니다.
- `data/`, `models/`, `outputs/`, `runs/` 등 아티팩트/대용량 파일은 커밋 금지입니다.
- 외부 네트워크 호출(HTTP 등)은 금지됩니다.
- PR 본문에는 **Goal / Changes / Result / Reproduce** 섹션이 필수입니다.

- Merge targets live in `src/`, `scripts/`, `configs/`, and docs. Notebooks are for exploration only.
- `scripts/train.py` and `scripts/infer.py` are the **only** entrypoints.
- Experiments must be defined in `configs/exp_XXX.yaml` (no hardcoding).
- `infer.py` **must** write `submission.csv` to the `--out` path.
- Large artifacts (`data/`, `models/`, `outputs/`, `runs/`, model binaries) are **not** committed.
- No external network calls in code.
- PR body must include **Goal / Changes / Result / Reproduce** sections.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details and [SETUP_GITHUB.md](SETUP_GITHUB.md) for required GitHub settings.
자세한 내용은 [CONTRIBUTING.md](CONTRIBUTING.md)와 [SETUP_GITHUB.md](SETUP_GITHUB.md)를 참고하세요.

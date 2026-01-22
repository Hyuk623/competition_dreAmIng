from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_PR_HEADERS = ["## Goal", "## Changes", "## Result", "## Reproduce"]
ALLOWED_SCRIPT_FILES = {"train.py", "infer.py", "check_policy.py"}
FORBIDDEN_DIRS = ("data/", "models/", "outputs/", "runs/")
FORBIDDEN_EXTENSIONS = {
    ".pth",
    ".pt",
    ".ckpt",
    ".onnx",
    ".pkl",
    ".joblib",
}
FORBIDDEN_FILENAMES = {"submission.csv"}


def load_event_payload() -> dict:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        return {}
    with open(event_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_pr_body(event: dict) -> str:
    return (event.get("pull_request", {}) or {}).get("body", "") or ""


def get_base_head(event: dict) -> tuple[str, str]:
    pr = event.get("pull_request", {}) or {}
    base_sha = (pr.get("base", {}) or {}).get("sha")
    head_sha = (pr.get("head", {}) or {}).get("sha")
    if base_sha and head_sha:
        return base_sha, head_sha

    base_env = os.environ.get("BASE_SHA")
    head_env = os.environ.get("HEAD_SHA")
    if base_env and head_env:
        return base_env, head_env

    return "HEAD~1", "HEAD"


def git_diff_names(base_sha: str, head_sha: str) -> list[str]:
    result = subprocess.check_output(
        ["git", "diff", "--name-only", base_sha, head_sha], text=True
    )
    return [line.strip() for line in result.splitlines() if line.strip()]


def has_required_pr_sections(body: str) -> bool:
    return all(section in body for section in REQUIRED_PR_HEADERS)


def is_forbidden_path(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if normalized.startswith(FORBIDDEN_DIRS):
        return True
    if Path(normalized).name in FORBIDDEN_FILENAMES:
        return True
    if Path(normalized).suffix in FORBIDDEN_EXTENSIONS:
        return True
    return False


def changed_disallowed_scripts(files: Iterable[str]) -> list[str]:
    invalid = []
    for path in files:
        if path.startswith("scripts/") and path.endswith(".py"):
            name = Path(path).name
            if name not in ALLOWED_SCRIPT_FILES:
                invalid.append(path)
    return invalid


def notebook_violation(path: Path) -> str | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "notebook is not valid JSON"

    cells = payload.get("cells", [])
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    code_lines = 0
    code_text = []
    for cell in code_cells:
        source = cell.get("source", [])
        if isinstance(source, str):
            source = [source]
        code_lines += sum(1 for line in source if line.strip())
        code_text.extend(source)

    if len(code_cells) > 20 or code_lines > 200:
        return "notebook contains too much code for core logic"

    joined = "\n".join(code_text)
    if re.search(r"\.fit\(|\.predict\(|xgboost|lightgbm|torch", joined, re.IGNORECASE):
        if "import src" not in joined and "from src" not in joined:
            return "notebook appears to implement training/inference logic"

    return None


def check_notebooks(files: Iterable[str]) -> list[str]:
    violations = []
    for path in files:
        if path.startswith("notebooks/") and path.endswith(".ipynb"):
            reason = notebook_violation(Path(path))
            if reason:
                violations.append(f"{path}: {reason}")
    return violations


def check_p1_warnings(files: Iterable[str], pr_body: str) -> list[str]:
    warnings = []
    configs_changed = any(
        path.startswith("configs/") and Path(path).name.startswith("exp_")
        for path in files
    )
    src_or_scripts_changed = any(
        path.startswith("src/") or path.startswith("scripts/") for path in files
    )
    if src_or_scripts_changed and not configs_changed:
        warnings.append(
            "Experiment changes detected without new configs/exp_XXX.yaml updates."
        )

    requirements_changed = any(
        path in {"requirements.txt", "requirements-dev.txt"} for path in files
    )
    if requirements_changed and "Requirement" not in pr_body and "Dependency" not in pr_body:
        warnings.append("Dependency changes detected without rationale in PR body.")

    return warnings


def main() -> int:
    event = load_event_payload()
    pr_body = get_pr_body(event)
    base_sha, head_sha = get_base_head(event)

    files = git_diff_names(base_sha, head_sha)

    p0_errors = []
    if not has_required_pr_sections(pr_body):
        p0_errors.append("PR body missing required sections: Goal/Changes/Result/Reproduce")

    forbidden = [path for path in files if is_forbidden_path(path)]
    if forbidden:
        p0_errors.append(f"Forbidden files detected: {', '.join(forbidden)}")

    disallowed_scripts = changed_disallowed_scripts(files)
    if disallowed_scripts:
        p0_errors.append(
            "Disallowed script entrypoints: " + ", ".join(disallowed_scripts)
        )

    notebook_violations = check_notebooks(files)
    if notebook_violations:
        p0_errors.append("Notebook violations: " + "; ".join(notebook_violations))

    for warning in check_p1_warnings(files, pr_body):
        print(f"P1 warning: {warning}")

    if p0_errors:
        for error in p0_errors:
            print(f"P0 violation: {error}")
        return 1

    print("Policy check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

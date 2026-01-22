# GitHub Setup (One-Time) / GitHub 설정 (1회)

## Branch Protection / Ruleset / 브랜치 보호 설정
`main` 보호 규칙에 다음을 설정하세요:
- 필수 상태 체크: **ci**, **pr_policy**, **codex_review**
- 머지 전 최신 상태 유지
- (선택) 최소 1명 승인
- (선택) 자동 머지 활성화

Configure `main` protection with:
- Required status checks: **ci**, **pr_policy**, **codex_review**
- Require branches to be up to date before merging
- (Optional) Require 1 approval
- (Optional) Enable auto-merge

## Secrets / 시크릿 설정
Codex 리뷰를 위해 `OPENAI_API_KEY`를 추가합니다:
1. Repo Settings → Secrets and variables → Actions
2. New repository secret
3. Name: `OPENAI_API_KEY`

Add `OPENAI_API_KEY` for Codex review:
1. Repo Settings → Secrets and variables → Actions
2. New repository secret
3. Name: `OPENAI_API_KEY`

## Optional: Claude Code / 옵션: Claude Code
원한다면 Claude Code 리뷰어를 추가할 수 있습니다:
- `anthropics/claude-code-action` 워크플로우
이는 **선택 사항**이며 기존 필수 체크를 대체하지 않습니다.

If you want an optional Claude Code reviewer, you can add:
- `anthropics/claude-code-action` workflow
This is **optional** and should not replace existing required checks.

# GitHub Setup (One-Time)

## Branch Protection / Ruleset
Configure `main` protection with:
- Required status checks: **ci**, **pr_policy**, **codex_review**
- Require branches to be up to date before merging
- (Optional) Require 1 approval
- (Optional) Enable auto-merge

## Secrets
Add `OPENAI_API_KEY` for Codex review:
1. Repo Settings → Secrets and variables → Actions
2. New repository secret
3. Name: `OPENAI_API_KEY`

## Optional: Claude Code
If you want an optional Claude Code reviewer, you can add:
- `anthropics/claude-code-action` workflow
This is **optional** and should not replace existing required checks.

# Source: fcakyon/claude-codex-settings

- Repository: https://github.com/fcakyon/claude-codex-settings
- Upstream path(s): `plugins/github-dev/hooks/`, `plugins/intelligent-compact/hooks/`
- Commit pinned at import: `bad8cb6eaf47c4fadc4128221dd45ac40530fe9b` (branch `main`)
- License: Apache-2.0
- Files here: 7

`github-dev/` — five guardrails on git and GitHub actions, all of them refusals rather
than actions: strip AI attribution from commit messages, require a conventional commit
type, confirm before `git commit` and before `gh pr create`, and require before/after
visual proof on UI pull requests. Shared because the upstream plugin publishes seven
skills and the hooks apply across all of them.

`intelligent-compact/` — a `PreCompact` hook whose stdout becomes the "Additional
Instructions" block appended to the compaction prompt. It raises fidelity on the parts
the default summary under-specifies: unanswered user questions, confirmed root causes
versus ruled-out hypotheses, exact numbers and identifiers, file-path importance tiers,
subagent reports as primary evidence, and A-vs-B decisions. It prints a heredoc and
nothing else — no network, no writes. The upstream plugin ships no skills at all, so
this is shared by definition.

Two other hook sets from the same repository were reviewed and **not** imported:
`claude-telemetry-hooks/` forwards prompt text and hostname to an OTLP endpoint, and
`claude-tools/` pulls the author's personal `CLAUDE.md` and `settings.json` (the tool
allowlist) from GitHub into `~/.claude/`.

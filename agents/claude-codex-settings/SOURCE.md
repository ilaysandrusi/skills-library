# Source: fcakyon/claude-codex-settings

- Repository: https://github.com/fcakyon/claude-codex-settings
- Upstream path(s): `plugins/github-dev/agents/`
- Commit pinned at import: `bad8cb6eaf47c4fadc4128221dd45ac40530fe9b` (branch `main`)
- License: Apache-2.0
- Files here: 4

Sub-agents for the git/GitHub workflow plugin: `commit-creator`, `pr-creator`,
`pr-reviewer` and `pr-comment-resolver`. They stay shared because the upstream plugin
publishes seven skills and the agents are dispatched from several of them.

Four of those seven skills were imported into `05-development/` (`clean-gone-branches`,
`commit-staged`, `resolve-pr-comments`, `update-pr-summary`); the library already had
`create-pr` and `review-pr` from another source.

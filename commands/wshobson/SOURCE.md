# Source: wshobson/agents

- Repository: https://github.com/wshobson/agents
- Upstream path(s): `plugins/*/commands/`
- Commit pinned at import: `d6837ae274c2cd817acad3fb98f193a4390a4c3e` (branch `main`)
- License: MIT
- Files here: 97

Slash commands from the same plugin marketplace as `agents/wshobson/`. Substantial
prompts rather than one-liners: the TDD cycle (`tdd-red`, `tdd-green`, `tdd-refactor`,
`tdd-cycle`), review and quality (`full-review`, `multi-agent-review`, `design-review`,
`code-explain`, `tech-debt`, `refactor-clean`), security (`security-sast`,
`security-hardening`, `security-dependencies`, `xss-scan`, `compliance-check`),
delivery (`workflow-automate`, `deps-upgrade`, `sql-migrations`, `slo-implement`,
`monitor-setup`, `cost-optimize`), scaffolding (`python-scaffold`,
`typescript-scaffold`, `component-scaffold`, `rust-project`, `api-mock`), and the
`team-*` multi-agent coordination set.

De-duplicated the same way as the agents: identical files shipped in several plugins are
stored once under the bare command name, and a differing same-named command keeps its
plugin prefix. Commands whose bare name carries no meaning outside their workflow were
prefixed (`conductor-*`, `plugin-eval-*`, `ship-mate-*`, `meigen-*`, `team-issue`).

Not imported: the `quantitative-trading` and `hr-legal-compliance` plugins (out of
scope), and `protect-mcp` / `review-agent-governance`, whose hooks run
`npx protect-mcp@0.7.4` on every tool call.

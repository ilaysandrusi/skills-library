# Source: tobihagemann/turbo

- Repository: https://github.com/tobihagemann/turbo
- Upstream path(s): `claude/` (edition root, excluding `claude/skills/`)
- Commit pinned at import: `d0f862f` (branch `main`)
- License: MIT
- Files here: 10

turbo is one composable dev process split into 74 interlinked skills, archived under
[`05-development/`](../../05-development/) — the un-prefixed slugs (`finalize`, `draft-plan`,
`polish-code`, `ship`, …) plus nine `turbo-*` ones that had to be renamed around existing
names. These files sit at the edition root upstream and are shared by all 74, so they
cannot be assigned to any single skill:

| File | What it is |
|---|---|
| `AGENTS.md`, `CLAUDE.md` | always-on rules for an agent working inside the pack |
| `SKILL-CONVENTIONS.md` | the authoring contract every turbo skill follows |
| `SKILL-INDEX.md` | the pack's own map of which skill to reach for when |
| `SETUP.md` | how to install the pack into `~/.claude/skills/` |
| `UPDATE.md` | how to pull a newer turbo into an existing install |
| `MIGRATION.md`, `ADDITIONS.md` | moving off older layouts, and adding local skills |
| `docs/harness-vocabulary.md` | Claude Code ↔ Codex tool-name mapping |
| `docs/skill-loading-reasoning.md` | why the pack is split the way it is |

`SETUP.md` and `UPDATE.md` are the reason these are archived rather than dropped: without
them the 74 skills are readable but not installable or upgradable.

## Not imported

Upstream ships a parallel `codex/` edition — the same 74 skills and the same eight root
documents, reworded for the Codex harness. Storing both would double the pack for a
vocabulary difference, so only the `claude/` edition is here.
`docs/harness-vocabulary.md` above is the translation table if you need the other one.

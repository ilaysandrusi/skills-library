# Source

- Repository: `tobihagemann/turbo`
- URL: https://github.com/tobihagemann/turbo
- Imported commit: `d0f862f`
- Upstream path: `claude/skills/review-code`
- Local skill path: `05-development/review-code`
- License: MIT
- Discovered: 2026-08-20

## What was imported

- `SKILL.md`
- `references/` — 6 file(s): extended reference documents that the SKILL.md body links to

## Ownership

turbo is one composable dev process split into 74 interlinked skills. Each skill
owns its own directory upstream, and the pack-level instruction, setup, update and
convention documents are shared by all 74, so they live in `rules/turbo/` rather
than inside any one skill.

Upstream also ships a parallel `codex/skills/` edition: the same 74 skills reworded
for the Codex harness. Only the `claude/` edition is archived here, to avoid storing
the pack twice. Fetch `codex/skills/` from upstream if you need that variant.

# Source

- Repository: `tobihagemann/turbo`
- URL: https://github.com/tobihagemann/turbo
- Imported commit: `d0f862f`
- Upstream path: `claude/skills/create-skill`
- Local skill path: `05-development/turbo-create-skill`
- License: MIT
- Discovered: 2026-08-20

## What was imported

- `SKILL.md`
- `references/` — 10 file(s): extended reference documents that the SKILL.md body links to

## Ownership

turbo is one composable dev process split into 74 interlinked skills. Each skill
owns its own directory upstream, and the pack-level instruction, setup, update and
convention documents are shared by all 74, so they live in `rules/turbo/` rather
than inside any one skill.

Upstream also ships a parallel `codex/skills/` edition: the same 74 skills reworded
for the Codex harness. Only the `claude/` edition is archived here, to avoid storing
the pack twice. Fetch `codex/skills/` from upstream if you need that variant.

## Local rename

Upstream names this skill `create-skill`, which is already taken in this library by an
unrelated skill from another source. It is filed here as
`turbo-create-skill`, and the frontmatter `name:` plus the `/create-skill` cross-references
that other turbo skills use to invoke it were updated to match, so the pack stays
internally consistent. No other content was changed.

# Source

- Repository: `mcollina/skills`
- URL: https://github.com/mcollina/skills
- Imported commit: `856efd268ae85482d882f3d0bed869fd020b5c06`
- Upstream path: `skills/fastify`
- Local skill path: `05-development/fastify`
- License: MIT
- Baseline verified: 2026-08-23

## What was imported

- `SKILL.md`
- `rules/` — 19 file(s): always-on rule files the skill applies
- `tile.json`

## Ownership

Upstream publishes this skill as a self-contained directory under `skills/`, with its
`rules/` tree beside `SKILL.md`. Everything listed above lives inside that directory
upstream, so it is owned by this skill and travels with it.

## Update history

- 2026-08-23 — updated to `856efd268ae8`. Upstream added a `## Contents` table of contents to all 19 `rules/` files. The
change is purely additive — no existing line was altered or removed in any file.

Note on naming: the upstream frontmatter `name:` is `fastify-best-practices`
while this folder is `fastify`, which is what `catalog.json` keys on. That local
folder name predates this run and was left alone; `SKILL.md` is byte-identical to
upstream.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

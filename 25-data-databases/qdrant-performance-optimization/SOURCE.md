# Source

- Repository: `qdrant/skills`
- URL: https://github.com/qdrant/skills
- Imported commit: `f90056b7a0c0491d164853eb1e42f952b685fb39`
- Upstream path: `skills/qdrant-performance-optimization`
- Local skill path: `25-data-databases/qdrant-performance-optimization`
- License: Apache-2.0
- Baseline verified: 2026-09-05

## What was imported

- `SKILL.md`
- `indexing-performance-optimization/` — 1 file(s)
- `memory-usage-optimization/` — 1 file(s)
- `search-speed-optimization/` — 1 file(s)

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`, and this one bundles nested `SKILL.md` sub-skills that the top-level routing table dispatches to. They are part of the same package and are deliberately preserved. First-party: Qdrant documents its own database here.

## Update history

- 2026-09-05 — updated to `f90056b7a0c0`, the skill's first recorded baseline. Same restructuring: the hub page is now a symptom-to-file routing table over its nested sub-skills.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

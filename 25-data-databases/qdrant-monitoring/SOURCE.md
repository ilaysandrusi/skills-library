# Source

- Repository: `qdrant/skills`
- URL: https://github.com/qdrant/skills
- Imported commit: `f90056b7a0c0491d164853eb1e42f952b685fb39`
- Upstream path: `skills/qdrant-monitoring`
- Local skill path: `25-data-databases/qdrant-monitoring`
- License: Apache-2.0
- Baseline verified: 2026-09-05

## What was imported

- `SKILL.md`
- `debugging/` — 1 file(s)
- `setup/` — 1 file(s)

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`, and this one bundles nested `SKILL.md` sub-skills that the top-level routing table dispatches to. They are part of the same package and are deliberately preserved. First-party: Qdrant documents its own database here.

## Update history

- 2026-09-05 — updated to `f90056b7a0c0`, the skill's first recorded baseline. The top-level `SKILL.md` becomes a pure routing table over the `setup/` and `debugging/` sub-skills instead of restating their content, and the description picks up alert-setup, cluster-health and log-centralisation triggers.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

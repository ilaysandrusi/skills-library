# Source

- Repository: `wshobson/agents`
- URL: https://github.com/wshobson/agents
- Imported commit: `367cb6a4a182cf7e9b0a17c9429f7411ddd9cf35`
- Upstream path: `plugins/database-design/skills/postgresql`
- Local skill path: `25-data-databases/postgresql-table-design`
- License: MIT
- Discovered: 2026-08-20

## What was imported

- `SKILL.md`

## Ownership

Upstream ships this skill as a self-contained directory under the
`database-design` plugin's `skills/` tree. Everything listed above lives inside that
directory upstream, so it is owned by this skill and travels with it.

## Local rename

The upstream directory is named `postgresql`, but its `SKILL.md` frontmatter
declares `name: postgresql-table-design`. This library keys a skill on its
directory name, and the frontmatter name is both the accurate one and specific
enough to live alongside the other Postgres skills here, so the directory was
renamed to match the frontmatter. No file contents were changed.

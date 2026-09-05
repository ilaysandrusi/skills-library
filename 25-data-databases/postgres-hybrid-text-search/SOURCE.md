# Source

- Repository: `timescale/pg-aiguide`
- URL: https://github.com/timescale/pg-aiguide
- Imported commit: `acf42427fed507b7bfe98c4039fbacf0c4a69b65`
- Upstream path: `skills/postgres-hybrid-text-search`
- Local skill path: `25-data-databases/postgres-hybrid-text-search`
- License: Apache-2.0 (Copyright 2025 Timescale, Inc., d/b/a Tiger Data)
- Imported: 2026-09-05

## What was imported

- `LICENSE`
- `NOTICE`
- `SKILL.md`

## Why this skill

Hybrid retrieval combining BM25 keyword search with pgvector semantic search through Reciprocal Rank Fusion, with the concrete SQL. The library's existing `16-ai-apis-media/hybrid-search-implementation` is a 56-line engine-agnostic sketch; this is 295 lines of Postgres-specific implementation, so the two are complementary rather than duplicates.

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`. This
skill is plain Markdown — no scripts, no network access, no executable content of any
kind — so the directory upstream is the whole package. `LICENSE` and `NOTICE` are
deliberate copies of the upstream repository-root files, kept here so the skill stays
legally attributable when it is installed on its own.

The rest of `timescale/pg-aiguide` is the pg-aiguide MCP server itself (`src/`,
`ingest/`, `docker/`, `migrations/`), which is the product these skills accompany
rather than material they own. It was deliberately left upstream, following the
precedent set by `15-integrations/hey` (basecamp/hey-cli).

## What was deliberately not imported

- `skills/postgres/` — an umbrella router whose `references/` are eleven **symlinks** to
  its sibling skill directories (`../../<skill>/SKILL.md`). It contains no content of its
  own, its slug collides with the existing `25-data-databases/postgres` (an unrelated
  read-only SQL query skill from `sanjay3290/ai-skills`), and its symlinks would dangle
  the moment `tools/install-skill.mjs` copied it out on its own.
- `skills/design-postgres-tables/` — substantially duplicates the existing
  `25-data-databases/postgresql-table-design` (both cover PostgreSQL data types,
  constraints, indexing and performance patterns for general table design).
- `rules/postgres-best-practices.mdc` — a Cursor rule that instructs the agent to call the
  pg-aiguide MCP server's `search_docs` tool and to invoke `design-postgres-tables`.
  Neither is present here, so archiving the rule would leave broken instructions.

## Security review

2026-09-05. The package is Markdown and SQL only. No scripts, no `curl`/`wget`, no
`http://` URLs, no subprocess or shell invocation, no hooks, no binaries, nothing that
executes. The single hit from the destructive-command sweep is the phrase
`DELETE / TRUNCATE` inside the DDL lock reference, where it is describing which
statements take which lock. Nothing here is auto-invoked.

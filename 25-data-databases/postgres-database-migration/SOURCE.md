# Source

- Repository: `timescale/pg-aiguide`
- URL: https://github.com/timescale/pg-aiguide
- Imported commit: `acf42427fed507b7bfe98c4039fbacf0c4a69b65`
- Upstream path: `skills/postgres-database-migration`
- Local skill path: `25-data-databases/postgres-database-migration`
- License: Apache-2.0 (Copyright 2025 Timescale, Inc., d/b/a Tiger Data)
- Imported: 2026-09-05

## What was imported

- `LICENSE`
- `NOTICE`
- `SKILL.md`
- `references/` — 3 file(s)

## Why this skill

Which `ALTER TABLE` operations take an ACCESS EXCLUSIVE lock, timeout strategy, backfill patterns, rollback planning and fork-based testing, plus three references (`backfill-strategies.md`, `validation-queries.md`, `complete-example.md`).

The library already has `25-data-databases/database-migration` and `29-ecc/database-migrations`, and both mention zero-downtime deployment — but both are ORM-workflow skills (Prisma, Drizzle, TypeORM, golang-migrate) and neither documents PostgreSQL's DDL lock levels: `ACCESS EXCLUSIVE` and `lock_timeout` appear in no skill in the archive. The overlap is at the topic level and the content is complementary, so this was imported rather than skipped. It is the one skill in this batch where that call is debatable; if a reviewer disagrees, this is the one to retire.

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

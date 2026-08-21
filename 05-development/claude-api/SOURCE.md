# Source

- Repository: `anthropics/skills`
- URL: https://github.com/anthropics/skills
- Upstream path: `skills/claude-api`
- Imported commit: `0a64e398ec6bb34a494f0c347e8ccae53a862f8e`
- Local skill path: `05-development/claude-api`
- License: Apache-2.0 (`LICENSE.txt`, shipped inside the skill)

## What was imported

The whole upstream skill directory: `SKILL.md`, `LICENSE.txt`, the per-SDK
example trees (`csharp/`, `curl/`, `go/`, `java/`, `php/`, `python/`, `ruby/`,
`typescript/`) and `shared/`.

## Ownership

Every one of these files sits inside `skills/claude-api/` upstream, so all of it
belongs to this skill. The per-language directories are the code examples
`SKILL.md` routes to once it has established which SDK the user is on, and
`shared/` holds the language-agnostic reference material. Importing `SKILL.md`
alone would leave a skill whose every branch points at a missing file.

## Baseline

Verified on 2026-08-21 by comparing the git blob SHA of every local file against
the upstream tree at `0a64e398`: all files match, so this copy is exactly that
commit rather than an approximation of it.

## Update history

- **2026-08-21** — brought up to `0a64e398` from an earlier unrecorded state. The
  change is Anthropic's `prompt-audit` addition (upstream `f6656c12`): a new
  `prompt-audit` subcommand row in the `SKILL.md` command table, a new
  `shared/prompt-audit.md` reference, a pointer to it from
  `shared/model-migration.md`, and a note in the language-selection section that
  language-agnostic tasks should not ask the user to pick an SDK. Documentation
  only — no scripts, no network access, nothing executable.

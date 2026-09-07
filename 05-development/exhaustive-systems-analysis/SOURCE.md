# Source

- Repository: `petekp/claude-code-setup`
- URL: https://github.com/petekp/claude-code-setup
- Imported commit: `dcd4ca772bcf4b0e773a43e93258d0a8f59169fb`
- Upstream path: `skills/exhaustive-systems-analysis`
- Local skill path: `05-development/exhaustive-systems-analysis`
- License: MIT (Copyright (c) 2024 Pete Petrash)
- Imported: 2026-09-05

## What was imported

- `LICENSE`
- `SKILL.md`
- `agents/` — 1 file(s)
- `references/` — 2 file(s)

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`.
Everything listed above lives inside that directory upstream, so it is owned by
this skill and travels with it. `LICENSE` is a deliberate copy of the upstream
repository-root MIT licence, kept here so the skill stays attributable when
installed on its own.

This skill was extracted from HEAD of `petekp/claude-code-setup` after a fresh
clone to the agent's Desktop. It was NOT copied from the whole-repo snapshot that
previously sat at `09-anthropic-tools/claude-code-setup`.

## What was deliberately not imported

The rest of `petekp/claude-code-setup` was deliberately omitted from this
legacy standalone skill extract because those files are repository-level, not
owned by this skill. The complete upstream tree, including dotfiles, hooks, and
`setup.sh`, is now preserved unchanged at
`repositories/05-development/petekp--claude-code-setup`. Its hooks and setup
scripts remain archive-only and are not enabled automatically.

`emil-design-eng` and `fixing-motion-performance` are not in this HEAD and were
not imported.

Every file in this directory except `SOURCE.md` and the copied root `LICENSE` was
compared to upstream HEAD by copy-from-clone; the commit above is that clone's HEAD.

# Source

- Repository: `petekp/claude-code-setup`
- URL: https://github.com/petekp/claude-code-setup
- Imported commit: `dcd4ca772bcf4b0e773a43e93258d0a8f59169fb`
- Upstream path: `skills/catch-up`
- Local skill path: `08-context-engineering/catch-up`
- License: MIT (Copyright (c) 2024 Pete Petrash)
- Imported: 2026-09-05

## What was imported

- `LICENSE`
- `SKILL.md`

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

The rest of `petekp/claude-code-setup` is personal dotfiles, hooks, and
`setup.sh`. Those were deliberately left out of the library (and out of this
skill) — hooks are archived nowhere from this repo, and the setup script is the
author's machine config, not material the skill owns.

`emil-design-eng` and `fixing-motion-performance` are not in this HEAD and were
not imported.

Every file in this directory except `SOURCE.md` and the copied root `LICENSE` was
compared to upstream HEAD by copy-from-clone; the commit above is that clone's HEAD.

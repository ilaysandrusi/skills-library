# Source

- Repository: `talkstream/ru-text`
- URL: https://github.com/talkstream/ru-text
- Imported commit: `73dc04a492fc0bbeae31bd5374ce90c2d3cad6e7`
- Upstream path: `skills/ru-check`
- Local skill path: `01-copy-writing/ru-check`
- License: MIT
- Baseline verified: 2026-08-23

## What was imported

- `SKILL.md`

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`.
Everything listed above lives inside that directory upstream, so it is owned by this
skill and travels with it. The skills form one pack that shares a rule corpus, and
`ru-check` reads the corpus that `ru-text` carries.

## Update history

- 2026-08-23 — updated to `73dc04a492fc`. Upstream propagated the same R30 correction («я» added to the single-letter word
list). This skill is a single `SKILL.md`, so `tools/check-upstream.py` reported it
as `unmatched-candidate` rather than `drift` — with one file, a changed file means
zero matched files. Confirmed a genuine update, not a same-name coincidence, by
matching the frontmatter `name` and `description` against upstream.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

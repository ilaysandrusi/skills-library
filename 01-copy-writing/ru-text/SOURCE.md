# Source

- Repository: `talkstream/ru-text`
- URL: https://github.com/talkstream/ru-text
- Imported commit: `73dc04a492fc0bbeae31bd5374ce90c2d3cad6e7`
- Upstream path: `skills/ru-text`
- Local skill path: `01-copy-writing/ru-text`
- License: MIT
- Baseline verified: 2026-08-23

## What was imported

- `SKILL.md`
- `agents/` — 2 file(s): agents shipped with the skill upstream
- `references/` — 10 file(s): extended reference documents that the SKILL.md body links to

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`.
Everything listed above lives inside that directory upstream, so it is owned by this
skill and travels with it. The skills form one pack that shares a rule corpus, and
`ru-check` reads the corpus that `ru-text` carries.

## Update history

- 2026-08-23 — updated to `73dc04a492fc`. Upstream corrected the single-letter-word rule (R30) to include the pronoun «я», and fixed two claims in `anti-patterns.md` about which rules live in `typography.md`.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

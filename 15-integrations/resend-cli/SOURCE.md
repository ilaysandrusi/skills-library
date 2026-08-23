# Source

- Repository: `resend/resend-skills`
- URL: https://github.com/resend/resend-skills
- Imported commit: `2a69b9f39a16c043cbfad45fbfa3c141bd27b050`
- Upstream path: `skills/resend-cli`
- Local skill path: `15-integrations/resend-cli`
- License: MIT
- Baseline verified: 2026-08-23

## What was imported

- `SKILL.md`
- `references/` — 17 file(s): extended reference documents that the SKILL.md body links to

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`.
Everything listed above lives inside that directory upstream, so it is owned by this
skill and travels with it. First-party: Resend documents its own API and CLI here.

## Update history

- 2026-08-23 — updated to `2a69b9f39a16`. Documented `automations duplicate` and the new `careers` command; skill version
2.6.0 → 2.8.0. `references/careers.md` is new upstream and describes
`resend careers list|apply`, a real command of the vendor's CLI. It uploads a
resume only when the user explicitly runs `careers apply`, to Resend's own
applicant tracking system; it is documentation only, with no code in this package.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

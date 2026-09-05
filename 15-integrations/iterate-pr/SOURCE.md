# Source

- Repository: `getsentry/skills`
- URL: https://github.com/getsentry/skills
- Imported commit: `c2f99a5b04b4cd992ec3022d7c2c3e23e938d241`
- Upstream path: `skills/iterate-pr`
- Local skill path: `15-integrations/iterate-pr`
- License: Apache-2.0
- Baseline verified: 2026-09-05

## What was imported

- `SKILL.md`
- `SPEC.md`
- `agents/` — 1 file(s)
- `scripts/` — 4 file(s)

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`, including the `scripts/` this skill shells out to. First-party: Sentry maintains this workflow skill for its own engineers.

## Update history

- 2026-09-05 — updated to `c2f99a5b04b4`, the skill's first recorded baseline. Sentry removed the hard-coded `*— Claude Code*` signature that `scripts/reply_to_thread.py` appended to every PR reply, so the script now posts the body it was given and nothing else. Reviewed: the scripts shell out to the `gh` CLI through `subprocess.run` with list arguments and no shell, which is unchanged.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

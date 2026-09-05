# Source

- Repository: `cloudflare/skills`
- URL: https://github.com/cloudflare/skills
- Imported commit: `b8aeca6d7e2d614d7bd0e5220c8dd7645fe58a93`
- Upstream path: `skills/workers-best-practices`
- Local skill path: `13-cloud-deploy/workers-best-practices`
- License: Apache-2.0
- Baseline verified: 2026-09-05

## What was imported

- `SKILL.md`
- `references/` — 2 file(s)

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`. Everything listed above lives inside that directory upstream, so it is owned by this skill and travels with it. First-party: Cloudflare documents its own platform here.

## Update history

- 2026-09-05 — updated to `b8aeca6d7e2d`, the skill's first recorded baseline. Adds one rule: Workers that validate with Zod need 4.5.0 or later, because older versions retain substantially more heap per schema and show up as high memory usage or OOMs.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

# Source

- Repository: `anthropics/skills`
- URL: https://github.com/anthropics/skills
- Imported commit: `41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f`
- Upstream path: `skills/claude-api`
- Local skill path: `05-development/claude-api`
- License: Apache-2.0 (upstream ships `LICENSE.txt` inside each skill directory)
- Baseline verified: 2026-09-05

## What was imported

- `LICENSE.txt`
- `SKILL.md`
- `csharp/` — 5 file(s)
- `curl/` — 2 file(s)
- `go/` — 5 file(s)
- `java/` — 5 file(s)
- `php/` — 6 file(s)
- `python/` — 7 file(s)
- `ruby/` — 4 file(s)
- `shared/` — 28 file(s)
- `typescript/` — 6 file(s)

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`. Everything listed above lives inside that directory upstream, so it is owned by this skill and travels with it. First-party: this is Anthropic's own skill. Upstream places `LICENSE.txt` inside the skill directory itself rather than at the repository root, so it is part of the package and travels with it.

## Update history

- 2026-09-05 — updated to `41bbe19d1a1a`. Model-currency refresh across all seven language guides: Claude Fable 5 → Fable 5.1 throughout the refusal-fallback documentation, plus two new `shared/` references (`admin-api.md`, covering OIDC workload federation for CI, and `cost-optimization.md`). The `prompt-audit` subcommand is now exempted from the interactive non-Anthropic-provider stop. The remainder of the 69-file diff is a mechanical ASCII pass replacing em dashes and `→` with `-` and `->`.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

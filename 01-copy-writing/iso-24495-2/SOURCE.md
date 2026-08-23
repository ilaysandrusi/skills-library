# Source

- Repository: `GaZmagik/iso-24495`
- URL: https://github.com/GaZmagik/iso-24495
- Imported commit: `58077fc4dd70daeedafc273f2abb9d341e6e5960` (tag `v0.6.1`, skill version 0.6.1)
- Upstream path: `skills/iso-24495-2`
- Local skill path: `01-copy-writing/iso-24495-2`
- License: MIT
- Discovered: 2026-08-23

## What this skill is

Legal writing (ISO 24495-2:2025): standardised modal verbs, no legalese, named actors, structured conditional clauses.

## What was imported

- `LICENSE` — MIT licence text, copied from the repository root
- `SKILL.md`
- `agents/` — 1 file(s): the `openai.yaml` agent definition upstream ships beside the skill

## Ownership

Upstream publishes this skill as a self-contained directory, and everything listed
above lives inside that directory upstream. Repository-level files shared by all eight
skills — the Claude Code output style, the README, the changelog and the Bun test
config — are archived together in [`rules/iso-24495/`](../../rules/iso-24495/) rather
than copied into each skill.

## The pack has to stay together

These skills are not independently self-contained, and that is the one thing to know before
moving any of them. Nine TypeScript files import a sibling skill by relative path:

- `iso-24495-text-audit/scripts/audit-text.ts` imports `../../iso-24495-4/scripts/audit-corpus.ts`
- `iso-24495-5/tests/*.test.ts` import `../../iso-24495-4/scripts/`
- `iso-24495-4/tests/text-audit.test.ts` imports `../../iso-24495-text-audit/scripts/audit-text.ts`

`../../` resolves to whatever directory holds the skills. Upstream that is `skills/`; here it is
`01-copy-writing/`. All 23 relative imports were checked and resolve in this layout, which is why
all eight skills sit in one category. Move one to another category, or install one on its own with
`tools/install-skill.mjs`, and its scripts lose their imports. The prose-only skills
(`iso-24495-1`, `-2`, `-3`, `-code`, `-style`) have no scripts and travel fine alone.

## Licensing and ISO text

MIT, Copyright (c) 2026 Gareth Williams. `LICENSE` is copied into this directory.

The skills are original guidance *inspired by* the ISO 24495 series; they do not reproduce ISO
text, and upstream says so in every skill. Parts 4 and 5 are based on an unpublished committee
draft and working draft respectively and are marked provisional upstream. No output from any of
these skills is a conformance claim.

## Security review

No script in any skill opens a network connection, shells out, or reads an environment variable.
The tooling reads and writes local files only: `audit-text.ts` writes a findings JSON where the
caller asks, and `audit-corpus.ts` reads an optional `.iso-24495-4/acronyms.json` from the project
being audited. Symlinked targets are skipped rather than followed. Every `https://` string in the
skills is a test fixture using `example.com`.

Three upstream things were deliberately left behind:

- `scripts/traffic-snapshot*.ts` and `.github/workflows/traffic-snapshot.yml` — the author's own
  GitHub traffic analytics for this repository. They read `GITHUB_TRAFFIC_TOKEN` and call the
  GitHub API. Repository housekeeping, not skill material, and the only token-reading code here.
- `scripts/check.sh` and `.github/workflows/tests.yml` — the repository's CI gate. It is clean and
  offline, but its third step runs the traffic-snapshot entry point, so importing it without that
  tooling would archive a gate that cannot pass. Run `bun test` from `01-copy-writing/` instead;
  `rules/iso-24495/bunfig.toml` holds the coverage thresholds upstream applies.
- `.iso-24495-4/acronyms.json` and `.iso-24495-4/state.json` at the upstream repository root — the
  author's own audit state from running the tool against their own repository, not seed data.

`bun` is not installed on the machine that performed this import, so `bun test` was not executed
here. Installation was tested with `tools/install-skill.mjs` for all eight skills.

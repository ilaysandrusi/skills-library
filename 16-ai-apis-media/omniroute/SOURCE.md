# Source

- Repository: `diegosouzapw/OmniRoute`
- URL: https://github.com/diegosouzapw/OmniRoute
- Upstream path: repository root (whole-repo clone)
- Imported commit: `42a13fedef8bb6806c1c4382b2c65539e871e88c` (2026-08-26) —
  **approximate, see "Baseline" below**
- License: MIT (Copyright (c) 2026 diegosouzapw)
- Local path: `16-ai-apis-media/omniroute`
- Imported: 2026-08-26, commit `618c95be`

## Status — awaiting manual review, not a catalogued skill

A **whole-repository clone**, not a skill package: no root `SKILL.md`, absent
from `catalog.json`, `SOURCES.json` and the category README, and the 2026-08-26
import wrote no `SOURCE.md`. This file was added on 2026-09-04 so the clone is
traceable; the structural question is queued in `UPDATE_CHECKS.json` under
`review_queue.unindexed_whole_repo_clones`.

**This is the largest single directory in the library: 250 MB across 13,098
files, or roughly a fifth of the working tree.**

## Baseline — approximate, not proven

Unlike the other two clones from the same import, no upstream commit matches
this directory exactly. The best match is `42a13fed` (2026-08-26T16:43:58Z) at
**13,079 of 13,098 files** (99.9%), with 19 files differing and **none absent**.

The reason is upstream's commit rate: `diegosouzapw/OmniRoute` lands commits
seconds apart (eight distinct commits inside 20 seconds on 2026-08-26T20:40),
so a clone taken while it advanced captures a working tree that spans several
commits and equals none of them. Match rates degrade monotonically in both
directions from `42a13fed`, which is what a snapshot straddling that point looks
like.

Treat this as a dated approximation, **not** a verified baseline. The 19
differing files are listed by
`python3 tools/check-upstream.py diegosouzapw/OmniRoute`.

## What this repository actually is

OmniRoute is an LLM API gateway — a Next.js/TypeScript application that fronts
many model providers behind one endpoint. The repository is the product:
`src/` (68 MB), `tests/` (41 MB), `open-sse/`, `electron/`, `docker/`, `bin/`,
plus `docs/` at 108 MB, of which **102 MB is `docs/i18n`** — the product
changelog and documentation translated into many languages.

The part relevant to this library is `skills/` — **500 KB, 46 skills**, split
into an `omni-*` family (`omni-auth`, `omni-models`, `omni-providers`,
`omni-routing` and so on) and a `cli-*` family (`cli-chat`, `cli-keys`,
`cli-serve`, …), all of which operate the gateway. None is indexed.

So the import brought in roughly 500× its own weight in product source and
translated documentation to obtain the skills.

## Also present: a test fixture that is not a skill

`tests/fixtures/devin-bridge/e2e-workspace/.claude/skills/bridge-proof/SKILL.md`
is an end-to-end test fixture, not a skill. This is the exact pattern that put a
live malware sample into `12-security/` in August 2026 (from
`snyk/agent-scan/tests/skills/`) and an eval harness into `25-data-databases`
(`score-eval`). It must not be catalogued if the skills here are ever extracted.

## Security review (2026-09-04, first review of this import)

- No committed secrets. `.env.example` is large (3,075 lines) but is a template
  for a many-provider gateway; scans for live-looking `sk-`, `ghp_`, `AIza`,
  `xox*` and `AKIA` values in it, in `config/` and in `docker/` came back empty.
- No hits in the standing malware sweep and no `base64 … | sh` construct.
- Nothing here is wired to run automatically from the archive.
- Worth flagging for the review, as a quality signal rather than a security one:
  the upstream repository commits every few seconds, is heavily marketed in its
  own description ("352 providers", "1200+ models", "Built by 550+
  contributors"), and ships a 2.1 MB changelog translated into many languages.
  That pattern warrants scepticism about how much of the 46-skill set is
  substantive before any of it is catalogued.

## Recommendation

Do not keep the clone as-is. Either import a reviewed subset of `skills/` under
`16-ai-apis-media/` with proper indexes, or drop the directory entirely — the
gateway is the product these skills drive, not material they own, which is the
call already made for `15-integrations/hey` and `02-design-ui/superdesign`.
Reviewing 46 skills individually and deleting 13,000 files is far past the
10-resource automatic limit, so it needs a human decision.

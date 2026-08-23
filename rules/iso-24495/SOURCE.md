# Source: GaZmagik/iso-24495

- Repository: https://github.com/GaZmagik/iso-24495
- Upstream path(s): `output-styles/iso-24495.md`, `README.md`, `CHANGELOG.md`, `LICENSE`, `bunfig.toml`
- Commit pinned at import: `58077fc4dd70` (tag `v0.6.1`, plugin version 0.6.1)
- License: MIT, Copyright (c) 2026 Gareth Williams
- Files here: 5

The ISO 24495 plain-language pack is eight interlinked skills, archived under
[`01-copy-writing/`](../../01-copy-writing/) as `iso-24495-1`, `-2`, `-3`, `-4`, `-5`,
`-code`, `-text-audit` and `-style`. These files sit at the repository root upstream and
serve all eight, so they cannot be assigned to any single skill:

| File | What it is |
|---|---|
| `iso-24495.md` | the Claude Code **output style**. Selected with `/output-style`, it holds every response to the core rules without waiting for a skill to activate, and names which sector skill to reach for. A genuine always-on rule, which is why it lives here. |
| `README.md` | the pack's own map of the eight skills, plus install instructions for Claude Code and Codex |
| `CHANGELOG.md` | upstream's version history — the record of what changed between releases |
| `bunfig.toml` | the `bun test` configuration, including the 100% line and function coverage thresholds upstream enforces |
| `LICENSE` | MIT licence text |

## Why this is a rule and not a skill

`iso-24495.md` is loaded for every response once selected, rather than activating when the
context matches, which is the distinction `ARTIFACTS.md` draws between a rule and a skill.
Codex has no output style, so upstream ships the same rules there as a skill; that variant
is archived as `01-copy-writing/iso-24495-style`. The two overlap on purpose — they are the
same rules for two harnesses — and neither was dropped, because dropping either would lose
one harness's route to them.

## Not imported

`scripts/traffic-snapshot*.ts` and `.github/workflows/traffic-snapshot.yml` are the author's
GitHub traffic analytics for this repository: they read `GITHUB_TRAFFIC_TOKEN` and call the
GitHub API. `scripts/check.sh` and `.github/workflows/tests.yml` are the CI gate, which is
clean but runs the traffic tooling as its third step. `.iso-24495-4/` at the repository root
is the author's own accumulated audit state, not seed data. Details in each skill's
`SOURCE.md`.

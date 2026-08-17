# Source

- Repository: https://github.com/trailofbits/skills
- Commit pinned at import: `4db88ee79db0a68bbe049fe827e272ee2bc19510` (branch `main`)
- License: CC-BY-SA-4.0

## Companion artifacts held in this skill

These were moved out of the shared artifact trees into this skill because the upstream
structure ties them to it. The evidence for each is below.

| Folder | Files | Upstream path | Evidence |
|---|---|---|---|
| `agents/` | 3 | `plugins/c-review/agents/` | trailofbits/skills: upstream `plugins/c-review/` contains exactly this one skill plus these agents |

See [`/ARTIFACTS.md`](../../ARTIFACTS.md) for the shared artifacts that could not be tied to a single skill.
| `scripts/` | 7 | `plugins/c-review/scripts/` | plugin publishes exactly this one skill, and its agents read these |
| `prompts/` | 63 | `plugins/c-review/prompts/` | plugin publishes exactly this one skill, and its agents read these |

The `scripts/` and `prompts/` layers were restored during the dependency-repair pass: the agents held here call `scripts/generate_sarif.py` and read `prompts/clusters/manifest.json`.

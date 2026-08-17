# Source

- Repository: https://github.com/trailofbits/skills
- Commit pinned at import: `4db88ee79db0a68bbe049fe827e272ee2bc19510` (branch `main`)
- License: CC-BY-SA-4.0

## Companion artifacts held in this skill

These were moved out of the shared artifact trees into this skill because the upstream
structure ties them to it. The evidence for each is below.

| Folder | Files | Upstream path | Evidence |
|---|---|---|---|
| `commands/` | 1 | `plugins/skill-improver/commands/` | trailofbits/skills: upstream `plugins/skill-improver/` contains exactly this one skill plus these commands |
| `hooks/` | 2 | `plugins/skill-improver/hooks/` | trailofbits/skills: upstream `plugins/skill-improver/` contains exactly this one skill plus these hooks |
| `scripts/` | 3 | `plugins/skill-improver/scripts/` | sourced by `hooks/stop-hook.sh` and called by `commands/cancel-skill-improver.md`; recovered so the moved hook resolves |

See [`/ARTIFACTS.md`](../../ARTIFACTS.md) for the shared artifacts that could not be tied to a single skill.

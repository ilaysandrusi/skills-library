# Source

- Repository: https://github.com/foryourhealth111-pixel/Vibe-Skills
- Commit pinned at import: `d5ae560440a9ecd83397bb68e77ea1aa2f2c9b78` (branch `main`)
- License: Apache-2.0

## Companion artifacts held in this skill

This folder holds the whole upstream repository, so the repo-root `agents/`, `commands/`
and `rules/` came down with it. The artifact pass had also copied them into the shared
trees; the skill-centric reorganization removed those duplicates and consolidated
everything here.

| Folder | Files | Upstream path | Evidence |
|---|---|---|---|
| `agents/templates/` | 4 | `agents/templates/` | already inside this folder; the shared copy was byte-identical |
| `agents/opencode/` | 3 | `.opencode/agent/` | repo-root artifact of the same repository this folder mirrors |
| `commands/` | 3 | `commands/` | already inside this folder; the shared copy was byte-identical |
| `rules/` | 5 | `rules/` | already inside this folder; the shared copy was byte-identical |

See [`/ARTIFACTS.md`](../../ARTIFACTS.md) for the shared artifacts that could not be tied
to a single skill.

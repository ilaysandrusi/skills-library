# Source

- Repository: `wshobson/agents`
- URL: https://github.com/wshobson/agents
- Imported commit: `367cb6a4a182cf7e9b0a17c9429f7411ddd9cf35`
- Upstream path: `plugins/ship-mate/skills/scan`
- Local skill path: `05-development/ship-mate-scan`
- License: MIT
- Discovered: 2026-08-20

## What was imported

- `SKILL.md`

## Ownership

Upstream ships this skill as a self-contained directory under the
`ship-mate` plugin's `skills/` tree. Everything listed above lives inside that
directory upstream, so it is owned by this skill and travels with it.

## Local rename

Upstream names this skill `scan`. That slug is too generic to sit in a
library of this size, so it is filed here as `ship-mate-scan`, keeping the
`ship-mate` plugin name as a prefix. The `name:` field in `SKILL.md` was
updated to match, because this library keys a skill on its directory name.

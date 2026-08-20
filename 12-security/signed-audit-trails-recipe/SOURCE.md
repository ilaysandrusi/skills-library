# Source

- Repository: `wshobson/agents`
- URL: https://github.com/wshobson/agents
- Imported commit: `367cb6a4a182cf7e9b0a17c9429f7411ddd9cf35`
- Upstream path: `plugins/signed-audit-trails/skills/signed-audit-trails-recipe`
- Local skill path: `12-security/signed-audit-trails-recipe`
- License: MIT
- Discovered: 2026-08-20

## What was imported

- `SKILL.md`

## Ownership

Upstream ships this skill as a self-contained directory under the
`signed-audit-trails` plugin's `skills/` tree. Everything listed above lives inside that
directory upstream, so it is owned by this skill and travels with it.

## Not imported

This skill documents a pattern whose runtime implementation lives in
upstream's `protect-mcp` plugin. That plugin was deliberately not imported:
its hooks shell out to `npx protect-mcp` on every `PreToolUse` and
`PostToolUse` event. The cookbook is archived; the runtime hooks are not.

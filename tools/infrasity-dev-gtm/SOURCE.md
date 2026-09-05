# Source

- Repository: https://github.com/infrasity-labs/dev-gtm-claude-skills
- Upstream path(s): `tools/`
- Commit pinned at import: `02cfefb3a213041de8b80bc659ebc5f17b5e746a` (branch `main`)
- License: MIT
- Files here: 62
- Serves: 358 skills in this library

The tool registry and the per-integration docs (`REGISTRY.md`, `integrations/*.md`) that the GTM skills consult before calling a vendor API.

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer, so the skills that read it had dangling references.

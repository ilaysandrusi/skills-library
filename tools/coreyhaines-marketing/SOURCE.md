# Source

- Repository: https://github.com/coreyhaines31/marketingskills
- Upstream path(s): `tools/`
- Commit pinned at import: `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` (branch `main`)
- License: MIT
- Files here: 161
- Serves: 50 skills in this library

Tool registry and per-integration docs (`REGISTRY.md`, `integrations/*.md`) the marketing skills consult before calling a vendor API. A separate pack from infrasity-dev-gtm even though the skills address it by the same upstream path, which is why each has its own namespace.

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer.

# Source

- Repository: https://github.com/infrasity-labs/dev-gtm-claude-skills
- Upstream path(s): `scripts/`
- Commit pinned at import: `02cfefb3a213041de8b80bc659ebc5f17b5e746a` (branch `main`)
- License: MIT
- Files here: 68
- Serves: 358 skills in this library

Repo-root script library shared by the pack.

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer, so the skills that read it had dangling references.

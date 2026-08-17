# Source

- Repository: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- Upstream path(s): `tools/`
- Commit pinned at import: `0c65f8b34668c39f391b871ac61479eb64497c37` (branch `main`)
- License: MIT
- Files here: 47
- Serves: 105 skills in this library

The research tool library (arXiv fetch, wiki ingest, ARIS install) that the research skills shell out to.

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer, so the skills that read it had dangling references.

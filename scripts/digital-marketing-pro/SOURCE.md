# Source

- Repository: https://github.com/indranilbanerjee/digital-marketing-pro
- Upstream path(s): `scripts/`
- Commit pinned at import: `fa4ccd0a4afc1b902ef8de8d297b180aa148d46a` (branch `main`)
- License: MIT
- Files here: 96
- Serves: 178 skills in this library

Repo-root script library shared by the whole pack — the skills call these by name (`python scripts/campaign-tracker.py`).

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer, so the skills that read it had dangling references.

# Source

- Repository: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- Upstream path(s): `skills/shared-references/`
- Commit pinned at import: `0c65f8b34668c39f391b871ac61479eb64497c37` (branch `main`)
- License: MIT
- Files here: 31
- Serves: 105 skills in this library

Upstream keeps this **inside** its `skills/` tree, so its skills address it as `../shared-references/…`. Holding it beside the skills in this category reproduces that exactly, which is why no reference in those skills had to be rewritten. This is a shared resource, not a skill: it has no `SKILL.md` and does not appear in `catalog.json`.

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer, so the skills that read it had dangling references.

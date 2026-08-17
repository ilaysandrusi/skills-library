# Source

- Repository: https://github.com/aaron-he-zhu/aaron-marketing-skills
- Upstream path(s): `scripts/`
- Commit pinned at import: `9ac17c013c2bac0d70d141a73cdcd2ae3f68fbfd` (branch `main`)
- License: Apache-2.0
- Files here: 100
- Serves: 120 skills in this library

The connector and audit scripts the marketing skills invoke. Skills that call them through `${CLAUDE_PLUGIN_ROOT}/scripts/…` keep that form: it is resolved by the harness at runtime, and rewriting it would break the pack when installed as a plugin. The files are now present either way.

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer, so the skills that read it had dangling references.

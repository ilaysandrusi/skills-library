# Source

- Repository: https://github.com/aaron-he-zhu/aaron-marketing-skills
- Upstream path(s): `references/`, `CONNECTORS.md`, `SECURITY.md`
- Commit pinned at import: `9ac17c013c2bac0d70d141a73cdcd2ae3f68fbfd` (branch `main`)
- License: Apache-2.0
- Files here: 377
- Serves: 120 skills in this library

The reference library and the two repo-root policy docs that all 120 upstream skills read. Upstream nests its skills three levels deep, so they address this as `../../../references/…`; the library flattens skills to one level, so the references in those skills now point at `../../references/aaron-marketing/…`.

Restored during the dependency-repair pass: the earlier imports took `agents`, `commands`, `rules` and `hooks` but never this layer, so the skills that read it had dangling references.

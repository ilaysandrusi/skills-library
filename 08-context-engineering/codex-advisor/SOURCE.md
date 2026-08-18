# Source

- **Skill:** `codex-advisor`
- **Origin:** fcakyon/claude-codex-settings — `codex-advisor` plugin
- **Repository:** https://github.com/fcakyon/claude-codex-settings
- **Path:** `plugins/codex-advisor/skills/codex-advisor`
- **Commit:** `bad8cb6eaf47c4fadc4128221dd45ac40530fe9b`
- **Discovered:** 2026-08-18 daily skills-library maintenance
- **License:** Apache-2.0 (repository is Apache-2.0; this plugin declares Apache-2.0)
- **Why included:** Cross-model second opinion: relays the live conversation to GPT through the Codex CLI and returns the verdict verbatim. A genuinely different pattern from the library's single-model review skills.
- **Companion artifacts:** the upstream `codex-advisor` plugin publishes exactly this one skill, so its plugin-level `claude-agents/` and `claude-hooks/` were copied into this skill directory as `agents/` and `hooks/` rather than into the shared trees.

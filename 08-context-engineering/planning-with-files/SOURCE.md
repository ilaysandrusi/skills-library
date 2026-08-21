# Source

- Repository: `OthmanAdi/planning-with-files`
- URL: https://github.com/OthmanAdi/planning-with-files
- Upstream path: `skills/planning-with-files`
- Imported commit: `84eb74c4b0cda85af1dc86ee883917f7b325eee5`
- Local skill path: `08-context-engineering/planning-with-files`
- License: MIT (Copyright (c) 2026 Ahmad Adi)

## What was imported

The canonical skill directory: `SKILL.md`, `reference.md`, `examples.md`,
`scripts/` (20 files — a `.sh` and `.ps1` pair per operation, plus
`session-catchup.py`) and `templates/` (6 plan and findings templates).

## Ownership

`skills/planning-with-files/` is one self-contained skill upstream. `SKILL.md`
does not restate the mechanics; it calls the scripts by name and tells the agent
to copy the templates, so importing the markdown alone would leave a skill whose
every instruction points at a missing file. The `.ps1` files are the Windows
half of the same operations, not an alternative package.

## What was deliberately not imported

- `skills/i18n/planning-with-files-{ar,de,es,zh,zht}` — five translations of this
  same skill. Same scripts, same templates, translated prose. Archiving them
  would add five near-duplicates of what is already here.
- The repository's per-harness copies (`.claude/`, `.codex/`, `.cursor/`,
  `.gemini/` and nine more) — the same skill vendored once per agent, which is
  how it ships to end users, not a set of distinct resources.
- `tests/`, `docs/`, `examples/`, `media/`, `scripts/` at the repository root —
  release and CI machinery for the npm package rather than files the skill reads.

## Hooks — read before enabling

`SKILL.md` carries a `hooks:` block in its frontmatter declaring
`UserPromptSubmit`, `PreToolUse`, `PreCompact` and `Stop` handlers, and
`scripts/gate-stop.sh` plus `scripts/inject-plan.sh` are their dispatchers. Per
`ARCHIVE_POLICY.md` these are archived, **not** enabled, and nothing here runs
until you wire it into a real agent config yourself.

Reviewed before import:

- No network access anywhere in the package. No `curl`, `wget`, `/dev/tcp`, no
  networking imports in `session-catchup.py`, no downloads, no remote execution.
- No destructive commands, no `sudo`, no writes outside the project's
  `.planning/` directory.
- `session-catchup.py` reads `~/.claude/projects/` and `~/.codex/sessions`
  transcripts. That is read-only and is the documented purpose of the skill —
  rebuilding plan state after `/clear` — but it does mean the script touches
  local session history, so it is worth knowing before enabling.
- `gate-stop.sh` is a thin dispatcher that resolves a sibling `check-complete.sh`
  and runs it; both honour a `PLANNING_DISABLED=1` opt-out and exit 0 when the
  skill is not in use.

## Why this is not a duplicate

The library already holds several planning skills (`05-development/draft-plan`,
`writing-plans`, `executing-plans`, `08-context-engineering/implementation-plan`).
Those are about *how to write a plan*. This one is about *keeping a plan alive*:
plans are held on disk, re-injected per turn, and recovered after a context clear
or compaction, with a completion gate. That is a context-persistence mechanism,
which is why it sits in `08-context-engineering` rather than with the authoring
skills.

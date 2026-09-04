# Source

- Repository: `OthmanAdi/planning-with-files`
- URL: https://github.com/OthmanAdi/planning-with-files
- Upstream path: `skills/planning-with-files`
- Imported commit: `03128b278b0926180854703e43abd7ea2ff18c00`
- Upstream version: `3.16.0`
- Previous imported commit: `84eb74c4b0cda85af1dc86ee883917f7b325eee5` (`3.11.0`)
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
- `gate-stop.sh` is a thin dispatcher that resolves a sibling `check-complete.sh`
  and runs it; both honour a `PLANNING_DISABLED=1` opt-out and exit 0 when the
  skill is not in use.

### `session-catchup.py` and the `3.16.0` hardening

At `3.11.0` this script read `~/.claude/projects/` and `~/.codex/sessions`
transcripts **by default**, including from the automatic session-start path. That
was read-only and was the skill's documented purpose, but it meant a lifecycle
hook reached into local session history unprompted.

`3.16.0` narrows that, and the change is the reason this update was taken:

- automatic recovery now reads the project's own planning files plus
  `git diff --stat` only, and no longer inspects any agent session store;
- session history is reachable solely through an explicit flag —
  `--metadata` emits aggregate counts for the same project only, and `--replay`
  emits bounded, nonce-framed excerpts;
- every hook command now short-circuits with `exit 0` when `CLAUDE_PLUGIN_ROOT`
  is set, so a plugin install no longer double-fires the handlers;
- the frontmatter description now states outright that the skill has no network
  upload path and never runs commands declared in Markdown.

Re-verified after the update: still no `curl`, `wget`, `urllib`, `requests`,
`socket`, `subprocess`, `os.system`, `eval`, `exec`, `Invoke-WebRequest` or
`Invoke-Expression` anywhere in the package. The nonce framing around replayed
excerpts is prompt-injection defence — replayed transcript text is fenced so the
reading agent cannot mistake it for instructions.

## Why this is not a duplicate

The library already holds several planning skills (`05-development/draft-plan`,
`writing-plans`, `executing-plans`, `08-context-engineering/implementation-plan`).
Those are about *how to write a plan*. This one is about *keeping a plan alive*:
plans are held on disk, re-injected per turn, and recovered after a context clear
or compaction, with a completion gate. That is a context-persistence mechanism,
which is why it sits in `08-context-engineering` rather than with the authoring
skills.

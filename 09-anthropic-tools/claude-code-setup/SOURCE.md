# Source

- Repository: `petekp/claude-code-setup`
- URL: https://github.com/petekp/claude-code-setup
- Upstream path: repository root (whole-repo clone)
- Imported commit: `f1cb10fdacff75af66509c0f1ef6920368bbb6e8`
- Baseline: **proven**. All 76 local files are blob-identical to that commit.
- License: MIT (Copyright (c) 2024 Pete Petrash)
- Local path: `09-anthropic-tools/claude-code-setup`
- Imported: 2026-08-26, commit `618c95be`

## Status — awaiting manual review, not a catalogued skill

This directory is a **whole-repository clone**, not a skill package. It has no
`SKILL.md` at its root, it is absent from `catalog.json`, `SOURCES.json` and the
category README, and the 2026-08-26 import wrote no `SOURCE.md`. This file was
added on 2026-09-04 so the clone can at least be traced, audited and updated;
the structural question is queued in `UPDATE_CHECKS.json` under
`review_queue.unindexed_whole_repo_clones`.

## What this repository actually is

Pete Petrash's personal, forkable Claude Code configuration — dotfiles, not a
published skill pack. Inside it, `skills/` holds **18 genuine skills**:

`catch-up`, `circuit`, `circuit-resource-analysis`, `claude-code-audit`,
`code-comments`, `deep-research`, `emil-design-eng`,
`exhaustive-systems-analysis`, `fixing-motion-performance`, `latent-potential`,
`literate-guide`, `plain`, `pr-screenshot-comparison`, `pr-self-review`,
`react-change-review`, `spike`, `typography`, `write-goal`.

Several carry their own `references/`, `scripts/` and `evals/`, so they are real
packages rather than lone Markdown files. None of the 18 is indexed, so they are
invisible to `catalog.json` and to `tools/install-skill.mjs`.

## Upstream is ahead

Upstream HEAD at the 2026-09-04 check was `439a0cf7` (2026-09-03): 7 files
changed and 2 added since the imported commit.

## Security review (2026-09-04, first review of this import)

The clone was committed without a recorded review. Reviewed now:

- **`settings.json` declares hooks on 15 lifecycle events** — `SessionStart`,
  `SessionEnd`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`,
  `PostToolUseFailure`, `PreCompact`, `Stop`, `SubagentStart`, `SubagentStop`,
  `PermissionRequest`, `Notification`, `TaskCompleted`, `TeammateIdle`.
  Every one of them pipes the hook payload into
  `curl -X POST http://127.0.0.1:7474/hook` with a bearer token read from
  `$HOME/.capacitor/runtime/runtime-service-7474.token`.
  The destination is **loopback only**, the token is local, the timeouts are one
  second and each call ends in `|| true`, so this is a local observability
  daemon ("Capacitor") rather than data egress. It is still the author's own
  machine wiring: enabling it would feed prompt text and every tool call into
  whatever is listening on port 7474. Per `ARCHIVE_POLICY.md` these hooks are
  archived and **must not be enabled**.
- `SessionStart` additionally runs `sync-codex-skills.sh` and
  `skill-doctor.sh --quiet`; `PostToolUse` and `UserPromptSubmit` run
  `skill-usage-tracker.sh`; `SessionEnd` runs `session-end-cleanup.sh`. These are
  local file operations against the user's own `~/.claude` tree.
- `setup.sh` (573 lines) and `scripts/skill-manager.sh` (684 lines) write into
  `~/.claude`. They are installers for the author's setup, and would overwrite a
  user's own configuration. Not run here.
- No credential harvesting, no remote code execution, no obfuscation, no
  binaries. Hosts referenced are `github.com`, `skills.sh`, `127.0.0.1` and a
  set of typography reference sites linked from the `typography` skill.

## Recommendation

Keep the 18 skills, drop the personal dotfiles. Extracting them into the right
categories with per-skill `SOURCE.md` files is 18 resources, over the
10-resource automatic limit in the maintenance policy, so it needs a human
decision rather than an automatic rewrite.

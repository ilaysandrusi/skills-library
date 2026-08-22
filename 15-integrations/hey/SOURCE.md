# Source

- Repository: `basecamp/hey-cli`
- URL: https://github.com/basecamp/hey-cli
- Upstream path: `skills/hey`
- Imported commit: `bf09d786da99a6540522e6cf3801da34a0342c0b`
- Local skill path: `15-integrations/hey`
- License: MIT (`LICENSE.md`, copied from the repository root)
- Publisher: Basecamp (first-party)

## What was imported

- `SKILL.md` — the skill itself, 631 lines covering the HEY surface the CLI
  exposes: email (boxes, labels, collections, threads, replies, forwarding,
  drafts, the screener), contacts, calendars, todos, habits, time tracking and
  journal entries.
- `LICENSE.md` — the repository licence.
- `API-COVERAGE.md` — the mapping from HEY API endpoints to the CLI operations,
  including the documented gaps (for example that `/topics/{id}/entries.json`
  cannot be paged by number, and the one reply-recipients endpoint the Go SDK
  does not yet expose). This is what makes the skill auditable: it says what the
  CLI can and cannot reach.
- `README.md` — installation and authentication instructions. Without it the
  skill cannot be run, because the `hey` binary is installed separately.
- `hooks/` — the upstream plugin's `hooks.json`, `session-start.sh` and
  `plugin.json`.

Left upstream: the Go CLI application itself (`cmd/`, `internal/`, `go.mod`,
`go.sum`, `Makefile`, `.goreleaser.yaml`, the CI workflows and the Nix flake).
That is the product the skill drives, not supporting material the skill owns, and
the archive is not the right place to carry a vendored copy of an application
whose releases are published as binaries.

## Ownership

This repository publishes exactly one skill, so under the archive policy the
adjacent repository files serve it. `SKILL.md` is self-contained and references
no other repository file, so only the files that are genuinely needed to run,
audit or update it were taken: the licence, the API coverage map, the install
instructions and the plugin hooks.

The hooks are kept inside the skill rather than in the shared `hooks/` tree
because with exactly one skill in the repository their ownership is
unambiguous — they exist to report on that skill's CLI.

## Hooks — archived, not enabled

`hooks/hooks.json` declares a single **`SessionStart`** hook running
`hooks/session-start.sh` with a 5 second timeout. Per the archive policy it is
stored, never wired up.

Reviewed: the script is a liveness check. It tests whether `hey` is on `PATH`,
runs `hey auth status --json`, parses `.data.authenticated` with `jq` when `jq`
is available, and prints one of four short status strings. It writes no files,
sets no environment, installs nothing, and makes no network call of its own. It
degrades quietly when either `hey` or `jq` is missing rather than failing the
session. If it were ever enabled, that is all it would do.

## Why this skill

First-party from Basecamp, MIT, and actively developed. The library already
covers Gmail and Google Workspace (`15-integrations/gws-*`,
`10-hyperfx-marketing/gmail`), transactional email APIs (`sendmux-*`,
`courier`) and agent inboxes (`agent-email-inbox`), but had nothing for HEY,
which is a separate product with its own model — boxes, the screener,
collections — that does not map onto the Gmail skills. It follows the same
pattern as the other first-party vendor packages already archived here
(Cloudflare, Redis, Firebase, Stripe, Supabase).

## Security review

The skill body is documentation of CLI invocations. Authentication is delegated
entirely to `hey auth login`, which is the vendor's own CLI storing its own
credentials; nothing in the imported files reads, writes or transmits a token.
The only executable content is the session-start hook reviewed above.

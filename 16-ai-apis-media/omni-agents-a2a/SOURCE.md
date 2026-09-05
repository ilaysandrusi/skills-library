# Source

- Repository: `diegosouzapw/OmniRoute`
- URL: https://github.com/diegosouzapw/OmniRoute
- Imported commit: `9d1a896c6058b2ade94c9078c2e54377b9aa76d3`
- Upstream path: `skills/omni-agents-a2a`
- Local skill path: `16-ai-apis-media/omni-agents-a2a`
- License: MIT (Copyright (c) 2026 diegosouzapw)
- Imported: 2026-09-05

## What was imported

- `LICENSE`
- `SKILL.md`
- `THIRD_PARTY_NOTICES.md`

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`.
Everything listed above lives inside that directory upstream. `LICENSE` is a
deliberate copy of the upstream repository-root MIT licence.

Extracted from HEAD of `diegosouzapw/OmniRoute` after a fresh Desktop clone. Not
copied from the 250 MB whole-repo snapshot that previously sat at
`16-ai-apis-media/omniroute`. Example `curl` calls in these files talk to
`localhost:20128` / `$OMNIROUTE_URL`, which is the local OmniRoute server, not an
external exfil path.

## What was deliberately not imported

The OmniRoute application, `docs/` (including ~102 MB of `docs/i18n`),
tests, and `tests/fixtures/devin-bridge/.../bridge-proof` were deliberately not
imported. `bridge-proof` is a test fixture (`evals/`, `fixtures/`) and must never
be catalogued. The application is the product these skills drive, not material
they own — same precedent as `15-integrations/hey`.

Every file in this directory except `SOURCE.md` and the copied root `LICENSE` was
compared to upstream HEAD by copy-from-clone; the commit above is that clone's HEAD.

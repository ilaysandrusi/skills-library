# Source

- Repository: `gokapso/agent-skills`
- URL: https://github.com/gokapso/agent-skills
- Imported commit: `d0cdd934dcc1bc69e53dc3d042c08a1150abebc4`
- Upstream path: `skills/integrate-whatsapp`
- Local skill path: `05-development/integrate-whatsapp`
- License: not declared upstream
- Baseline verified: 2026-08-23

## What was imported

- `SKILL.md`
- `assets/` — 13 file(s): bundled assets
- `package.json`
- `references/` — 11 file(s): extended reference documents that the SKILL.md body links to
- `scripts/` — 52 file(s): helper scripts the skill invokes

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`.
Everything listed above lives inside that directory upstream, so it is owned by this
skill and travels with it.

Licensing caveat: the upstream repository declares no license, so no grant is on
record for this material. The copy predates this run; only the two reference files
were refreshed here. Flagged for the owner to decide whether to keep it.

## Update history

- 2026-08-23 — updated to `d0cdd934dcc1`. Documented the `whatsapp.contact.identity_changed` webhook and the `payload_version: v2` phone-number lifecycle events. Documentation only, no code.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

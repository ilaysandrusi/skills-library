# Source

- Repository: `expo/skills`
- URL: https://github.com/expo/skills
- Imported commit: `d0075ffa09928f1edb3e7ac4f5af07586d4b344d`
- Upstream path: `plugins/expo/skills/eas-simulator`
- Local skill path: `26-mobile-apple/eas-simulator`
- License: MIT
- Baseline verified: 2026-09-05

## What was imported

- `SKILL.md`
- `agents/` — 1 file(s)
- `references/` — 3 file(s)

## Ownership

Upstream ships its skills inside the `expo` plugin, one self-contained directory per skill under `plugins/expo/skills/`. Everything listed above lives inside that directory upstream. First-party: Expo documents its own tooling here.

## Update history

- 2026-09-05 — updated to `d0075ffa0992`, the skill's first recorded baseline. Expo retracted the warning that `eas-cli simulator:exec` strips `--flag` arguments: `simulator:exec` is `strict = false` and passes args verbatim, so the `sh -c` wrapper and `--args` JSON workaround are gone. Adds the native dev-client launch path on eas-cli ≥ 22.4.0 and reworks the troubleshooting notes.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

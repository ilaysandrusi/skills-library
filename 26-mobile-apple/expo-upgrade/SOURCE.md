# Source

- Repository: `expo/skills`
- URL: https://github.com/expo/skills
- Imported commit: `d0075ffa09928f1edb3e7ac4f5af07586d4b344d`
- Upstream path: `plugins/expo/skills/expo-upgrade`
- Local skill path: `26-mobile-apple/expo-upgrade`
- License: MIT
- Baseline verified: 2026-09-05

## What was imported

- `SKILL.md`
- `agents/` — 1 file(s)
- `references/` — 7 file(s)

## Ownership

Upstream ships its skills inside the `expo` plugin, one self-contained directory per skill under `plugins/expo/skills/`. Everything listed above lives inside that directory upstream. First-party: Expo documents its own tooling here.

## Update history

- 2026-09-05 — updated to `d0075ffa0992`, the skill's first recorded baseline. Corrects a step that could break a project: formerly implicit packages (`@babel/core`, `babel-preset-expo`, `expo-constants`) must now be reviewed individually instead of removed wholesale, `expo-constants` stays a direct dependency whenever `expo-router` is installed, and `npx expo-doctor` should run after any dependency removal.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

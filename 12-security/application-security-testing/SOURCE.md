# Source

- Repository: `usestrix/strix`
- URL: https://github.com/usestrix/strix
- Imported commit: `ff5c8cc8e46d8e60c2bc2439f7bcb07c05ca3db2`
- Upstream path: `skills/application-security-testing`
- Local skill path: `12-security/application-security-testing`
- License: Apache-2.0
- Imported: 2026-09-05

## What was imported

- `LICENSE`
- `SKILL.md`

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`.
These nine skills *drive* Strix rather than containing the engine. `LICENSE` is a
deliberate copy of the upstream repository-root Apache-2.0 licence.

Extracted from HEAD of `usestrix/strix` after a fresh Desktop clone. Not copied
from the whole-repo snapshot that previously sat at `12-security/strix`.

## What was deliberately not imported

The Strix application itself (the autonomous exploitation engine with a
shell tool, browser driver and intercepting proxy) was deliberately not imported.
That is executable offensive tooling, a class this archive has rejected before.
Install Strix from upstream if you need the engine; these skills only tell an
agent how to invoke it.

The documented `curl -sSL https://strix.ai/install | bash` is the official vendor
installer. It is recorded here rather than executed.

Every file in this directory except `SOURCE.md` and the copied root `LICENSE` was
compared to upstream HEAD by copy-from-clone; the commit above is that clone's HEAD.

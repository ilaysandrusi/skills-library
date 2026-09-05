# Source

- Repository: `hashicorp/agent-skills`
- URL: https://github.com/hashicorp/agent-skills
- Imported commit: `c2d65dfe492f74d360d35b859b88932222470bd8`
- Upstream path: `plugins/terraform/skills/terraform-policy`
- Local skill path: `13-cloud-deploy/terraform-policy`
- License: MPL-2.0
- Baseline verified: 2026-09-05

## What was imported

- `.gitignore`
- `README.md`
- `SKILL.md`
- `examples/` — 49 file(s)
- `references/` — 3 file(s)

## Ownership

Upstream ships its skills inside per-product plugins, one self-contained directory per skill under `plugins/terraform/skills/`. Everything listed above lives inside that directory upstream. First-party: HashiCorp documents its own tooling here.

## Update history

- 2026-09-05 — updated to `c2d65dfe492f`, the skill's first recorded baseline. Purely additive (62 insertions, 0 deletions): documents the `policy { required_providers { ... } }` block that `tfpolicy validate` requires from 0.2.0 onwards, and tells the agent to branch its guidance on the installed CLI version rather than assuming 0.2.0+.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

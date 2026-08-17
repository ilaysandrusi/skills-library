# Agents

Delegated sub-agent role prompts. Each file defines one specialist (reviewer, architect, analyst, …) that a coding agent can hand a task to.

**Total files:** 260 — from 19 source projects.

Every source folder carries a `SOURCE.md` with the upstream repository, path, pinned commit and license.

| Source folder | Files | Upstream repository | License |
|---|---|---|---|
| [`addyosmani/`](./addyosmani/) | 4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | MIT |
| [`alirezarezvani/`](./alirezarezvani/) | 33 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | MIT |
| [`auto-research-in-sleep/`](./auto-research-in-sleep/) | 2 | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | MIT |
| [`claude-bootstrap/`](./claude-bootstrap/) | 1 | [alinaqi/claude-bootstrap](https://github.com/alinaqi/claude-bootstrap) | MIT |
| [`claude-seo/`](./claude-seo/) | 18 | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | MIT |
| [`coderabbit/`](./coderabbit/) | 1 | [coderabbitai/skills](https://github.com/coderabbitai/skills) | MIT |
| [`context-engineering-kit/`](./context-engineering-kit/) | 23 | [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | GPL-3.0 |
| [`digital-marketing-pro/`](./digital-marketing-pro/) | 24 | [indranilbanerjee/digital-marketing-pro](https://github.com/indranilbanerjee/digital-marketing-pro) | MIT |
| [`ecc/`](./ecc/) | 68 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | MIT |
| [`infrasity-dev-gtm/`](./infrasity-dev-gtm/) | 23 | [infrasity-labs/dev-gtm-claude-skills](https://github.com/infrasity-labs/dev-gtm-claude-skills) | MIT |
| [`kreuzberg/`](./kreuzberg/) | 1 | [kreuzberg-dev/kreuzberg](https://github.com/kreuzberg-dev/kreuzberg) | MIT |
| [`microsoft/`](./microsoft/) | 6 | [microsoft/skills](https://github.com/microsoft/skills) | MIT |
| [`minimax/`](./minimax/) | 5 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MIT |
| [`sentry/`](./sentry/) | 2 | [getsentry/skills](https://github.com/getsentry/skills) | Apache-2.0 |
| [`trailofbits/`](./trailofbits/) | 30 | [trailofbits/skills](https://github.com/trailofbits/skills) | CC-BY-SA-4.0 |
| [`ui-ux-pro-max/`](./ui-ux-pro-max/) | 1 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT |
| [`understand-anything/`](./understand-anything/) | 10 | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) | MIT |
| [`vibe-skills/`](./vibe-skills/) | 7 | [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) | Apache-2.0 |
| [`zapier/`](./zapier/) | 1 | [zapier/zapier-mcp](https://github.com/zapier/zapier-mcp) | MIT |

> These are **not** skills. They are kept separate on purpose: an agent loads skills on demand, while rules are always on, commands are invoked explicitly, hooks run on runtime events and agents are delegated to. See [`../ARTIFACTS.md`](../ARTIFACTS.md).

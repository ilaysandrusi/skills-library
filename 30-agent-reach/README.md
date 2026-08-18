# 30 — Agent Reach

Source: [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) (MIT, ~72K stars)

Gives your AI agent "eyes" on the internet: read and search Twitter/X, Reddit, YouTube (transcripts), GitHub, web pages (Jina Reader), RSS, LinkedIn, Bilibili, XiaoHongShu and more — one CLI, zero API fees. It is a capability layer: it picks, installs, and health-checks the best backend per platform (`agent-reach doctor`).

## Contents

- `agent-reach/` — full project snapshot (Python CLI + skill files)
  - `agent-reach/agent_reach/skill/SKILL.md` — the skill file agents read (English version: `SKILL_en.md`)
  - `agent-reach/docs/install.md` — the official agent-driven install guide

## Install so it works in EVERY Cursor session (on your computer)

Two parts are needed on the local machine — the skill file (so the agent knows the commands) and the CLI itself (so the commands exist):

1. **Install the CLI** (one time):

```bash
pip install git+https://github.com/Panniantong/Agent-Reach
agent-reach install --env=auto        # safe check; add --system to auto-install missing tools
agent-reach doctor                    # see which channels are live
```

2. **Register the skill for Cursor** (user-level, applies to all projects):

```bash
mkdir -p ~/.cursor/skills
cp -r <this-repo>/30-agent-reach/agent-reach/agent_reach/skill ~/.cursor/skills/agent-reach
```

Cursor loads user-level skills from `~/.cursor/skills/` in every chat, so after this the agent will automatically know how to reach Twitter/YouTube/Reddit/etc. whenever relevant.

Alternatively, the fully automatic way — paste this single line to the agent in Cursor and let it do everything:

```
Help me install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

## Notes

- Zero-config channels out of the box: web pages, YouTube transcripts + search, RSS, GitHub (via `gh`), Bilibili search.
- Login-based channels (Twitter/X, Reddit, Instagram, Facebook, XiaoHongShu) need cookies/sessions — use a throwaway account, not your main one.
- Cloud Agents (like this one) run on fresh VMs; for the skill to work there too, add the `pip install` + skill copy to the environment's install script.

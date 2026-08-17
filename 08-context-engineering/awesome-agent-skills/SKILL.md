---
name: awesome-agent-skills
description: Discovery guide for finding new agent skills on the internet. Use when the user wants to find, browse, or install new skills for their agent — e.g. "find a skill for X," "is there a skill that does Y," "what skills exist for marketing/design/testing," "add more skills to my library," or "where can I get official skills from Anthropic/Vercel/Stripe/Cloudflare." Points to curated, hand-picked skill collections (1400+ skills) from leading teams and the community, with install paths per agent (Claude Code, Cursor, Codex, Gemini CLI, and more).
---

# Awesome Agent Skills — Discovery Guide

This skill wraps the [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) curated list — a hand-picked directory of 1400+ real-world Agent Skills from teams like Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, and Figma, plus community collections.

## When to use

- The user asks to find a skill for a specific task that this library doesn't cover.
- The user wants to expand the skills library with new categories or sources.
- You need to check whether an official first-party skill exists (e.g. Stripe for payments, Sentry for error monitoring) before writing one from scratch.

## How to use

1. Read `references/awesome-agent-skills-readme.md` — it is the full curated index, organized by publisher and by topic.
2. Search it for the relevant keyword (e.g. `rg -i "stripe" references/awesome-agent-skills-readme.md`).
3. Each entry links to the source repository and the path of the skill inside it. Clone the repo (shallow) and copy the skill folder into the right category in this library.
4. After installing, update `catalog.json`, the root `README.md` index, and the category `README.md` — keep the counts accurate.

## Freshness

The bundled reference is a snapshot. For the latest list, fetch the live README from the GitHub repo — the collection is updated frequently.

# Source

- Repository: `google-gemini/gemini-skills`
- URL: https://github.com/google-gemini/gemini-skills
- Imported commit: `e2e931ffd78c503f2a9ad848152e561c8f4e1ea8`
- Upstream path: `skills/gemini-omni-flash-api`
- Local skill path: `16-ai-apis-media/gemini-omni-flash-api`
- License: Apache-2.0
- Baseline verified: 2026-09-05

## What was imported

- `SKILL.md`
- `scripts/` — 4 file(s)

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/`, including the `scripts/` the skill runs. First-party: Google documents its own Gemini API here.

## Update history

- 2026-09-05 — updated to `e2e931ffd78c`, the skill's first recorded baseline. Taken for its security hardening: `scripts/upload_file.py` drops the `--api-key` command-line argument (a key passed as an argv is visible in shell history and the process table) and now reads `GEMINI_API_KEY` from the environment only, and both it and `scripts/video/generate_video.py` gain a `sanitize_error()` pass that redacts API keys, OAuth and Bearer tokens, sensitive URL query parameters, internal Google hosts and raw response bodies before any error text is printed.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

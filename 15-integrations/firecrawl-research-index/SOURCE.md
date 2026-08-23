# Source

- Repository: `firecrawl/skills`
- URL: https://github.com/firecrawl/skills
- Imported commit: `8b18f3b161ff3081e8dc8417dcdc8cb24aa0fd9e`
- Upstream path: `skills/core/firecrawl-research-index`
- Local skill path: `15-integrations/firecrawl-research-index`
- License: ISC
- Baseline verified: 2026-08-23

## What was imported

- `SKILL.md`

## Ownership

Upstream publishes each skill as a self-contained directory under `skills/core/`.
This skill is a single `SKILL.md` upstream and here, so there are no supporting files
to assign. First-party: Firecrawl documents its own index API and CLI here.

Identified as the same skill rather than a same-name coincidence with
`tools/check-upstream.py --probe-frontmatter`: a single-file skill whose one file changed
reports as `unmatched-candidate`, because one changed file means zero matched files, so
the frontmatter had to settle it. Both sides agree on `name`, and the body opens
identically.

## Update history

- 2026-08-23 — updated to `8b18f3b161ff`. Typo fix ("sturctural" → "structural") and a markdown emphasis change (`*x*` → `_x_`).
Small, but a real upstream correction.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

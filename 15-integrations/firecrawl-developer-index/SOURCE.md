# Source

- Repository: `firecrawl/skills`
- URL: https://github.com/firecrawl/skills
- Imported commit: `8b18f3b161ff3081e8dc8417dcdc8cb24aa0fd9e`
- Upstream path: `skills/core/firecrawl-developer-index`
- Local skill path: `15-integrations/firecrawl-developer-index`
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

- 2026-08-23 — updated to `8b18f3b161ff`. Upstream corrected the documented API surface: `--skills-only` is no longer a CLI
flag (`skills="only"` is HTTP/MCP only), results no longer carry a `type` field (the
artifact kind is the `id` prefix), and the `coverage` object is gone from the response.
The local copy documented all three, so this is a compatibility fix, not a rewording.
The upstream `description` was also shortened; `catalog.json` and the category README
keep their existing description, per the rule that index rows are never regenerated
from frontmatter.

Every file in this directory was compared to upstream by git blob SHA and matched,
so the commit above is a verified baseline rather than an assumption.

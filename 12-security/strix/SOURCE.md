# Source

- Repository: `usestrix/strix`
- URL: https://github.com/usestrix/strix
- Upstream path: repository root (whole-repo clone)
- Imported commit: `a5856108a7c628cf45cf2231692271f20ae136b5` (2026-08-26)
- Baseline: **proven**. All 467 local files are blob-identical to that commit.
- License: Apache-2.0
- Local path: `12-security/strix`
- Imported: 2026-08-26, commit `618c95be`

## Status — awaiting manual review, not a catalogued skill

A **whole-repository clone**, not a skill package: no root `SKILL.md`, absent
from `catalog.json`, `SOURCES.json` and the category README, and the 2026-08-26
import wrote no `SOURCE.md` and recorded no security review. This file was added
on 2026-09-04 so the clone is traceable; the structural question is queued in
`UPDATE_CHECKS.json` under `review_queue.unindexed_whole_repo_clones`.

## What this repository actually is

Strix is an open-source **autonomous AI penetration-testing tool** (60k stars).
The repository is the Python application: `strix/` holds the agent engine, its
tool belt (`shell`, `agent_browser`, `proxy`, `apply_patch`, `threat_model`,
`reporting`, `web_search`), prompt templates, and a vulnerability knowledge base
under `strix/skills/`.

Nine `SKILL.md` files are present, none of them indexed:

- `skills/` (repo level, 9 skills): `penetration-testing-with-strix`,
  `managed-pentesting-with-strix`, `fix-security-vulnerabilities-with-strix`,
  `ci-security-scanning-with-strix`, `application-security-testing`,
  `api-security-testing`, `web-app-penetration-testing`,
  `owasp-top-10-testing`, `find-security-vulnerabilities-in-code`.

These skills *drive* Strix; they are not Strix. That distinction is the whole
question below.

## Security review (2026-09-04, first review of this import)

Strix is a reputable, widely used tool and nothing here is disguised or
malicious. The concern is category, not trust:

- The clone contains **executable offensive tooling** — an agent engine whose
  stated purpose is to exploit a target and prove the exploit, with a shell
  tool, a browser driver and an intercepting proxy. Comparable executable attack
  tooling has been rejected from this library before (Trail of Bits Burp/APK
  helpers, `elementalsouls/Claude-BugHunter`).
- `strix/skills/vulnerabilities/rce.md` documents payload patterns including
  `echo payload | base64 -d | sh`. This is the standing malware sweep's only hit
  in the whole repository. In context it is dual-use *knowledge* in a
  vulnerability reference, which the archive accepts — but it is worth knowing
  that the sweep will keep flagging it.
- No committed secrets. `uv.lock` accounts for the ~1500
  `files.pythonhosted.org` references (dependency hashes, normal). Network hosts
  otherwise are `strix.ai` / `app.strix.ai` (the vendor's own managed API),
  `127.0.0.1`, and `example.com` / `target.tld` placeholders in docs.
- The CLI runs targets inside a Docker sandbox with the user's own LLM key. The
  managed path sends the target to `app.strix.ai`, which is the documented
  product behaviour, not covert egress.

**Nothing in this clone should be executed from the archive.**

## Recommendation

Keep the 9 skills that drive Strix — they are legitimate defensive-testing
skills for the owner's own applications and fit `12-security`. Leave the engine
upstream, which is the call already made for `15-integrations/hey`
(Basecamp's Go application) and `02-design-ui/superdesign` (the `dsh` CLI): the
product a skill drives is not material the skill owns. Nine resources plus the
removal of the application is a structural rewrite that needs a human decision.

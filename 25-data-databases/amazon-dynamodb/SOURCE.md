# Source

- **Skill:** `amazon-dynamodb`
- **Origin:** Official AWS Agent Toolkit (AWS-supported skills for AI agents)
- **Repository:** https://github.com/aws/agent-toolkit-for-aws
- **Path:** `skills/specialized-skills/database-skills/amazon-dynamodb`
- **Commit:** `d6ad2e44d5e3077b85b63f322e007c84f94f3a6c`
- **Discovered:** 2026-08-18 daily skills-library maintenance
- **License:** Apache License 2.0 (see upstream `LICENSE`)
- **Why included:** First-party, AWS-maintained deep-dive skill from the official AWS agent toolkit. Complements the broad `aws-*` core skills already in the library with service-level, reference-backed guidance (design axioms, runbooks, troubleshooting tables, ready-to-use templates and scripts).

## Baseline

Verified on 2026-08-22 by comparing the git blob SHA of every local file against
the upstream tree at `d6ad2e44`: all files match, so this copy is exactly that
commit.

## Update history

- **2026-08-22** — updated from `3cba90bc` to `d6ad2e44`, the upstream `version: 1`
  → `version: 2` release. Adds DynamoDB vector search: a new
  `references/vector-search.md`, `SearchVectors` coverage in the skill
  description, and a guardrail section explaining that the skill resolves its own
  bundled files differently when loaded over the AWS MCP `retrieve_skill` tool
  than when installed locally. The five `scripts/*.py` were substantially
  rewritten upstream; reviewed for egress before applying — they reach only AWS
  APIs through boto3 and the ambient credential chain, and the only URLs anywhere
  in the package are `aws.amazon.com` documentation links.

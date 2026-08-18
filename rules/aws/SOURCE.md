# Source: aws/agent-toolkit-for-aws

- Repository: https://github.com/aws/agent-toolkit-for-aws
- Upstream path(s): `rules/aws-agent-rules.md`
- Commit pinned at import: `3cba90bc8ecf1c98ff817896806a8660b2b22b6a` (branch `main`)
- License: Apache-2.0
- Files here: 1

Always-on house rules for agents working against AWS: prefer the AWS MCP server over raw
CLI, load the matching AWS skill before starting, verify API parameters and limits against
documentation instead of guessing, prefer CDK/CloudFormation over ad-hoc CLI calls, and a
"Secret Safety" section that forbids reading secret values directly.

The companion `rules/aws-starter-rules.md` was not imported: it only applies to accounts on
one specific AWS signup tier and is not reusable guidance.

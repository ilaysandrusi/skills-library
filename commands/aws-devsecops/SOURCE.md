# Source: aws/agent-toolkit-for-aws

- Repository: https://github.com/aws/agent-toolkit-for-aws
- Upstream path(s): `plugins/aws-agents-for-devsecops/commands/`
- Commit pinned at import: `3cba90bc8ecf1c98ff817896806a8660b2b22b6a` (branch `main`)
- License: Apache-2.0
- Files here: 8

Slash commands for the official AWS DevSecOps plugin: `/chat`, `/cost`, `/investigate`,
`/release-readiness`, `/release-testing`, `/spaces` and the two setup commands. They stay
shared because the upstream plugin ships 13 skills and every command dispatches into one
of them, so no single skill owns them.

The upstream `setup.md` command was not imported: it only chains the trivial `setup`
meta-skill, which was skipped as a five-line wrapper around `setup-devops-agent` and
`setup-security-agent` (both imported into the library).

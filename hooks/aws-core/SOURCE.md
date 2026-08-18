# Source: aws/agent-toolkit-for-aws

- Repository: https://github.com/aws/agent-toolkit-for-aws
- Upstream path(s): `plugins/aws-core/com.anthropic.claude-code/hooks/`
- Commit pinned at import: `3cba90bc8ecf1c98ff817896806a8660b2b22b6a` (branch `main`)
- License: Apache-2.0
- Files here: 2

A defensive `PreToolUse` hook. `secret-safety.py` reads the pending tool call from stdin
and denies it when it would pull a plaintext secret out of AWS Secrets Manager —
`get-secret-value` / `batch-get-secret-value` in any casing, the SDK call shapes for
boto3 and the JS v3 client, and direct hits on the Secrets Manager Agent daemon on
`localhost:2773`. The point is to keep secret values from ever entering the agent's
context; the skill guidance routes callers to
`{{resolve:secretsmanager:...}}` with `asm-exec` instead.

The hook only inspects and denies. It performs no network calls and writes nothing.

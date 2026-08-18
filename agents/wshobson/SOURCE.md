# Source: wshobson/agents

- Repository: https://github.com/wshobson/agents
- Upstream path(s): `plugins/*/agents/`
- Commit pinned at import: `d6837ae274c2cd817acad3fb98f193a4390a4c3e` (branch `main`)
- License: MIT
- Files here: 142

The largest sub-agent collection in the library: language specialists (`python-pro`,
`rust-pro`, `golang-pro`, `typescript-pro`, `java-pro`, `elixir-pro`, `haskell-pro`,
`scala-pro`, `csharp-pro`, `cpp-pro`, `c-pro`, `php-pro`, `ruby-pro`, `julia-pro`,
`bash-pro`, `posix-shell-pro`, `sql-pro`), architecture and review roles
(`backend-architect`, `architect-review`, `code-reviewer`, `security-auditor`, the four
C4 model agents), infrastructure (`kubernetes-architect`, `terraform-specialist`,
`cloud-architect`, `deployment-engineer`, `network-engineer`, `service-mesh-expert`),
data and ML (`data-engineer`, `ml-engineer`, `mlops-engineer`, `vector-database-engineer`,
the three LLM-finetuning roles), QA and debugging (`test-automator`, `tdd-orchestrator`,
`debugger`, `error-detective`, `incident-responder`), plus documentation, SEO, design
and orchestration roles.

## De-duplication

Upstream distributes the same agent into every plugin that needs it, so 195 in-scope
files hold only 130 distinct agents — the copies differ solely in the plugin-scoped
`name:` line. Files were grouped by (filename, body-with-`name:`-masked). The dominant
body for each agent is stored under the bare agent name; a genuinely different agent that
happens to share a filename keeps its plugin prefix, which is why you will find both
`debugger.md` and `incident-response-debugger.md` here. `name:` was rewritten to match
the filename so the two never disagree. That is the only content change. The six
`ship-mate` pipeline agents were prefixed because bare `architect`, `implement`, `qa`,
`review`, `orchestrate` and `playwright` mean nothing outside that pipeline.

## Not imported

- `quantitative-trading` (`quant-analyst`, `risk-manager`) and `hr-legal-compliance`
  (`hr-pro`, `legal-advisor`) — outside this library's scope.
- `protect-mcp` and `review-agent-governance` — their hooks run
  `npx protect-mcp@0.7.4` on every `PreToolUse` and `PostToolUse` event. Fetching and
  executing a third-party package on every single tool call is not something to ship by
  default, so the plugins were dropped whole rather than half-imported.

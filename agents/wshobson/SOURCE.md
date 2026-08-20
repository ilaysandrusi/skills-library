# Source: wshobson/agents

- Repository: https://github.com/wshobson/agents
- Upstream path(s): `plugins/*/agents/`
- Commit pinned at import: `d6837ae274c2cd817acad3fb98f193a4390a4c3e` (branch `main`)
- Commit of the 2026-08-20 top-up: `367cb6a4a182cf7e9b0a17c9429f7411ddd9cf35`
- License: MIT
- Files here: 146

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

## Added 2026-08-20

`quant-analyst`, `risk-manager`, `hr-pro` and `legal-advisor`. The first import left
them out as off-topic, but their plugins' skills are now archived here under
`18-finance-accounting` and `22-legal`/`12-security`, and both categories already carry
several hundred skills each. `legal-advisor` in particular is software work: privacy
policies, ToS, cookie consent and DPAs for a product. Leaving the matching agents
behind would have made those imports half-packages.

## Not imported

- `protect-mcp` and `review-agent-governance` — their hooks run
  `npx protect-mcp@0.7.4` on every `PreToolUse` and `PostToolUse` event. Fetching and
  executing a third-party package on every single tool call is not something to ship by
  default, so the plugins were dropped whole rather than half-imported.

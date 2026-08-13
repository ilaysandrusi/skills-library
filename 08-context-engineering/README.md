# Context Engineering

ניהול קונטקסט, סוכני משנה, חשיבה

**מספר סקילים:** 63

| סקיל | מה הוא עושה |
|---|---|
| `actualize` | Reconcile the project's FPF state with recent repository changes |
| `add-task` | creates draft task file in .specs/tasks/draft/ with original user intent |
| `agent-evaluation` | Evaluate and improve Claude Code commands, skills, and agents. Use when testing prompt effectiveness, validating context engineering choices, or measuring improvement quality. |
| `analyse` | Auto-selects best Kaizen method (Gemba Walk, Value Stream, or Muda) for target |
| `analyse-problem` | Comprehensive A3 one-page problem analysis with root cause and action plan |
| `analyze-issue` | Analyze a GitHub issue and create a detailed technical specification |
| `attach-review-to-pr` | Add line-specific review comments to pull requests using GitHub CLI API |
| `brainstorm` | Use when creating or developing, before writing code or implementation plans - refines rough ideas into fully-formed designs through collaborative questioning, alternative exploration, and incremental validation. Don't use during clear 'mechanical' processes |
| `build-mcp` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). |
| `cause-and-effect` | Systematic Fishbone analysis exploring problem causes across six categories |
| `commit` | Create well-formatted commits with conventional commit messages and emoji |
| `context-engineering` | Understand the components, mechanics, and constraints of context in agent systems. Use when writing, editing, or optimizing commands, skills, or sub-agents prompts. |
| `create-agent` | Comprehensive guide for creating Claude Code agents with proper structure, triggering conditions, system prompts, and validation - combines official Anthropic best practices with proven patterns |
| `create-command` | Interactive assistant for creating new Claude commands with proper structure, patterns, and MCP tool integration |
| `create-hook` | Create and configure git hooks with intelligent project analysis, suggestions, and automated testing |
| `create-ideas` | Generate ideas in one shot using creative sampling |
| `create-pr` | Create pull requests using GitHub CLI with proper templates and formatting |
| `create-rule` | Use when found gap or repetative issue, that produced by you or implemenataion agent. Esentially use it each time when you say "You absolutly right, I should have done it differently." -> need create rule for this issue so it not appears again. |
| `create-skill` | Guide for creating effective skills. This command should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. Use when creating new skills, editing existing skills, or verifying skills work before deployment - applies TDD to process documentation by testing with subagents before writing, iterating until bulletproof against rationalization |
| `create-workflow-command` | Create a workflow command that orchestrates multi-step execution through sub-agents with file-based task prompts |
| `critique` | Comprehensive multi-perspective review using specialized judges with debate and consensus building |
| `decay` | Manage evidence freshness by identifying stale decisions and providing governance actions |
| `design-testing-strategy` | Use before writing any type of tests. Distills 14 industry sources into deterministic decision gates, schemas, and worked test examples. |
| `do-and-judge` | Execute a task with sub-agent implementation and LLM-as-a-judge verification with automatic retry loop |
| `do-competitively` | Execute tasks through competitive multi-agent generation, meta-judge evaluation specification, multi-judge evaluation, and evidence-based synthesis |
| `do-in-parallel` | Run independent tasks concurrently across multiple files or targets using parallel sub-agents, with per-task model selection and LLM-as-a-judge verification. Use when tasks do not depend on each other and can run side by side. |
| `do-in-steps` | Execute one complex task as ordered, dependent steps run sequentially, passing context from each step to the next, with per-step LLM-as-a-judge verification. Use when later steps depend on the results of earlier ones. |
| `git-notes` | Use when adding metadata to commits without changing history, tracking review status, test results, code quality annotations, or supplementing commit messages post-hoc - provides git notes commands and patterns for attaching non-invasive metadata to Git objects. |
| `git-worktrees` | Use when working on multiple branches simultaneously, context switching without stashing, reviewing PRs while developing, testing in isolation, or comparing implementations across branches - provides git worktree commands and workflow patterns for parallel development with multiple working directories. |
| `implement-task` | Implement a task with automated LLM-as-Judge verification per step |
| `judge` | Launch a meta-judge then a judge sub-agent to evaluate results produced in the current conversation |
| `judge-with-debate` | Evaluate solutions through multi-round debate between independent judges until consensus |
| `kaizen` | Use when Code implementation and refactoring, architecturing or designing systems, process and workflow improvements, error handling and validation. Provide tehniquest to avoid over-engineering and apply iterative improvements. |
| `launch-sub-agent` | Launch an intelligent sub-agent with automatic model selection based on task complexity, specialized agent matching, Zero-shot CoT reasoning, and mandatory self-critique verification |
| `load-issues` | Load all open issues from GitHub and save them as markdown files |
| `load-pr-comments` | Use to load open/unresolved PR review comments then aggregate them as tasks in .specs/comments/*.md for parallel agents to fix. |
| `memorize` | Curates insights from reflections and critiques into CLAUDE.md using Agentic Context Engineering |
| `multi-agent-patterns` | Design multi-agent architectures for complex tasks. Use when single-agent context limits are exceeded, when tasks decompose naturally into subtasks, or when specializing agents improves quality. |
| `plan-do-check-act` | Iterative PDCA cycle for systematic experimentation and continuous improvement |
| `plan-task` | Refine, parallelize, and verify a draft task specification into a fully planned implementation-ready task |
| `prompt-engineering` | Use this skill when you writing commands, hooks, skills for Agent, or prompts for sub agents or any other LLM interaction, including optimizing prompts, improving LLM outputs, or designing production prompt templates. |
| `propose-hypotheses` | Execute complete FPF cycle from hypothesis generation to decision |
| `query` | Search the FPF knowledge base and display hypothesis details with assurance information |
| `reflect` | Reflect on previus response and output, based on Self-refinement framework for iterative improvement with complexity triage and verification |
| `reset` | Reset the FPF reasoning cycle to start fresh |
| `resolve-fixed-pr-comments` | Verify what PR review comments have been addressed (committed/pushed OR uncommitted local changes) and resolve the threads that are genuinely fixed or no longer relevant. |
| `review-local-changes` | Review your local uncommitted working-tree changes (git diff plus untracked files) and return actionable improvement suggestions. Use before committing, when nothing has been pushed yet. |
| `review-pr` | Review an existing GitHub pull request and post inline review comments on its diff. Use when the changes are on an opened PR rather than your local working tree. |
| `root-cause-tracing` | Use when errors occur deep in execution and you need to trace back to find the original trigger - systematically traces bugs backward through call stack, adding instrumentation when needed, to identify source of invalid data or incorrect behavior |
| `setup-arxiv-mcp` | Guide for setup arXiv paper search MCP server using Docker MCP |
| `setup-codemap-cli` | Guide for setup Codemap CLI for intelligent codebase visualization and navigation |
| `setup-context7-mcp` | Guide for setup Context7 MCP server to load documentation for specific technologies. |
| `setup-serena-mcp` | Guide for setup Serena MCP server for semantic code retrieval and editing capabilities |
| `status` | Display the current state of the FPF knowledge base |
| `test-coverage` | Use after writing tests to assess coverage quality across structural, mutation, requirements, and API/integration dimensions; organized knowledge for choosing and interpreting coverage analyses. |
| `test-prompt` | Use when creating or editing any prompt (commands, hooks, skills, subagent instructions) to verify it produces desired behavior - applies RED-GREEN-REFACTOR cycle to prompt engineering using subagents for isolated testing |
| `test-skill` | Use when creating or editing skills, before deployment, to verify they work under pressure and resist rationalization - applies RED-GREEN-REFACTOR cycle to process documentation by running baseline without skill, writing to address failures, iterating to close loopholes |
| `thought-based-reasoning` | Use when tackling complex reasoning tasks requiring step-by-step logic, multi-step arithmetic, commonsense reasoning, symbolic manipulation, or problems where simple prompting fails - provides comprehensive guide to Chain-of-Thought and related prompting techniques (Zero-shot CoT, Self-Consistency, Tree of Thoughts, Least-to-Most, ReAct, PAL, Reflexion) with templates, decision matrices, and research-backed patterns |
| `traiage-review` | This skill should be used when need prioritize what changed code in repository human must review. |
| `tree-of-thoughts` | Execute tasks through systematic exploration, pruning, and expansion using Tree of Thoughts methodology with meta-judge evaluation specifications and multi-agent evaluation |
| `update-docs` | Update and maintain project documentation for local code changes using multi-agent workflow with tech-writer agents. Covers docs/, READMEs, JSDoc, and API documentation. |
| `why` | Iterative Five Whys root cause analysis drilling from symptoms to fundamentals |
| `write-tests` | Add missing test coverage for your local code changes by generating new test files (covers uncommitted and untracked changes, or the latest commit if everything is committed). Use when you want write tests for new logic or increase test coverage. |

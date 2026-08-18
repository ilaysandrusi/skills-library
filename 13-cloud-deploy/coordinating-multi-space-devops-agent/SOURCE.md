# Source

- **Skill:** `coordinating-multi-space-devops-agent`
- **Origin:** Official AWS Agent Toolkit — `aws-agents-for-devsecops` plugin
- **Repository:** https://github.com/aws/agent-toolkit-for-aws
- **Path:** `plugins/aws-agents-for-devsecops/skills/coordinating-multi-space-devops-agent`
- **Commit:** `3cba90bc8ecf1c98ff817896806a8660b2b22b6a`
- **Discovered:** 2026-08-18 daily skills-library maintenance
- **License:** Apache License 2.0 (see upstream `LICENSE`)
- **Why included:** First-party AWS DevSecOps workflow skill: pre-merge release-readiness review, automated release testing, incident root-cause investigation, code/diff security scanning, STRIDE threat modelling and finding remediation. Fills a gap the library only covered with third-party scanners.
- **Companion artifacts:** the plugin's shared slash commands live in [`commands/aws-devsecops/`](../../commands/aws-devsecops/); they serve all skills in this plugin, so they were not copied into any single skill.

# Complete repository snapshots

Each imported upstream is stored once at:

```text
repositories/<primary-category>/<owner>--<repo>/
```

The directory below that path is an unchanged snapshot of the recorded Git
commit. Library metadata is intentionally kept outside imported source trees:

- `REPOSITORIES.json` — source, revision, license, category, tags, uses,
  completeness, dependencies, and review status.
- `repository-manifests/` — expected mode, Git blob SHA, and size for every
  tracked file.
- `MAINTENANCE_STATE.json` — bounded migration and update queues.

Archived `AGENTS.md`, `SKILL.md`, hooks, workflows, and configuration files are
source material, not instructions for maintaining or running this library.
Snapshots are not installed or enabled automatically.

#!/usr/bin/env python3
"""Synchronize the gradual repository-migration inventory.

This tool only reads library-owned metadata. Imported repository instructions
are archive content and are never loaded or executed.
"""

import argparse
import collections
import datetime
import json
import os


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_PATH = os.path.join(ROOT, "MAINTENANCE_STATE.json")


def load_json(name, default=None):
    path = os.path.join(ROOT, name)
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def write_json_if_changed(path, payload):
    rendered = json.dumps(payload, ensure_ascii=False, indent=1) + "\n"
    current = ""
    if os.path.exists(path):
        with open(path, encoding="utf-8") as handle:
            current = handle.read()
    if current == rendered:
        return False
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(rendered)
    return True


def source_inventory(sources):
    paths = collections.defaultdict(list)
    categories = collections.defaultdict(collections.Counter)
    for path, record in sources["attribution"].items():
        category = path.split("/", 1)[0]
        for repo in record.get("sources") or []:
            paths[repo].append(path)
            categories[repo][category] += 1
    return paths, categories


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--material-change-date",
        default=None,
        help="YYYY-MM-DD; set only when this run made a material archive change",
    )
    args = parser.parse_args()

    sources = load_json("SOURCES.json")
    repository_index = load_json("REPOSITORIES.json", {"repositories": []})
    legacy_update_checks = load_json("UPDATE_CHECKS.json", {"checked": {}})
    previous = load_json("MAINTENANCE_STATE.json", {})
    paths, categories = source_inventory(sources)

    archived = {
        entry["source_repository"]: entry
        for entry in repository_index.get("repositories", [])
    }
    old_queue = {
        entry["source_repository"]: entry
        for entry in previous.get("migration_queue", [])
    }

    queue = []
    for repo, legacy_paths in paths.items():
        if repo in archived:
            continue
        category_counts = categories[repo]
        primary = sorted(
            category_counts,
            key=lambda category: (-category_counts[category], category),
        )[0]
        old = old_queue.get(repo, {})
        queue.append(
            {
                "source_repository": repo,
                "status": old.get("status", "queued-source-verification"),
                "primary_category_candidate": primary,
                "legacy_entries": len(legacy_paths),
                "category_counts": dict(
                    sorted(category_counts.items(), key=lambda item: item[0])
                ),
                "note": old.get(
                    "note",
                    "Verify the exact upstream identity and provenance before migration.",
                ),
            }
        )
    queue.sort(key=lambda item: (-item["legacy_entries"], item["source_repository"].lower()))

    mappings = {}
    completed = []
    upstream_checks = {}
    for repo, check in legacy_update_checks.get("checked", {}).items():
        result = check.get("result", {})
        unreachable = result.get("unreachable", 0) > 0
        checked_revision = check.get("candidate_commit") or check.get("verified_commit")
        upstream_checks[repo] = {
            "last_successful_check": None if unreachable else check.get("last_checked"),
            "last_attempt": check.get("last_checked"),
            "checked_revision": checked_revision,
            "verified_revision": check.get("verified_commit"),
            "result": result,
            "record_source": "UPDATE_CHECKS.json",
        }
        if checked_revision is None and not unreachable:
            upstream_checks[repo]["note"] = (
                "The legacy checker found drift or ambiguity but did not retain "
                "the candidate commit; recheck before migration."
            )
    for repo, metadata in sorted(archived.items()):
        legacy_paths = sorted(paths.get(repo, []))
        for legacy_path in legacy_paths:
            mappings[legacy_path] = metadata["local_path"]
        completed.append(
            {
                "source_repository": repo,
                "local_path": metadata["local_path"],
                "commit": metadata["commit"],
                "legacy_entries_linked": len(legacy_paths),
                "legacy_entries_retired": 0,
                "status": metadata["snapshot"]["status"],
            }
        )
        catalog_check = metadata.get("upstream_check", {})
        candidate_revision = catalog_check.get("candidate_revision", metadata["commit"])
        upstream_checks[repo] = {
            "last_successful_check": catalog_check.get(
                "last_successful_check",
                metadata["review"]["reviewed_on"],
            ),
            "last_attempt": catalog_check.get(
                "last_attempt",
                catalog_check.get(
                    "last_successful_check",
                    metadata["review"]["reviewed_on"],
                ),
            ),
            "checked_revision": candidate_revision,
            "verified_revision": metadata["commit"],
            "result": catalog_check.get("status", metadata["snapshot"]["status"]),
        }

    unresolved = previous.get(
        "unresolved_issues",
        [
            {
                "id": "ruflo-size-review",
                "source_record": "28-career-education-health/Vibe-Skills/THIRD_PARTY_LICENSES.md",
                "recorded_identity": "ruvnet/claude-flow",
                "verified_identity": "ruvnet/ruflo",
                "source_url": "https://github.com/ruvnet/ruflo",
                "checked_revision": "277c7bc03ad192eef6d6f57e59ab7bab69a5728d",
                "status": "deferred-size-and-security-review",
                "note": "The recorded GitHub repository redirects to ruvnet/ruflo. Its current tree has 5,628 blobs and about 82 MB of tracked content; a complete security and redistribution review is too large to combine safely with the initial model migration.",
            }
        ],
    )
    unresolved = [
        issue
        for issue in unresolved
        if not issue.get("id", "").startswith("upstream-unreachable:")
        and not (
            issue.get("id") == "ruflo-size-review"
            and issue.get("verified_identity") in archived
        )
    ]
    for repo, check in sorted(legacy_update_checks.get("checked", {}).items()):
        if check.get("result", {}).get("unreachable", 0) == 0:
            continue
        unresolved.append(
            {
                "id": f"upstream-unreachable:{repo}",
                "source_repository": repo,
                "last_attempt": check.get("last_checked"),
                "status": "source-unreachable",
                "note": check.get(
                    "note",
                    "The recorded upstream could not be read; preserve its legacy entries until the exact source identity is verified.",
                ),
            }
        )
    for issue in unresolved:
        if issue.get("id") == "ruflo-size-review":
            upstream_checks["ruvnet/ruflo"] = {
                "last_successful_check": issue.get(
                    "last_successful_check",
                    "2026-09-06",
                ),
                "last_attempt": issue.get(
                    "last_attempt",
                    issue.get("last_successful_check", "2026-09-06"),
                ),
                "checked_revision": issue.get(
                    "candidate_revision",
                    issue["checked_revision"],
                ),
                "verified_revision": issue.get(
                    "reviewed_revision",
                    issue["checked_revision"],
                ),
                "result": issue.get(
                    "status",
                    "identity-verified-migration-deferred",
                ),
                "record_source": issue["source_record"],
            }
    next_work = previous.get(
        "next_work_items",
        [
            "Review ruvnet/ruflo as a dedicated bounded migration; do not import a partial tree.",
            "Verify the next highest-impact queued source identity and license.",
            "Retire legacy skill copies only after content equivalence is documented, at no more than 10 entries per run.",
        ],
    )
    if "ruvnet/ruflo" in archived:
        next_work = [
            item
            for item in next_work
            if not item.startswith(
                "Review ruvnet/ruflo as a dedicated bounded migration"
            )
        ]

    state = {
        "schema_version": 1,
        "last_material_change": args.material_change_date
        or previous.get("last_material_change")
        or datetime.date.today().isoformat(),
        "migration_limits": {
            "upstream_repositories_per_run": 2,
            "legacy_entries_retired_per_run": 10,
            "upstream_checks_per_run": 5,
        },
        "progress": {
            "cataloged_repositories": len(archived),
            "completed_migrations": len(completed),
            "queued_source_repositories": len(queue),
            "legacy_source_repositories": len(paths),
            "legacy_entries_mapped": len(mappings),
            "legacy_entries_total": len(sources["attribution"]),
            "upstream_sources_with_checks": len(upstream_checks),
            "upstream_sources_with_verified_revisions": sum(
                1 for check in upstream_checks.values() if check.get("checked_revision")
            ),
        },
        "migration_queue": queue,
        "completed_migrations": completed,
        "legacy_to_repository_mappings": dict(sorted(mappings.items())),
        "upstream_checks": dict(sorted(upstream_checks.items())),
        "unresolved_issues": unresolved,
        "next_work_items": next_work,
    }
    changed = write_json_if_changed(STATE_PATH, state)
    print(
        json.dumps(
            {
                "changed": changed,
                "queued": len(queue),
                "completed": len(completed),
                "legacy_entries_mapped": len(mappings),
            }
        )
    )


if __name__ == "__main__":
    main()

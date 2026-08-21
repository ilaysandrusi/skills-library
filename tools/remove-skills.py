#!/usr/bin/env python3
"""Retire skill directories and drop them from every index.

    python3 tools/remove-skills.py <spec.json> --reason <text> [--keep-files] [--check]

`spec.json` is a list of `{"category": "12-security", "slug": "malicious-skill"}`
objects. The script deletes each directory and removes it from `catalog.json`,
the category README table, the root README counts and `SOURCES.json`.

This is the counterpart of `index-skills.py` and follows the same rule: every
index row that is not being retired is copied through byte-for-byte. A full
regeneration would silently rewrite thousands of unrelated entries, because a
handful of the original descriptions cannot be reproduced from their
frontmatter.

`catalog.json` is keyed on the folder name — `validate-catalog.mjs` resolves an
entry to `<category>/<name>/SKILL.md` — so a catalog entry is matched by slug.
Removing something that is not indexed, or that is indexed more than once, is an
error rather than a silent no-op.

Pass `--check` to report what would be removed without touching anything, and
`--keep-files` to unindex a directory that should stay on disk.
"""
import argparse
import datetime
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROW_RE = re.compile(r"^\| \[`([^`]+)`\]")
COUNT_RE = re.compile(r"\*\*מספר סקילים:\*\*\s*\d+")
MAX_AUTOMATIC_REMOVALS = 10


def write_json(path, payload):
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=1)
        handle.write("\n")


def skill_folders(category):
    directory = os.path.join(ROOT, category)
    return sorted(
        (
            name
            for name in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, name, "SKILL.md"))
        ),
        key=str.lower,
    )


def drop_directories(entries, check):
    for category, slug in entries:
        directory = os.path.join(ROOT, category, slug)
        if not os.path.isdir(directory):
            sys.exit(f"{category}/{slug} is not a directory")
        if not check:
            shutil.rmtree(directory)


def update_catalog(entries, check):
    path = os.path.join(ROOT, "catalog.json")
    catalog = json.load(open(path, encoding="utf-8"))
    by_id = {category["id"]: category for category in catalog["categories"]}
    removed = 0
    for category, slug in entries:
        if category not in by_id:
            sys.exit(f"{category} is not a catalog category")
        skills = by_id[category]["skills"]
        matches = [skill for skill in skills if skill["name"] == slug]
        if len(matches) != 1:
            sys.exit(f"{category}/{slug} has {len(matches)} catalog entries, expected 1")
        skills.remove(matches[0])
        removed += 1
    catalog["total"] = sum(len(c["skills"]) for c in catalog["categories"])
    if not check:
        write_json(path, catalog)
    return removed, catalog["total"]


def update_category_readme(category, retired, check):
    """Rewrite the table from the folders that survive, keeping their rows verbatim."""
    path = os.path.join(ROOT, category, "README.md")
    lines = open(path, encoding="utf-8").read().split("\n")
    existing = {}
    for line in lines:
        match = ROW_RE.match(line)
        if match:
            existing[match.group(1)] = line

    folders = [f for f in skill_folders(category) if f not in retired]
    missing = [f for f in folders if f not in existing]
    if missing:
        sys.exit(f"{category}/README.md has no row for {', '.join(missing)}; "
                 "run index-skills.py first")
    rows = [existing[folder] for folder in folders]

    output, in_table, written = [], False, False
    for line in lines:
        if COUNT_RE.match(line):
            output.append(f"**מספר סקילים:** {len(folders)}")
            continue
        if line.startswith("|---"):
            output.append(line)
            in_table = True
            continue
        if in_table and line.startswith("|"):
            if not written:
                output.extend(rows)
                written = True
            continue
        if in_table and not line.startswith("|"):
            in_table = False
        output.append(line)
    if not written:
        sys.exit(f"could not locate the skill table in {path}")
    if not check:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write("\n".join(output))
    return len(folders)


def update_root_readme(counts, total, check):
    path = os.path.join(ROOT, "README.md")
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"\*\*סה״כ סקילים:\*\* \d+", f"**סה״כ סקילים:** {total}", text, count=1)
    for category, count in counts.items():
        text = re.sub(
            r"(\]\(\./" + re.escape(category) + r"/\) \| )\d+( \|)",
            lambda match: match.group(1) + str(count) + match.group(2),
            text,
        )
    if not check:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)


def update_sources(entries, check):
    path = os.path.join(ROOT, "SOURCES.json")
    data = json.load(open(path, encoding="utf-8"))
    attribution = data["attribution"]
    for category, slug in entries:
        attribution.pop(f"{category}/{slug}", None)
    counts = {}
    for record in attribution.values():
        for repo in record.get("sources") or []:
            counts[repo] = counts.get(repo, 0) + 1
    data["skills"] = len(attribution)
    data["traced_to_source_repo"] = sum(1 for r in attribution.values() if r.get("sources"))
    data["distinct_source_repos"] = len(counts)
    data["source_repo_skill_counts"] = dict(
        sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    )
    if not check:
        write_json(path, data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", help="JSON list of {category, slug} objects")
    parser.add_argument("--reason", required=True,
                        help="why these are being retired, for the commit message")
    parser.add_argument("--keep-files", action="store_true",
                        help="only unindex; leave the directories on disk")
    parser.add_argument("--check", action="store_true", help="report without writing")
    parser.add_argument("--allow-mass-removal", action="store_true",
                        help=f"permit more than {MAX_AUTOMATIC_REMOVALS} removals in one run")
    args = parser.parse_args()

    entries = []
    for item in json.load(open(args.spec, encoding="utf-8")):
        entries.append((item["category"], item["slug"]))
    if len(entries) != len(set(entries)):
        sys.exit("the spec lists the same skill twice")
    if len(entries) > MAX_AUTOMATIC_REMOVALS and not args.allow_mass_removal:
        sys.exit(f"{len(entries)} removals exceeds the {MAX_AUTOMATIC_REMOVALS} allowed "
                 "without --allow-mass-removal; send this batch to manual review")

    removed, total = update_catalog(entries, args.check)
    if not args.keep_files:
        drop_directories(entries, args.check)
    retired = {
        category: {slug for c, slug in entries if c == category}
        for category in {entry[0] for entry in entries}
    }
    counts = {
        category: update_category_readme(category, retired[category], args.check)
        for category in sorted(retired)
    }
    update_root_readme(counts, total, args.check)
    update_sources(entries, args.check)
    print(json.dumps({
        "removed": removed,
        "total": total,
        "categories": counts,
        "reason": args.reason,
        "checked_on": datetime.date.today().isoformat(),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

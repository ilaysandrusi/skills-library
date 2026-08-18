#!/usr/bin/env python3
"""Register newly copied skill directories in every index.

    python3 tools/index-skills.py <spec.json> --source <repo> --note <text> [--check]

`spec.json` is a list of `{"category": "13-cloud-deploy", "slug": "aws-lambda"}`
objects for skill directories that are already on disk. The script appends them
to `catalog.json`, the category README tables, the root README counts and
`SOURCES.json`, then leaves everything else byte-for-byte untouched.

That last property is the whole point. The original indexes were generated
without a YAML parser, so a handful of descriptions cannot be reproduced from
their frontmatter, and a full regeneration silently rewrites thousands of
unrelated entries. Existing rows are therefore copied through verbatim and only
missing ones are rendered.

The formatting rules below were recovered from the existing files and have to
stay exactly as they are:

- `catalog.json` and `SOURCES.json` use `indent=1`, `ensure_ascii=False` and a
  trailing newline.
- Catalog entries are keyed on the frontmatter `name`, which differs from the
  folder name for roughly 700 skills, and sort case-insensitively.
- Category README rows are `| [`slug`](./slug/SKILL.md) | description |`, sorted
  case-insensitively by folder name, with the description collapsed to one line
  and cut at the last word boundary before 300 characters, trailing `,;:`
  stripped, then `…` appended.

Pass `--check` to verify the indexes against the working tree without writing.
"""
import argparse
import bisect
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROW_RE = re.compile(r"^\| \[`([^`]+)`\]")
COUNT_RE = re.compile(r"\*\*מספר סקילים:\*\*\s*\d+")


def load_frontmatter(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    try:
        import yaml
    except ImportError:
        return _parse_frontmatter(block)
    try:
        data = yaml.safe_load(block)
    except Exception:
        return _parse_frontmatter(block)
    return data if isinstance(data, dict) else _parse_frontmatter(block)


def _parse_frontmatter(block):
    """Minimal fallback for machines without PyYAML: top-level scalars and
    `>`/`|` block scalars, which is everything a SKILL.md header uses."""
    fields, key, buffer = {}, None, []
    for line in block.split("\n"):
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if match and not line.startswith((" ", "\t")):
            if key:
                fields[key] = " ".join(buffer).strip()
            key, value = match.group(1), match.group(2).strip()
            buffer = [] if value in (">", ">-", "|", "|-") else [value]
        elif key and line.strip():
            buffer.append(line.strip())
    if key:
        fields[key] = " ".join(buffer).strip()
    return fields


def collapse(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def truncate(description):
    if len(description) <= 300:
        return description
    trimmed = description[:300]
    cut = trimmed.rfind(" ")
    return (trimmed[:cut] if cut > 0 else trimmed).rstrip(" ,;:") + "…"


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


def write_json(path, payload):
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=1)
        handle.write("\n")


def update_catalog(entries, check):
    path = os.path.join(ROOT, "catalog.json")
    catalog = json.load(open(path, encoding="utf-8"))
    by_id = {category["id"]: category for category in catalog["categories"]}
    added = 0
    for category, _folder, name, description in entries:
        skills = by_id[category]["skills"]
        if any(skill["name"] == name for skill in skills):
            continue
        keys = [skill["name"].lower() for skill in skills]
        skills.insert(bisect.bisect_left(keys, name.lower()),
                      {"name": name, "description": description})
        added += 1
    catalog["total"] = sum(len(c["skills"]) for c in catalog["categories"])
    if not check:
        write_json(path, catalog)
    return added, catalog["total"]


def update_category_readme(category, check):
    path = os.path.join(ROOT, category, "README.md")
    lines = open(path, encoding="utf-8").read().split("\n")
    existing = {}
    for line in lines:
        match = ROW_RE.match(line)
        if match:
            existing[match.group(1)] = line

    folders = skill_folders(category)
    rows = []
    for folder in folders:
        if folder in existing:
            rows.append(existing[folder])
            continue
        frontmatter = load_frontmatter(os.path.join(ROOT, category, folder, "SKILL.md"))
        description = collapse(frontmatter.get("description"))
        if not description:
            sys.exit(f"no description could be parsed for {category}/{folder}")
        description = truncate(description).replace("|", "\\|")
        rows.append(f"| [`{folder}`](./{folder}/SKILL.md) | {description} |")

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


def update_sources(entries, source, note, added_in, check):
    path = os.path.join(ROOT, "SOURCES.json")
    data = json.load(open(path, encoding="utf-8"))
    attribution = data["attribution"]
    for category, folder, _name, _description in entries:
        key = f"{category}/{folder}"
        attribution[key] = {
            "skill": key,
            "sources": [source],
            "method": "direct-import",
            "added_in": added_in,
            "import_note": note,
        }
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
    parser.add_argument("--source", required=True, help="upstream repo, e.g. owner/name")
    parser.add_argument("--note", required=True, help="import note stored in SOURCES.json")
    parser.add_argument("--added-in", default=datetime.date.today().isoformat(),
                        help="commit sha or date recorded on each attribution record")
    parser.add_argument("--check", action="store_true", help="report without writing")
    args = parser.parse_args()

    entries = []
    for item in json.load(open(args.spec, encoding="utf-8")):
        category, folder = item["category"], item["slug"]
        frontmatter = load_frontmatter(os.path.join(ROOT, category, folder, "SKILL.md"))
        entries.append((
            category,
            folder,
            frontmatter.get("name") or folder,
            collapse(frontmatter.get("description")),
        ))

    added, total = update_catalog(entries, args.check)
    counts = {
        category: update_category_readme(category, args.check)
        for category in sorted({entry[0] for entry in entries})
    }
    update_root_readme(counts, total, args.check)
    update_sources(entries, args.source, args.note, args.added_in, args.check)
    print(json.dumps({"added": added, "total": total, "categories": counts}, indent=2))


if __name__ == "__main__":
    main()

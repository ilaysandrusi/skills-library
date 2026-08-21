#!/usr/bin/env python3
"""Compare locally archived skills against their upstream repository at HEAD.

    python3 tools/check-upstream.py <owner/repo> [--json]

Reads `SOURCES.json` for every skill attributed to that repository, fetches the
upstream tree at the default branch, and compares each local file to upstream by
**git blob SHA**. That is the point of the script: a blob SHA is exact, so when
every file in a skill matches, the local copy is provably that commit rather than
an approximation, and the commit can be recorded as a real baseline.

Most of the library was imported without an `Imported commit`, so this is how a
baseline gets established after the fact. Where files disagree, the report names
them, which separates "upstream changed this skill" from "upstream changed
something else in the repository".

Statuses per skill:

- `identical`             every file matches upstream; the baseline is HEAD
- `upstream-added-files`  local files all match, upstream has extra files
- `drift`                 some files differ or are missing upstream
- `no-upstream-path`      no upstream directory matches this skill's name
- `local-missing`         indexed in SOURCES.json but not on disk

`no-upstream-path` is usually a renamed or removed upstream skill, or a skill
whose `sources` entry is a name-match rather than a real origin — `SOURCES.json`
lists every repository that publishes a skill of the same name, not one origin.
Both cases need a human, so they are reported rather than guessed at.

Requires an authenticated `gh`. Costs three API calls per repository regardless
of how many skills it owns, because the whole comparison runs off one recursive
tree.
"""
import argparse
import collections
import hashlib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def gh(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"gh api {path} failed: {out.stderr.strip()[:300]}")
    return json.loads(out.stdout)


def blob_sha(path):
    data = open(path, "rb").read()
    digest = hashlib.sha1()
    digest.update(b"blob %d\0" % len(data))
    digest.update(data)
    return digest.hexdigest()


def local_skills_for(repo):
    src = json.load(open(os.path.join(ROOT, "SOURCES.json"), encoding="utf-8"))
    return sorted(k for k, v in src["attribution"].items()
                  if repo in (v.get("sources") or []))


def upstream_tree(repo):
    info = gh(f"repos/{repo}")
    head = gh(f"repos/{repo}/commits/{info['default_branch']}")
    tree = gh(f"repos/{repo}/git/trees/{head['sha']}?recursive=1")
    blobs = {n["path"]: n["sha"] for n in tree["tree"] if n["type"] == "blob"}
    return info, head["sha"], blobs, bool(tree.get("truncated"))


def compare(repo):
    info, sha, up, truncated = upstream_tree(repo)

    bydir = collections.defaultdict(list)
    for path in up:
        parts = path.split("/")
        for i in range(len(parts) - 1):
            bydir[parts[i]].append(path)

    report = {
        "repo": repo,
        "head": sha,
        "pushed_at": info["pushed_at"],
        "archived": info["archived"],
        "license": (info.get("license") or {}).get("spdx_id"),
        "stars": info["stargazers_count"],
        "tree_truncated": truncated,
        "skills": [],
        "summary": collections.Counter(),
    }

    for key in local_skills_for(repo):
        category, slug = key.split("/", 1)
        directory = os.path.join(ROOT, category, slug)
        if not os.path.isdir(directory):
            report["summary"]["local-missing"] += 1
            report["skills"].append({"skill": key, "status": "local-missing"})
            continue

        local = {}
        for root, _dirs, files in os.walk(directory):
            for name in files:
                path = os.path.join(root, name)
                local[os.path.relpath(path, directory)] = blob_sha(path)
        local.pop("SOURCE.md", None)  # written here, never upstream

        # the archive renames colliding slugs, so try the bare name too
        candidates = set()
        for name in (slug, slug.split("--")[0]):
            for path in bydir.get(name, []):
                parts = path.split("/")
                candidates.add("/".join(parts[:parts.index(name) + 1]))

        best = None
        for candidate in sorted(candidates):
            differ, absent = [], []
            matched = 0
            for rel, want in local.items():
                have = up.get(f"{candidate}/{rel}")
                if have is None:
                    absent.append(rel)
                elif have != want:
                    differ.append(rel)
                else:
                    matched += 1
            added = sorted(p[len(candidate) + 1:] for p in up
                           if p.startswith(candidate + "/")
                           and p[len(candidate) + 1:] not in local)
            score = matched - len(differ) - len(absent)
            if best is None or score > best["score"]:
                best = {"upstream": candidate, "score": score, "matched": matched,
                        "differ": sorted(differ), "absent_upstream": sorted(absent),
                        "new_upstream": added}

        if best is None or best["matched"] == 0:
            status = "no-upstream-path"
            entry = {"skill": key, "status": status}
        elif not best["differ"] and not best["absent_upstream"]:
            status = "identical" if not best["new_upstream"] else "upstream-added-files"
            entry = {"skill": key, "status": status, "upstream": best["upstream"]}
            if best["new_upstream"]:
                entry["new_upstream"] = best["new_upstream"]
        else:
            status = "drift"
            entry = {"skill": key, "status": status, "upstream": best["upstream"]}
            for field in ("differ", "absent_upstream", "new_upstream"):
                if best[field]:
                    entry[field] = best[field]
        report["summary"][status] += 1
        report["skills"].append(entry)

    report["summary"] = dict(report["summary"])
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="upstream repository, e.g. anthropics/skills")
    parser.add_argument("--json", action="store_true", help="emit the full per-skill report")
    args = parser.parse_args()

    report = compare(args.repo)
    if args.json:
        print(json.dumps(report, indent=1))
        return
    print(f"{report['repo']}  head={report['head'][:12]}  "
          f"pushed={report['pushed_at'][:10]}  license={report['license']}")
    print(f"  {json.dumps(report['summary'])}")
    for entry in report["skills"]:
        if entry["status"] != "identical":
            print(f"  {entry['status']:22s} {entry['skill']}")


if __name__ == "__main__":
    main()

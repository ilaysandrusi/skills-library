#!/usr/bin/env python3
"""Compare locally archived skills against their upstream repository at HEAD.

    python3 tools/check-upstream.py <owner/repo> [--json]
    python3 tools/check-upstream.py --batch <owner/repo> <owner/repo> ...
    python3 tools/check-upstream.py --rotate 20 [--record]

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

`--rotate N` picks the next N repositories from `UPDATE_CHECKS.json` following the
rotation the maintenance policy asks for — never-checked sources first (largest
local footprint first, so the widest blind spots close first), then the sources
whose `last_checked` is oldest. `--record` writes each result back into
`UPDATE_CHECKS.json` so the next run resumes the cycle instead of re-checking the
same repositories. Nothing outside that state file is modified: applying an update
is a separate, deliberate act that needs the diff read first.
"""
import argparse
import collections
import hashlib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Unreachable(RuntimeError):
    """Upstream could not be read — renamed, deleted, made private, or rate limited."""


def gh(path):
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if out.returncode != 0:
        raise Unreachable(f"gh api {path} failed: {out.stderr.strip()[:200]}")
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


STATE = os.path.join(ROOT, "UPDATE_CHECKS.json")


def load_state():
    with open(STATE, encoding="utf-8") as handle:
        return json.load(handle)


def save_state(state):
    with open(STATE, "w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=1, ensure_ascii=False)
        handle.write("\n")


def footprints():
    with open(os.path.join(ROOT, "SOURCES.json"), encoding="utf-8") as handle:
        src = json.load(handle)
    counts = collections.Counter()
    for value in src["attribution"].values():
        for repo in (value.get("sources") or []):
            counts[repo] += 1
    return counts


def rotation(count):
    """Never-checked sources first (widest blind spots), then the stalest."""
    checked = load_state()["checked"]
    counts = footprints()
    fresh = sorted((-n, r) for r, n in counts.items() if r not in checked)
    stale = sorted((checked[r].get("last_checked") or "", -counts.get(r, 0), r)
                   for r in checked)
    order = [r for _, r in fresh] + [r for _, _, r in stale]
    return order[:count]


def render(report):
    print(f"{report['repo']}  head={report['head'][:12]}  "
          f"pushed={report['pushed_at'][:10]}  license={report['license']}"
          f"{'  ARCHIVED' if report['archived'] else ''}")
    print(f"  {json.dumps(report['summary'])}")
    for entry in report["skills"]:
        if entry["status"] != "identical":
            print(f"  {entry['status']:22s} {entry['skill']}")


def record(state, report, today):
    """Store the outcome. `verified_commit` is only a baseline when nothing drifted."""
    clean = not any(e["status"] in ("drift", "local-missing") for e in report["skills"])
    entry = {
        "last_checked": today,
        "verified_commit": report["head"] if clean else None,
        "upstream_pushed_at": report["pushed_at"][:10],
        "license": report["license"],
        "local_skills": len(report["skills"]),
        "result": report["summary"],
    }
    if report["archived"]:
        entry["upstream_archived"] = True
    if report["tree_truncated"]:
        entry["tree_truncated"] = True
        entry["note"] = ("Upstream tree came back truncated, so this comparison is "
                         "incomplete and the commit is not a baseline.")
        entry["verified_commit"] = None
    elif not clean:
        entry["note"] = ("Drift found; no baseline recorded. The diff has to be read "
                         "before anything is applied.")
    state["checked"][report["repo"]] = entry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="*", help="upstream repositories, e.g. anthropics/skills")
    parser.add_argument("--json", action="store_true", help="emit the full per-skill report")
    parser.add_argument("--rotate", type=int, metavar="N",
                        help="check the next N repositories in the rotation")
    parser.add_argument("--record", action="store_true",
                        help="write results back into UPDATE_CHECKS.json")
    args = parser.parse_args()

    repos = list(args.repo)
    if args.rotate:
        repos += rotation(args.rotate)
    if not repos:
        parser.error("give at least one repository, or --rotate N")

    state = load_state() if args.record else None
    today = __import__("datetime").date.today().isoformat()
    reports = []

    for repo in repos:
        # One dead upstream must not abandon the rest of the batch, and an
        # unreachable repository is a finding in its own right.
        try:
            report = compare(repo)
        except Unreachable as error:
            print(f"{repo}  UNREACHABLE  {error}")
            if args.record:
                state["checked"][repo] = {
                    "last_checked": today,
                    "verified_commit": None,
                    "local_skills": len(local_skills_for(repo)),
                    "result": {"unreachable": 1},
                    "note": f"Upstream could not be read ({error}). Renamed, deleted, "
                            "or made private — needs a manual look before the local "
                            "copies are treated as orphaned.",
                }
                save_state(state)
            continue

        reports.append(report)
        if args.record:
            record(state, report, today)
            save_state(state)  # checkpoint, so a later failure keeps earlier work
        if not args.json:
            render(report)

    if args.json:
        print(json.dumps(reports if len(reports) > 1 else reports[0], indent=1))
    if args.record:
        state["source_repos_total"] = len(footprints())
        save_state(state)
        print(f"\nrecorded {len(repos)} source(s) in UPDATE_CHECKS.json "
              f"({len(state['checked'])}/{state['source_repos_total']} covered)")


if __name__ == "__main__":
    main()

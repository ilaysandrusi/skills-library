#!/usr/bin/env python3
"""Generate an integrity manifest from a reviewed upstream Git checkout."""

import argparse
import json
import os
import subprocess


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(repo_dir, *args):
    return subprocess.check_output(
        ["git", "-C", repo_dir, *args],
        text=False,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-dir", required=True)
    parser.add_argument("--source-repository", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    commit = git(args.repo_dir, "rev-parse", f"{args.commit}^{{commit}}").decode().strip()
    tree = git(args.repo_dir, "rev-parse", f"{commit}^{{tree}}").decode().strip()
    raw = git(args.repo_dir, "ls-tree", "-r", "-l", "-z", commit)

    entries = []
    for record in raw.split(b"\0"):
        if not record:
            continue
        metadata, encoded_path = record.split(b"\t", 1)
        mode, object_type, sha, size = metadata.decode().split()
        if object_type != "blob":
            raise SystemExit(
                f"nested Git object requires materialization before archiving: "
                f"{encoded_path.decode(errors='replace')} ({object_type})"
            )
        entries.append(
            {
                "path": encoded_path.decode("utf-8", "surrogateescape"),
                "mode": mode,
                "blob": sha,
                "bytes": int(size),
            }
        )

    payload = {
        "schema_version": 1,
        "source_repository": args.source_repository,
        "commit": commit,
        "tree": tree,
        "tracked_files": len(entries),
        "tracked_bytes": sum(entry["bytes"] for entry in entries),
        "entries": entries,
    }
    output = args.output
    if not os.path.isabs(output):
        output = os.path.join(ROOT, output)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=1)
        handle.write("\n")


if __name__ == "__main__":
    main()

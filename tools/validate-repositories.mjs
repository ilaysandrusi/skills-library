#!/usr/bin/env node
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const indexPath = path.join(root, "REPOSITORIES.json");
const statePath = path.join(root, "MAINTENANCE_STATE.json");
const errors = [];
const warnings = [];

function readJson(file) {
  return JSON.parse(fs.readFileSync(path.join(root, file), "utf8"));
}

function blobSha(content) {
  return crypto
    .createHash("sha1")
    .update(Buffer.from(`blob ${content.length}\0`))
    .update(content)
    .digest("hex");
}

function snapshotEntries(directory, relative = "") {
  const entries = [];
  for (const item of fs.readdirSync(directory, { withFileTypes: true })) {
    const itemRelative = relative ? `${relative}/${item.name}` : item.name;
    const itemPath = path.join(directory, item.name);
    if (item.isSymbolicLink()) {
      const content = Buffer.from(fs.readlinkSync(itemPath));
      entries.push({
        path: itemRelative,
        mode: "120000",
        blob: blobSha(content),
        bytes: content.length,
      });
    } else if (item.isDirectory()) {
      entries.push(...snapshotEntries(itemPath, itemRelative));
    } else if (item.isFile()) {
      const content = fs.readFileSync(itemPath);
      const executable = (fs.statSync(itemPath).mode & 0o111) !== 0;
      entries.push({
        path: itemRelative,
        mode: executable ? "100755" : "100644",
        blob: blobSha(content),
        bytes: content.length,
      });
    } else {
      errors.push(`unsupported filesystem entry: ${itemRelative}`);
    }
  }
  return entries.sort((a, b) => a.path.localeCompare(b.path));
}

if (!fs.existsSync(indexPath)) {
  errors.push("REPOSITORIES.json is missing");
}

const index = errors.length ? { repositories: [] } : readJson("REPOSITORIES.json");
const ids = new Set();
const sources = new Set();
const localPaths = new Set();
let complete = 0;

for (const repository of index.repositories ?? []) {
  const label = repository.id ?? "<missing-id>";
  for (const field of [
    "id",
    "source_repository",
    "source_url",
    "commit",
    "license",
    "local_path",
    "primary_category",
  ]) {
    if (!repository[field]) errors.push(`${label}: missing ${field}`);
  }
  if (!Array.isArray(repository.tags) || repository.tags.length === 0) {
    errors.push(`${label}: tags must be a non-empty array`);
  }
  if (!Array.isArray(repository.practical_uses) || repository.practical_uses.length === 0) {
    errors.push(`${label}: practical_uses must be a non-empty array`);
  }
  if (!/^[0-9a-f]{40}$/.test(repository.commit ?? "")) {
    errors.push(`${label}: commit must be a full Git SHA`);
  }
  if (!/^[0-9a-f]{40}$/.test(repository.tree ?? "")) {
    errors.push(`${label}: tree must be a full Git SHA`);
  }
  if (repository.source_url !== `https://github.com/${repository.source_repository}`) {
    errors.push(`${label}: source_url does not match source_repository`);
  }
  if (ids.has(repository.id)) errors.push(`${label}: duplicate id`);
  if (sources.has(repository.source_repository)) {
    errors.push(`${label}: source repository is cataloged more than once`);
  }
  if (localPaths.has(repository.local_path)) errors.push(`${label}: duplicate local_path`);
  ids.add(repository.id);
  sources.add(repository.source_repository);
  localPaths.add(repository.local_path);

  const expectedPath = `repositories/${repository.primary_category}/${repository.id}`;
  if (repository.local_path !== expectedPath) {
    errors.push(`${label}: local_path must be ${expectedPath}`);
  }
  const snapshotPath = path.join(root, repository.local_path ?? "");
  if (!fs.existsSync(snapshotPath)) {
    errors.push(`${label}: snapshot directory is missing`);
    continue;
  }
  if (fs.existsSync(path.join(snapshotPath, ".git"))) {
    errors.push(`${label}: nested .git metadata must not be archived`);
  }
  if (repository.snapshot?.status === "complete") complete += 1;
  else errors.push(`${label}: snapshot status is not complete`);
  if (repository.review?.status !== "reviewed") {
    errors.push(`${label}: review status is not reviewed`);
  }
  if (repository.review?.archive_only !== true) {
    errors.push(`${label}: imported hooks and instructions must be marked archive_only`);
  }

  const manifestPath = repository.snapshot?.manifest;
  if (!manifestPath || !fs.existsSync(path.join(root, manifestPath))) {
    errors.push(`${label}: integrity manifest is missing`);
    continue;
  }
  const manifest = readJson(manifestPath);
  for (const field of ["source_repository", "commit", "tree"]) {
    if (manifest[field] !== repository[field]) {
      errors.push(`${label}: manifest ${field} does not match repository metadata`);
    }
  }

  const actual = snapshotEntries(snapshotPath);
  const expected = [...(manifest.entries ?? [])].sort((a, b) =>
    a.path.localeCompare(b.path),
  );
  const actualByPath = new Map(actual.map((entry) => [entry.path, entry]));
  const expectedByPath = new Map(expected.map((entry) => [entry.path, entry]));
  for (const entry of expected) {
    const found = actualByPath.get(entry.path);
    if (!found) {
      errors.push(`${label}: snapshot is missing ${entry.path}`);
      continue;
    }
    for (const field of ["mode", "blob", "bytes"]) {
      if (found[field] !== entry[field]) {
        errors.push(`${label}: ${entry.path} ${field} differs from upstream manifest`);
      }
    }
  }
  for (const entry of actual) {
    if (!expectedByPath.has(entry.path)) {
      errors.push(`${label}: snapshot contains untracked extra file ${entry.path}`);
    }
  }
  if (manifest.tracked_files !== expected.length) {
    errors.push(`${label}: manifest tracked_files does not equal its entry count`);
  }
  if (repository.snapshot?.tracked_files !== expected.length) {
    errors.push(`${label}: metadata tracked_files does not equal manifest`);
  }
  const expectedBytes = expected.reduce((sum, entry) => sum + entry.bytes, 0);
  if (
    manifest.tracked_bytes !== expectedBytes ||
    repository.snapshot?.tracked_bytes !== expectedBytes
  ) {
    errors.push(`${label}: tracked byte totals are inconsistent`);
  }
}

let state = null;
if (!fs.existsSync(statePath)) {
  errors.push("MAINTENANCE_STATE.json is missing");
} else {
  state = readJson("MAINTENANCE_STATE.json");
  const completed = new Map(
    (state.completed_migrations ?? []).map((entry) => [entry.source_repository, entry]),
  );
  const queued = new Set(
    (state.migration_queue ?? []).map((entry) => entry.source_repository),
  );
  for (const repository of index.repositories ?? []) {
    const migration = completed.get(repository.source_repository);
    if (!migration) {
      errors.push(`${repository.id}: missing completed migration state`);
    } else if (
      migration.local_path !== repository.local_path ||
      migration.commit !== repository.commit
    ) {
      errors.push(`${repository.id}: completed migration state differs from catalog`);
    }
    if (queued.has(repository.source_repository)) {
      errors.push(`${repository.id}: completed source remains in migration queue`);
    }
  }
  for (const [legacyPath, replacement] of Object.entries(
    state.legacy_to_repository_mappings ?? {},
  )) {
    if (!localPaths.has(replacement)) {
      errors.push(`${legacyPath}: replacement path is not cataloged`);
    }
  }
  if (state.progress?.cataloged_repositories !== (index.repositories?.length ?? 0)) {
    errors.push("maintenance progress cataloged_repositories is stale");
  }
  if (state.progress?.completed_migrations !== completed.size) {
    errors.push("maintenance progress completed_migrations is stale");
  }
  if (state.progress?.queued_source_repositories !== queued.size) {
    errors.push("maintenance progress queued_source_repositories is stale");
  }
}

const report = {
  catalogedRepositories: index.repositories?.length ?? 0,
  completeSnapshots: complete,
  queuedMigrations: state?.migration_queue?.length ?? 0,
  legacyMappings: Object.keys(state?.legacy_to_repository_mappings ?? {}).length,
  errors,
  warnings,
};
console.log(JSON.stringify(report, null, 2));
if (errors.length > 0) process.exit(1);

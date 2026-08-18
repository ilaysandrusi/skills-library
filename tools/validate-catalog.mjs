#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const root = process.cwd();
const strict = process.argv.includes("--strict");
const strictSourceFiles = process.argv.includes("--strict-source-files");

function readJson(file) {
  return JSON.parse(fs.readFileSync(path.join(root, file), "utf8"));
}

function gitFiles(pattern) {
  const output = execFileSync("git", ["ls-files", pattern], {
    cwd: root,
    encoding: "utf8",
  }).trim();
  return output ? output.split(/\r?\n/) : [];
}

function rootReadmeCount(readme, categoryId) {
  const marker = `](./${categoryId}/) | `;
  const line = readme.split(/\r?\n/).find((candidate) => candidate.includes(marker));
  if (!line) return null;
  const columns = line.split("|").map((column) => column.trim());
  const parsed = Number(columns[2]);
  return Number.isFinite(parsed) ? parsed : null;
}

function categoryReadmeCount(categoryId) {
  const file = path.join(root, categoryId, "README.md");
  if (!fs.existsSync(file)) return null;
  const text = fs.readFileSync(file, "utf8");
  const match = text.match(/\*\*מספר סקילים:\*\*\s*(\d+)/);
  return match ? Number(match[1]) : null;
}

function hasFrontmatter(file) {
  const text = fs.readFileSync(path.join(root, file), "utf8");
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return false;
  return /^name:\s*/m.test(match[1]) && /^description:\s*/m.test(match[1]);
}

function nearestCatalogSkillDir(file) {
  const normalized = file.replaceAll("\\", "/");
  const ancestors = [...expectedSkillDirs].filter((dir) => normalized.startsWith(`${dir}/`));
  return ancestors.sort((a, b) => b.length - a.length)[0] ?? null;
}

function isNestedWorkflowSkillFile(file) {
  const parentDir = nearestCatalogSkillDir(file);
  if (!parentDir) return false;

  const relative = file.slice(parentDir.length + 1);
  if (!relative.includes("/")) return false;

  const text = fs.readFileSync(path.join(root, file), "utf8");
  return (
    /\|\s*Parent\s*\|/i.test(text) ||
    /Invoked by the `[^`]+` orchestrator/i.test(text) ||
    /Not directly user-routable/i.test(text)
  );
}

const catalog = readJson("catalog.json");
const sources = readJson("SOURCES.json");
const readme = fs.readFileSync(path.join(root, "README.md"), "utf8");

const expectedSkillFiles = new Set();
const expectedSkillDirs = new Set();
const errors = [];
const warnings = [];
const missingSourceFiles = [];

let computedTotal = 0;
for (const category of catalog.categories) {
  computedTotal += category.skills.length;

  const rootCount = rootReadmeCount(readme, category.id);
  if (rootCount === null) {
    errors.push(`README.md is missing category ${category.id}`);
  } else if (rootCount !== category.skills.length) {
    errors.push(
      `README.md count mismatch for ${category.id}: README=${rootCount}, catalog=${category.skills.length}`,
    );
  }

  const categoryCount = categoryReadmeCount(category.id);
  if (categoryCount === null) {
    errors.push(`${category.id}/README.md is missing its skill count`);
  } else if (categoryCount !== category.skills.length) {
    errors.push(
      `${category.id}/README.md count mismatch: README=${categoryCount}, catalog=${category.skills.length}`,
    );
  }

  for (const skill of category.skills) {
    const dir = `${category.id}/${skill.name}`;
    const skillFile = `${dir}/SKILL.md`;
    expectedSkillDirs.add(dir);
    expectedSkillFiles.add(skillFile);

    if (!fs.existsSync(path.join(root, skillFile))) {
      errors.push(`catalog entry is missing on disk: ${skillFile}`);
    } else if (!hasFrontmatter(skillFile)) {
      errors.push(`catalog skill has invalid frontmatter: ${skillFile}`);
    }

    if (!sources.attribution?.[dir]) {
      warnings.push(`catalog skill has no source attribution: ${dir}`);
    }

    if (!fs.existsSync(path.join(root, dir, "SOURCE.md"))) {
      missingSourceFiles.push(dir);
    }
  }
}

if (catalog.total !== computedTotal) {
  errors.push(`catalog total mismatch: total=${catalog.total}, computed=${computedTotal}`);
}

if (sources.skills !== catalog.total) {
  errors.push(`SOURCES.json skill count mismatch: sources=${sources.skills}, catalog=${catalog.total}`);
}

const allSkillFiles = gitFiles("*SKILL.md");
const extraSkillFiles = allSkillFiles.filter((file) => !expectedSkillFiles.has(file));
const nestedWorkflowSkillFiles = extraSkillFiles.filter(
  (file) => !hasFrontmatter(file) && isNestedWorkflowSkillFile(file),
);
const badExtraFrontmatter = extraSkillFiles.filter(
  (file) => !hasFrontmatter(file) && !nestedWorkflowSkillFiles.includes(file),
);
for (const file of badExtraFrontmatter) {
  warnings.push(`nested/non-catalog SKILL.md has invalid frontmatter: ${file}`);
}

const duplicateNames = new Map();
for (const category of catalog.categories) {
  for (const skill of category.skills) {
    const refs = duplicateNames.get(skill.name) ?? [];
    refs.push(`${category.id}/${skill.name}`);
    duplicateNames.set(skill.name, refs);
  }
}
const duplicateNameGroups = [...duplicateNames.entries()].filter(([, refs]) => refs.length > 1);

const report = {
  catalogTotal: catalog.total,
  computedTotal,
  gitSkillFiles: allSkillFiles.length,
  catalogSkillFiles: expectedSkillFiles.size,
  nestedOrNonCatalogSkillFiles: extraSkillFiles.length,
  nestedWorkflowSkillFiles: nestedWorkflowSkillFiles.length,
  nestedWorkflowSkillFilesSample: nestedWorkflowSkillFiles.slice(0, 25),
  duplicateCatalogNameGroups: duplicateNameGroups.length,
  missingSourceAttribution: warnings.filter((warning) =>
    warning.includes("has no source attribution"),
  ).length,
  missingSourceFiles: missingSourceFiles.length,
  missingSourceFilesSample: missingSourceFiles.slice(0, 25),
  invalidNestedFrontmatter: badExtraFrontmatter.length,
  errors,
  warnings: strict ? warnings : warnings.slice(0, 25),
};

console.log(JSON.stringify(report, null, 2));

if (errors.length > 0 || (strict && warnings.length > 0) || (strictSourceFiles && missingSourceFiles.length > 0)) {
  process.exit(1);
}

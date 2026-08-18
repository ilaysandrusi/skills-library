#!/usr/bin/env node
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const root = process.cwd();
const args = process.argv.slice(2);

function usage(exitCode = 0) {
  console.log(`Usage:
  node tools/install-skill.mjs <skill-name-or-category/skill> [--force] [--dest <dir>]
  node tools/install-skill.mjs --list <search-text>

Examples:
  node tools/install-skill.mjs agent-reach
  node tools/install-skill.mjs 15-integrations/agent-reach --force
  node tools/install-skill.mjs --list outreach`);
  process.exit(exitCode);
}

if (args.length === 0 || args.includes("--help") || args.includes("-h")) usage();

const force = args.includes("--force");
const listIndex = args.indexOf("--list");
const destIndex = args.indexOf("--dest");
const destRoot =
  destIndex === -1
    ? path.join(process.env.CODEX_HOME || path.join(os.homedir(), ".codex"), "skills")
    : path.resolve(args[destIndex + 1] || "");

if (destIndex !== -1 && !args[destIndex + 1]) {
  console.error("Missing value after --dest");
  process.exit(2);
}

const catalog = JSON.parse(fs.readFileSync(path.join(root, "catalog.json"), "utf8"));
const skills = catalog.categories.flatMap((category) =>
  category.skills.map((skill) => ({
    category: category.id,
    name: skill.name,
    description: skill.description,
    dir: `${category.id}/${skill.name}`,
  })),
);

function matches(query) {
  const normalized = query.toLowerCase();
  return skills.filter(
    (skill) =>
      skill.name.toLowerCase().includes(normalized) ||
      skill.dir.toLowerCase().includes(normalized) ||
      skill.description.toLowerCase().includes(normalized),
  );
}

if (listIndex !== -1) {
  const query = args[listIndex + 1];
  if (!query) {
    console.error("Missing search text after --list");
    process.exit(2);
  }
  for (const skill of matches(query).slice(0, 50)) {
    console.log(`${skill.dir} - ${skill.description.slice(0, 160).replace(/\s+/g, " ")}${skill.description.length > 160 ? "..." : ""}`);
  }
  process.exit(0);
}

const query = args.find((arg, index) => {
  if (arg.startsWith("-")) return false;
  if (index > 0 && args[index - 1] === "--dest") return false;
  return true;
});

if (!query) usage(2);

let candidates = skills.filter((skill) => skill.dir === query || skill.name === query);
if (candidates.length === 0) candidates = matches(query);

if (candidates.length === 0) {
  console.error(`No skill matched: ${query}`);
  process.exit(1);
}

if (candidates.length > 1) {
  console.error(`Multiple skills matched "${query}". Use a full category/skill path:`);
  for (const skill of candidates.slice(0, 25)) console.error(`  ${skill.dir}`);
  if (candidates.length > 25) console.error(`  ...and ${candidates.length - 25} more`);
  process.exit(1);
}

const skill = candidates[0];
const sourceDir = path.join(root, skill.dir);
const targetDir = path.join(destRoot, skill.name);

if (!fs.existsSync(path.join(sourceDir, "SKILL.md"))) {
  console.error(`Resolved skill has no SKILL.md: ${skill.dir}`);
  process.exit(1);
}

if (fs.existsSync(targetDir)) {
  if (!force) {
    console.error(`Destination already exists: ${targetDir}`);
    console.error("Re-run with --force to replace it.");
    process.exit(1);
  }
  fs.rmSync(targetDir, { recursive: true, force: true });
}

fs.mkdirSync(destRoot, { recursive: true });
fs.cpSync(sourceDir, targetDir, { recursive: true });

console.log(`Installed ${skill.dir} to ${targetDir}`);

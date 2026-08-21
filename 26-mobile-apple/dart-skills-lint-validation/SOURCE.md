# Source

- Repository: `flutter/skills`
- URL: https://github.com/flutter/skills
- Upstream path: `tool/dart_skills_lint/skills/dart-skills-lint-validation`
- Imported commit: `1e5696a2`
- Local skill path: `26-mobile-apple/dart-skills-lint-validation`
- License: BSD-3-Clause (repository level)

## What was imported

`SKILL.md` and the `evals/` directory that ships beside it upstream.

## Ownership

The skill lives inside `tool/dart_skills_lint/`, the Dart package that provides
the `dart_skills_lint` linter the skill drives. Only the skill directory itself
was imported; the surrounding package is the tool being invoked, not part of the
skill, and it is installed from pub rather than from this archive.

`evals/` is kept because it is the only record of what the skill is expected to
catch, which is what makes the skill testable later.

## Baseline

Verified on 2026-08-21 by comparing the git blob SHA of every local file against
the upstream tree at `1e5696a2`. The directory matches.

## Update history

- **2026-08-21** — brought up to `1e5696a2` from an earlier unrecorded state.
  Upstream documents the `dart install` invocation of the linter alongside the
  existing `dart pub global activate` one, and notes that the installed binary
  accepts `--help` directly. Documentation only.

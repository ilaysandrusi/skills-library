# Source

- Repository: `tmchow/illo-skill`
- URL: https://github.com/tmchow/illo-skill
- Upstream path: `skills/illo`
- Imported commit: `873f4d851f51ad4db1b9026df8a940e658f9f60d`
- Upstream version: `0.34.4`
- Local skill path: `16-ai-apis-media/illo`
- License: MIT (`LICENSE`, copied from the repository root; see also `NOTICE`)
- Author: Trevin Chow

## Attribution

`NOTICE` asks that anyone redistributing the skill retain it and credit
**"Illo by Trevin Chow."** That applies to this archive, so `NOTICE` is imported
with the package and the credit is recorded here. The notice covers the code, the
prompts, the reference docs, the "Blot" mascot and the bundled example artwork.

## What was imported

The whole upstream skill directory:

- `SKILL.md`, `README.md`, `NOTICE`
- `references/` — 25 files, including the seventeen bundled style guides under
  `references/styles/` and the character, composition, cutout, palette,
  prompt-recipe and quality-bar references
- `scripts/illo.py` — the renderer
- `scripts/repair-hermes-assets.sh` — an asset-integrity preflight
- `assets/` — `character-reference.webp`, `character-reference-pixel.png` and
  `checksums.txt`

`LICENSE` was taken from the repository root because `NOTICE` points at it and the
skill directory does not carry its own copy.

Left upstream: `_assets/` (marketing samples, logos and model-comparison
galleries for the project website, not used by the skill at runtime) and the
repository's own `AGENTS.md` and plugin marketplace manifest.

## Ownership

Every imported file except `LICENSE` sits inside `skills/illo/` upstream, so the
package is self-contained by construction. `SKILL.md` routes to
`references/styles/<look>.md` to render a chosen look and to the other references
for composition, palettes and cutouts, so importing `SKILL.md` alone would leave
a skill whose every branch points at a missing file. `scripts/illo.py` is the
executable the skill drives, and `assets/character-reference.webp` is the visual
identity of the default mascot that renders are conditioned on.

## Why this skill and not an existing one

The library already generates images (`imagegen`, `imagen`, `character-design`,
`fal-recipes`) and already documents illustration style
(`19-sales-gtm-startup/illustration-style`). Those are a raw generation call and
a style-guide authoring exercise respectively. `illo` is neither: it is a
complete opinionated editorial-illustration pipeline — a recurring mascot
performs the idea, in one of seventeen bundled print looks, with hand-built
explainer diagrams, transparent character cutouts for compositing, a character
builder, and a quality bar the render is checked against. No existing skill
covers that.

## Integrity

`assets/checksums.txt` is an upstream manifest of SHA256 hashes for the bundled
binaries. Both binary assets were verified against it after import, so neither
was corrupted in transit — a real failure mode for this archive, which has
previously acquired 0-byte fonts and tarballs from binary-unsafe imports.

## Security review

The package handles credentials carefully and says so in comments that turn out
to be accurate:

- The OpenRouter API key is read from the user's own local config
  (`resolve_key`, written by `illo init` via `getpass`) and sent only to
  `https://openrouter.ai/api/v1/...` in an `Authorization` header. It is not
  written anywhere else and reaches no other host.
- The Codex and Grok backends run `subprocess` against the user's own
  already-installed, already-logged-in CLI. The script reads no
  `~/.codex/auth.json`, runs no OAuth and holds no token for either path.
- Captured subprocess output is passed through a redactor that masks
  secret-shaped substrings before anything is printed.
- Character packs are fetched from `raw.githubusercontent.com/tmchow/illo-characters`
  and are data only — `index.json`, `character.md`, `reference.png`. Nothing
  fetched is executed. Pack names are validated against a strict kebab-case
  regex before being interpolated into a URL or a filesystem path, which closes
  the path-traversal route.
- `scripts/repair-hermes-assets.sh` re-downloads only files listed in
  `assets/checksums.txt`, from immutable per-asset pinned commits, and verifies
  the SHA256 of each download **before** installing it, aborting on mismatch.

Network access from `scripts/illo.py` is limited to exactly two hosts,
`openrouter.ai` (the image model the skill exists to call) and
`raw.githubusercontent.com` (character packs). No hooks are declared, so nothing
in this package runs automatically.

One thing worth flagging because it looks odd on a host scan:
`references/styles/snes.md` links to two password-protected reference galleries on
random-looking `*.ht-ml.app` subdomains (the password is printed next to each
link). They are the author's visual calibration examples for that one style, they
are documentation a reader opens by hand, and no script in the package fetches
them — the two hosts above are the only ones any code contacts. Nothing is sent
to them.

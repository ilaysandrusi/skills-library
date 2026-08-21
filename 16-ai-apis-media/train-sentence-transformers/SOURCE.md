# Source

- Repository: `huggingface/skills`
- URL: https://github.com/huggingface/skills
- Upstream path: `skills/train-sentence-transformers`
- Imported commit: `02019491`
- Local skill path: `16-ai-apis-media/train-sentence-transformers`
- License: Apache-2.0 (repository level)

## What was imported

The whole upstream skill directory: `SKILL.md`, `references/` (loss selection,
evaluators, dataset formats, training arguments, hardware, troubleshooting and
the HF Jobs execution guide) and `scripts/` (runnable training examples).

## Ownership

Everything lives under `skills/train-sentence-transformers/` upstream. `SKILL.md`
is a router: it decides which model class the user needs and then sends the
reader to the matching `references/` page and `scripts/` example. Neither part is
usable without the other.

## Baseline

Verified on 2026-08-21 by comparing the git blob SHA of every local file against
the upstream tree at `02019491`. The whole directory matches.

## Update history

- **2026-08-21** — brought up to `02019491` from an earlier unrecorded state.
  Upstream added `MultiVectorEncoder` (ColBERT / late-interaction) support: a new
  `references/evaluators_multi_vector_encoder.md`, a new
  `references/losses_multi_vector_encoder.md`, a new
  `scripts/train_multi_vector_encoder_example.py`, and matching revisions across
  the existing references, the model-architecture notes and the frontmatter
  description. Also refreshes the base-model recommendations and switches the
  login instructions to the current `hf auth login` command.

  Reviewed for security: the new script uses `sentence_transformers`, `datasets`
  and `torch` only. Its `HF_TOKEN` references are the user's own Hugging Face
  token, read from their environment so their own trained model can be pushed to
  their own Hub account, and the reference text explicitly tells the reader never
  to hardcode a token. No shell execution, no downloads outside the Hub.

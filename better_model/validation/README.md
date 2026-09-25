# Validation record — 2026-09-25

Compute class: `LOCAL_LIGHT`. These checks establish engineering behavior, not biological superiority.

- **15 unittest checks passed**, including matching the original architecture, total objective, preprocessing, graph construction, spatial-loss gradients and small two-stage training/selection loop. CPU repeated runs and checkpoint reload matched. See [tests.log](tests.log).
- **Portable notebook passed**: all code cells executed from an empty directory using its embedded source, with synthetic smoke mode and a headless plotting backend. See [notebook_check.json](notebook_check.json) and [notebook.log](notebook.log). Colab installation/GPU execution was not exercised.
- **A1 and D1 input/preprocessing/graph checks passed** on the full local inputs. A small A1 subset completed both training stages with finite outputs; no subset ARI was reported. Details, graph statistics and checksums are in [local_checks.json](local_checks.json).
- Original `hello.py` SHA-256 remains `c2ec5c2172b3f3f8e762ff89abe8f4173f508d3444490a104e437268142593fa`. Its JSON notebook content is intentionally preserved, so it is excluded from Python-module compilation.
- The new Python modules and JSON configs parse successfully; the new text artifacts have no trailing whitespace.
- Repository-wide `git diff --check` reports a pre-existing blank line at EOF in `.gitignore:34`. That unrelated user edit was left untouched.
- Repomix compression and Graphify code extraction/report refresh completed. These are structural context tools, not scientific validation. Generated Graphify files were refreshed under the standing repository rules; unrelated pre-existing deletions and edits were preserved.

The reference and affinity candidate still need matched full 400-epoch, three-seed GPU runs and the user's original ASTRA ARI records. Synthetic ARI in engineering logs must not be interpreted as a real-data result. Existing historical ARISE/SMART metrics were not relabeled as ASTRA outcomes. No biological experiment was added to `experiments.csv` because this session performed implementation, input checks and engineering smoke tests only.

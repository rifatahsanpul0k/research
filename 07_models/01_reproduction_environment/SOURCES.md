# Phase 3B engineering sources

Phase 3A paper and code provenance remains authoritative in [the source ledger](../../03_papers/01_systematic_method_mapping/SOURCES.md) and [codebase audit](../../03_papers/01_systematic_method_mapping/31_CODEBASE_VERIFICATION.md). Phase 3B adds read-only remote HEAD/default-branch observations dated 2026-09-12.

| Repository | Selected HEAD | Default branch | Use |
|---|---|---|---|
| https://github.com/scikit-learn/scikit-learn | 7eec52f9b21b88c02876853e10ab426db063245e | main | controls and PCA engineering snapshot |
| https://github.com/bioFAM/MOFA2 | 4a102f2b491ab600738ddf693a70f0baf032ca68 | master | MOFA+ engineering snapshot |
| https://github.com/rsinghlab/SCOT | 14649be6e14017dcfe7ba619091b33d1df55f6a9 | master | SCOT engineering snapshot |
| https://github.com/scverse/scvi-tools | 73b28e44223621470e582a81a102c107bb22678b | main | totalVI/MultiVI engineering snapshot |
| https://github.com/JinmiaoChenLab/SpatialGlue | 7c976d811d27ace51ce47ae0ad94a068a7d222fa | main | SpatialGlue engineering snapshot |
| https://github.com/zhou-1314/Garfield | 2c315b26d5454feb1ee9218482dbbc0dbcfbedd8 | main | Garfield engineering snapshot |

The selected commits are current remote heads, not verified paper-release commits. No repository was cloned while collecting these identifiers. Official repository documentation and Phase 3A records provide dependency, license and input-format evidence with their stated limitations.

## Installed baseline packages

The isolated baseline environment was resolved from the official Python package index on 2026-09-12. It pins [NumPy 2.4.4](https://pypi.org/project/numpy/2.4.4/), [SciPy 1.17.1](https://pypi.org/project/scipy/1.17.1/), [scikit-learn 1.9.1](https://pypi.org/project/scikit-learn/1.9.1/) and [h5py 3.16.0](https://pypi.org/project/h5py/3.16.0/). The installed versions imported successfully. A synthetic PCA calculation verified executable linkage only; Phase 3C scientific runs are separately registered and reported.

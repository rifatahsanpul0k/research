# Dataset statistics (read-only)

Values below are computed from `X` in the complete local H5AD files. `sparsity` is (1-\mathrm{nnz}/(np)), counting logical nonzeros (`data != 0`) without densification. Row-total and detected-feature moments are population descriptive moments. ADT/ATAC row totals are reported without assigning molecule semantics.

| Dataset/modality | shape | dtype/encoding | sparsity | sum | row total median (mean) | detected median (mean) |
|---|---:|---|---:|---:|---:|---:|
| A1 RNA | 3484×18085 | float32 CSR | 0.891689 | 10,014,640 | 2,551 (2,874.47) | 1,825.5 (1,958.81) |
| A1 ADT | 3484×31 | float32 CSR | 0.023425 | 1,638,639,634 | 449,112.5 (470,332.85) | 31 (30.27) |
| D1 RNA | 3359×18085 | float32 CSR | 0.939010 | 4,868,570 | 1,343 (1,449.41) | 1,052 (1,103.01) |
| D1 ADT | 3359×31 | float32 CSR | 0.020840 | 1,437,726,924 | 403,382 (428,022.31) | 31 (30.35) |
| E11 RNA | 1263×32285 | float32 CSR | 0.925207 | 5,428,009 | 3,735 (4,297.71) | 2,351 (2,414.68) |
| E11 ATAC | 1263×69370 | float32 CSR | 0.935089 | 13,424,364 | 8,517 (10,628.95) | 4,005 (4,502.88) |
| E13 RNA | 1777×32285 | float32 CSR | 0.910601 | 9,327,578 | 3,797 (5,249.06) | 2,517 (2,886.26) |
| E13 ATAC | 1777×123840 | float32 CSR | 0.942814 | 30,789,801 | 12,351 (17,326.84) | 5,653 (7,081.94) |
| E15 RNA | 1949×32285 | float32 CSR | 0.894722 | 13,835,704 | 6,024 (7,098.87) | 3,302 (3,398.89) |
| E15 ATAC | 1949×141420 | float32 CSR | 0.917140 | 75,764,525 | 29,986 (38,873.54) | 10,715 (11,718.03) |
| E18 RNA | 2129×32285 | float32 CSR | 0.934338 | 7,291,169 | 3,158 (3,424.69) | 2,089 (2,119.90) |

E18 ATAC is unavailable and has no row in this table. Full extrema, variance and checksums are in `matrix_statistics.json`; source files remain ignored and unchanged. These are descriptive properties, not QC thresholds or biological conclusions.

All available `obsm/spatial` arrays are (n\times2) with one unique row per observation. Coordinate value ranges are A1 0–127, D1 0–119, E11 2–50, E13 1–50, E15 1–50 and E18 1–50. Units, orientation and image registration remain undocumented locally; ranges are therefore numerical descriptors rather than physical distances. See `coordinate_summary.json`.

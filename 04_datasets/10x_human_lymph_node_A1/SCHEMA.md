# Schema

RNA: expected local AnnData shape 3,484 × 18,085; ADT: 3,484 × 31; both use CSR X and `obsm/spatial` shape 3,484 × 2. RNA/ADT observation IDs are barcode-like and must be checked for exact equality before pairing. `var` contains `_index`, `gene_ids`, `feature_types`, `genome`. The local inspector output is the authoritative file summary.

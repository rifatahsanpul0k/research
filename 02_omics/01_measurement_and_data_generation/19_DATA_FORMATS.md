# 19. Common data formats

CSV/TSV store delimited metadata; Matrix Market stores sparse coordinate entries with one-based row/column indices [S24]; HDF5/H5 stores hierarchical arrays; `.h5ad` stores an AnnData object. AnnData requires `obs` and `var`; `X` is an optional dense or sparse (n_{obs}\times n_{var}) array, `layers` hold same-shape alternatives, `obsm` stores observation-aligned arrays such as coordinates, and `uns` stores unstructured metadata [S22][S23].

Sparse CSR/CSC storage separates data and index arrays. 10x feature-barcode HDF5 commonly stores a feature-by-barcode CSC matrix, so orientation must be read from the schema rather than guessed [S20]. A project may transpose it when constructing AnnData.

`.obsm["spatial"]` is an observation-aligned coordinate array; its name does not mean image-derived features. `X` may be counts, normalized values, or another layer. Inspect keys, shapes, dtypes, identifiers, and provenance before interpretation.

**Evidence:** [S20], [S22], [S23], [S24].

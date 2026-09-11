# Transformer versus GNN

Phase 2C · method study · studied_not_fitted · not_reproduced.

## Definition and mechanism

Transformers learn attention without explicit graph; GNNs propagate on A. Neither is inherently superior.

## Numerical and computational representation

For observations in rows, feature/node matrices have explicit dimensions. The output can be a point matrix, distribution parameters, graph relation, or reconstructed view; it is model-derived, not raw biology.

## Project relevance

These ideas may apply to single-cell matrices, spatial spots, and paired or mosaic multi-omics only after observation units, feature identifiers, pairing, masks, graph provenance, and coordinate semantics are verified. No project task is run in Phase 2C.

## Method bookkeeping

Architecture, training objective, biological prior, downstream model, and evaluation are separate. Similar numerical vectors do not imply biologically equivalent cells; correlation does not establish causation.

## Misconceptions and limitations

Transformers learn attention without explicit graph; GNNs propagate on A. Latent dimensions and learned weights are not direct measurements.

## Evidence

Vaswani et al. (2017); Kipf & Welling (2017). See `SOURCES.md`; no project dataset was fitted.

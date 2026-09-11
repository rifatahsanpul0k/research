# 14. Raw versus processed data

The levels are distinct: `raw reads → assigned counts → filtered counts → normalized values → transformed values → selected features → dimension-reduced coordinates → learned representation`. In symbols, (X_{counts}\neq X_{normalized}\neq X_{PCA}\neq Z_{learned}).

Raw FASTQ retains read sequences and indexes. A count matrix retains feature-by-observation aggregates and may already embody mapping, UMI handling, filtering, or annotation. Normalization and transformations change units; feature selection changes columns; PCA changes both units and dimension. A matrix named `X` does not guarantee raw counts [S02][S16].

Record the level, software/version, annotation, and filters before using data. Comparing two vectors requires knowing whether their entries are counts, transformed values, peaks, proteins, or embeddings. No normalization ranking is performed here.

**Evidence:** [S02], [S16], [S22], [S33], [S34].

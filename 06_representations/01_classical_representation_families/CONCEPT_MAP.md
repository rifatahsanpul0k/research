# Classical representation landscape

```text
RAW BIOLOGICAL MEASUREMENT
          |
          v
      MATRIX DATA (X)
          |
   +------+------+------+------+------+------+------+
   |      |      |      |      |      |      |      |
   v      v      v      v      v      v      v      v
 vector  latent distance kernel neighborhood graph tensor
 space   factor  matrix          set        /network
   |      |      |      |      |      |      |
   +------+------+------+------+------+------+------+
                  |
                  v
       COMPUTATIONAL REPRESENTATION (R=f(X))
                  |
                  v
             FUTURE ML MODEL
```

This map is a taxonomy, not a ranking. A single study may retain several objects: raw counts, a PCA score table, a spatial coordinate table, a pathway score table and a graph can coexist. A graph is one branch; dimensional reduction, concatenation, latent factors and graph encoding are optional choices with different assumptions. A transport coupling is a relationship between two measures, not a feature embedding. A tensor requires compatible axes; a heterogeneous graph requires entity and relation types. The [comparison framework](REPRESENTATION_COMPARISON_FRAMEWORK.md) records these distinctions without scores.

## Pipeline boundary

Measurement and preprocessing produce (X); a representation mechanism (f) produces (R); a later model consumes (R). A latent coordinate is not directly measured biology. Similarity is not equivalence, correlation is not causation, and numerical compactness is not biological correctness. Chronological labels and inferred pseudotime remain separate objects. All project-data transformations and model fitting are deferred to an explicitly authorized later phase.

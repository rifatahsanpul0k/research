# ADT preprocessing

Antibody-derived tags (ADT) measure oligo tags attached to antibodies, which report antibody binding to epitopes rather than total protein activity. Background includes nonspecific binding, free antibody, ambient tags and differences in antibody affinity. A positive ADT value therefore needs assay controls and marker context [S06,S07].

Centered log-ratio (CLR) for a row (x) is (clr(x_j)=\log(x_j/g(x))), where (g(x)=(\prod_j(x_j+\epsilon))^{1/p}); (epsilon) handles zeros and must be documented. For (1,3), with (epsilon=1), the geometric mean is 2 and CLR is (log 1/2, log 2/2) = (-0.693,0.405). CLR changes compositional scale and can be background-sensitive. Alternatives include isotype/background correction and assay-specific transformations; no universal best exists [S07,S40]. ADT has 31 features in our lymph-node files versus 18,085 RNA genes, so raw concatenation silently weights modalities by scale and dimension.

# Modality comparison without equivalence claims

RNA, ADT and ATAC differ in molecular target, feature definition, count scale, background and feature-set construction. Lymph-node RNA has 18,085 features and ADT 31; mouse-brain RNA has 32,285 and ATAC peak counts vary by stage. Thus a larger row sum or lower sparsity is not evidence of more biology. Within-stage RNA/ATAC comparisons are descriptive and still depend on the paired assay and feature sets.

The report compares dimensions, sparsity, row totals and detections only. Cross-stage differences may reflect developmental biology, peak calling, library depth or preparation. Spatial coordinate ranges are reported separately and are not merged with molecular values. “Two similar numerical vectors” means only closeness under a chosen scale and metric; biological equivalence requires assay validity, context, identity/state evidence and uncertainty. Evidence: CITE-seq [S06], scATAC [S08,S09], spatial/multimodal reviews [S43].

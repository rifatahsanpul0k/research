# 2. Sequencing foundations

Sequencing-by-synthesis reads bases from library molecules. A read is a finite sequence observation; read length is its number of bases. Paired-end sequencing reads both ends of one insert, while single-end reads one end. Depth is the number of reads; genomic coverage is the average number of reads covering a base and depends on read count, length, and genome size [S02][S19].

Libraries contain adapter-flanked DNA or cDNA molecules. Demultiplexing uses sample indexes; barcode reads identify observations and molecule tags; sequence reads are mapped to a reference genome/transcriptome and assigned through an annotation. Exonic, intronic, junction, or intergenic assignments depend on the assay and annotation [S02][S26].

The computational chain is `FASTQ → barcode/index parsing → mapping → feature assignment → counts`. A mapping is an inference with ambiguity, reference-build dependence, and possible multi-mapping. Read count, UMI count, fragment count, and coverage are different quantities. Do not treat depth as biological abundance or a reference annotation as the genome itself.

For this project sequencing concepts explain why two matrices from the same biology can differ by depth, library, chemistry, reference, and assignment rules; they do not prescribe an alignment workflow.

**Evidence:** [S02], [S19], [S26].

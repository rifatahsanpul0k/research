# 1. Sample to matrix

## A–B. Quantity and mechanism

An assay samples a biological specimen, preserves or dissociates it, captures molecules, attaches identifiers, makes a measurable library, and sequences or images the library. Reverse transcription converts captured RNA to cDNA; tagmentation samples accessible DNA; oligonucleotide-conjugated antibodies provide sequenceable tags [S01][S06][S09][S11][S13].

## C–F. Observation and data

The observation may be a cell, nucleus, spot, bin, or pixel-defined capture location. Raw output is FASTQ reads (or instrument signals). Processing demultiplexes samples, corrects observation barcodes, assigns reads to features, and aggregates them into (X\in\mathbb N_0^{n\times p}), with `obs` metadata, `var` feature identifiers, and optional coordinates. A read is evidence sampled from a library; a matrix entry is a processed assignment, not a census of molecules.

## G–I. Losses and relevance

Preparation can lyse cells, lose transcripts, mix ambient RNA, or change composition. Capture and PCR are nonuniform; sequencing undersamples; mapping and annotation can misassign; filtering removes observations/features. Thus true biological state ≠ measured state ≠ processed matrix. These distinctions determine what biological similarity can mean in single-cell, spatial, and multimodal data. Rows that look similar can share a technical artifact or represent different mixtures.

## J. Evidence

See [S01], [S02], [S06], [S09], [S11], [S13], and the project’s [BIOLOGY_TO_DATA](BIOLOGY_TO_DATA.md).

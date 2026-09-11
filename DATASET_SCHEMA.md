# Dataset documentation schema

Six datasets are registered from the user's brief. Their links have not been accessed and no data are local. User-reported organism, tissue, and sample/stage labels are explicitly unverified. A dataset name does not verify an assay or modality.

Use the exact six supplied IDs as canonical dataset IDs. Future datasets need stable unique IDs. Place detailed metadata under `04_datasets/<dataset_id>/` after acquisition; maintain the root `datasets.csv` index.

| Field | Required documentation |
|---|---|
| dataset_id / aliases | Stable canonical ID; explicit alternate names and original filename mappings |
| biological_system | System grouping and evidence for it |
| organism | Species, reference taxonomy/build when known, source and verification state |
| tissue | Tissue/anatomical region with provenance |
| biological_condition | Condition, treatment, disease/control status; unknown unless documented |
| developmental_stage | Exact reported stage and interpretation; separate label from confirmed timing |
| sample_label | Source sample identifier; distinguish sample, donor, section, replicate, and batch |
| technology_platform | Assay name/version, chemistry, resolution, acquisition process |
| modalities | Each measured modality, pairing/alignment, units, and evidence |
| observation_unit | Cell, nucleus, spot, bin, region, sample, or unknown |
| number_of_observations | Per modality and sample; pre/post-QC counts and correspondence |
| number_of_features | Per modality and version; identifiers and reference annotations |
| raw_processed_state | Raw, processed, mixed, or unknown, at file level |
| counts_availability | What counts are present, matrix location/layer, integer/transformed state |
| spatial_coordinate_availability | Presence, file, units, dimensions, coordinate frame, orientation, registration |
| ground_truth_annotations | Labels, provenance, method of creation, uncertainty, and independence from inputs |
| biological_meaning_of_labels | Label definition, granularity, context, ambiguity, source evidence |
| preprocessing | Original and project transformations, order, parameters, code, fitted observations |
| QC | Criteria, exclusions, thresholds, source rationale, before/after summaries |
| missing_values_modalities | Missingness encoding, structural versus unmeasured entries, modality masks |
| original_source_publication | Accession, DOI, canonical source, and evidence tying files to publication |
| download_location | Provided URL, resolved file URL/ID when checked, access date and restrictions |
| local_path | Actual local location or unknown when absent |
| version_checksums | Acquisition snapshot ID and file manifest with bytes and SHA-256 |
| license_consent_access | Documented use terms, restrictions, and access requirements |
| verification_status | What was checked, by whom, when, and where evidence is stored |

## Future acquisition and validation

1. Verify access, provenance, permitted use, and file inventory before downloading data.
2. Record raw files immutably, with checksums and original names. Store derived outputs separately with preprocessing IDs.
3. Inspect matrix shape, orientation, identifiers, units, storage format, layers, and observation/feature uniqueness without assuming the schema from the extension.
4. Check observation matching across modalities and coordinate files. Record absent data without imputing them during inventory.
5. Trace annotations and any image-derived provenance; apply the project's image-exclusion policy before defining core inputs or evaluation.
6. Establish donor/sample/stage/batch relationships before choosing splits or claiming independent replication.
7. Record all uncertainty. No QC thresholds, normalization, biological label meaning, or data dimensions are preselected here.

## Registry conventions

All CSV files use UTF-8 with one header row, explicit `unknown` for unavailable metadata, `not_assessed` for pending review, and `not_applicable` only with an explanation in the detailed record. Header-only registries intentionally contain no observations. Registry IDs are unique and stable; aliases do not create duplicate datasets.

`datasets.csv` is a summary, not a substitute for a per-file/per-modality manifest. `user_provided_unverified` applies even where organism or stage fields contain the user's descriptive labels. `local_status=not_present` is supported by the bootstrap filesystem inventory; `access_status=not_checked` makes no assertion about whether Drive access is possible.

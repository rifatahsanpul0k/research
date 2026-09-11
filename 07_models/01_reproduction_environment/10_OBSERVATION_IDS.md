# Observation identity policy

Every adapter receives explicit observation IDs and emits an ordered ID sidecar. Stable IDs, not row positions, join RNA, ADT, ATAC, coordinates, labels and method outputs. Duplicate source IDs require a documented disambiguation key rather than silent suffixing.

Validation compares input and output ID sets and order. Any dropped observation is recorded with reason. The mapping original_observation_id ↔ method_internal_id is mandatory.

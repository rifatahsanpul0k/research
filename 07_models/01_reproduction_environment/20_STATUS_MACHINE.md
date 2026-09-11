# Status machine

Allowed states are PLANNED → PREPARING → RUNNING → SUCCEEDED, with FAILED, INVALID or BLOCKED terminal outcomes. Retries create a new attempt record without overwriting logs.

FAILED means execution failure. INVALID means scientific/provenance contract failure. BLOCKED means a prerequisite such as E18 ATAC is unavailable. None describes method performance.

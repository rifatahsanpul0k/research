# Failure handling

A failure record includes method, stage, error, environment, command, logs, attempted fix, source supporting the fix and resolution. Preserve stdout/stderr and exit code. Do not omit failed attempts from engineering history.

Retries use new attempt IDs. A workaround is classified under the patch policy before application.

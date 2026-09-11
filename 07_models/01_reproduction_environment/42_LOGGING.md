# Logging

Canonical scripts capture stdout.log, stderr.log and structured event records with timestamps, stage, status and durations. Notebook output is insufficient. Logs redact tokens, cookies and environment secrets.

The run controller writes status transitions atomically and preserves errors and tracebacks.

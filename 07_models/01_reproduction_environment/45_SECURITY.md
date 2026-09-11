# Security policy

Never commit tokens, passwords, SSH keys, cookies, cloud credentials, raw private data or environment secrets. external/, local virtual environments and experiment output directories are ignored.

Before completion and before any future commit, scan tracked changes and Repomix security output. Environment capture uses allowlisted fields rather than dumping all environment variables.

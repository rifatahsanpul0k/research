# Smoke-test policy

Allowed ENGINEERING_SMOKE_TEST actions are imports, CLI help, config parsing, official tiny data loading, one cheap forward pass and expected-file creation. Inputs and outputs must be labeled synthetic or upstream example. No smoke output enters experiments.csv or performance tables.

Each test records command, environment, commit, timestamp, exit status and logs. It stops before project-data fitting or comparative metrics.

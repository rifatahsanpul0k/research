# Method adapter design

Each adapter exposes prepare_input, run_method, collect_embedding, collect_native_output and record_metadata. Wrappers call official implementations and do not rewrite scientific logic. Method source remains under ignored external/ checkouts.

Adapter-specific transformations are declared DATA_ADAPTER patches. Any change to loss, graph construction or model logic is a SCIENTIFIC_LOGIC_CHANGE and requires separate review.

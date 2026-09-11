# Feature identity policy

RNA mappings preserve original ID, symbol, reference/annotation version and duplicate handling. ADT mappings preserve antibody/protein label, panel identity and duplicates. ATAC mappings preserve genome build and chromosome:start-end coordinates.

No adapter silently changes identifiers, merges duplicates or harmonizes features. Every derived mapping is saved with source and target IDs, operation, ambiguity and loss.

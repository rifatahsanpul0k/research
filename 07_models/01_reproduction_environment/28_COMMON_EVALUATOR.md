# Common evaluator

The evaluator accepts embedding, ordered IDs and optional labels, modality IDs, paired IDs and coordinates. Individual metric functions request only the fields they need and return value, status, parameters and warnings.

It rejects row mismatches and non-finite embeddings. It does not construct labels, infer pairing or silently build a graph. A monolithic hidden preprocessing path is prohibited.

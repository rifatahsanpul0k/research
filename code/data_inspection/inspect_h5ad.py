"""Read H5AD structure and descriptive values without modifying input or densifying X.

Requires h5py and numpy. Supports dense and CSR/CSC matrices and standard AnnData
categorical columns. Reports stored values, never infers biological count semantics.
"""
import argparse
import hashlib
import json
from pathlib import Path

import h5py
import numpy as np


def plain(value):
    if isinstance(value, bytes):
        return value.decode('utf-8')
    if isinstance(value, np.ndarray):
        return [plain(x) for x in value.tolist()]
    if isinstance(value, np.generic):
        return plain(value.item())
    if isinstance(value, list):
        return [plain(x) for x in value]
    return value


def sha256(path):
    with open(path, 'rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def column_values(obj):
    if isinstance(obj, h5py.Dataset):
        return plain(obj[()])
    if 'codes' in obj and 'categories' in obj:
        categories = plain(obj['categories'][()])
        return [None if x < 0 else categories[x] for x in obj['codes'][()]]
    raise ValueError(f'Unsupported column encoding at {obj.name}')


def dataframe(group):
    result = {}
    for key, obj in group.items():
        try:
            values = column_values(obj)
            unique = list(dict.fromkeys(values))
            result[key] = {'length': len(values), 'n_unique': len(unique),
                           'missing': sum(x is None for x in values),
                           'examples': values[:5]}
            if len(unique) <= 40:
                result[key]['values'] = unique
        except (ValueError, TypeError) as exc:
            result[key] = {'unsupported': str(exc)}
    return {'attrs': {k: plain(v) for k, v in group.attrs.items()}, 'columns': result}


def matrix_summary(obj):
    sparse = isinstance(obj, h5py.Group)
    if sparse:
        encoding = plain(obj.attrs.get('encoding-type', 'UNKNOWN'))
        if encoding not in ('csr_matrix', 'csc_matrix'):
            return {'unsupported_encoding': encoding}
        shape = tuple(int(x) for x in obj.attrs['shape'])
        data = obj['data']
        chunks = (data[start:start + 1000000] for start in range(0, data.size, 1000000))
    else:
        encoding, shape, data = 'dense', obj.shape, obj
        rows = max(1, 1000000 // max(1, int(np.prod(shape[1:]))))
        chunks = (data[start:start + rows] for start in range(0, shape[0], rows))
    nonzero = invalid = negative = noninteger = 0
    minimum, maximum = None, None
    for chunk in chunks:
        nonzero += int(np.count_nonzero(chunk))
        finite = np.isfinite(chunk)
        invalid += int(np.count_nonzero(~finite))
        vals = chunk[finite]
        if vals.size:
            low, high = float(vals.min()), float(vals.max())
            minimum = low if minimum is None else min(minimum, low)
            maximum = high if maximum is None else max(maximum, high)
            negative += int(np.count_nonzero(vals < 0))
            noninteger += int(np.count_nonzero(vals != np.floor(vals)))
    total = int(np.prod(shape))
    # Valid AnnData sparse matrices have unique coordinates. Without proving that,
    # distinguish stored-entry statistics from logical matrix sparsity.
    return {'shape': list(shape), 'encoding': encoding, 'dtype': str(data.dtype),
            'stored_entries': int(data.size), 'stored_nonzero_entries': nonzero,
            'finite_stored_min': minimum, 'finite_stored_max': maximum,
            'nonfinite_stored_entries': invalid, 'negative_stored_entries': negative,
            'noninteger_stored_entries': noninteger,
            'zero_fraction': (1 - nonzero / total) if not sparse and total else None,
            'sparse_note': 'Stored entries only; duplicate coordinates not canonicalized or summed.' if sparse else None}


def inspect(path):
    before = sha256(path)
    with h5py.File(path, 'r') as handle:
        result = {'filename': Path(path).name, 'bytes': Path(path).stat().st_size,
                  'root_attrs': {k: plain(v) for k, v in handle.attrs.items()},
                  'root_keys': list(handle.keys())}
        for key in ('obs', 'var'):
            if key in handle:
                result[key] = dataframe(handle[key])
        result['matrices'] = {}
        for key in ('X', 'raw/X'):
            if key in handle:
                result['matrices'][key] = matrix_summary(handle[key])
        if 'layers' in handle:
            for key, obj in handle['layers'].items():
                result['matrices'][f'layers/{key}'] = matrix_summary(obj)
        result['obsm'] = {}
        if 'obsm' in handle:
            for key, obj in handle['obsm'].items():
                result['obsm'][key] = {'shape': list(obj.shape), 'dtype': str(obj.dtype)} if isinstance(obj, h5py.Dataset) else {'group_keys': list(obj.keys())}
                if key == 'spatial' and isinstance(obj, h5py.Dataset):
                    result['obsm'][key]['examples'] = plain(obj[:3])
        result['uns_keys'] = list(handle['uns'].keys()) if 'uns' in handle else []
        result['uns_scalar_metadata'] = {}
        if 'uns' in handle:
            def scalar(name, obj):
                if isinstance(obj, h5py.Dataset) and obj.size <= 20:
                    result['uns_scalar_metadata'][name] = plain(obj[()])
            handle['uns'].visititems(scalar)
    after = sha256(path)
    if before != after:
        raise RuntimeError('Input checksum changed during inspection')
    result.update(sha256=after, input_unchanged=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.path), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()

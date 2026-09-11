"""Read-only, sparse-safe H5AD matrix summaries for Phase 1E.

The utility never writes to an input H5AD, densifies a matrix, filters rows or
features, or applies a transformation.  For CSR/CSC matrices it calculates
logical nonzero counts from stored values (explicit zeros are excluded) and
row totals/detections without materialising the matrix.
"""
import argparse, hashlib, json
from pathlib import Path
import h5py
import numpy as np

def decode(x):
    if isinstance(x, bytes): return x.decode("utf-8")
    if isinstance(x, np.generic): return decode(x.item())
    return x

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8_388_608), b""): h.update(block)
    return h.hexdigest()

def values(obj):
    if isinstance(obj, h5py.Dataset): return obj[()]
    enc = decode(obj.attrs.get("encoding-type", ""))
    shape = tuple(int(x) for x in obj.attrs["shape"])
    data = obj["data"][()]
    indices = obj["indices"][()]
    indptr = obj["indptr"][()]
    return enc, shape, data, indices, indptr

def stats(obj):
    sparse = isinstance(obj, h5py.Group)
    if sparse:
        enc, shape, data, indices, indptr = values(obj)
        n, p = shape
        # This phase's files use CSR. Handle CSC explicitly so the report is honest.
        if enc == "csr_matrix":
            row_sum = np.add.reduceat(data.astype(np.float64), indptr[:-1]) if n else np.array([])
            empty = np.diff(indptr) == 0
            row_sum[empty] = 0.0
            row_detect = np.zeros(n, dtype=np.int64)
            for i in range(n): row_detect[i] = np.count_nonzero(data[indptr[i]:indptr[i+1]])
        elif enc == "csc_matrix":
            row_sum = np.zeros(n, dtype=np.float64); row_detect = np.zeros(n, dtype=np.int64)
            for j in range(p):
                sl = data[indptr[j]:indptr[j+1]]
                ii = indices[indptr[j]:indptr[j+1]]
                row_sum[ii] += sl
                row_detect[ii] += (sl != 0)
        else: raise ValueError(f"unsupported sparse encoding {enc}")
        logical_nnz = int(np.count_nonzero(data))
        stored = int(data.size)
        finite = data[np.isfinite(data)]
        minv = float(finite.min()) if finite.size else None; maxv = float(finite.max()) if finite.size else None
        dtype = str(data.dtype)
    else:
        shape = tuple(int(x) for x in obj.shape); n, p = shape; enc = "dense"; dtype = str(obj.dtype)
        # Dense matrices in this repository are small enough for row summaries; read row chunks.
        rows = []
        for start in range(0, n, max(1, 1_000_000 // max(1, p))): rows.append(obj[start:start+max(1, 1_000_000 // max(1,p))])
        arr = np.concatenate(rows, axis=0) if rows else np.empty(shape)
        row_sum = arr.astype(np.float64).sum(axis=1); row_detect = np.count_nonzero(arr, axis=1)
        logical_nnz = int(np.count_nonzero(arr)); stored = int(arr.size)
        finite = arr[np.isfinite(arr)]; minv = float(finite.min()) if finite.size else None; maxv = float(finite.max()) if finite.size else None
    total = int(shape[0] * shape[1])
    def desc(a):
        a = np.asarray(a, dtype=np.float64)
        return {"min": float(a.min()) if a.size else None, "max": float(a.max()) if a.size else None,
                "mean": float(a.mean()) if a.size else None, "median": float(np.median(a)) if a.size else None,
                "variance_population": float(a.var()) if a.size else None}
    return {"shape": list(shape), "encoding": enc, "dtype": dtype, "stored_entries": stored,
            "logical_nonzero_entries": logical_nnz, "logical_zero_fraction": 1-logical_nnz/total if total else None,
            "stored_value_min": minv, "stored_value_max": maxv, "row_total": desc(row_sum),
            "row_detected_features": desc(row_detect), "total_stored_value_sum": float(np.asarray(data, dtype=np.float64).sum()) if sparse else float(arr.astype(np.float64).sum()),
            "explicit_zero_entries": stored-logical_nnz if sparse else int(stored-logical_nnz)}

def column_values(obj):
    if isinstance(obj, h5py.Dataset): return obj[()]
    if "codes" in obj and "categories" in obj:
        cat = obj["categories"][()]; codes = obj["codes"][()]
        return np.array([None if c < 0 else decode(cat[c]) for c in codes], dtype=object)
    return None

def inspect(path):
    before = sha(path)
    with h5py.File(path, "r") as f:
        out = {"path": str(path), "filename": path.name, "sha256": before, "root_keys": list(f.keys()), "matrices": {}, "obs_columns": {}, "var_columns": {}, "obsm": {}}
        for key in ("X", "raw/X"):
            if key in f: out["matrices"][key] = stats(f[key])
        if "layers" in f:
            for key, obj in f["layers"].items(): out["matrices"][f"layers/{key}"] = stats(obj)
        for group_name, dest in (("obs", "obs_columns"), ("var", "var_columns")):
            if group_name in f:
                g=f[group_name]
                for key,obj in g.items():
                    v=column_values(obj)
                    if v is not None:
                        vals=[decode(x) for x in v.tolist()]
                        uniq, counts=np.unique(np.asarray([x for x in vals if x is not None], dtype=object), return_counts=True) if vals else ([],[])
                        out[dest][key]={"length":len(vals),"missing":sum(x is None for x in vals),"n_unique":len(set(vals)),"values":{str(decode(k)):int(c) for k,c in zip(uniq,counts)} if len(uniq)<=100 else None}
        if "obsm" in f:
            for key,obj in f["obsm"].items():
                if isinstance(obj,h5py.Dataset):
                    item={"shape":list(obj.shape),"dtype":str(obj.dtype)}
                    if obj.size and obj.ndim==2: item.update({"min":float(np.nanmin(obj[()])),"max":float(np.nanmax(obj[()])),"examples":obj[:3].tolist()})
                    out["obsm"][key]=item
    if sha(path)!=before: raise RuntimeError("input checksum changed")
    out["input_unchanged"]=True
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("paths", nargs="+"); ap.add_argument("--output")
    a=ap.parse_args(); result=[inspect(Path(p)) for p in a.paths]
    text=json.dumps(result if len(result)>1 else result[0], indent=2, allow_nan=False)
    if a.output: Path(a.output).write_text(text+"\n")
    else: print(text)
if __name__=="__main__": main()

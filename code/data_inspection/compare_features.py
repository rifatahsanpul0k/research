"""Read-only comparison of AnnData obs/var identifiers; no harmonisation."""
import argparse, hashlib, json
from pathlib import Path
import h5py, numpy as np
def decode(x): return x.decode() if isinstance(x,bytes) else x.item() if isinstance(x,np.generic) else x
def ids(path, group):
    with h5py.File(path,"r") as f:
        g=f[group]; key=decode(g.attrs.get("_index","_index")); obj=g[key]
        if isinstance(obj,h5py.Dataset): return [str(decode(x)) for x in obj[()]]
        cat=obj["categories"][()]; return [str(decode(cat[x])) if x>=0 else None for x in obj["codes"][()]]
def compare(paths, group):
    arrays={str(p):ids(p,group) for p in paths}; names=list(arrays); sets={k:set(v) for k,v in arrays.items()}
    base=names[0]; inter=set.intersection(*(sets[k] for k in names)); union=set.union(*(sets[k] for k in names))
    pairwise={}
    for i,a in enumerate(names):
        for b in names[i+1:]:
            pairwise[f"{a} :: {b}"]={"overlap":len(sets[a]&sets[b]),"union":len(sets[a]|sets[b]),"same_order":arrays[a]==arrays[b]}
    return {"group":group,"files":names,"counts":{k:len(v) for k,v in arrays.items()},"same_ids":len({frozenset(s) for s in sets.values()})==1,
            "same_order":all(arrays[k]==arrays[base] for k in names),"overlap_all":len(inter),"union":len(union),"duplicates":{k:len(v)-len(set(v)) for k,v in arrays.items()},"pairwise":pairwise}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("group",choices=["obs","var"]); ap.add_argument("paths",nargs="+"); ap.add_argument("--output"); a=ap.parse_args(); out=compare(a.paths,a.group); text=json.dumps(out,indent=2)
    if a.output: Path(a.output).write_text(text+"\n")
    else: print(text)
if __name__=="__main__": main()

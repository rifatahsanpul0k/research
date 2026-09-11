"""Read-only CSV annotation summary; no label normalization or relabeling."""
import argparse,csv,json
from collections import Counter
from pathlib import Path
def summarize(path):
    with open(path,newline="") as f: rows=list(csv.DictReader(f))
    out={"path":str(path),"rows":len(rows),"columns":{}}
    for k in (rows[0].keys() if rows else []):
        vals=[r.get(k,"") for r in rows]; c=Counter(vals)
        item={"missing":sum(v=="" for v in vals),"n_unique":len(c)}
        # Identifier columns are deliberately summarized by cardinality only.
        if len(c)<=100: item["counts"]=dict(sorted(c.items(),key=lambda x:(-x[1],x[0])))
        out["columns"][k]=item
    return out
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("paths",nargs="+"); ap.add_argument("--output"); a=ap.parse_args(); out=[summarize(Path(p)) for p in a.paths]; text=json.dumps(out,indent=2,ensure_ascii=False)+"\n"; Path(a.output).write_text(text) if a.output else print(text)
if __name__=="__main__": main()

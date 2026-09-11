"""Read-only summary of AnnData obsm coordinate arrays."""
import argparse,json
from pathlib import Path
import h5py,numpy as np
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("paths",nargs="+"); ap.add_argument("--key",default="spatial"); ap.add_argument("--output"); a=ap.parse_args(); out=[]
    for p in a.paths:
        with h5py.File(p,"r") as f:
            if "obsm" not in f or a.key not in f["obsm"]: out.append({"path":p,"present":False}); continue
            x=f["obsm"][a.key][()]; out.append({"path":p,"present":True,"shape":list(x.shape),"dtype":str(x.dtype),"min":float(np.nanmin(x)),"max":float(np.nanmax(x)),"unique_rows":int(np.unique(x,axis=0).shape[0]),"examples":x[:3].tolist()})
    text=json.dumps(out,indent=2)+"\n"; Path(a.output).write_text(text) if a.output else print(text)
if __name__=="__main__": main()

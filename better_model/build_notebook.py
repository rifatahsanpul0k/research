"""Build a portable notebook with an embedded, checksum-verified source bundle."""

import base64
import hashlib
import io
import json
from pathlib import Path
import textwrap
import zipfile


def build():
    root = Path(__file__).resolve().parent
    buffer = io.BytesIO()
    paths = [p for p in root.glob("*.py") if p.name != Path(__file__).name]
    paths += list(root.glob("configs/*.json")) + list(root.glob("tests/*.py")) + [root / "requirements.txt"]
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(paths):
            info = zipfile.ZipInfo("better_model/" + str(path.relative_to(root)), date_time=(2026, 9, 25, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
    bundle = buffer.getvalue()
    encoded = base64.b64encode(bundle).decode()
    digest = hashlib.sha256(bundle).hexdigest()
    cells = []

    def cell(kind, source):
        item = {"cell_type": kind, "metadata": {}, "source": textwrap.dedent(source).strip().splitlines(keepends=True)}
        item["id"] = f"astra-{len(cells):02d}"
        if kind == "code":
            item.update(execution_count=None, outputs=[])
        cells.append(item)

    cell("markdown", """
    # ASTRA — working model from `hello.py`

    This notebook runs the user's preferred gated spatial DEC model. The default **reference**
    configuration preserves its layers, loss weights, 250 + 150 epochs and silhouette selection.
    The **affinity candidate** changes graph weights and rejects degenerate partitions; higher
    biological ARI has **not** been demonstrated for that candidate.

    Upload this notebook to Colab and select a GPU runtime. It contains the Python modules and
    configs, so a GitHub push is not needed. Raw data are read from your dataset directory.
    Each seed gets its own checkpoint, AnnData output, metrics, configuration and source hashes.
    All observations participate in training: this is **transductive spatial clustering**.
    """)
    cell("code", f'''
from pathlib import Path
import base64, hashlib, io, os, sys, tempfile, zipfile

# Use the repository when available; otherwise unpack the exact bundled source.
SOURCE_BUNDLE = {encoded!r}
SOURCE_SHA256 = {digest!r}
roots = [Path.cwd(), Path.cwd().parent]
PROJECT_ROOT = next((p for p in roots if (p / "better_model/run.py").is_file()), None)
if PROJECT_ROOT is None:
    payload = base64.b64decode(SOURCE_BUNDLE)
    assert hashlib.sha256(payload).hexdigest() == SOURCE_SHA256
    PROJECT_ROOT = Path(tempfile.gettempdir()) / ("astra-" + SOURCE_SHA256[:12])
    PROJECT_ROOT.mkdir(exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        for name in archive.namelist():
            target = (PROJECT_ROOT / name).resolve()
            if not target.is_relative_to(PROJECT_ROOT.resolve()):
                raise ValueError("Invalid bundle path")
        archive.extractall(PROJECT_ROOT)
os.chdir(PROJECT_ROOT)
sys.path.insert(0, str(PROJECT_ROOT))
print("Source:", PROJECT_ROOT)
''')
    cell("code", """
    import subprocess
    IN_COLAB = "google.colab" in sys.modules or Path("/content").exists()
    # On a local machine, use an environment with requirements.txt installed.
    if IN_COLAB:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r",
                        str(PROJECT_ROOT / "better_model/requirements.txt")], check=True)
    import torch
    print("PyTorch:", torch.__version__, "CUDA:", torch.cuda.is_available())
    """)
    cell("markdown", """
    Set `DATA_ROOT` to the directory containing dataset subdirectories. Both layouts work:
    `DATA_ROOT/10x_human_lymph_node_A1/adata_RNA.h5ad` and
    `DATA_ROOT/10x_human_lymph_node_A1/raw/adata_RNA.h5ad`.
    Each A1/D1 directory also needs `adata_ADT.h5ad` and `annotation.csv`.
    Input barcodes and coordinates are checked before training; no files are downloaded or overwritten.
    """)
    cell("code", """
    if IN_COLAB:
        from google.colab import drive
        drive.mount("/content/drive")
    DATA_ROOT = Path("/content/drive/MyDrive/Colab/ARISE/data") if IN_COLAB else PROJECT_ROOT / "04_datasets"
    OUTPUT_ROOT = Path("/content/drive/MyDrive/ASTRA_runs") if IN_COLAB else PROJECT_ROOT / "better_model/outputs"
    PROFILE = "reference"  # Or "affinity_candidate" for the separate unvalidated candidate.
    DATASETS = ["10x_human_lymph_node_A1", "10x_human_lymph_node_D1"]
    SMOKE = False  # True: 48 synthetic spots, five epochs, CPU; not a biological benchmark.
    print("Data:", DATA_ROOT, "Outputs:", OUTPUT_ROOT)
    """)
    cell("code", """
    import json
    from better_model.run import load_inputs, smoke_config, write_json
    from better_model.config import ModelConfig, PreprocessConfig
    configuration = smoke_config() if SMOKE else json.loads(
        (PROJECT_ROOT / "better_model/configs" / f"{PROFILE}.json").read_text())
    if not SMOKE:
        configuration["datasets"] = [x for x in configuration["datasets"] if x["name"] in DATASETS]
        assert len(configuration["datasets"]) == len(DATASETS), "Dataset is absent from the selected config"
        for spec in configuration["datasets"]:
            rna, aux, annotations, source = load_inputs(spec, DATA_ROOT)
            print(spec["name"], rna.shape, aux.shape, "K =", spec["n_clusters"])
            del rna, aux, annotations
        assert torch.cuda.is_available(), "Enable a GPU runtime for the full reference benchmark"
    print(json.dumps(configuration, indent=2))
    """)
    cell("markdown", """
    K is frozen to the reference's annotation cardinality (A1: 10; D1: 11, including `Exclude`).
    That is privileged information and is recorded as reference-assisted K. ARI/NMI are computed
    only after checkpoint selection. The mean/std summarizes optimization seeds, not independent
    biological replicates. Keep D1's exclusion policy identical when comparing with earlier runs.
    """)
    cell("code", """
    from datetime import datetime, timezone
    from better_model.run import run_suite
    run_id = datetime.now(timezone.utc).strftime("EXP-%Y%m%d-%H%M%S-%f")
    RUN_DIR = OUTPUT_ROOT / f"{run_id}-{PROFILE}"
    run_suite(configuration, DATA_ROOT, RUN_DIR, smoke=SMOKE)
    print("Completed:", RUN_DIR)
    """)
    cell("code", """
    import pandas as pd
    metrics = pd.read_csv(RUN_DIR / "metrics.csv")
    display(metrics)
    display(metrics.groupby(["dataset", "method"])[["ari", "nmi", "silhouette", "max_cluster_fraction"]].agg(["mean", "std"]))
    """)
    cell("code", """
    import anndata as ad
    import matplotlib.pyplot as plt
    # Explicit dataset/seed selection: never accidentally plot the last loop iteration.
    dataset = configuration["datasets"][0]["name"]
    seed = configuration["seeds"][0]
    seed_dir = RUN_DIR / dataset / f"seed_{seed}"
    result = ad.read_h5ad(seed_dir / "result.h5ad")
    positions = result.obsm["spatial"]
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    if "reference_annotation" in result.obs:
        labels = pd.factorize(result.obs["reference_annotation"])[0]
        axes[0].scatter(*positions.T, c=labels, s=8, cmap="tab20")
    axes[0].set_title("Reference annotations")
    axes[1].scatter(*positions.T, c=pd.factorize(result.obs["astra_cluster"])[0], s=8, cmap="tab20")
    axes[1].set_title("ASTRA selected partition")
    image = axes[2].scatter(*positions.T, c=result.obs["mean_rna_gate"], s=8, cmap="coolwarm", vmin=0, vmax=1)
    axes[2].set_title("Mean RNA gate (model weight)")
    fig.colorbar(image, ax=axes[2])
    for axis in axes:
        axis.set_aspect("equal")
        axis.invert_yaxis()
        axis.axis("off")
    fig.suptitle(f"{dataset}, seed {seed}")
    plt.show()
    history = pd.read_json(seed_dir / "history.jsonl", lines=True)
    history.plot(x="epoch", y=["total_loss", "reconstruction_loss"], figsize=(9, 3))
    plt.show()
    """)
    cell("markdown", """
    `result.X` contains observed log-normalized HVG expression. `reconstructed_scaled_rna` is
    model output in standardized units. It must not be used as count data or for the reference's
    automatic marker test. Gate maps describe internal model weighting, not biological importance.

    To compare the candidate, change `PROFILE`, rerun configuration and training, then compare the
    two `metrics.csv` files by dataset and seed. Do not promote a new model based on a single seed
    or on whichever test dataset happens to improve. Review the supplied audit and benchmark plan.
    """)
    notebook = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                 "language_info": {"name": "python", "version": "3.11"}, "colab": {"name": "ASTRA_working_model.ipynb"}},
                "nbformat": 4, "nbformat_minor": 5}
    (root / "ASTRA_working_model.ipynb").write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n")
    print("Built", root / "ASTRA_working_model.ipynb", "bundle SHA256", digest)


if __name__ == "__main__":
    build()

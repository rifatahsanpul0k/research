"""Frozen Phase 3D configuration generation and validation; no model execution."""
from pathlib import Path
import hashlib
import json

START_COMMIT = '951a61ca15239a7f644b60ec56dd1a463cd5570f'
MOFA_COMMIT = '90418e5021b3ae735ebf1fea5d7e07cae71c8bb7'
SCOT_COMMIT = '14649be6e14017dcfe7ba619091b33d1df55f6a9'
SEEDS = (1729, 2718, 31415)
DATASETS = {
 'LN_A1': ('10x_human_lymph_node_A1','ADT','annotation.csv','manual-anno'),
 'LN_D1': ('10x_human_lymph_node_D1','ADT','annotation.csv','manual-anno'),
 'MB_E11': ('Mouse_Brain_E11_S1','ATAC','anno.csv','cluster'),
 'MB_E13': ('Mouse_Brain_E13_S1','ATAC','anno.csv','cluster'),
 'MB_E15': ('Mouse_Brain_E15_S1','ATAC','anno.csv','cluster'),
}


def configs():
    for method in ('MOFAPLUS', 'SCOT'):
        for dataset, (folder, second, annotation, label) in DATASETS.items():
            for seed in SEEDS:
                c = dict(experiment_id=f'EXP-{dataset.replace("_","-")}-{method}-KMEANS-S{seed}',
                    method=method, dataset=dataset, folder=folder, second_modality=second,
                    annotation=annotation, label_column=label, seed=seed, start_commit=START_COMMIT,
                    compute_classification='COLAB_CPU' if method=='MOFAPLUS' else 'COLAB_HIGH_MEMORY',
                    series='PHASE_3D_S1',
                    source_semantics='SOURCE_PROVIDED_PROCESSED_X_COUNTS_UNKNOWN',
                    rna_features=2000, mofa_atac_features=2000, timeout_seconds=3600,
                    official_commit=MOFA_COMMIT if method=='MOFAPLUS' else SCOT_COMMIT,
                    evaluation='PHASE_3C_KMEANS_ARI_NMI_SILHOUETTE',
                    preprocessing='RNA_LOG1P_TOP2000_ZSCORE;ADT_PHASE3C_CLR_ZSCORE;MOFA_ATAC_LOG1P_TOP2000_ZSCORE;SCOT_ATAC_PHASE3C_LSI30',
                    output_directory=f'08_experiments/EXP-{dataset.replace("_","-")}-{method}-KMEANS-S{seed}')
                if method=='MOFAPLUS':
                    c.update(data_options=dict(scale_views=True,scale_groups=False,center_groups=True,use_float32=False),
                        model_options=dict(factors=10,spikeslab_factors=False,spikeslab_weights=True,ard_factors=False,ard_weights=True),
                        train_options=dict(iter=1000,startELBO=1,freqELBO=5,startSparsity=50,convergence_mode='fast',
                            startDrop=1,freqDrop=1,dropR2=None,nostop=False,verbose=False,quiet=False,
                            gpu_mode=False,weight_views=False,save_interrupted=False))
                else:
                    c.update(k=50,epsilon=0.001,solver_defaults=dict(max_iter=1000,tol=1e-9,solver='PGD',
                        sinkhorn_numItermax=1000,sinkhorn_stopThr=1e-9), self_tune=False, projection='SECOND_ONTO_RNA')
                yield c


def validate_config(c):
    if c['dataset'] not in DATASETS:
        raise ValueError('dataset excluded; E18 ATAC remains unverified')
    expected = next((x for x in configs() if x['experiment_id']==c['experiment_id']), None)
    if expected is None or c != expected:
        raise ValueError('configuration differs from frozen Phase 3D series')
    return c


if __name__ == '__main__':
    destination = Path('07_models/02_classical_integration/configs')
    destination.mkdir(parents=True,exist_ok=True)
    records={}
    for c in configs():
        p=destination/(c['experiment_id']+'.json')
        content=json.dumps(c,indent=2,sort_keys=True)+'\n'
        if p.exists() and p.read_text()!=content:
            raise ValueError('refusing to overwrite changed frozen config')
        p.write_text(content)
        records[str(p)]=hashlib.sha256(content.encode()).hexdigest()
    Path('07_models/02_classical_integration/CONFIG_CHECKSUMS.json').write_text(json.dumps(records,indent=2)+'\n')

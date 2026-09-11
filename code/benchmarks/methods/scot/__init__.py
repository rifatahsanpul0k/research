"""Official SCOT v1 wrapper: native coupling and explicit second-view-to-RNA projection."""
import importlib.util
from pathlib import Path
import numpy as np


def load_official(source_root):
    path = Path(source_root) / 'src/scotv1.py'
    spec = importlib.util.spec_from_file_location('astra_official_scotv1', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.SCOT


def validate_coupling(plan, rows, columns, tolerance=1e-4):
    if plan.shape != (rows, columns) or not np.isfinite(plan).all() or np.any(plan < 0):
        raise ValueError('invalid SCOT coupling shape or values')
    row_error = float(np.max(np.abs(plan.sum(1) - 1 / rows)))
    col_error = float(np.max(np.abs(plan.sum(0) - 1 / columns)))
    if row_error > tolerance or col_error > tolerance or abs(plan.sum()-1) > tolerance:
        raise ValueError(f'invalid SCOT marginals: {row_error}, {col_error}')
    return {'row_marginal_max_error': row_error, 'column_marginal_max_error': col_error}


def fit(views, ids, features, config, output):
    if len(views) != 2 or any(x.shape[0] != len(ids) for x in views):
        raise ValueError('two views with explicit full observation coverage required')
    if len(set(ids)) != len(ids) or any(not np.isfinite(x).all() for x in views):
        raise ValueError('invalid identities or input values')
    SCOT = load_official(config['official_source_root'])
    # The solver receives matrices only; known pairing and labels are withheld.
    permutation = np.random.default_rng(0).permutation(len(ids))
    model = SCOT(views[0].copy(), views[1][permutation].copy())
    model.normalize(norm='l2')
    model.init_marginals()
    model.construct_graph(k=config['k'], mode='connectivity', metric='correlation')
    from scipy.sparse.csgraph import connected_components
    components = [int(connected_components(g, directed=False)[0]) for g in (model.Xgraph, model.ygraph)]
    model.init_distances()
    model.find_correspondences(e=config['epsilon'], verbose=True)
    if model.coupling is not None:
        np.savez_compressed(output / 'coupling.npz', coupling=model.coupling,
                            row_ids=np.asarray(ids), column_ids=np.asarray(ids)[permutation])
    if not model.flag:
        raise ValueError('official SCOT convergence flag is false; coupling preserved')
    diagnostics = validate_coupling(model.coupling, len(ids), len(ids))
    _, projected = model.barycentric_projection(XontoY=False)
    z = projected[np.argsort(permutation)]
    np.savez_compressed(output / 'native_alignment.npz', rna=model.X, projected_second=z,
                        observation_ids=np.asarray(ids))
    diagnostics.update({'official_flag': bool(model.flag), 'gw_distance': float(model.gwdist),
        'connected_components': components, 'projection': 'diag(1 / coupling.sum(axis=0)) @ coupling.T @ L2_RNA',
        'source_domain': config['second_modality'], 'target_domain': 'RNA',
        'pairing_used_in_fit': False, 'second_permutation_seed': 0,
        'distance_policy': 'official undirected kNN shortest paths; disconnected distances capped at finite maximum; max normalization',
        'solver': 'POT.entropic_gromov_wasserstein; pinned library defaults; square_loss'})
    return z, diagnostics

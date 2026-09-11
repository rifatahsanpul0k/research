"""Thin wrapper around the official mofapy2 implementation."""
import numpy as np


def fit(views, ids, features, config, output):
    if len(views) != 2 or any(x.shape[0] != len(ids) for x in views):
        raise ValueError('MOFA requires two aligned views')
    if len(set(ids)) != len(ids) or any(not np.isfinite(x).all() for x in views):
        raise ValueError('invalid identities or nonfinite input')
    view_names = ['RNA', config['second_modality']]
    if len(features) != len(view_names) or any(len(names) != x.shape[1] for names, x in zip(features, views, strict=True)):
        raise ValueError('feature identity lists must match the two view dimensions')
    from mofapy2.run.entry_point import entry_point
    ent = entry_point()
    ent.set_data_options(**config['data_options'])
    # mofapy2 enforces global feature-name uniqueness; namespace IDs without
    # changing their modality-specific biological identity in project metadata.
    namespaced_features = [[f'{view}::{name}' for name in names] for view, names in zip(view_names, features, strict=True)]
    ent.set_data_matrix([[x.copy()] for x in views], likelihoods=['gaussian'] * 2,
                        views_names=view_names, groups_names=['dataset'],
                        samples_names=[ids], features_names=namespaced_features)
    ent.set_model_options(**config['model_options'])
    ent.set_train_options(**config['train_options'], seed=config['seed'])
    ent.build()
    ent.run()
    z = ent.model.getNodes()['Z'].getExpectation().copy()
    weights = ent.model.getNodes()['W'].getExpectation()
    np.savez_compressed(output / 'loadings.npz', **{f'view_{i}': w for i, w in enumerate(weights)})
    stats = ent.model.getTrainingStats()
    np.savez_compressed(output / 'training_stats.npz', **{k: v for k, v in stats.items() if k != 'elbo_terms'})
    finite_elbo = np.asarray(stats['elbo'])[np.isfinite(stats['elbo'])]
    metadata = {
        'implementation': 'mofapy2.run.entry_point.entry_point',
        'feature_id_namespace': 'view_name::original_feature_id',
        'factors_shape': list(z.shape), 'loading_shapes': [list(w.shape) for w in weights],
        'data_options': ent.data_opts, 'model_options': ent.model_opts, 'train_options': ent.train_opts,
        'variance_explained_per_factor': ent.model.calculate_variance_explained(),
        'variance_explained_total': ent.model.calculate_variance_explained(total=True),
        'finite_elbo_evaluations': len(finite_elbo),
        'last_finite_elbo': float(finite_elbo[-1]) if len(finite_elbo) else None,
        'training_iterations': len(stats['number_factors']),
        'convergence_assessment': 'inspect recorded ELBO trajectory and upstream stdout; successful return alone is not convergence',
    }
    return z, metadata

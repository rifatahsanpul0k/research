"""Check Phase 2A synthetic arithmetic only; never read datasets or fit models.

Run: python3 code/data_inspection/check_phase2a_toys.py
Requires numpy. Uses fixed tiny arrays, explicit factors and hand-assigned labels.
"""
import json
import math
from collections import Counter
from itertools import combinations, permutations

import numpy as np

CHECKS = []


def check(name, actual, expected, atol=1e-10):
    if not np.allclose(actual, expected, rtol=1e-10, atol=atol):
        raise AssertionError(f"{name}: {actual!r} != {expected!r}")
    CHECKS.append(name)


def contingency(y, c):
    if len(y) != len(c) or len(y) < 2:
        raise ValueError("Toy partitions require the same n >= 2.")
    joint = Counter(zip(c, y))
    return joint, Counter(c), Counter(y)


def choose2(n):
    return n * (n - 1) // 2


def ari(y, c):
    joint, rows, cols = contingency(y, c)
    together = sum(choose2(v) for v in joint.values())
    a = sum(choose2(v) for v in rows.values())
    b = sum(choose2(v) for v in cols.values())
    expected = a * b / choose2(len(y))
    denom = (a + b) / 2 - expected
    return 1.0 if denom == 0 else (together - expected) / denom


def entropy(prob):
    return -sum(p * math.log(p) for p in prob if p > 0)


def information(y, c):
    joint, rows, cols = contingency(y, c)
    n = len(y)
    mi = sum((v / n) * math.log(v * n / (rows[a] * cols[b]))
             for (a, b), v in joint.items())
    hc = entropy([v / n for v in rows.values()])
    hy = entropy([v / n for v in cols.values()])
    return mi, hc, hy, 1.0 if hc + hy == 0 else 2 * mi / (hc + hy)


def silhouette(dist, labels):
    labels = np.array(labels)
    groups = set(labels.tolist())
    if not 2 <= len(groups) <= len(labels) - 1:
        raise ValueError("Silhouette needs 2 through n-1 clusters.")
    result = []
    for i in range(len(labels)):
        own = np.flatnonzero(labels == labels[i])
        own = own[own != i]
        if not len(own):
            result.append(0.0)
            continue
        a = dist[i, own].mean()
        b = min(dist[i, labels == g].mean() for g in groups if g != labels[i])
        result.append(0.0 if max(a, b) == 0 else (b - a) / max(a, b))
    return np.array(result)


def main():
    x = np.array([[2, 1, 0], [3, 0, 1], [8, 7, 6], [9, 8, 5]], dtype=float)
    means = x.mean(axis=0)
    xc = x - means
    check("means", means, [5.5, 4, 3])
    check("centered column sums", xc.sum(axis=0), [0, 0, 0])
    cross = np.array([[37, 42, 30], [42, 50, 34], [30, 34, 26]], dtype=float)
    check("centered cross-products", xc.T @ xc, cross)
    check("sample covariance independently via numpy", np.cov(x, rowvar=False), cross / 3)
    check("sample variances", x.var(axis=0, ddof=1), [37 / 3, 50 / 3, 26 / 3])
    check("population variances", x.var(axis=0), [37 / 4, 50 / 4, 26 / 4])
    check("feature correlation", np.corrcoef(x.T)[0, 1], 42 / math.sqrt(1850))
    distances = np.linalg.norm(x[:, None, :] - x[None, :, :], axis=2)
    check("all squared distances", distances**2,
          [[0, 3, 108, 123], [3, 0, 99, 116], [108, 99, 0, 3], [123, 116, 3, 0]])
    check("Manhattan", np.abs(x[0] - x[1]).sum(), 3)
    check("dot product", x[0] @ x[1], 6)
    check("cosine", x[0] @ x[1] / np.linalg.norm(x[0]) / np.linalg.norm(x[1]),
          6 / math.sqrt(50))
    check("profile correlation", np.corrcoef(x[:2])[0, 1], 3 / math.sqrt(21))
    z = xc / x.std(axis=0, ddof=1)
    check("standardized means", z.mean(axis=0), [0, 0, 0])
    check("standardized sample variances", z.var(axis=0, ddof=1), [1, 1, 1])
    w = np.array([[1, 0, 1], [0, 2, 0]])
    check("matrix product", x @ w.T, [[2, 2], [4, 0], [14, 14], [14, 16]])
    check("affine map", x @ w.T + [1, -1], [[3, 1], [5, -1], [15, 13], [15, 15]])

    a = np.array([[2, 1], [1, 2]])
    q = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    check("eigenvectors orthonormal", q.T @ q, np.eye(2))
    check("eigen relations", a @ q, q @ np.diag([3, 1]))
    check("eigen reconstruction", q @ np.diag([3, 1]) @ q.T, a)
    b = np.array([[3, 0, 0], [0, 1, 0]])
    u, d, vt = np.eye(2), np.diag([3, 1]), np.array([[1, 0, 0], [0, 1, 0]])
    check("thin SVD reconstruction", u @ d @ vt, b)
    check("thin right factors orthonormal", vt @ vt.T, np.eye(2))
    check("full SVD reconstruction", np.eye(2) @ b @ np.eye(3), b)
    check("singular values from Gram", b.T @ b, np.diag([9, 1, 0]))
    b1 = 3 * np.outer(u[:, 0], vt[0])
    check("rank-one residual", np.square(b - b1).sum(), 1)
    check("energy retained", np.square(b1).sum() / np.square(b).sum(), 0.9)
    f = lambda t: (t - 3)**2
    check("forward finite difference", (f(1.01) - f(1)) / .01, -3.99)
    t1 = 1 - .1 * (-4)
    check("gradient update one", t1, 1.4)
    t2 = t1 - .1 * 2 * (t1 - 3)
    check("gradient update two", t2, 1.72)
    check("gradient losses", [f(1), f(t1), f(t2)], [4, 2.56, 1.6384])
    check("RBF bandwidth 1", math.exp(-distances[0, 1]**2 / 2), math.exp(-1.5))
    check("RBF bandwidth 2", math.exp(-distances[0, 1]**2 / 8), math.exp(-.375))

    p, qprob = [.75, .25], [.5, .5]
    hp = entropy(p)
    cross_entropy = -sum(pv * math.log(qv) for pv, qv in zip(p, qprob))
    kl = sum(pv * math.log(pv / qv) for pv, qv in zip(p, qprob))
    check("KL equals cross-entropy minus entropy", kl, cross_entropy - hp)
    check("entropy", hp, 0.5623351446188083)
    check("entropy bits", hp / math.log(2), 0.8112781244591328)
    check("KL forward", kl, 0.13081203594113697)

    y = [0, 0, 1, 1]
    crossed = [0, 1, 0, 1]
    partial = [0, 0, 0, 1]
    agreements = sum((y[i] == y[j]) == (crossed[i] == crossed[j])
                     for i, j in combinations(range(4), 2))
    check("Rand index by six pairs", agreements / 6, 1 / 3)
    check("ARI crossed", ari(y, crossed), -.5)
    check("ARI identical under relabeling", ari(y, ["u", "u", "v", "v"]), 1)
    check("ARI partial", ari(y, partial), 0)
    check("ARI fixed-margin null expectation",
          np.mean([ari(y, c) for c in set(permutations(y))]), 0)
    check("ARI singleton convention", ari(range(4), ["a", "b", "c", "d"]), 1)
    check("NMI crossed", information(y, crossed)[3], 0)
    check("NMI matching", information(y, y)[3], 1)
    check("MI partial", information(y, partial)[0], .21576155433883565)
    check("NMI partial", information(y, partial)[3], .3437110184854508)
    check("NMI both constant convention", information([0]*4, [1]*4)[3], 1)
    check("NMI one constant", information(y, [0]*4)[3], 0)
    ss = silhouette(distances, y)
    check("silhouette values", ss,
          [.838750308651424, .832815274303423, .829708426963917, .841538684620838],
          atol=1e-8)
    check("silhouette mean", ss.mean(), .8357031736349004)
    check("silhouette singleton convention", silhouette(distances, [0, 1, 1, 1])[0], 0)
    check("silhouette coincident convention", silhouette(np.zeros((4, 4)), y), [0]*4)
    try:
        silhouette(distances, [0]*4)
    except ValueError:
        CHECKS.append("silhouette ineligible partition rejected")
    else:
        raise AssertionError("Expected invalid silhouette partition.")

    check("Bernoulli MLE derivative", 2 / (2 / 3) - 1 / (1 - 2 / 3), 0)
    check("posterior integral", 12 * (1 / 3 - 1 / 4), 1)
    check("posterior mean", 12 * (1 / 4 - 1 / 5), .6)
    check("posterior variance", 12 * (1 / 5 - 1 / 6) - .6**2, .04)
    check("Gaussian two-sided p", math.erfc(4 / math.sqrt(2)), .00006334248366623996)
    check("masked mean", np.array([2., 0.]).mean(), 1)
    check("confusion metrics", [7/10, 3/4, 3/5, 4/5, 6/9], [.7, .75, .6, .8, 2/3])
    print(json.dumps({"scope": "synthetic arithmetic only", "checks_passed": len(CHECKS),
                      "checks": CHECKS, "mean_silhouette": float(ss.mean())}, indent=2))


if __name__ == "__main__":
    main()

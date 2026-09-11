"""Fixed synthetic arithmetic validation only; no project-data input or model training."""
import numpy as np

checks = 0


def equal(actual, expected, atol=1e-6):
    global checks
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=0)
    checks += 1


X = np.array([[4, 0, 1], [5, 1, 1], [0, 5, 4], [1, 6, 5], [3, 2, 2]], dtype=float)
mu = X.mean(axis=0)
equal(mu, [2.6, 2.8, 2.6])
Xc = X - mu
equal(Xc.sum(axis=0), [0, 0, 0])
C = Xc.T @ Xc / 4
equal(C, [[4.3, -4.85, -3.45], [-4.85, 6.7, 4.65], [-3.45, 4.65, 3.3]])
equal(np.poly(C), [1, -14.3, 8.0625, -0.3375])
s = X.std(axis=0, ddof=1)
equal(s, [2.073644, 2.588436, 1.816590])
T = Xc / s
equal(T, [[.675140, -1.081734, -.880771], [1.157383, -.695401, -.880771],
          [-1.253831, .849934, .770675], [-.771589, 1.236268, 1.321157],
          [.192897, -.309067, -.330289]])
equal(T.mean(axis=0), [0, 0, 0])
equal(T.var(axis=0, ddof=1), [1, 1, 1])
equal(T * s + mu, X)
# Eigensolver checks the manually derived 3x3 covariance polynomial.
values, W = np.linalg.eigh(C)
order = np.argsort(values)[::-1]
values, W = values[order], W[:, order]
W *= np.where(W[0] >= 0, 1, -1)
equal(values, [13.713887, .540589, .045525])
equal(W, [[.534389, .842232, .071224], [-.691637, .484160, -.535936],
          [-.485866, .237137, .841249]])
equal(C @ W, W * values)
equal(W.T @ W, np.eye(3))
Z = Xc @ W
equal(Z, [[3.462115, -.555941, .254336], [3.304867, .770451, -.210377],
          [-3.591227, -.792661, -.186492], [-4.234341, .770869, .190044],
          [1.058585, -.192717, -.047511]])
equal(Z.T @ Z / 4, np.diag(values))
equal(values / values.sum(), [.959013, .037803, .003184])
equal(Z @ W.T + mu, X)
Xhat = Z[:, :2] @ W[:, :2].T + mu
equal(((X - Xhat) ** 2).sum(), 4 * values[2])
equal(((X - Xhat) ** 2).sum(), .182098)
equal(Xhat[0], [3.981885, .136308, .786040])
U, singular, Vt = np.linalg.svd(Xc, full_matrices=False)
equal(singular ** 2 / 4, values)
equal((U * singular) @ Vt, Xc)
D2 = ((X[:, None, :] - X[None, :, :]) ** 2).sum(axis=2)
equal(D2, [[0, 2, 50, 61, 6], [2, 0, 50, 57, 6], [50, 50, 0, 3, 22],
           [61, 57, 3, 0, 29], [6, 6, 22, 29, 0]])
D = np.sqrt(D2)
equal(D, [[0, 1.414214, 7.071068, 7.810250, 2.449490],
          [1.414214, 0, 7.071068, 7.549834, 2.449490],
          [7.071068, 7.071068, 0, 1.732051, 4.690416],
          [7.810250, 7.549834, 1.732051, 0, 5.385165],
          [2.449490, 2.449490, 4.690416, 5.385165, 0]])
norms = np.linalg.norm(X, axis=1)
equal(norms ** 2, [17, 27, 41, 62, 17])
B = (X @ X.T) / np.outer(norms, norms)
equal(B, [[1, .980196, .151511, .277218, .823529],
          [.980196, 1, .270501, .391059, .886844],
          [.151511, .270501, 1, .991704, .681799],
          [.277218, .391059, .991704, 1, .770051],
          [.823529, .886844, .681799, .770051, 1]])
neighbors = [sorted((j for j in range(5) if j != i), key=lambda j: (D2[i, j], j))[:2]
             for i in range(5)]
equal(neighbors, [[1, 4], [0, 4], [3, 4], [2, 4], [0, 1]])
A = np.zeros((5, 5), dtype=int)
for i, js in enumerate(neighbors):
    A[i, js] = 1
equal(A, [[0, 1, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 1, 1],
          [0, 0, 1, 0, 1], [1, 1, 0, 0, 0]])
equal(A.sum(), 10)
equal(np.maximum(A, A.T)[[2, 3], 4], [1, 1])
equal(np.minimum(A, A.T)[[2, 3], 4], [0, 0])
K = np.exp(-D2 / 10)
equal(K, [[1, .818731, .006738, .002243, .548812],
          [.818731, 1, .006738, .003346, .548812],
          [.006738, .006738, 1, .740818, .110803],
          [.002243, .003346, .740818, 1, .055023],
          [.548812, .548812, .110803, .055023, 1]])
assert np.linalg.eigvalsh(K).min() > 0
assert np.linalg.eigvalsh(B).min() > -1e-12
checks += 2
equal(-10 * np.log(K), D2)
prototypes = np.vstack([X[[0, 1, 4]].mean(axis=0), X[[2, 3]].mean(axis=0)])
equal(prototypes, [[4, 1, 4 / 3], [.5, 5.5, 4.5]])
R2 = ((X[:, None, :] - prototypes[None, :, :]) ** 2).sum(axis=2)
equal(R2, [[10 / 9, 54.75], [10 / 9, 52.75], [352 / 9, .75], [427 / 9, .75], [22 / 9, 24.75]])
equal(np.sqrt(R2), [[1.054093, 7.399324], [1.054093, 7.262920],
                    [6.253888, .866025], [6.887993, .866025], [1.563472, 4.974937]])
equal(np.argmin(R2, axis=1), [0, 0, 1, 1, 0])
P = np.exp(-R2 / 10)
P /= P.sum(axis=1, keepdims=True)
equal(P, [[.995339, .004661], [.994313, .005687], [.021122, .978878],
          [.009290, .990710], [.902960, .097040]])
equal(P.sum(axis=1), np.ones(5))
equal(np.argmax(P, axis=1), np.argmin(R2, axis=1))
# Other explicitly defined examples in the notes, not additional fitted models.
plan = np.diag([.5, .5])
cost = np.array([[0, 2], [2, 0]])
equal(plan.sum(axis=0), [.5, .5])
equal(plan.sum(axis=1), [.5, .5])
equal((plan * cost).sum(), 0)
equal((np.full((2, 2), .25) * cost).sum(), 1)
equal(18085 + 31, 18116)
print(f"PASS: {checks} fixed synthetic arithmetic checks; no project dataset read or fitted.")

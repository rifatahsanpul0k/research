# Clustering backend interfaces

Common backends accept a finite n×d embedding plus ordered observation IDs, seed and a declared K/resolution. KMeans uses a pinned scikit-learn implementation; Leiden consumes a separately built neighbor graph; MClust uses an R bridge and explicit model/K.

Native outputs are retained separately. Common-backend results test representation plus a standardized backend and never replace the native pipeline record.

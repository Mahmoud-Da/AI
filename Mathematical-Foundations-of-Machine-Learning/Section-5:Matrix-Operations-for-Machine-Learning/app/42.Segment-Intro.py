import numpy as np
from sklearn.decomposition import PCA

# --------------------------------------------------
# 1. Singular Value Decomposition
# --------------------------------------------------

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

U, S, VT = np.linalg.svd(A)

print("SVD")
print("U:")
print(U)

print("\nSingular Values:")
print(S)

print("\nVT:")
print(VT)

# --------------------------------------------------
# 2. Moore-Penrose Pseudoinverse
# --------------------------------------------------

B = np.array([
    [1, 1],
    [2, 1],
    [3, 1]
])

B_pinv = np.linalg.pinv(B)

print("\nPseudoinverse:")
print(B_pinv)

# --------------------------------------------------
# 3. Trace Operator
# --------------------------------------------------

C = np.array([
    [1, 2],
    [3, 4]
])

print("\nTrace:")
print(np.trace(C))

# --------------------------------------------------
# 4. Principal Component Analysis
# --------------------------------------------------

X = np.array([
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8]
])

pca = PCA(n_components=1)

X_reduced = pca.fit_transform(X)

print("\nPCA Result:")
print(X_reduced)

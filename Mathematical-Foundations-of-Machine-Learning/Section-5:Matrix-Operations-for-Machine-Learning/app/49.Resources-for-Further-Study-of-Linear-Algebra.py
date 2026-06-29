import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Matrix
A = np.array([
    [0, 1],
    [2, 3]
])

# Eigen Decomposition
eigenvalues, eigenvectors = np.linalg.eig(A)

Lambda = np.diag(eigenvalues)

A_reconstructed = (
    eigenvectors
    @ Lambda
    @ np.linalg.inv(eigenvectors)
)

# SVD
U, S, VT = np.linalg.svd(A)

# Pseudoinverse
A_pinv = np.linalg.pinv(A)

# Trace
trace_A = np.trace(A)

# Frobenius Norm
fro_norm = np.sqrt(
    np.trace(A.T @ A)
)

# PCA
iris = load_iris()

X = iris.data

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

print("Eigenvalues:")
print(eigenvalues)

print("\nSingular Values:")
print(S)

print("\nPseudoinverse:")
print(A_pinv)

print("\nTrace:")
print(trace_A)

print("\nFrobenius Norm:")
print(fro_norm)

print("\nPCA Shape:")
print(X_pca.shape)

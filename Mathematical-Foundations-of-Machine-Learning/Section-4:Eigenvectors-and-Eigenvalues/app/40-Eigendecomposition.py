import numpy as np

# ----------------------------
# General Eigen Decomposition
# ----------------------------

A = np.array([
    [1, 2],
    [4, 3]
])

# Eigenvalues and eigenvectors
lambdas, V = np.linalg.eig(A)

# Inverse of eigenvector matrix
V_inv = np.linalg.inv(V)

# Diagonal matrix of eigenvalues
Lambda = np.diag(lambdas)

# Reconstruct original matrix
A_reconstructed = V @ Lambda @ V_inv

print("Original Matrix:")
print(A)

print("\nEigenvectors (V):")
print(V)

print("\nEigenvalues:")
print(lambdas)

print("\nDiagonal Matrix (Lambda):")
print(Lambda)

print("\nInverse of V:")
print(V_inv)

print("\nReconstructed Matrix:")
print(A_reconstructed)

# ----------------------------
# Symmetric Matrix Example
# ----------------------------

S = np.array([
    [1, 2],
    [2, 1]
])

lambdas_s, Q = np.linalg.eig(S)

Lambda_s = np.diag(lambdas_s)

S_reconstructed = Q @ Lambda_s @ Q.T

print("\nSymmetric Matrix:")
print(S)

print("\nEigenvectors (Q):")
print(Q)

print("\nEigenvalues:")
print(lambdas_s)

print("\nQ^T Q:")
print(Q.T @ Q)

print("\nQ Q^T:")
print(Q @ Q.T)

print("\nReconstructed Symmetric Matrix:")
print(S_reconstructed)

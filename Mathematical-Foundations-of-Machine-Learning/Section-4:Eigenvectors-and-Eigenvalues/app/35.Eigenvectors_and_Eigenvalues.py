import torch
import numpy as np

# Create matrix
A = np.array([
    [-1, 4],
    [2, -2]
])

# Compute eigenvalues and eigenvectors
lambdas, V = np.linalg.eig(A)

print("Eigenvalues:")
print(lambdas)

print("\nEigenvectors:")
print(V)

# First eigenvector and eigenvalue
v1 = V[:, 0]
lambda1 = lambdas[0]

print("\nFirst Eigenvector:")
print(v1)

print("\nFirst Eigenvalue:")
print(lambda1)

# Verify Av = λv
Av = A.dot(v1)

lambda_v = lambda1 * v1

print("\nA dot v:")
print(Av)

print("\nLambda times v:")
print(lambda_v)

# Second eigenvector and eigenvalue
v2 = V[:, 1]
lambda2 = lambdas[1]

Av2 = A.dot(v2)

lambda_v2 = lambda2 * v2

print("\nSecond Eigenvector:")
print(v2)

print("\nSecond Eigenvalue:")
print(lambda2)

print("\nA dot v2:")
print(Av2)

print("\nLambda times v2:")
print(lambda_v2)

# Pytorch
# Create matrix
A = torch.tensor([
    [-1., 4.],
    [2., -2.]
])

# Compute eigenvalues and eigenvectors
eigens = torch.eig(A, eigenvectors=True)

# Extract eigenvectors
v1 = eigens.eigenvectors[:, 0]
v2 = eigens.eigenvectors[:, 1]

# Extract eigenvalues
lambda1 = eigens.eigenvalues[0, 0]
lambda2 = eigens.eigenvalues[1, 0]

# Verify first eigenvector
Av1 = torch.matmul(A, v1)
lambda_v1 = lambda1 * v1

print("First Eigenvector Verification")
print(Av1)
print(lambda_v1)

# Verify second eigenvector
Av2 = torch.matmul(A, v2)
lambda_v2 = lambda2 * v2

print("\nSecond Eigenvector Verification")
print(Av2)
print(lambda_v2)

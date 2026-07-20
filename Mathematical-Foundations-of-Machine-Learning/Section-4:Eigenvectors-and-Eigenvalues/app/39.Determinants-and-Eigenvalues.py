import numpy as np

# Matrix X
X = np.array([
    [1, 2, 4],
    [5, 2, 0],
    [3, -1, 1]
])

# Determinant
det_x = np.linalg.det(X)
print("Determinant:", det_x)

# Eigenvalues and Eigenvectors
lambdas, V = np.linalg.eig(X)

print("\nEigenvalues:")
print(lambdas)

print("\nProduct of Eigenvalues:")
print(np.prod(lambdas))

# Identity Matrix
I = np.eye(2)

print("\nIdentity determinant:")
print(np.linalg.det(I))

# Matrix J
J = np.array([
    [-0.5, 0],
    [0, 2]
])

print("\nDeterminant of J:")
print(np.linalg.det(J))

# Matrix D
D = np.array([
    [2, 0],
    [0, 2]
])

print("\nDeterminant of D:")
print(np.linalg.det(D))

# Singular Matrix N
N = np.array([
    [-4, 1],
    [-8, 2]
])

print("\nDeterminant of N:")
print(np.linalg.det(N))

print("\nEigenvalues of N:")
print(np.linalg.eig(N)[0])

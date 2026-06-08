import numpy as np
import torch

# Matrix A
A = np.array([
    [25, 2],
    [3, 4]
])

print("Determinant of A:")
print(np.linalg.det(A))

# Matrix B
B = np.array([
    [-2, 0],
    [0, -2]
])

print("\nDeterminant of B:")
print(np.linalg.det(B))

# Matrix C
C = np.array([
    [2, 1, -3],
    [0, 4, 2],
    [-1, -5, 3]
])

print("\nDeterminant of C:")
print(np.linalg.det(C))

# PyTorch example
C_torch = torch.tensor([
    [2., 1., -3.],
    [0., 4., 2.],
    [-1., -5., 3.]
])

print("\nDeterminant of C (PyTorch):")
print(torch.det(C_torch))

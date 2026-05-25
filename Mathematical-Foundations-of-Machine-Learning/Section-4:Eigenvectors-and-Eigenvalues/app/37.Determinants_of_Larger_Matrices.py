import torch
import numpy as np

# NumPy Version
# 3x3 matrix
X = np.array([
    [1, 2, 4],
    [5, 2, 0],
    [3, -1, 1]
])

# Determinant
det_X = np.linalg.det(X)

print("Determinant of X:")
print(det_X)

# Singular matrix example
N = np.array([
    [-4, 1],
    [8, -2]
])

print("\nDeterminant of N:")
print(np.linalg.det(N))

# Attempt inversion
try:
    print("\nInverse of N:")
    print(np.linalg.inv(N))
except np.linalg.LinAlgError as e:
    print("\nError:")
    print(e)


# PyTorch Version
X_torch = torch.tensor([
    [1., 2., 4.],
    [5., 2., 0.],
    [3., -1., 1.]
])

print("Determinant of X:")
print(torch.det(X_torch))

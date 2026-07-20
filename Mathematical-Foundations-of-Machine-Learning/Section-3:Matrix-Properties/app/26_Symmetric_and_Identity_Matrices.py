# =========================
# Symmetric Matrix Example
# =========================

import numpy as np
import torch

# Create symmetric matrix
A = np.array([
    [1, 7, 3],
    [7, 4, -5],
    [3, -5, 6]
])

print("Original Matrix:")
print(A)

# Transpose
print("\nTranspose:")
print(A.T)

# Check symmetry
print("\nIs Symmetric?")
print(np.array_equal(A, A.T))

# =========================
# Identity Matrix Example
# =========================

# Create identity matrix
I = torch.eye(3)

print("\nIdentity Matrix:")
print(I)

# Create vector
x = torch.tensor([25., 2., 5.])

print("\nOriginal Vector:")
print(x)

# Multiply identity matrix by vector
result = torch.matmul(I, x)

print("\nResult After Multiplication:")
print(result)

import numpy as np
import torch

# =====================================
# PART 1 — Identity Matrix in NumPy
# =====================================

I3 = np.eye(3)

print("Identity Matrix:")
print(I3)

# Extract columns
c1 = I3[:, 0]
c2 = I3[:, 1]
c3 = I3[:, 2]

# Dot products
print("\nDot Products:")
print(np.dot(c1, c2))
print(np.dot(c1, c3))
print(np.dot(c2, c3))

# Norms
print("\nL2 Norms:")
print(np.linalg.norm(c1))
print(np.linalg.norm(c2))
print(np.linalg.norm(c3))

# =====================================
# PART 2 — Matrix K in PyTorch
# =====================================

K = torch.tensor([
    [2/3, 1/3,  2/3],
    [-2/3, 2/3,  1/3],
    [1/3, 2/3, -2/3]
], dtype=torch.float32)

print("\nMatrix K:")
print(K)

# Extract columns
k1 = K[:, 0]
k2 = K[:, 1]
k3 = K[:, 2]

# Dot products
print("\nDot Products:")
print(torch.dot(k1, k2))
print(torch.dot(k1, k3))
print(torch.dot(k2, k3))

# Norms
print("\nL2 Norms:")
print(torch.norm(k1))
print(torch.norm(k2))
print(torch.norm(k3))

# Orthogonality check
result = torch.matmul(K.T, K)

print("\nK^T K:")
print(result)

# Compare with identity matrix
is_orthogonal = torch.allclose(result, torch.eye(3))

print("\nIs K orthogonal?")
print(is_orthogonal)

import torch
import numpy as np

# NumPy Version
# Identity matrix
I3 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Columns
c1 = I3[:, 0]
c2 = I3[:, 1]
c3 = I3[:, 2]

# Dot products
print(np.dot(c1, c2))
print(np.dot(c1, c3))
print(np.dot(c2, c3))

# Norms
print(np.linalg.norm(c1))
print(np.linalg.norm(c2))
print(np.linalg.norm(c3))


# PyTorch Version
K = torch.tensor([
    [2/3, 1/3, 2/3],
    [-2/3, 2/3, 1/3],
    [1/3, 2/3, -2/3]
], dtype=torch.float32)

# Columns
c1 = K[:, 0]
c2 = K[:, 1]
c3 = K[:, 2]

# Dot products
print(torch.dot(c1, c2))
print(torch.dot(c1, c3))
print(torch.dot(c2, c3))

# Norms
print(torch.norm(c1))
print(torch.norm(c2))
print(torch.norm(c3))

# Orthogonality test
print(torch.matmul(K.T, K))

import numpy as np
import torch

# --------------------------
# NumPy Example
# --------------------------

A = np.array([
    [25, 2],
    [5, 4]
])

# Trace
print("Trace:")
print(np.trace(A))

# Trace of transpose
print("\nTrace of A^T:")
print(np.trace(A.T))

# Frobenius norm via trace
fro_trace = np.sqrt(
    np.trace(A.T @ A)
)

print("\nFrobenius norm via trace:")
print(fro_trace)

# Frobenius norm via NumPy
fro_numpy = np.linalg.norm(A, 'fro')

print("\nFrobenius norm via NumPy:")
print(fro_numpy)

# --------------------------
# Cyclic Property Example
# --------------------------

A_rand = np.random.randn(3, 3)
B_rand = np.random.randn(3, 3)
C_rand = np.random.randn(3, 3)

tr1 = np.trace(A_rand @ B_rand @ C_rand)
tr2 = np.trace(C_rand @ A_rand @ B_rand)
tr3 = np.trace(B_rand @ C_rand @ A_rand)

print("\nCyclic Property:")
print(tr1)
print(tr2)
print(tr3)

# --------------------------
# PyTorch Example
# --------------------------

A_torch = torch.tensor([
    [25., 2.],
    [5., 4.]
])

trace_torch = torch.trace(A_torch)

print("\nPyTorch Trace:")
print(trace_torch)

fro_torch = torch.norm(
    A_torch,
    p='fro'
)

print("\nPyTorch Frobenius Norm:")
print(fro_torch)

fro_trace_torch = torch.sqrt(
    torch.trace(
        A_torch.T @ A_torch
    )
)

print("\nFrobenius via Trace:")
print(fro_trace_torch)

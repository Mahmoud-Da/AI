import numpy as np

# Create matrix
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

# Compute SVD
U, d, VT = np.linalg.svd(A)

print("U:")
print(U)

print("\nSingular Values:")
print(d)

print("\nVT:")
print(VT)

# Create diagonal matrix
D = np.diag(d)

# Expand to match dimensions (3x2)
D = np.vstack([
    D,
    [0, 0]
])

print("\nD:")
print(D)

# Reconstruct matrix
A_reconstructed = U @ D @ VT

print("\nReconstructed A:")
print(A_reconstructed)

# Verify equality
print("\nOriginal A:")
print(A)

import numpy as np

# -----------------------------------
# Create an orthogonal matrix
# -----------------------------------

A = np.array([
    [0, -1],
    [1,  0]
])

print("Matrix A:")
print(A)

# -----------------------------------
# Compute transpose
# -----------------------------------

A_T = A.T

print("\nTranspose of A:")
print(A_T)

# -----------------------------------
# Verify orthogonality
# A^T A should equal identity matrix
# -----------------------------------

result = A_T @ A

print("\nA^T @ A:")
print(result)

# -----------------------------------
# Create identity matrix for comparison
# -----------------------------------

I = np.eye(2)

print("\nIdentity Matrix:")
print(I)

# -----------------------------------
# Check if orthogonal
# -----------------------------------

is_orthogonal = np.allclose(result, I)

print("\nIs A orthogonal?")
print(is_orthogonal)

# -----------------------------------
# Compute inverse
# -----------------------------------

A_inv = np.linalg.inv(A)

print("\nInverse of A:")
print(A_inv)

# -----------------------------------
# Verify inverse equals transpose
# -----------------------------------

same = np.allclose(A_inv, A_T)

print("\nDoes inverse equal transpose?")
print(same)

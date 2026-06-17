import numpy as np

# Non-square matrix
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

# Step 1: SVD
U, d, VT = np.linalg.svd(A)

# Step 2: U transpose
UT = U.T

# Step 3: V
V = VT.T

# Step 4: D+
D_plus = np.linalg.inv(np.diag(d))

# Step 5: Match dimensions
zeros = np.zeros((2, 1))

D_plus = np.concatenate(
    (D_plus, zeros),
    axis=1
)

# Step 6: Calculate pseudoinverse
A_plus = V @ D_plus @ UT

print("Manual pseudoinverse:")
print(A_plus)

# NumPy built-in method
A_plus_builtin = np.linalg.pinv(A)

print("\nNumPy pinv():")
print(A_plus_builtin)

# Verification
print("\nResults match:")
print(np.allclose(A_plus, A_plus_builtin))

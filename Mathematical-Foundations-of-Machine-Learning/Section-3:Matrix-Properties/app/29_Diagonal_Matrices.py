import numpy as np

# -----------------------------------
# Create a diagonal matrix
# -----------------------------------

X = np.diag([2, 3, 4])

print("Diagonal Matrix:")
print(X)

# -----------------------------------
# Create a vector
# -----------------------------------

y = np.array([5, 6, 7])

print("\nVector:")
print(y)

# -----------------------------------
# Matrix-vector multiplication
# -----------------------------------

result_matrix = X @ y

print("\nMatrix Multiplication Result:")
print(result_matrix)

# -----------------------------------
# Efficient element-wise multiplication
# -----------------------------------

x = np.array([2, 3, 4])

result_elementwise = x * y

print("\nElement-wise Multiplication Result:")
print(result_elementwise)

# -----------------------------------
# Invert a diagonal matrix
# -----------------------------------

X_inv = np.linalg.inv(X)

print("\nInverse of Diagonal Matrix:")
print(X_inv)

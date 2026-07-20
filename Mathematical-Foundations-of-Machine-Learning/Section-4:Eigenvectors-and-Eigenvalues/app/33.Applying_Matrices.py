import numpy as np

# Identity matrix
I3 = np.eye(3)

# Vector u
u = np.array([
    [1],
    [2],
    [3]
])

# Apply identity matrix
result1 = np.dot(I3, u)

print("I3 * u:")
print(result1)

# Matrix B
B = np.array([
    [1, 2, 0],
    [0, 1, 2],
    [3, 4, 5]
])

# Apply B to u
result2 = np.dot(B, u)

print("\nB * u:")
print(result2)

# Second vector
u2 = np.array([
    [4],
    [5],
    [6]
])

# Concatenate vectors
U = np.concatenate((u, u2), axis=1)

print("\nMatrix U:")
print(U)

# Apply B to U
result3 = np.dot(B, U)

print("\nB * U:")
print(result3)

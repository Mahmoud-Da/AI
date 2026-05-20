import numpy as np

# Scalars, vectors, matrices
scalar = np.array(5)

vector = np.array([1, 2, 3])

matrix = np.array([
    [1, 2],
    [3, 4]
])

# Vector transpose
x = np.array([[1, 2, 3]])
print(x.T)

# L2 norm
v = np.array([3, 4])
print(np.linalg.norm(v))

# Unit vector
unit_v = v / np.linalg.norm(v)
print(unit_v)

# Dot product
a = np.array([1, 0])
b = np.array([0, 1])

print(np.dot(a, b))

# Symmetric matrix
S = np.array([
    [1, 2],
    [2, 3]
])

print(np.array_equal(S, S.T))

# Matrix multiplication
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5],
    [6]
])

print(np.dot(A, B))

# Identity matrix
I = np.eye(3)
print(I)

# Matrix inversion
X = np.array([
    [4, 2],
    [-5, -3]
])

y = np.array([4, -7])

X_inv = np.linalg.inv(X)

w = np.dot(X_inv, y)

print(w)

# Diagonal matrix
D = np.diag([1, 2, 3])
print(D)

# Orthogonal matrix check
Q = np.array([
    [1, 0],
    [0, 1]
])

print(np.dot(Q.T, Q))

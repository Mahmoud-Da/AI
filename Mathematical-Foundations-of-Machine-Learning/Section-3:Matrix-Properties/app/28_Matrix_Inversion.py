import numpy as np
import torch
import tensorflow as tf

# ==========================================
# NumPy Example
# ==========================================

X = np.array([
    [4, 2],
    [-5, -3]
])

Y = np.array([
    [4],
    [-7]
])

# Matrix inverse
X_inv = np.linalg.inv(X)

print("Inverse of X:")
print(X_inv)

# Solve for W
W = np.dot(X_inv, Y)

print("\nWeights W:")
print(W)

# Verify solution
Y_check = np.dot(X, W)

print("\nVerification:")
print(Y_check)

# ==========================================
# Singular Matrix Example
# ==========================================

X_singular = np.array([
    [1, 2],
    [2, 4]
])

# Uncomment to test singular matrix error
# np.linalg.inv(X_singular)

# ==========================================
# PyTorch Example
# ==========================================

X_torch = torch.tensor([
    [4., 2.],
    [-5., -3.]
])

torch_inverse = torch.inverse(X_torch)

print("\nPyTorch Inverse:")
print(torch_inverse)

# ==========================================
# TensorFlow Example
# ==========================================

X_tf = tf.constant([
    [4., 2.],
    [-5., -3.]
])

tf_inverse = tf.linalg.inv(X_tf)

print("\nTensorFlow Inverse:")
print(tf_inverse)

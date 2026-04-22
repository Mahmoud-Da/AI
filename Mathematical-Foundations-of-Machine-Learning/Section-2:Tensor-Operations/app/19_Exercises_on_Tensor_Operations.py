import numpy as np
import torch
import tensorflow as tf

# -----------------------
# 1. Transpose
# -----------------------
Y = np.array([[1, 2],
              [3, 4]])

print("NumPy Transpose:\n", Y.T)

# -----------------------
# 2. Hadamard Product
# -----------------------
A = np.array([[25, 10],
              [-2, 5]])

B = np.array([[-1, 7],
              [10, 3]])

print("NumPy Hadamard:\n", A * B)

# PyTorch
A_t = torch.tensor([[25, 10], [-2, 5]])
B_t = torch.tensor([[-1, 7], [10, 3]])
print("PyTorch Hadamard:\n", A_t * B_t)

# TensorFlow
A_tf = tf.constant([[25, 10], [-2, 5]])
B_tf = tf.constant([[-1, 7], [10, 3]])
print("TensorFlow Hadamard:\n", tf.multiply(A_tf, B_tf))

# -----------------------
# 3. Dot Product
# -----------------------
W = np.array([-1, 4, 0])
X = np.array([5, 5, 2])

print("NumPy Dot:", np.dot(W, X))

# PyTorch
W_t = torch.tensor([-1.0, 4.0, 0.0])
X_t = torch.tensor([5.0, 5.0, 2.0])
print("PyTorch Dot:", torch.dot(W_t, X_t))

# TensorFlow
W_tf = tf.constant([-1.0, 4.0, 0.0])
X_tf = tf.constant([5.0, 5.0, 2.0])
print("TensorFlow Dot:", tf.reduce_sum(tf.multiply(W_tf, X_tf)))

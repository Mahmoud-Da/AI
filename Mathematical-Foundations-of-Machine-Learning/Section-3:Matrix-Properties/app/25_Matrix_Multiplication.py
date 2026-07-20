# =========================
# 1. Frobenius Norm
# =========================
import numpy as np
import torch
import tensorflow as tf

X_np = np.array([[1, 2],
                 [3, 4]])

print("NumPy Frobenius:", np.linalg.norm(X_np))

X_torch = torch.tensor([[1., 2.],
                        [3., 4.]])
print("PyTorch Frobenius:", torch.norm(X_torch))

X_tf = tf.constant([[1., 2.],
                    [3., 4.]])
print("TensorFlow Frobenius:", tf.norm(X_tf))

# =========================
# 2. Matrix × Vector
# =========================
A = np.array([[3, 4],
              [5, 6],
              [7, 8]])

B = np.array([[1],
              [2]])

print("NumPy mat-vec:", np.dot(A, B))

A_t = torch.tensor(A)
B_t = torch.tensor(B)
print("PyTorch mat-vec:", torch.matmul(A_t, B_t))

A_tf = tf.constant(A)
B_tf = tf.constant(B)
print("TensorFlow mat-vec:", tf.linalg.matmul(A_tf, B_tf))

# =========================
# 3. Matrix × Matrix
# =========================
B2 = np.array([[1, 9],
               [2, 0]])

print("NumPy mat-mat:", np.dot(A, B2))

B2_t = torch.tensor(B2)
print("PyTorch mat-mat:", torch.matmul(A_t, B2_t))

B2_tf = tf.constant(B2)
print("TensorFlow mat-mat:", tf.linalg.matmul(A_tf, B2_tf))

# =========================
# 4. ML Example
# =========================
# Linear regression style
X = np.array([[1, 2],
              [3, 4]])

W = np.array([[0.5],
              [1.0]])

b = np.array([[1]])

Y = np.dot(X, W) + b
print("Predictions:", Y)

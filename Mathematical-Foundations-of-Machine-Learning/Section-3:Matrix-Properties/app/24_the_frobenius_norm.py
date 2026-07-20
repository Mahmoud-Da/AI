# NumPy Example
import tensorflow as tf
import torch
import numpy as np

X_np = np.array([[1, 2],
                 [3, 4]])

# Manual computation
fro_manual = np.sqrt(np.sum(X_np ** 2))

# Built-in
fro_numpy = np.linalg.norm(X_np)

print("NumPy Manual:", fro_manual)
print("NumPy Built-in:", fro_numpy)


# PyTorch Example

X_torch = torch.tensor([[1., 2.],
                        [3., 4.]])

fro_torch = torch.norm(X_torch)

print("PyTorch:", fro_torch)


# TensorFlow Example

X_tf = tf.constant([[1., 2.],
                    [3., 4.]])

fro_tf = tf.norm(X_tf)

print("TensorFlow:", fro_tf)

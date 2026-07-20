import numpy as np
import torch
import tensorflow as tf


def numpy_demo():
    print("=== NumPy ===")
    x = np.array([25, 2, 5])
    y = np.array([0, 1, 2])

    # Manual computation
    products = x * y
    print("Element-wise product:", products)

    dot_manual = products.sum()
    print("Dot product (manual):", dot_manual)

    # Built-in
    dot_builtin = np.dot(x, y)
    print("Dot product (numpy):", dot_builtin)


def pytorch_demo():
    print("\n=== PyTorch ===")
    x = torch.tensor([25., 2., 5.])
    y = torch.tensor([0., 1., 2.])

    dot_product = torch.dot(x, y)
    print("Dot product (torch):", dot_product)


def tensorflow_demo():
    print("\n=== TensorFlow ===")
    x = tf.constant([25, 2, 5], dtype=tf.float32)
    y = tf.constant([0, 1, 2], dtype=tf.float32)

    # Step 1: multiply
    products = tf.multiply(x, y)

    # Step 2: reduce sum
    dot_product = tf.reduce_sum(products)

    print("Dot product (tensorflow):", dot_product)


if __name__ == "__main__":
    numpy_demo()
    pytorch_demo()
    tensorflow_demo()

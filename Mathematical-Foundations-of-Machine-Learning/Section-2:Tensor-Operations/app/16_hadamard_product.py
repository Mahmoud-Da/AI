import numpy as np
import torch
import tensorflow as tf


def numpy_demo():
    print("=== NumPy ===")
    X = np.array([
        [25, 2],
        [5, 26],
        [3, 7]
    ])

    # Scalar operations
    print("Multiply by 2:\n", X * 2)
    print("Add 2:\n", X + 2)
    print("Combined:\n", X * 2 + 2)

    # Element-wise operations
    A = X + 2
    print("Element-wise addition:\n", X + A)
    print("Hadamard product:\n", X * A)


def pytorch_demo():
    print("\n=== PyTorch ===")
    X = torch.tensor([
        [25, 2],
        [5, 26],
        [3, 7]
    ])

    print("Multiply by 2:\n", X * 2)
    print("Add 2:\n", X + 2)
    print("Combined:\n", X * 2 + 2)

    A = X + 2
    print("Element-wise addition:\n", X + A)
    print("Hadamard product:\n", X * A)


def tensorflow_demo():
    print("\n=== TensorFlow ===")
    X = tf.constant([
        [25, 2],
        [5, 26],
        [3, 7]
    ])

    print("Multiply by 2:\n", X * 2)
    print("Add 2:\n", X + 2)
    print("Combined:\n", X * 2 + 2)

    A = X + 2
    print("Element-wise addition:\n", X + A)
    print("Hadamard product:\n", X * A)


if __name__ == "__main__":
    numpy_demo()
    pytorch_demo()
    tensorflow_demo()

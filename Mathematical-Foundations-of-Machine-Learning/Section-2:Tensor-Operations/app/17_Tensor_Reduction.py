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

    print("Full sum:", X.sum())

    print("Sum along columns (axis=0):", X.sum(axis=0))
    print("Sum along rows (axis=1):", X.sum(axis=1))

    print("Max:", np.max(X))
    print("Min:", np.min(X))
    print("Mean:", np.mean(X))
    print("Product:", np.prod(X))


def pytorch_demo():
    print("\n=== PyTorch ===")
    X = torch.tensor([
        [25, 2],
        [5, 26],
        [3, 7]
    ])

    print("Full sum:", torch.sum(X))

    print("Sum along columns (dim=0):", torch.sum(X, dim=0))
    print("Sum along rows (dim=1):", torch.sum(X, dim=1))


def tensorflow_demo():
    print("\n=== TensorFlow ===")
    X = tf.constant([
        [25, 2],
        [5, 26],
        [3, 7]
    ])

    print("Full sum:", tf.reduce_sum(X))

    print("Sum along columns (axis=0):", tf.reduce_sum(X, axis=0))
    print("Sum along rows (axis=1):", tf.reduce_sum(X, axis=1))


if __name__ == "__main__":
    numpy_demo()
    pytorch_demo()
    tensorflow_demo()

import numpy as np
import torch
import tensorflow as tf


def numpy_demo():
    print("=== NumPy Demo ===")

    X = np.array([
        [1, 2],
        [5, 26],
        [3, 7]
    ])

    print("Matrix:\n", X)
    print("Shape:", X.shape)
    print("Size:", X.size)

    print("First column:", X[:, 0])
    print("Second row:", X[1, :])
    print("Submatrix:\n", X[0:2, 0:2])


def pytorch_demo():
    print("\n=== PyTorch Demo ===")

    X = torch.tensor([
        [1, 2],
        [5, 26],
        [3, 7]
    ])

    print("Matrix:\n", X)
    print("Shape:", X.shape)
    print("Second row:", X[1, :])


def tensorflow_demo():
    print("\n=== TensorFlow Demo ===")

    X = tf.Variable([
        [1, 2],
        [5, 26],
        [3, 7]
    ])

    print("Matrix:\n", X)
    print("Rank:", tf.rank(X))
    print("Shape:", X.shape)
    print("Second row:", X[1, :])


def main():
    numpy_demo()
    pytorch_demo()
    tensorflow_demo()


if __name__ == "__main__":
    main()

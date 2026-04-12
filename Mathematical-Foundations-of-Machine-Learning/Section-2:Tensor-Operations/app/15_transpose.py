import numpy as np
import torch
import tensorflow as tf


def numpy_example():
    print("=== NumPy ===")

    X = np.array([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    print("Original:\n", X)
    print("Transpose:\n", X.T)


def pytorch_example():
    print("\n=== PyTorch ===")

    X = torch.tensor([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    print("Original:\n", X)
    print("Transpose:\n", X.T)


def tensorflow_example():
    print("\n=== TensorFlow ===")

    X = tf.Variable([
        [1, 2],
        [3, 4],
        [5, 6]
    ])

    X_T = tf.transpose(X)

    print("Original:\n", X)
    print("Transpose:\n", X_T)


def main():
    numpy_example()
    pytorch_example()
    tensorflow_example()


if __name__ == "__main__":
    main()

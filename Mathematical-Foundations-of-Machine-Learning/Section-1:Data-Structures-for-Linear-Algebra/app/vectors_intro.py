import numpy as np
import torch
import tensorflow as tf


def main():
    # --------------------
    # NumPy Vector
    # --------------------
    x = np.array([25, 2, 5])
    print("NumPy vector:", x)
    print("Shape:", x.shape)

    # Access elements
    print("First element:", x[0])

    # Float vector
    x_float = np.array([25, 2, 5], dtype=np.float32)
    print("Float vector:", x_float)

    # --------------------
    # Transposition
    # --------------------
    # 1D transpose (no effect)
    x_t = x.T
    print("1D transpose shape:", x_t.shape)

    # Proper 2D vector
    y = np.array([[25, 2, 5]])
    print("Row vector shape:", y.shape)

    y_t = y.T
    print("Column vector:\n", y_t)
    print("Column shape:", y_t.shape)

    # Transpose back
    print("Back to row shape:", y_t.T.shape)

    # --------------------
    # Zero Vector
    # --------------------
    zero_vector = np.zeros(3)
    print("Zero vector:", zero_vector)

    # --------------------
    # PyTorch Vector
    # --------------------
    x_torch = torch.tensor([25, 2, 5])
    print("PyTorch vector:", x_torch)
    print("Shape:", x_torch.shape)

    # --------------------
    # TensorFlow Vector
    # --------------------
    x_tf = tf.Variable([25, 2, 5])
    print("TensorFlow vector:", x_tf)
    print("Shape:", x_tf.shape)


if __name__ == "__main__":
    main()

import numpy as np
import torch
import tensorflow as tf


def main():
    # --------------------
    # Base Python
    # --------------------
    x = 25
    y = 3

    z = x + y
    print("Python scalar:", z, type(z))

    x_float = 25.0
    z_float = x_float + y
    print("Python float result:", z_float, type(z_float))

    # --------------------
    # NumPy
    # --------------------
    x_np = np.array(25)
    print("NumPy scalar:", x_np)
    print("Shape:", x_np.shape)

    x_np_float = np.array(25, dtype=np.float32)
    print("NumPy float scalar:", x_np_float)

    # --------------------
    # PyTorch
    # --------------------
    x_torch = torch.tensor(25)
    y_torch = torch.tensor(3)

    z_torch = x_torch + y_torch
    print("PyTorch scalar:", z_torch)
    print("Shape:", x_torch.shape)

    x_torch_float = torch.tensor(25.0, dtype=torch.float32)
    print("PyTorch float scalar:", x_torch_float)

    # --------------------
    # TensorFlow
    # --------------------
    x_tf = tf.Variable(25, dtype=tf.int32)
    y_tf = tf.Variable(3, dtype=tf.int32)

    z_tf = x_tf + y_tf
    print("TensorFlow scalar:", z_tf)
    print("Shape:", x_tf.shape)

    z_np = z_tf.numpy()
    print("Converted to NumPy:", z_np, type(z_np))

    x_tf_float = tf.Variable(25.0, dtype=tf.float32)
    print("TensorFlow float scalar:", x_tf_float)


if __name__ == "__main__":
    main()

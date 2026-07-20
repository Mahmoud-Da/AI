import torch
import tensorflow as tf


def pytorch_demo():
    print("=== PyTorch 4D Tensor ===")

    tensor = torch.zeros((32, 28, 28, 3))

    print("Shape:", tensor.shape)


def tensorflow_demo():
    print("\n=== TensorFlow 4D Tensor ===")

    tensor = tf.zeros((32, 28, 28, 3))

    print("Shape:", tensor.shape)


def main():
    pytorch_demo()
    tensorflow_demo()


if __name__ == "__main__":
    main()

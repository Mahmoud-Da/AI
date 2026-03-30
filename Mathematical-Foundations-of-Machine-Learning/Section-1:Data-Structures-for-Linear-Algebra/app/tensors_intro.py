import numpy as np


def main():
    # Scalar (0D)
    scalar = np.array(5)

    # Vector (1D)
    vector = np.array([1, 2, 3])

    # Matrix (2D)
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    # 3D Tensor
    tensor_3d = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ])

    # 4D Tensor
    tensor_4d = np.random.rand(2, 3, 4, 5)

    # Print shapes
    print("Scalar shape:", scalar.shape)
    print("Vector shape:", vector.shape)
    print("Matrix shape:", matrix.shape)
    print("3D Tensor shape:", tensor_3d.shape)
    print("4D Tensor shape:", tensor_4d.shape)


if __name__ == "__main__":
    main()

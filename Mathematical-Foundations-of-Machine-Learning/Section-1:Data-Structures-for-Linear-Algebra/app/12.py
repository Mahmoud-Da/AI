import numpy as np


def transpose_example():
    print("=== Vector Transpose ===")

    x = np.array([[1],
                  [2],
                  [3]])

    x_T = x.T

    print("Original vector:\n", x)
    print("Transposed vector:\n", x_T)


def matrix_dimensions_example():
    print("\n=== Matrix Dimensions ===")

    Y = np.array([
        [5, 8, 17, 2],
        [9, 4, 6, 1]
    ])

    print("Matrix:\n", Y)
    print("Shape (rows, cols):", Y.shape)


def element_position_example():
    print("\n=== Element Position ===")

    Y = np.array([
        [5, 8, 17, 2],
        [9, 4, 6, 1]
    ])

    value = Y[1, 2]

    print("Element at (2,3):", value)


def main():
    transpose_example()
    matrix_dimensions_example()
    element_position_example()


if __name__ == "__main__":
    main()

import numpy as np


def main():
    # --------------------
    # Basis Vectors
    # --------------------
    i = np.array([1, 0])
    j = np.array([0, 1])

    print("Basis vectors:")
    print("i:", i)
    print("j:", j)

    # Construct vector using basis
    a, b = 1.5, 2
    v = a * i + b * j
    print("\nConstructed vector v:", v)

    # --------------------
    # Orthogonal Vectors
    # --------------------
    x = np.array([1, 0])
    y = np.array([0, 1])

    dot_product = np.dot(x, y)
    print("\nDot product (x · y):", dot_product)

    if dot_product == 0:
        print("x and y are orthogonal")

    # --------------------
    # Orthonormal Vectors
    # --------------------
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)

    print("\nNorm of x:", norm_x)
    print("Norm of y:", norm_y)

    if dot_product == 0 and norm_x == 1 and norm_y == 1:
        print("x and y are orthonormal")


if __name__ == "__main__":
    main()

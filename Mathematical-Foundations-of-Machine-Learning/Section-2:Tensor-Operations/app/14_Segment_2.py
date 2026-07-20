import numpy as np


def transpose_example():
    x = np.array([[1, 2, 3]])
    print("Transpose:\n", x.T)


def arithmetic_example():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Addition:", a + b)
    print("Multiplication:", a * b)


def reduction_example():
    x = np.array([1, 2, 3, 4])

    print("Sum:", np.sum(x))
    print("Mean:", np.mean(x))


def dot_product_example():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])

    print("Dot Product:", np.dot(x, y))


def main():
    transpose_example()
    arithmetic_example()
    reduction_example()
    dot_product_example()


if __name__ == "__main__":
    main()

import numpy as np


def main():
    # --------------------
    # Vector
    # --------------------
    x = np.array([25, 2, 5])
    print("Vector:", x)

    # --------------------
    # L2 Norm
    # --------------------
    l2_manual = np.sqrt(np.sum(x**2))
    print("L2 norm (manual):", l2_manual)

    l2_numpy = np.linalg.norm(x)
    print("L2 norm (numpy):", l2_numpy)

    # --------------------
    # Unit Vector
    # --------------------
    unit_x = x / np.linalg.norm(x)
    print("Unit vector:", unit_x)
    print("Unit vector norm:", np.linalg.norm(unit_x))

    # --------------------
    # L1 Norm
    # --------------------
    l1 = np.sum(np.abs(x))
    print("L1 norm:", l1)

    # --------------------
    # Squared L2 Norm
    # --------------------
    l2_squared = np.sum(x**2)
    print("Squared L2 norm:", l2_squared)

    l2_squared_dot = x.T @ x
    print("Squared L2 (dot product):", l2_squared_dot)

    # --------------------
    # Max Norm
    # --------------------
    l_inf = np.max(np.abs(x))
    print("Max norm:", l_inf)


if __name__ == "__main__":
    main()

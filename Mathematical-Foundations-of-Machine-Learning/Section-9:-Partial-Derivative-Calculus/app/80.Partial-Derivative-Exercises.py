# ============================================================
# Calculus 2 - Partial Derivatives Exercises
# ============================================================

# ------------------------------------------------------------
# 1. Define the multivariate function
# ------------------------------------------------------------

def f(x, y):
    return x**2 - y**2


# ------------------------------------------------------------
# 2. Partial derivative with respect to X
#
# z = x² - y²
# ∂z/∂x = 2x
# ------------------------------------------------------------

def del_z_del_x(x, y):
    return 2 * x


# ------------------------------------------------------------
# 3. Partial derivative with respect to Y
#
# z = x² - y²
# ∂z/∂y = -2y
# ------------------------------------------------------------

def del_z_del_y(x, y):
    return -2 * y


# ------------------------------------------------------------
# 4. Exercise points
# ------------------------------------------------------------

points = [
    (3, 0),
    (2, 3),
    (-2, -3)
]


# ------------------------------------------------------------
# 5. Calculate and display the results
# ------------------------------------------------------------

for x, y in points:

    # Calculate Z
    z = f(x, y)

    # Calculate partial derivative with respect to X
    slope_x = del_z_del_x(x, y)

    # Calculate partial derivative with respect to Y
    slope_y = del_z_del_y(x, y)

    print("x =", x)
    print("y =", y)
    print("z =", z)
    print("∂z/∂x =", slope_x)
    print("∂z/∂y =", slope_y)
    print("-" * 30)

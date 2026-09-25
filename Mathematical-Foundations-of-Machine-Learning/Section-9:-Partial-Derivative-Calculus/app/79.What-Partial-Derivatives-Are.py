import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. Define the multivariate function
# ============================================================

def f(x, y):
    return x**2 - y**2


# ============================================================
# 2. Partial derivative with respect to X
# ============================================================

def del_z_del_x(x, y):
    return 2 * x


# ============================================================
# 3. Partial derivative with respect to Y
# ============================================================

def del_z_del_y(x, y):
    return -2 * y


# ============================================================
# 4. Plot Z with respect to X
# ============================================================

x = np.linspace(-3, 3, 1000)
y = 0

z = f(x, y)

plt.figure()

plt.plot(x, z)

plt.axhline(0, color="gray")
plt.axvline(0, color="gray")

plt.xlabel("X")
plt.ylabel("Z")
plt.title("Z as a function of X")

plt.show()


# ============================================================
# 5. Plot Z with respect to Y
# ============================================================

y = np.linspace(-3, 3, 1000)
x = 0

z = f(x, y)

plt.figure()

plt.plot(y, z)

plt.axhline(0, color="gray")
plt.axvline(0, color="gray")

plt.xlabel("Y")
plt.ylabel("Z")
plt.title("Z as a function of Y")

plt.show()


# ============================================================
# 6. Helper function for X tangent lines
# ============================================================

def point_and_tangent_x(x_values, x_value, y, f, derivative):
    z = f(x_value, y)

    # Plot the point
    plt.scatter(x_value, z)

    # Calculate slope
    m = derivative(x_value, y)

    # Calculate intercept
    b = z - m * x_value

    # Calculate tangent line
    tangent = m * x_values + b

    # Plot tangent
    plt.plot(x_values, tangent, "--")


# ============================================================
# 7. Plot X tangent lines at five points
# ============================================================

x_values = np.linspace(-3, 3, 1000)

plt.figure()

plt.plot(
    x_values,
    f(x_values, 0),
    label="z = x²"
)

plt.axhline(0, color="gray")
plt.axvline(0, color="gray")

for x_value in [-2, -1, 0, 1, 2]:
    point_and_tangent_x(
        x_values,
        x_value,
        0,
        f,
        del_z_del_x
    )

plt.xlabel("X")
plt.ylabel("Z")
plt.title("Partial Derivative of Z with Respect to X")

plt.show()


# ============================================================
# 8. Helper function for Y tangent lines
# ============================================================

def point_and_tangent_y(y_values, y_value, x, f, derivative):
    z = f(x, y_value)

    # Plot the point
    plt.scatter(y_value, z)

    # Calculate slope
    m = derivative(x, y_value)

    # Calculate intercept
    b = z - m * y_value

    # Calculate tangent line
    tangent = m * y_values + b

    # Plot tangent
    plt.plot(y_values, tangent, "--")


# ============================================================
# 9. Plot Y tangent lines at five points
# ============================================================

y_values = np.linspace(-3, 3, 1000)

plt.figure()

plt.plot(
    y_values,
    f(0, y_values),
    label="z = -y²"
)

plt.axhline(0, color="gray")
plt.axvline(0, color="gray")

for y_value in [-2, -1, 0, 1, 2]:
    point_and_tangent_y(
        y_values,
        y_value,
        0,
        f,
        del_z_del_y
    )

plt.xlabel("Y")
plt.ylabel("Z")
plt.title("Partial Derivative of Z with Respect to Y")

plt.show()

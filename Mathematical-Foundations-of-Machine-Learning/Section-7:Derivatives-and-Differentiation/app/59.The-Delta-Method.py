import numpy as np
import matplotlib.pyplot as plt

# Function


def f(x):
    return x**2 + 2*x + 2


# Generate curve
x = np.linspace(-10, 10, 1000)
y = f(x)

# Point P
x1 = 2
y1 = f(x1)

# Small Delta x
delta_x = 1e-6

# Point Q
x2 = x1 + delta_x
y2 = f(x2)

# Slope
m = (y2 - y1) / (x2 - x1)

# Intercept
b = y1 - m*x1

# Tangent line
line = m*x + b

# Plot
plt.plot(x, y, label="Curve")
plt.scatter(x1, y1, label="P")
plt.scatter(x2, y2, label="Q")
plt.plot(x, line, label="Tangent")

plt.legend()
plt.show()

print("Slope =", m)

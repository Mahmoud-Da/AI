import numpy as np
import matplotlib.pyplot as plt

# Function


def f(x):
    return x**2 + 2*x + 2


# Plot curve
x = np.linspace(-10, 10, 1000)
y = f(x)

plt.plot(x, y)

# Point P
x1 = 2
y1 = f(x1)

plt.scatter([x1], [y1])

# Point Q
delta = 1e-6
x2 = x1 + delta
y2 = f(x2)

plt.scatter([x2], [y2])

# Slope
m = (y2 - y1) / (x2 - x1)

# Line equation
b = y2 - m * x2

line = m * x + b

plt.plot(x, line)

plt.show()

print("Slope:", m)

# General differentiation function


def differentiation_demo(func, x, delta):
    return (func(x + delta) - func(x)) / delta


deltas = [1, 0.1, 0.01, 0.001, 1e-6]

print("\nDerivative at x = 2")
for d in deltas:
    print(d, differentiation_demo(f, 2, d))

print("\nDerivative at x = -1")
for d in deltas:
    print(d, differentiation_demo(f, -1, d))

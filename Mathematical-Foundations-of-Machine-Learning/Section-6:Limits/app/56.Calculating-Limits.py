import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Continuous function
# -----------------------------
x = np.linspace(-10, 10, 1000)
y = x**2 + 2*x + 2

plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.title("Continuous Function")
plt.grid(True)
plt.show()

# -----------------------------
# Function with removable discontinuity
# -----------------------------


def f(x):
    return (x**2 - 1)/(x - 1)


print("Approaching 1 from the left:")
print(f(0.9))
print(f(0.99))
print(f(0.999))

print("\nApproaching 1 from the right:")
print(f(1.1))
print(f(1.01))
print(f(1.001))

# -----------------------------
# Sine limit
# -----------------------------


def sine_function(x):
    return np.sin(x)/x


print("\nApproaching 0 from the right:")
print(sine_function(0.1))
print(sine_function(0.01))
print(sine_function(0.001))

print("\nApproaching 0 from the left:")
print(sine_function(-0.1))
print(sine_function(-0.01))
print(sine_function(-0.001))

# -----------------------------
# Infinity example
# -----------------------------


def infinity_function(x):
    return 25/x


print("\nApproaching infinity:")
print(infinity_function(100))
print(infinity_function(1000))
print(infinity_function(1000000))

# -----------------------------
# Plot 25/x without connecting across x = 0
# -----------------------------
x = np.linspace(-10, 10, 1000)

left_x = x[x < 0]
right_x = x[x > 0]

left_y = 25 / left_x
right_y = 25 / right_x

plt.figure(figsize=(6, 4))
plt.plot(left_x, left_y)
plt.plot(right_x, right_y)
plt.title("y = 25/x")
plt.grid(True)
plt.show()

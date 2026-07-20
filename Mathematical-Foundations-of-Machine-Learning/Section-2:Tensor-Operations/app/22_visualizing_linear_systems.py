import numpy as np
import matplotlib.pyplot as plt

# -------- Substitution Example --------
x = np.linspace(-10, 10, 1000)

y1 = 3 * x
y2 = 1 + (5 * x) / 2

plt.figure()
plt.plot(x, y1, label="y = 3x")
plt.plot(x, y2, label="y = (1 + 5x)/2")
plt.scatter(2, 6, label="Solution (2,6)")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0, 3)
plt.ylim(0, 8)
plt.legend()
plt.show()

# -------- Elimination Example --------
x = np.linspace(-10, 10, 1000)

y1 = -5 + (2 * x) / 3
y2 = (7 - 2 * x) / 5

plt.figure()
plt.plot(x, y1, label="y = -5 + (2x/3)")
plt.plot(x, y2, label="y = (7 - 2x)/5")

# Axes
plt.axhline(0)
plt.axvline(0)

# Solution point
plt.scatter(6, -1, label="Solution (6,-1)")

plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1, 8)
plt.ylim(-5, 5)
plt.legend()
plt.show()

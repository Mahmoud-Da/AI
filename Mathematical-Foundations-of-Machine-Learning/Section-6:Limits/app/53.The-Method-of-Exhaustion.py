import numpy as np
import matplotlib.pyplot as plt

# Create circle
theta = np.linspace(0, 2*np.pi, 200)

x = np.cos(theta)
y = np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.axis("equal")
plt.title("Unit Circle")
plt.show()


# Polygon area approximation
def polygon_area(n):
    return 0.5 * n * np.sin(2*np.pi/n)


# Compare approximations
sides = [4, 6, 8, 16, 32, 64]

print("Polygon Area Approximations:")

for n in sides:
    print(f"{n} sides -> {polygon_area(n):.6f}")

print("\nActual Circle Area:")
print(np.pi)

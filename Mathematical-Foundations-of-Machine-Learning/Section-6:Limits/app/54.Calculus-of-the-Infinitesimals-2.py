import numpy as np
import matplotlib.pyplot as plt

# 1. Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  # Relationship: y = 2x

# 2. Start with random guess
m = 0  # slope
b = 0  # intercept
learning_rate = 0.01

# 3. Loss function (Mean Squared Error)


def loss(m, b, x, y):
    y_pred = m * x + b
    return np.mean((y_pred - y) ** 2)

# 4. Derivative (slope) with respect to m


def gradient_m(m, b, x, y):
    y_pred = m * x + b
    return np.mean(2 * (y_pred - y) * x)

# 5. Derivative (slope) with respect to b


def gradient_b(m, b, x, y):
    y_pred = m * x + b
    return np.mean(2 * (y_pred - y))


# 6. Training (Gradient Descent)
losses = []
ms = []

for i in range(100):
    # Calculate slope (derivative)
    dm = gradient_m(m, b, x, y)
    db = gradient_b(m, b, x, y)

    # Update weights (go downhill)
    m = m - learning_rate * dm
    b = b - learning_rate * db

    # Track progress
    losses.append(loss(m, b, x, y))
    ms.append(m)

    if i % 10 == 0:
        print(f"Step {i}: m = {m:.4f}, b = {b:.4f}, Error = {losses[-1]:.4f}")

print(f"\nFinal result: m = {m:.4f}, b = {b:.4f}")

# 7. Visualize the loss curve
plt.figure(figsize=(12, 4))

# Loss function vs weight m
m_values = np.linspace(0, 3, 100)
loss_values = [loss(m_val, b, x, y) for m_val in m_values]

plt.subplot(1, 2, 1)
plt.plot(m_values, loss_values, label="Loss Function")
plt.scatter(ms, losses, color='red', s=10, label="Descent Path")
plt.xlabel("Weight (m)")
plt.ylabel("Error")
plt.title("Loss Curve & Gradient Descent")
plt.legend()
plt.grid(True)

# Data and final line
plt.subplot(1, 2, 2)
plt.scatter(x, y, label="Actual Data")
x_line = np.linspace(0, 6, 100)
y_line = m * x_line + b
plt.plot(x_line, y_line, 'r-', label=f"Final: y = {m:.2f}x + {b:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

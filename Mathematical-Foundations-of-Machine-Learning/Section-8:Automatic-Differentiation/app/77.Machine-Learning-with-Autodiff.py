import torch
import matplotlib.pyplot as plt


# ============================================================
# 1. Data
# ============================================================

x = torch.tensor([
    0.0, 1.0, 2.0, 3.0,
    4.0, 5.0, 6.0, 7.0
])

# Example noisy data generated around:
# y = -0.5x + 2

y = torch.tensor([
    1.8,
    1.6,
    1.1,
    0.4,
    0.1,
    -0.5,
    -1.0,
    -1.4
])


# ============================================================
# 2. Initialize model parameters
# ============================================================

m = torch.tensor(0.9, requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)


# ============================================================
# 3. Regression model
# ============================================================

def regression(x, m, b):
    return m * x + b


# ============================================================
# 4. Mean Squared Error
# ============================================================

def mean_squared_error(y_hat, y):
    error = y_hat - y
    squared_error = error ** 2
    sum_squared_error = torch.sum(squared_error)
    cost = sum_squared_error / len(y)

    return cost


# ============================================================
# 5. Optimizer
# ============================================================

optimizer = torch.optim.SGD(
    [m, b],
    lr=0.01
)


# ============================================================
# 6. Training loop
# ============================================================

epochs = 1000

for epoch in range(epochs):

    # Clear previous gradients
    optimizer.zero_grad()

    # Step 1: Forward pass
    y_hat = regression(x, m, b)

    # Step 2: Calculate cost
    cost = mean_squared_error(y_hat, y)

    # Step 3: Automatic differentiation
    cost.backward()

    # Step 4: Update parameters
    optimizer.step()

    if epoch % 100 == 0:
        print(
            f"Epoch: {epoch}, "
            f"Cost: {cost.item():.4f}, "
            f"m: {m.item():.4f}, "
            f"b: {b.item():.4f}"
        )


# ============================================================
# 7. Final parameters
# ============================================================

print("\nFinal parameters:")
print(f"Slope (m): {m.item():.4f}")
print(f"Y-intercept (b): {b.item():.4f}")


# ============================================================
# 8. Final predictions
# ============================================================

y_hat = regression(x, m, b)

print("\nPredictions:")
print(y_hat)


# ============================================================
# 9. Plot results
# ============================================================

plt.scatter(x.detach().numpy(), y.detach().numpy())

plt.plot(
    x.detach().numpy(),
    y_hat.detach().numpy()
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression with PyTorch Autodiff")

plt.show()

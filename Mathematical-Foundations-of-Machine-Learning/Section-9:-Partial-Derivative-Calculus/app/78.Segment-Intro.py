import torch


# --------------------------------------------------
# 1. Input data
# --------------------------------------------------

x = torch.tensor(
    [0., 1., 2., 3., 4., 5., 6., 7.]
)

y = torch.tensor(
    [2.0, 1.6, 1.0, 0.7, 0.1, -0.4, -0.9, -1.5]
)


# --------------------------------------------------
# 2. Initialize model parameters
# --------------------------------------------------

m = torch.tensor(
    0.9,
    requires_grad=True
)

b = torch.tensor(
    0.1,
    requires_grad=True
)


# --------------------------------------------------
# 3. Regression model
# --------------------------------------------------

def regression(x, m, b):
    return m * x + b


# --------------------------------------------------
# 4. Mean Squared Error
# --------------------------------------------------

def mse(y_hat, y):
    error = y_hat - y
    squared_error = error ** 2
    return squared_error.mean()


# --------------------------------------------------
# 5. Optimizer
# --------------------------------------------------

optimizer = torch.optim.SGD(
    [m, b],
    lr=0.01
)


# --------------------------------------------------
# 6. Machine learning loop
# --------------------------------------------------

for epoch in range(1000):

    # Step 0: Clear previous gradients
    optimizer.zero_grad()

    # Step 1: Forward pass
    y_hat = regression(x, m, b)

    # Step 2: Calculate cost
    cost = mse(y_hat, y)

    # Step 3: Automatic differentiation
    cost.backward()

    # Step 4: Update parameters
    optimizer.step()

    # Display progress
    if epoch % 100 == 0:
        print(
            f"Epoch: {epoch}, "
            f"Cost: {cost.item():.4f}, "
            f"m: {m.item():.4f}, "
            f"b: {b.item():.4f}"
        )


# --------------------------------------------------
# 7. Final results
# --------------------------------------------------

print("\nFinal parameters:")
print(f"m = {m.item():.4f}")
print(f"b = {b.item():.4f}")

print("\nFinal predictions:")
print(regression(x, m, b))

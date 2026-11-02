import torch
import matplotlib.pyplot as plt


# ==================================================
# 1. Prepare the training data
# ==================================================

xs = torch.tensor(
    [0., 1., 2., 3., 4., 5., 6., 7.]
)

ys = torch.tensor(
    [2.1, 1.6, 0.9, 0.4, -0.2, -0.7, -1.0, -1.377]
)

N = len(xs)


# ==================================================
# 2. Define the regression model and MSE
# ==================================================

def regression(x, m, b):
    return m * x + b


def mse(y_hat, y):
    squared_errors = (y_hat - y) ** 2
    return squared_errors.sum() / len(y)


# ==================================================
# 3. Initialize model parameters
# ==================================================

m = torch.tensor(0.9, requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)


# ==================================================
# 4. Initial forward pass and cost
# ==================================================

y_hat = regression(xs, m, b)
cost = mse(y_hat, ys)

print("Initial cost:", cost.item())
print("Initial slope m:", m.item())
print("Initial intercept b:", b.item())


# ==================================================
# 5. Calculate gradients with PyTorch autodiff
# ==================================================

cost.backward()

autodiff_dm = m.grad.detach().clone()
autodiff_db = b.grad.detach().clone()

print("\nAutomatic differentiation:")
print("dC/dm:", autodiff_dm.item())
print("dC/db:", autodiff_db.item())


# ==================================================
# 6. Calculate gradients manually
# ==================================================

with torch.no_grad():
    errors = regression(xs, m, b) - ys

    dC_dm = (2 / N) * (xs * errors).sum()
    dC_db = (2 / N) * errors.sum()

print("\nManual gradients:")
print("dC/dm:", dC_dm.item())
print("dC/db:", dC_db.item())


# ==================================================
# 7. Compare manual gradients with autodiff
# ==================================================

print("\nGradient comparison:")

print(
    "dC/dm matches:",
    torch.allclose(autodiff_dm, dC_dm)
)

print(
    "dC/db matches:",
    torch.allclose(autodiff_db, dC_db)
)


# ==================================================
# 8. Construct the gradient column vector
#    Parameter order: [b, m]
# ==================================================

gradient = torch.stack([
    dC_db,
    dC_dm
]).reshape(-1, 1)

print("\nGradient vector:")
print(gradient)


# ==================================================
# 9. Define a plotting function
# ==================================================

def plot_regression(xs, ys, m, b, cost, epoch):
    with torch.no_grad():
        predictions = regression(xs, m, b)

    plt.figure(figsize=(8, 5))

    plt.scatter(
        xs.numpy(),
        ys.numpy(),
        label="Training data"
    )

    plt.plot(
        xs.numpy(),
        predictions.numpy(),
        label="Regression line"
    )

    plt.title(
        f"Epoch {epoch} | "
        f"MSE: {cost.item():.4f} | "
        f"m: {m.item():.4f} | "
        f"b: {b.item():.4f}"
    )

    plt.xlabel("Input (x)")
    plt.ylabel("Output (y)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


# Plot the initial model
plot_regression(xs, ys, m, b, cost, epoch=0)


# ==================================================
# 10. Initialize the SGD optimizer
# ==================================================

learning_rate = 0.01

optimizer = torch.optim.SGD(
    [m, b],
    lr=learning_rate
)


# ==================================================
# 11. Train the model
# ==================================================

num_epochs = 1000

for epoch in range(1, num_epochs + 1):

    # Step 1: Clear previous gradients
    optimizer.zero_grad()

    # Step 2: Forward pass
    y_hat = regression(xs, m, b)

    # Step 3: Calculate MSE
    cost = mse(y_hat, ys)

    # Step 4: Calculate gradients
    cost.backward()

    # Step 5: Update parameters
    optimizer.step()

    # Display progress at selected intervals
    if epoch % 100 == 0:
        with torch.no_grad():
            current_predictions = regression(xs, m, b)
            current_cost = mse(current_predictions, ys)

        print(
            f"Epoch {epoch:4d} | "
            f"Cost: {current_cost.item():.6f} | "
            f"m: {m.item():.6f} | "
            f"b: {b.item():.6f}"
        )


# ==================================================
# 12. Evaluate and plot the final model
# ==================================================

with torch.no_grad():
    final_predictions = regression(xs, m, b)
    final_cost = mse(final_predictions, ys)

print("\nFinal results:")
print("Final MSE:", final_cost.item())
print("Final slope m:", m.item())
print("Final intercept b:", b.item())

plot_regression(
    xs,
    ys,
    m,
    b,
    final_cost,
    epoch=num_epochs
)

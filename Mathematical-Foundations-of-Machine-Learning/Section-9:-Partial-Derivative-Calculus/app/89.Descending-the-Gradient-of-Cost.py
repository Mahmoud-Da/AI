import torch
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Prepare the data
# --------------------------------------------------

xs = torch.tensor(
    [0., 1., 2., 3., 4., 5., 6., 7.]
)

ys = torch.tensor(
    [2.1, 1.6, 0.9, 0.4, -0.2, -0.7, -1.0, -1.377]
)


# --------------------------------------------------
# 2. Initialize the model parameters
# --------------------------------------------------

m = torch.tensor(0.9, requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)


# --------------------------------------------------
# 3. Define the regression model
# --------------------------------------------------

def regression(x, m, b):
    return m * x + b


# --------------------------------------------------
# 4. Define mean squared error
# --------------------------------------------------

def mse(y_hat, y):
    squared_errors = (y_hat - y) ** 2
    return squared_errors.sum() / len(y)


# --------------------------------------------------
# 5. Step 1: Forward pass
# --------------------------------------------------

y_hat = regression(xs, m, b)

print("Predictions:")
print(y_hat.detach())

print("\nNumber of input examples:", len(xs))
print("Number of predictions:", len(y_hat))


# --------------------------------------------------
# 6. Step 2: Calculate cost
# --------------------------------------------------

cost = mse(y_hat, ys)

print("\nMean squared error:")
print(cost.item())


# --------------------------------------------------
# 7. Step 3: Calculate gradients
# --------------------------------------------------

cost.backward()

print("\nGradients from automatic differentiation:")
print("dC/dm:", m.grad.item())
print("dC/db:", b.grad.item())


# --------------------------------------------------
# 8. Visualize the predictions
# --------------------------------------------------

with torch.no_grad():
    predictions = regression(xs, m, b)

plt.scatter(xs.numpy(), ys.numpy(), label="True data")
plt.plot(
    xs.numpy(),
    predictions.numpy(),
    label="Model predictions"
)

plt.xlabel("Input (x)")
plt.ylabel("Output (y)")
plt.title("Batch Linear Regression")
plt.legend()
plt.show()

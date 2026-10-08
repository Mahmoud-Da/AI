import torch


# --------------------------------------------------
# 1. Define the regression model
# --------------------------------------------------

def regression(x, m, b):
    return m * x + b


# --------------------------------------------------
# 2. Define quadratic cost for one data point
# --------------------------------------------------

def quadratic_cost(y_hat, y):
    return (y_hat - y) ** 2


# --------------------------------------------------
# 3. Example values
# --------------------------------------------------

# These should be replaced with the exact x, y,
# m, and b values from the lecture notebook.

x = torch.tensor(7.0)
y = torch.tensor(-1.4)

m = torch.tensor(0.9, requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)


# --------------------------------------------------
# 4. Forward pass
# --------------------------------------------------

y_hat = regression(x, m, b)

print("Prediction (y_hat):", y_hat.item())


# --------------------------------------------------
# 5. Calculate quadratic cost
# --------------------------------------------------

cost = quadratic_cost(y_hat, y)

print("Cost:", cost.item())


# --------------------------------------------------
# 6. Calculate gradients automatically with PyTorch
# --------------------------------------------------

cost.backward()

print("\nPyTorch automatic differentiation:")
print("dC/dm:", m.grad.item())
print("dC/db:", b.grad.item())


# --------------------------------------------------
# 7. Calculate gradients manually
# --------------------------------------------------

dC_dm = 2 * x * (y_hat.detach() - y)
dC_db = 2 * (y_hat.detach() - y)

print("\nManual derivatives:")
print("dC/dm:", dC_dm.item())
print("dC/db:", dC_db.item())


# --------------------------------------------------
# 8. Compare the results
# --------------------------------------------------

print("\nComparison:")
print(
    "dC/dm match:",
    torch.allclose(m.grad, dC_dm)
)

print(
    "dC/db match:",
    torch.allclose(b.grad, dC_db)
)


# --------------------------------------------------
# 9. Construct the gradient vector
# --------------------------------------------------

# Parameter order:
# [b, m]

gradient = torch.tensor([
    dC_db.item(),
    dC_dm.item()
])

print("\nGradient vector:")
print(gradient)


# --------------------------------------------------
# 10. Convert to a column vector
# --------------------------------------------------

gradient_column = gradient.reshape(-1, 1)

print("\nGradient as a column vector:")
print(gradient_column)

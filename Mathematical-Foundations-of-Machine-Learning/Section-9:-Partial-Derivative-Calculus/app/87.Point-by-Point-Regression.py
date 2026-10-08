import torch


# ============================================================
# 1. Data
# ============================================================

# Artificial data used in the lecture.
# The values represent:
# x = drug dosage
# y = forgetfulness

xs = torch.tensor([
    0.0,
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
    7.0
])

ys = torch.tensor([
    2.1,
    1.6,
    0.9,
    0.4,
    -0.2,
    -0.7,
    -1.0,
    -1.377
])


# ============================================================
# 2. Model parameters
# ============================================================

# Near-zero initialization.
# requires_grad=True tells PyTorch to track operations
# involving these parameters.

m = torch.tensor(0.9, requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)


# ============================================================
# 3. Select one data point
# ============================================================

# Python uses zero-based indexing.
# Index 7 is the eighth and final data point.

i = 7

x = xs[i]
y = ys[i]


print("Selected data point")
print("x =", x.item())
print("y =", y.item())


# ============================================================
# 4. Step 1 — Forward pass
# ============================================================

# Linear regression model:
#
# ŷ = mx + b

y_hat = m * x + b

print()
print("Step 1 — Forward pass")
print("ŷ =", y_hat.item())


# ============================================================
# 5. Step 2 — Quadratic cost
# ============================================================

def squared_error(y_hat, y):
    return (y_hat - y) ** 2


cost = squared_error(y_hat, y)

print()
print("Step 2 — Quadratic cost")
print("Cost =", cost.item())


# ============================================================
# 6. Step 3 — Automatic differentiation
# ============================================================

# PyTorch calculates:
#
# ∂C/∂m
# ∂C/∂b

cost.backward()

print()
print("Step 3 — Gradient")
print("∂C/∂m =", m.grad.item())
print("∂C/∂b =", b.grad.item())


# ============================================================
# 7. Gradient
# ============================================================

gradient = torch.tensor([
    m.grad.item(),
    b.grad.item()
])

print()
print("Gradient =", gradient)

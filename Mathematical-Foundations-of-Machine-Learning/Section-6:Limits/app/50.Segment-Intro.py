import numpy as np
import torch

# Function


def f(x):
    return x**2


# Evaluate function
x = 2

print("f(x):", f(x))

# Manual derivative
manual_derivative = 2 * x

print("Manual derivative:", manual_derivative)

# Automatic differentiation with PyTorch
x_torch = torch.tensor(
    2.0,
    requires_grad=True
)

y = x_torch ** 2

y.backward()

print(
    "PyTorch derivative:",
    x_torch.grad.item()
)

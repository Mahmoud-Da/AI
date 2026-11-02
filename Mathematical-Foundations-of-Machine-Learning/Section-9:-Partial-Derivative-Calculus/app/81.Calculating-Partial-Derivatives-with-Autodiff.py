import torch


# ============================================================
# 1. Define the multivariate function
# ============================================================

def f(x, y):
    return x**2 - y**2


# ============================================================
# 2. Function to calculate Z and its partial derivatives
#    using PyTorch automatic differentiation
# ============================================================

def calculate_gradients(x_value, y_value):

    # Create fresh tensors for each calculation
    # and enable gradient tracking.
    x = torch.tensor(float(x_value), requires_grad=True)
    y = torch.tensor(float(y_value), requires_grad=True)

    # Forward pass
    z = f(x, y)

    # Backward pass
    z.backward()

    # Return the output and both gradients
    return z, x.grad, y.grad


# ============================================================
# 3. Exercises from the previous lecture
# ============================================================

points = [
    (3, 0),
    (2, 3),
    (-2, -3)
]


# ============================================================
# 4. Calculate all exercises automatically
# ============================================================

for x_value, y_value in points:

    z, dx, dy = calculate_gradients(
        x_value,
        y_value
    )

    print("x =", x_value)
    print("y =", y_value)
    print("z =", z.item())
    print("∂z/∂x =", dx.item())
    print("∂z/∂y =", dy.item())
    print("-" * 30)

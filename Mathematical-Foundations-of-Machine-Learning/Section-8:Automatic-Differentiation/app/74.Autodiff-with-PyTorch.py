import torch

# Create the input tensor
x = torch.tensor(5.0)

# Enable gradient tracking
x.requires_grad_()

# Forward pass: y = x²
y = x**2

# Automatic differentiation
y.backward()

# Display the result
print("x:", x)
print("y:", y)
print("dy/dx:", x.grad)

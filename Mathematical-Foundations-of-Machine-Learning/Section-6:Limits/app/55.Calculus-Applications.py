import numpy as np

# Function to minimize


def f(x):
    return x**2

# Derivative of the function


def df(x):
    return 2*x


# Initial parameter
x = 5

learning_rate = 0.1
iterations = 20

print("Starting x:", x)

for i in range(iterations):
    gradient = df(x)
    x = x - learning_rate * gradient
    print(f"Iteration {i+1}: x = {x:.6f}, f(x) = {f(x):.6f}")

print("\nApproximate minimum:")
print("x =", x)
print("f(x) =", f(x))

# Constant function
def f(x):
    return 25

# Numerical derivative


def derivative(f, x, delta=1e-6):
    return (f(x + delta) - f(x)) / delta


# Test function values
print("Function values:")
print(f(-100))
print(f(0))
print(f(10))
print(f(500))

# Test derivative
print("\nDerivative:")
print(derivative(f, 2))
print(derivative(f, -5))
print(derivative(f, 100))

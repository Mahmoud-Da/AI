# Power Rule on a Function Chain
# Example:
# y = (3x + 1)^2

# Original function
def f(x):
    return (3 * x + 1) ** 2


# Inner function
def u(x):
    return 3 * x + 1


# Derivative of the inner function
def du_dx(x):
    return 3


# Derivative using the power rule on a function chain
def df_dx(x):
    n = 2
    return n * u(x) ** (n - 1) * du_dx(x)


# Simplified derivative:
# dy/dx = 18x + 6
def df_dx_simplified(x):
    return 18 * x + 6


# Example calculation
x = 2

print("f(x) =", f(x))
print("Derivative using chain-power rule =", df_dx(x))
print("Simplified derivative =", df_dx_simplified(x))

def f(x):
    return x**2 + 2*x + 2

# Numerical first derivative


def derivative(f, x, delta=1e-6):
    return (f(x + delta) - f(x)) / delta

# Numerical second derivative


def second_derivative(f, x, delta=1e-6):
    return (
        f(x + delta)
        - 2 * f(x)
        + f(x - delta)
    ) / (delta ** 2)


# Test
print("f(2) =", f(2))
print("First derivative =", derivative(f, 2))
print("Second derivative =", second_derivative(f, 2))

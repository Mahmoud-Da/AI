import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. Power Rule
# Integral of x^4 = x^5 / 5 + C
# ============================================================

def power_function(x):
    return x**4


def power_antiderivative(x):
    return x**5 / 5


# ============================================================
# 2. Constant Multiple Rule
# Integral of 9x^2 = 3x^3 + C
# ============================================================

def constant_multiple_function(x):
    return 9 * x**2


def constant_multiple_antiderivative(x):
    return 3 * x**3


# ============================================================
# 3. Sum Rule
# Integral of x^4 + 9x^2
# = x^5 / 5 + 3x^3 + C
# ============================================================

def combined_function(x):
    return x**4 + 9 * x**2


def combined_antiderivative(x):
    return x**5 / 5 + 3 * x**3


# ============================================================
# 4. Plot the Functions
# ============================================================

x_values = np.linspace(0, 2, 200)

plt.figure(figsize=(15, 4))

# Power rule
plt.subplot(1, 3, 1)
plt.plot(
    x_values,
    power_function(x_values),
    label="f(x) = x^4"
)
plt.plot(
    x_values,
    power_antiderivative(x_values),
    label="F(x) = x^5 / 5"
)
plt.title("Power Rule")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
plt.legend()

# Constant multiple rule
plt.subplot(1, 3, 2)
plt.plot(
    x_values,
    constant_multiple_function(x_values),
    label="f(x) = 9x^2"
)
plt.plot(
    x_values,
    constant_multiple_antiderivative(x_values),
    label="F(x) = 3x^3"
)
plt.title("Constant Multiple Rule")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
plt.legend()

# Sum rule
plt.subplot(1, 3, 3)
plt.plot(
    x_values,
    combined_function(x_values),
    label="f(x) = x^4 + 9x^2"
)
plt.plot(
    x_values,
    combined_antiderivative(x_values),
    label="F(x) = x^5/5 + 3x^3"
)
plt.title("Sum Rule")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()


# ============================================================
# 5. Numerical Verification
# Differentiate the antiderivative approximately and compare
# it with the original function.
# ============================================================

print("Numerical Verification")
print("=" * 60)

test_points = [0.5, 1.0, 1.5, 2.0]
h = 1e-5

for x in test_points:
    numerical_derivative = (
        combined_antiderivative(x + h)
        - combined_antiderivative(x - h)
    ) / (2 * h)

    original_value = combined_function(x)

    print(f"\nx = {x:.1f}")
    print(f"Original function:    {original_value:.6f}")
    print(f"Numerical derivative: {numerical_derivative:.6f}")

    assert np.isclose(
        numerical_derivative,
        original_value,
        rtol=1e-5,
        atol=1e-5
    )

print("\nAll numerical verification tests passed!")

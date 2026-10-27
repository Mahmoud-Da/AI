import numpy as np


# ============================================================
# 1. Exercise 1: Integrate x^5
# Integral: x^6 / 6 + C
# ============================================================

def integrate_x5(x):
    return x**6 / 6


# ============================================================
# 2. Exercise 2: Integrate 12x^5
# Integral: 2x^6 + C
# ============================================================

def integrate_12x5(x):
    return 2 * x**6


# ============================================================
# 3. Exercise 3: Integrate 12x^5 - x
# Integral: 2x^6 - x^2 / 2 + C
# ============================================================

def original_function(x):
    return 12 * x**5 - x


def integrate_12x5_minus_x(x):
    return 2 * x**6 - x**2 / 2


# ============================================================
# 4. Display the Results at x = 2
# These functions use C = 0.
# ============================================================

x = 2

print("Integration Exercises")
print("=" * 45)

print("\nExercise 1: Integral of x^5")
print("Antiderivative: x^6 / 6 + C")
print(f"Value at x = {x}: {integrate_x5(x)}")

print("\nExercise 2: Integral of 12x^5")
print("Antiderivative: 2x^6 + C")
print(f"Value at x = {x}: {integrate_12x5(x)}")

print("\nExercise 3: Integral of 12x^5 - x")
print("Antiderivative: 2x^6 - x^2 / 2 + C")
print(f"Value at x = {x}: {integrate_12x5_minus_x(x)}")


# ============================================================
# 5. Verify Exercise 3 Numerically
# Approximate the derivative of the antiderivative.
# ============================================================

print("\nNumerical Verification")
print("=" * 45)

h = 1e-5
test_points = [0.5, 1.0, 1.5, 2.0]

for x in test_points:
    numerical_derivative = (
        integrate_12x5_minus_x(x + h)
        - integrate_12x5_minus_x(x - h)
    ) / (2 * h)

    expected_value = original_function(x)

    print(f"\nx = {x}")
    print(f"Original function:    {expected_value:.6f}")
    print(f"Numerical derivative: {numerical_derivative:.6f}")

    assert np.isclose(
        numerical_derivative,
        expected_value,
        rtol=1e-5,
        atol=1e-5
    )

print("\nAll verification tests passed!")

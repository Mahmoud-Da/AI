
# ============================================================
# 1. Import the numerical integration function
# ============================================================

from scipy.integrate import quad


# ============================================================
# 2. Define the mathematical function
# f(x) = x / 2
# ============================================================

def g(x):
    return x / 2


# ============================================================
# 3. Define the integration limits
# ============================================================

lower_limit = 1
upper_limit = 2


# ============================================================
# 4. Calculate the definite integral
# ============================================================

result, error = quad(
    g,
    lower_limit,
    upper_limit
)


# ============================================================
# 5. Display the results
# ============================================================

print("Numerical Integration")
print("-" * 40)

print(f"Function: f(x) = x / 2")
print(f"Integration interval: [{lower_limit}, {upper_limit}]")

print(f"\nIntegration result: {result}")
print(f"Estimated numerical error: {error}")


# ============================================================
# 6. Compare with the symbolic result
# ============================================================

symbolic_result = 3 / 4

print("\nComparison")
print("-" * 40)

print(f"Numerical result: {result}")
print(f"Symbolic result:  {symbolic_result}")

print(f"Difference: {abs(result - symbolic_result)}")

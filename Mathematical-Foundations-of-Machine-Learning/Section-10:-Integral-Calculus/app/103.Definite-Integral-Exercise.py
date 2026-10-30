
from scipy.integrate import quad

# Step 1: Define the function


def f(x):
    return 2 * x


# Step 2: Define the integration limits
lower_limit = 3
upper_limit = 4


# Step 3: Calculate the definite integral
result, error = quad(f, lower_limit, upper_limit)


# Step 4: Display the numerical result
print("Numerical Integration")
print("---------------------")
print("Function: f(x) = 2x")
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("Integral result:", result)
print("Estimated absolute error:", error)


# Step 5: Compare with the symbolic solution
symbolic_result = 4**2 - 3**2

print("\nSymbolic Integration")
print("--------------------")
print("Exact result:", symbolic_result)

print("\nComparison")
print("-----------")
print("Both methods agree:", abs(result - symbolic_result) < 1e-10)

import sympy as sp

# Variable
x = sp.Symbol('x')

# Numerator and denominator
W = 4*x**2
Z = x**3 + 1

# Step 1: Differentiate numerator
dW = sp.diff(W, x)

# Step 2: Differentiate denominator
dZ = sp.diff(Z, x)

print("W' =", dW)
print("Z' =", dZ)

# Step 3: Apply Quotient Rule
quotient_derivative = (Z*dW - W*dZ) / Z**2

print("\nBefore Simplification:")
print(quotient_derivative)

# Step 4: Simplify numerator
simplified_numerator = sp.expand((Z*dW) - (W*dZ))

print("\nSimplified Numerator:")
print(simplified_numerator)

print("\nFinal Derivative:")
print(simplified_numerator / Z**2)

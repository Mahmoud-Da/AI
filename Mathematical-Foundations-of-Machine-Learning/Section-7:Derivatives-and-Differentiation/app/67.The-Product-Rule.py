import sympy as sp

# Variable
x = sp.Symbol('x')

# Original functions
W = 6*x**3
Z = 7*x**4

# Step 1: Differentiate
dW = sp.diff(W, x)
dZ = sp.diff(Z, x)

print("W' =", dW)
print("Z' =", dZ)

# Step 2: Product Rule
product_derivative = W*dZ + Z*dW

print("\nBefore Simplification:")
print(product_derivative)

# Step 3: Simplify
final_answer = sp.expand(product_derivative)

print("\nFinal Derivative:")
print(final_answer)

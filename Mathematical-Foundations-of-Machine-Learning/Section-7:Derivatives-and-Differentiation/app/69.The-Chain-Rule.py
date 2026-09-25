import sympy as sp

# Define variable
x = sp.symbols('x')

# Original function
y = (2*x**2 + 8)**2

# Differentiate using SymPy
dy_dx = sp.diff(y, x)

print("Original Function:")
print(y)

print("\nDerivative:")
print(dy_dx)

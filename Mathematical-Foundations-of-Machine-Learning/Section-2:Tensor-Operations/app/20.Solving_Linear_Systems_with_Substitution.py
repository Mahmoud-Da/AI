import sympy as sp

x, y = sp.symbols('x y')

# Example 1
eq1 = sp.Eq(x + y, 6)
eq2 = sp.Eq(2*x + 3*y, 16)
print("Example 1:", sp.solve((eq1, eq2), (x, y)))

# Example 2
eq1 = sp.Eq(-x + 4*y, 0)
eq2 = sp.Eq(2*x - 5*y, -6)
print("Example 2:", sp.solve((eq1, eq2), (x, y)))

# Example 3 (No solution)
eq1 = sp.Eq(y, x + 1)
eq2 = sp.Eq(-4*x + y, 2)
print("Example 3:", sp.solve((eq1, eq2), (x, y)))

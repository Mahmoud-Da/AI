import sympy as sp

x, y = sp.symbols('x y')

# Example 1
eq1 = sp.Eq(2*x - 3*y, 15)
eq2 = sp.Eq(4*x + 10*y, 14)
print("Example 1:", sp.solve((eq1, eq2), (x, y)))

# Practice Example 1
eq1 = sp.Eq(4*x - 3*y, 25)
eq2 = sp.Eq(-3*x + 8*y, 10)
print("Example 2:", sp.solve((eq1, eq2), (x, y)))

# Practice Example 3
eq1 = sp.Eq(2*x + y, 2)
eq2 = sp.Eq(5*x + 3*y, 7)
print("Example 3:", sp.solve((eq1, eq2), (x, y)))

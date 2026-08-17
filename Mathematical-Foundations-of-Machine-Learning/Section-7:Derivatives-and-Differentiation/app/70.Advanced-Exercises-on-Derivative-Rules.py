import sympy as sp

# Define the variable
x = sp.symbols('x')


# --------------------------------------------------
# Exercise 1: Product Rule
# y = (2x^2 + 6x)(2x^3 + 5x^2)
# --------------------------------------------------

W1 = 2*x**2 + 6*x
Z1 = 2*x**3 + 5*x**2

y1 = W1 * Z1
dy1_dx = sp.simplify(sp.diff(y1, x))

print("Exercise 1:")
print("y =", y1)
print("dy/dx =", dy1_dx)


# --------------------------------------------------
# Exercise 2: Quotient Rule
# y = 6x^2 / (2 - x)
# --------------------------------------------------

W2 = 6*x**2
Z2 = 2 - x

y2 = W2 / Z2
dy2_dx = sp.simplify(sp.diff(y2, x))

print("\nExercise 2:")
print("y =", y2)
print("dy/dx =", dy2_dx)


# --------------------------------------------------
# Exercise 3: Chain Rule
# y = (3x + 1)^2
# --------------------------------------------------

y3 = (3*x + 1)**2
dy3_dx = sp.simplify(sp.diff(y3, x))

print("\nExercise 3:")
print("y =", y3)
print("dy/dx =", dy3_dx)


# --------------------------------------------------
# Exercise 4: Chain Rule
# y = (x^2 + 5x)^6
# --------------------------------------------------

y4 = (x**2 + 5*x)**6
dy4_dx = sp.simplify(sp.diff(y4, x))

print("\nExercise 4:")
print("y =", y4)
print("dy/dx =", dy4_dx)


# --------------------------------------------------
# Exercise 5: Multiple Chain Rule
# y = 1 / ((x^4 + 1)^5 + 7)
# --------------------------------------------------

y5 = 1 / ((x**4 + 1)**5 + 7)
dy5_dx = sp.simplify(sp.diff(y5, x))

print("\nExercise 5:")
print("y =", y5)
print("dy/dx =", dy5_dx)

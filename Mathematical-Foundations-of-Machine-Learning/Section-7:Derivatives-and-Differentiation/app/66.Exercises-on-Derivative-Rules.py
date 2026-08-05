import sympy as sp

x = sp.Symbol('x')

# Exercise 1
y1 = -5*x**3
print("Exercise 1:")
print(sp.diff(y1, x))

# Exercise 2
y2 = 2*x**2 + 2*x + 2
print("\nExercise 2:")
print(sp.diff(y2, x))

# Exercise 3
y3 = 10*x**5 - 6*x**3 - x + 5
print("\nExercise 3:")
print(sp.diff(y3, x))

# Exercise 4
y4 = x**2 + 2*x + 2
dy4 = sp.diff(y4, x)

print("\nExercise 4:")
print("Derivative:", dy4)
print("Slope at x=2:", dy4.subs(x, 2))

# Exercise 5
print("\nExercise 5:")
print("Slope at x=-1:", dy4.subs(x, -1))

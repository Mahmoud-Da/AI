import numpy as np

# ==========================================
# Exercise 1: Matrix × Vector
# ==========================================

A = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

b = np.array([
    [-1],
    [1],
    [-2]
])

result1 = np.dot(A, b)

print("Exercise 1 Result:")
print(result1)

# ==========================================
# Exercise 2: Identity Matrix × Vector
# ==========================================

I = np.eye(3)

result2 = np.dot(I, b)

print("\nExercise 2 Result:")
print(result2)

# ==========================================
# Exercise 3: Matrix × Matrix
# ==========================================

B = np.array([
    [-1, 0],
    [1, 1],
    [-2, 2]
])

result3 = np.dot(A, B)

print("\nExercise 3 Result:")
print(result3)

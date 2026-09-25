# -----------------------------------
# Exercise 1
# -----------------------------------

def ex1(x):
    return (x**2 - 1)/(x - 1)


print("Exercise 1:", ex1(0))


# -----------------------------------
# Exercise 2
# -----------------------------------

def ex2(x):
    return (x**2 - 25)/(x + 5)


print("\nExercise 2 (Left)")
for x in [-5.1, -5.01, -5.001]:
    print(x, ex2(x))

print("\nExercise 2 (Right)")
for x in [-4.9, -4.99, -4.999]:
    print(x, ex2(x))


# -----------------------------------
# Exercise 3
# -----------------------------------

def ex3(x):
    return (x**2 - 2*x - 8)/(x - 4)


print("\nExercise 3 (Left)")
for x in [3.9, 3.99, 3.999]:
    print(x, ex3(x))

print("\nExercise 3 (Right)")
for x in [4.1, 4.01, 4.001]:
    print(x, ex3(x))


# -----------------------------------
# Exercise 4
# -----------------------------------

def infinity_function(x):
    return 25/x


print("\nApproaching Negative Infinity")
for x in [-100, -1000, -1000000]:
    print(x, infinity_function(x))


# -----------------------------------
# Exercise 5
# -----------------------------------

print("\nApproaching Zero From Right")
for x in [0.1, 0.01, 0.001]:
    print(x, infinity_function(x))

print("\nApproaching Zero From Left")
for x in [-0.1, -0.01, -0.001]:
    print(x, infinity_function(x))

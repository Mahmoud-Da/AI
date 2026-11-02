# Example function:
# z = x^2 + y^2

def f(x, y):
    return x**2 + y**2


# Partial derivative with respect to x:
# ∂z/∂x = 2x

def dz_dx(x, y):
    return 2 * x


# Partial derivative with respect to y:
# ∂z/∂y = 2y

def dz_dy(x, y):
    return 2 * y


# Example input values
x = 3
y = 4


# Calculate the function
z = f(x, y)


# Calculate the partial derivatives
partial_x = dz_dx(x, y)
partial_y = dz_dy(x, y)


# Display results
print("z =", z)
print("∂z/∂x =", partial_x)
print("∂z/∂y =", partial_y)

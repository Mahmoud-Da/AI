# Automatic Differentiation - Conceptual Example
#
# The lecture explains autodiff conceptually through
# a sequence of arithmetic operations.
#
# Forward computation:
# x -> u -> y

# Input
x = 2.0

# First operation
u = x ** 2

# Second operation
y = u ** 3

# Display the forward-pass values
print("x =", x)
print("u =", u)
print("y =", y)

# The mathematical chain rule for this computation is:
#
# dy/dx = dy/du * du/dx
#
# For:
# u = x²
# y = u³
#
# dy/du = 3u²
# du/dx = 2x
#
# Therefore:
# dy/dx = (3u²)(2x)

dy_du = 3 * u ** 2
du_dx = 2 * x

dy_dx = dy_du * du_dx

print("dy/du =", dy_du)
print("du/dx =", du_dx)
print("dy/dx =", dy_dx)

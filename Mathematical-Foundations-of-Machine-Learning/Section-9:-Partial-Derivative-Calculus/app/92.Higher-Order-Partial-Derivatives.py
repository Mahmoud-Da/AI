import sympy as sp

# ============================================================
# Step 1: Define symbolic variables
# ============================================================

x, y, t, theta = sp.symbols("x y t theta")

# ============================================================
# Step 2: Demonstrate distance, speed, and acceleration
# ============================================================

distance = t**2

speed = sp.diff(distance, t)
acceleration = sp.diff(distance, t, 2)

print("DISTANCE, SPEED, AND ACCELERATION")
print("Distance function:", distance)
print("Speed function:", speed)
print("Acceleration function:", acceleration)

time_value = 3

print("Distance at t=3:", distance.subs(t, time_value))
print("Speed at t=3:", speed.subs(t, time_value))
print(
    "Acceleration at t=3:",
    acceleration.subs(t, time_value)
)

# ============================================================
# Step 3: Define the multivariable function
# z = x^2 + 5xy + 2y^2
# ============================================================

z = x**2 + 5*x*y + 2*y**2

print("\nMULTIVARIABLE FUNCTION")
print("z =", z)

# ============================================================
# Step 4: Calculate first-order partial derivatives
# ============================================================

dz_dx = sp.diff(z, x)
dz_dy = sp.diff(z, y)

print("\nFIRST-ORDER PARTIAL DERIVATIVES")
print("dz/dx =", dz_dx)
print("dz/dy =", dz_dy)

# ============================================================
# Step 5: Calculate unmixed second-order partial derivatives
# ============================================================

d2z_dx2 = sp.diff(z, x, 2)
d2z_dy2 = sp.diff(z, y, 2)

print("\nUNMIXED SECOND-ORDER PARTIAL DERIVATIVES")
print("d²z/dx² =", d2z_dx2)
print("d²z/dy² =", d2z_dy2)

# ============================================================
# Step 6: Calculate mixed second-order partial derivatives
# ============================================================

# Differentiate with respect to y, then x
d2z_dydx = sp.diff(sp.diff(z, y), x)

# Differentiate with respect to x, then y
d2z_dxdy = sp.diff(sp.diff(z, x), y)

print("\nMIXED SECOND-ORDER PARTIAL DERIVATIVES")
print("Differentiate y, then x:", d2z_dydx)
print("Differentiate x, then y:", d2z_dxdy)

# ============================================================
# Step 7: Verify equality of the mixed derivatives
# ============================================================

mixed_derivatives_equal = sp.simplify(
    d2z_dydx - d2z_dxdy
) == 0

print("\nMIXED DERIVATIVE CHECK")
print("Are they equal?", mixed_derivatives_equal)

# ============================================================
# Step 8: Calculate the Hessian matrix
# ============================================================

variables = (x, y)

hessian = sp.hessian(z, variables)

print("\nHESSIAN MATRIX")
sp.pprint(hessian)

# ============================================================
# Step 9: Demonstrate second-order differentiation of a cost
# C(theta) = theta^2
# ============================================================

cost = theta**2

first_derivative = sp.diff(cost, theta)
second_derivative = sp.diff(cost, theta, 2)

print("\nCOST FUNCTION EXAMPLE")
print("Cost:", cost)
print("First derivative:", first_derivative)
print("Second derivative:", second_derivative)

# ============================================================
# Step 10: Final verification
# ============================================================

assert dz_dx == 2*x + 5*y
assert dz_dy == 5*x + 4*y

assert d2z_dx2 == 2
assert d2z_dy2 == 4

assert d2z_dydx == 5
assert d2z_dxdy == 5

assert mixed_derivatives_equal

assert hessian == sp.Matrix([
    [2, 5],
    [5, 4]
])

print("\nAll derivative checks passed.")

import sympy as sp

# ============================================================
# Step 1: Define the symbolic variables and function
# ============================================================

x, y = sp.symbols("x y")

z = x**3 + 2*x*y

print("Original function:")
print("z =", z)

# ============================================================
# Step 2: Calculate first-order partial derivatives
# ============================================================

dz_dx = sp.diff(z, x)
dz_dy = sp.diff(z, y)

print("\nFirst-order partial derivatives:")
print("dz/dx =", dz_dx)
print("dz/dy =", dz_dy)

# ============================================================
# Step 3: Calculate unmixed second-order partial derivatives
# ============================================================

d2z_dx2 = sp.diff(z, x, 2)
d2z_dy2 = sp.diff(z, y, 2)

print("\nUnmixed second-order partial derivatives:")
print("d²z/dx² =", d2z_dx2)
print("d²z/dy² =", d2z_dy2)

# ============================================================
# Step 4: Calculate mixed second-order partial derivatives
# ============================================================

# First differentiate with respect to y, then x
d2z_dydx = sp.diff(sp.diff(z, y), x)

# First differentiate with respect to x, then y
d2z_dxdy = sp.diff(sp.diff(z, x), y)

print("\nMixed second-order partial derivatives:")
print("Differentiate y, then x:", d2z_dydx)
print("Differentiate x, then y:", d2z_dxdy)

# ============================================================
# Step 5: Check that the mixed derivatives are equal
# ============================================================

mixed_equal = sp.simplify(d2z_dydx - d2z_dxdy) == 0

print("\nAre the mixed derivatives equal?", mixed_equal)

# ============================================================
# Step 6: Verify the expected answers
# ============================================================

assert dz_dx == 3*x**2 + 2*y
assert dz_dy == 2*x

assert d2z_dx2 == 6*x
assert d2z_dy2 == 0

assert d2z_dydx == 2
assert d2z_dxdy == 2

assert mixed_equal

print("\nAll derivative checks passed.")

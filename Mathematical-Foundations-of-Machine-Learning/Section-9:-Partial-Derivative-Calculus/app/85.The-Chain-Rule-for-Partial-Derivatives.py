# Multivariate Chain Rule Example

# --------------------------------------------------
# 1. Define the functions
# --------------------------------------------------

def u_function(x, z):
    return x + z


def v_function(x, z):
    return x * z


def y_function(u, v):
    return u**2 + 3 * v


# --------------------------------------------------
# 2. Define the individual partial derivatives
# --------------------------------------------------

# y = u^2 + 3v
def dy_du(u):
    return 2 * u


def dy_dv():
    return 3


# u = x + z
def du_dx():
    return 1


def du_dz():
    return 1


# v = xz
def dv_dx(z):
    return z


def dv_dz(x):
    return x


# --------------------------------------------------
# 3. Input values
# --------------------------------------------------

x = 2
z = 3


# --------------------------------------------------
# 4. Forward pass
# --------------------------------------------------

u = u_function(x, z)
v = v_function(x, z)
y = y_function(u, v)

print("Forward pass")
print("x =", x)
print("z =", z)
print("u =", u)
print("v =", v)
print("y =", y)


# --------------------------------------------------
# 5. Apply the multivariate chain rule
# --------------------------------------------------

# ∂y/∂x
#
# There are two paths:
#
# x → u → y
# x → v → y

partial_y_x = (
    dy_du(u) * du_dx()
    + dy_dv() * dv_dx(z)
)


# ∂y/∂z
#
# There are two paths:
#
# z → u → y
# z → v → y

partial_y_z = (
    dy_du(u) * du_dz()
    + dy_dv() * dv_dz(x)
)


# --------------------------------------------------
# 6. Display results
# --------------------------------------------------

print()
print("Partial derivatives")
print("∂y/∂x =", partial_y_x)
print("∂y/∂z =", partial_y_z)


# --------------------------------------------------
# 7. Show the individual path contributions
# --------------------------------------------------

x_to_u_to_y = dy_du(u) * du_dx()
x_to_v_to_y = dy_dv() * dv_dx(z)

z_to_u_to_y = dy_du(u) * du_dz()
z_to_v_to_y = dy_dv() * dv_dz(x)

print()
print("Path contributions")

print("For ∂y/∂x:")
print("x → u → y =", x_to_u_to_y)
print("x → v → y =", x_to_v_to_y)
print("Total =", x_to_u_to_y + x_to_v_to_y)

print()
print("For ∂y/∂z:")
print("z → u → y =", z_to_u_to_y)
print("z → v → y =", z_to_v_to_y)
print("Total =", z_to_u_to_y + z_to_v_to_y)

# Chain Rule for Multivariate Functions
# Three exercise patterns from the lecture


# ============================================================
# Exercise 1
# ============================================================
#
# y = f(u, v)
# u = g(x)
# v = h(z)
#
# Dependency tree:
#
#        y
#       / \
#      u   v
#      |   |
#      x   z
#
# There is one path from x to y
# and one path from z to y.


# Partial derivative components
dy_du = 2.0
du_dx = 3.0

dy_dv = 4.0
dv_dz = 5.0


# Chain rule
dy_dx_ex1 = dy_du * du_dx
dy_dz_ex1 = dy_dv * dv_dz


print("Exercise 1")
print("∂y/∂x =", dy_dx_ex1)
print("∂y/∂z =", dy_dz_ex1)
print()


# ============================================================
# Exercise 2
# ============================================================
#
# y = f(u, v)
# u = g(x)
# v = h(x, z)
#
# Dependency tree:
#
#          y
#         / \
#        u   v
#        |  / \
#        x x   z
#
# x has TWO paths to y:
#
# x → u → y
# x → v → y
#
# z has ONE path:
#
# z → v → y


# Partial derivative components
dy_du = 2.0
du_dx = 3.0

dy_dv = 4.0
dv_dx = 5.0
dv_dz = 6.0


# ∂y/∂x has two paths
path_x_through_u = dy_du * du_dx
path_x_through_v = dy_dv * dv_dx

dy_dx_ex2 = (
    path_x_through_u
    + path_x_through_v
)


# ∂y/∂z has one path
dy_dz_ex2 = dy_dv * dv_dz


print("Exercise 2")
print("x → u → y =", path_x_through_u)
print("x → v → y =", path_x_through_v)
print("∂y/∂x =", dy_dx_ex2)
print("∂y/∂z =", dy_dz_ex2)
print()


# ============================================================
# Exercise 3
# ============================================================
#
# y = f(u, v, w)
# u = g(x)
# v = h(x)
# w = j(x)
#
# Dependency tree:
#
#             y
#          /  |  \
#         u   v   w
#         |   |   |
#         x   x   x
#
# x has THREE paths to y:
#
# x → u → y
# x → v → y
# x → w → y


# Partial derivative components
dy_du = 2.0
du_dx = 3.0

dy_dv = 4.0
dv_dx = 5.0

dy_dw = 6.0
dw_dx = 7.0


# Calculate each path contribution
path_x_through_u = dy_du * du_dx
path_x_through_v = dy_dv * dv_dx
path_x_through_w = dy_dw * dw_dx


# Add all three paths
dy_dx_ex3 = (
    path_x_through_u
    + path_x_through_v
    + path_x_through_w
)


print("Exercise 3")
print("x → u → y =", path_x_through_u)
print("x → v → y =", path_x_through_v)
print("x → w → y =", path_x_through_w)
print("∂y/∂x =", dy_dx_ex3)


# Because x is the only independent input in Exercise 3:
# ∂y/∂x is also equal to the full derivative dy/dx.
print("dy/dx =", dy_dx_ex3)

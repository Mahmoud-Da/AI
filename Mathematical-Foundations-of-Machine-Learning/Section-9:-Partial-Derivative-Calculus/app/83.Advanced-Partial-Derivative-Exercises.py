import math


# ============================================================
# Exercise 1: z = y^3 + 5xy
# ============================================================

def f1(x, y):
    return y**3 + 5 * x * y


def dz_dx(x, y):
    return 5 * y


def dz_dy(x, y):
    return 3 * y**2 + 5 * x


# Example values
x1 = 2
y1 = 3

print("EXERCISE 1")
print("z =", f1(x1, y1))
print("∂z/∂x =", dz_dx(x1, y1))
print("∂z/∂y =", dz_dy(x1, y1))


# ============================================================
# Exercise 2: A = 2πR² + 2πRH
# ============================================================

def cylinder_surface_area(R, H):
    return 2 * math.pi * R**2 + 2 * math.pi * R * H


def dA_dR(R, H):
    return 4 * math.pi * R + 2 * math.pi * H


def dA_dH(R, H):
    return 2 * math.pi * R


# Example values
R = 3
H = 5

print("\nEXERCISE 2")
print("Surface area =", cylinder_surface_area(R, H))
print("∂A/∂R =", dA_dR(R, H))
print("∂A/∂H =", dA_dH(R, H))


# ============================================================
# Exercise 3: V = x²y - z³
# ============================================================

def solid_volume(x, y, z):
    return x**2 * y - z**3


def dV_dx(x, y, z):
    return 2 * x * y


def dV_dy(x, y, z):
    return x**2


def dV_dz(x, y, z):
    return -3 * z**2


# Example values
x3 = 2
y3 = 3
z3 = 1

print("\nEXERCISE 3")
print("V =", solid_volume(x3, y3, z3))
print("∂V/∂x =", dV_dx(x3, y3, z3))
print("∂V/∂y =", dV_dy(x3, y3, z3))
print("∂V/∂z =", dV_dz(x3, y3, z3))

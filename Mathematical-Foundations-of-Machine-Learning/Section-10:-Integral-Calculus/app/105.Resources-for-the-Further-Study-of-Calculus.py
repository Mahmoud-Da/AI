
import sympy as sp
from scipy.integrate import quad
from sklearn.metrics import auc

# ==========================================
# 1. SYMBOLIC DIFFERENTIATION
# ==========================================

x, y = sp.symbols("x y")

f = x**2 + 3*x*y + y**2

derivative = sp.diff(x**2, x)

print("1. Derivative")
print("Derivative of x^2:", derivative)


# ==========================================
# 2. PARTIAL DERIVATIVES
# ==========================================

df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("\n2. Partial Derivatives")
print("Partial derivative with respect to x:", df_dx)
print("Partial derivative with respect to y:", df_dy)


# ==========================================
# 3. GRADIENT
# ==========================================

gradient = [df_dx, df_dy]

print("\n3. Gradient")
print(gradient)


# ==========================================
# 4. SYMBOLIC INTEGRATION
# ==========================================

integrand = x**2

indefinite_integral = sp.integrate(integrand, x)

print("\n4. Indefinite Integral")
print(indefinite_integral)


# ==========================================
# 5. DEFINITE INTEGRATION
# ==========================================

definite_integral = sp.integrate(x, (x, 1, 2))

print("\n5. Definite Integral")
print("Integral of x from 1 to 2:", definite_integral)


# ==========================================
# 6. NUMERICAL INTEGRATION
# ==========================================

def g(x):
    return x


result, error = quad(g, 1, 2)

print("\n6. Numerical Integration")
print("Integral:", result)
print("Estimated error:", error)


# ==========================================
# 7. ROC AUC
# ==========================================

fpr = [0, 0, 0.5, 0.5, 1]
tpr = [0, 0.5, 0.5, 1, 1]

roc_auc = auc(fpr, tpr)

print("\n7. ROC AUC")
print("Area under ROC curve:", roc_auc)

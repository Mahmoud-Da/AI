import sympy as sp

# ============================================================
# Step 1: Define the symbolic variable and function
# ============================================================

x = sp.symbols("x")
f = x**2

print("STEP 1: Original function")
print("f(x) =", f)


# ============================================================
# Step 2: Calculate the derivative
# ============================================================

derivative = sp.diff(f, x)

print("\nSTEP 2: Differentiation")
print("f'(x) =", derivative)


# ============================================================
# Step 3: Calculate the indefinite integral
# ============================================================

indefinite_integral = sp.integrate(f, x)

print("\nSTEP 3: Indefinite integration")
print("Integral of f(x) =", indefinite_integral, "+ C")


# ============================================================
# Step 4: Calculate the definite integral from 0 to 2
# ============================================================

definite_integral = sp.integrate(f, (x, 0, 2))

print("\nSTEP 4: Definite integration")
print("Integral from 0 to 2 =", definite_integral)
print("Numerical value =", float(definite_integral))


# ============================================================
# Step 5: Define a sample binary-classification confusion matrix
# ============================================================

TP = 80
FP = 20
FN = 10
TN = 90

print("\nSTEP 5: Confusion matrix")
print("True Positives (TP):", TP)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)
print("True Negatives (TN):", TN)


# ============================================================
# Step 6: Calculate the True Positive Rate (TPR)
# ============================================================

positive_total = TP + FN

if positive_total > 0:
    TPR = TP / positive_total
else:
    TPR = None

print("\nSTEP 6: True Positive Rate")
if TPR is not None:
    print("TPR =", TPR)
else:
    print("TPR is undefined because there are no actual positive cases.")


# ============================================================
# Step 7: Calculate the False Positive Rate (FPR)
# ============================================================

negative_total = FP + TN

if negative_total > 0:
    FPR = FP / negative_total
else:
    FPR = None

print("\nSTEP 7: False Positive Rate")
if FPR is not None:
    print("FPR =", FPR)
else:
    print("FPR is undefined because there are no actual negative cases.")


# ============================================================
# Step 8: Display the results
# ============================================================

print("\nSTEP 8: Results summary")
print("Derivative of x^2:", derivative)
print("Indefinite integral of x^2:", indefinite_integral)
print("Definite integral from 0 to 2:", definite_integral)

if TPR is not None:
    print(f"True Positive Rate: {TPR:.2%}")

if FPR is not None:
    print(f"False Positive Rate: {FPR:.2%}")

def derivative_constant():
    return 0


def derivative_power(coefficient, exponent):
    new_coefficient = coefficient * exponent
    new_exponent = exponent - 1
    return new_coefficient, new_exponent


print("Constant Rule")
print("d/dx(25) =", derivative_constant())

coef, power = derivative_power(1, 4)
print(f"d/dx(x^4) = {coef}x^{power}")

coef, power = derivative_power(1, 5)
print(f"d/dx(x^5) = {coef}x^{power}")

coef, power = derivative_power(1, 3)
print(f"d/dx(x^3) = {coef}x^{power}")

coef, power = derivative_power(1, 2)
print(f"d/dx(x^2) = {coef}x^{power}")

coef, power = derivative_power(1, 1)

if power == 0:
    print("d/dx(x) = 1")
else:
    print(f"d/dx(x) = {coef}x^{power}")

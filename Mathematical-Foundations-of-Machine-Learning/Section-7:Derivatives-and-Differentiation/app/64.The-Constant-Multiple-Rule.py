def derivative_constant_multiple(coefficient, exponent):
    """
    Differentiate coefficient * x^exponent
    using the Constant Multiple Rule
    and the Power Rule.
    """
    new_coefficient = coefficient * exponent
    new_exponent = exponent - 1
    return new_coefficient, new_exponent


examples = [
    (2, 4),
    (3, 5),
    (7, 2),
    (10, 1),
    (5, 3)
]

for coefficient, exponent in examples:
    coef, power = derivative_constant_multiple(coefficient, exponent)

    if power == 0:
        print(f"d/dx({coefficient}x^{exponent}) = {coef}")
    elif power == 1:
        print(f"d/dx({coefficient}x^{exponent}) = {coef}x")
    else:
        print(f"d/dx({coefficient}x^{exponent}) = {coef}x^{power}")

def derivative_term(coefficient, exponent):
    """
    Differentiate coefficient * x^exponent
    using the Constant Rule,
    Constant Multiple Rule,
    and Power Rule.
    """

    if exponent == 0:
        return (0, 0)

    return coefficient * exponent, exponent - 1


terms = [
    (2, 4),   # 2x^4
    (5, 2),   # 5x^2
    (7, 0)    # constant
]

print("Derivative:")

for coefficient, exponent in terms:

    new_coefficient, new_exponent = derivative_term(coefficient, exponent)

    if new_coefficient == 0:
        continue

    if new_exponent == 0:
        print(f"{new_coefficient}")
    elif new_exponent == 1:
        print(f"{new_coefficient}x")
    else:
        print(f"{new_coefficient}x^{new_exponent}")

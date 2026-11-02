import math


# --------------------------------------------------
# 1. Factorial
# --------------------------------------------------

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers")

    return math.factorial(n)


# --------------------------------------------------
# 2. Combinations
# --------------------------------------------------

def combinations(n, k):
    """
    Calculate the number of ways to select k items
    from n items, where order does not matter.
    """

    if n < 0 or k < 0 or k > n:
        raise ValueError("Require n >= 0 and 0 <= k <= n")

    return math.comb(n, k)


# --------------------------------------------------
# 3. Total outcomes of coin flips
# --------------------------------------------------

def total_coin_flip_outcomes(n):
    """
    Calculate the total number of possible sequences
    for n coin flips.
    """

    if n < 0:
        raise ValueError("Number of flips cannot be negative")

    return 2 ** n


# --------------------------------------------------
# 4. Probability of exactly k heads
# --------------------------------------------------

def coin_flip_probability(n, k):
    """
    Calculate the probability of getting exactly k heads
    in n independent flips of a fair coin.
    """

    if n < 0 or k < 0 or k > n:
        raise ValueError("Require n >= 0 and 0 <= k <= n")

    favorable_outcomes = combinations(n, k)
    total_outcomes = total_coin_flip_outcomes(n)

    probability = favorable_outcomes / total_outcomes

    return probability


# --------------------------------------------------
# 5. Examples
# --------------------------------------------------

if __name__ == "__main__":

    # Factorial examples
    print("Factorial examples:")
    print("4! =", factorial(4))
    print("5! =", factorial(5))

    print()

    # Combination example
    print("Combination example:")
    print("3 choose 2 =", combinations(3, 2))

    print()

    # Total coin flip outcomes
    print("Total coin flip outcomes:")
    print("3 flips =", total_coin_flip_outcomes(3))
    print("5 flips =", total_coin_flip_outcomes(5))

    print()

    # Probability examples
    print("Coin flip probabilities:")

    examples = [
        (3, 2),
        (5, 3),
        (5, 5),
        (3, 0)
    ]

    for n, k in examples:
        probability = coin_flip_probability(n, k)

        print(
            f"{n} flips, exactly {k} heads: "
            f"{probability:.5f} "
            f"({probability * 100:.2f}%)"
        )

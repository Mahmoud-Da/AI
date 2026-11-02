import math


# ==================================================
# 1. Exercise 1: Ace of Spades Twice
# ==================================================

def ace_of_spades_twice():
    """
    Probability of drawing the Ace of Spades twice
    with replacement.
    """

    probability = (1 / 52) * (1 / 52)

    return probability


# ==================================================
# 2. Exercise 2: Drawing the Same Card Twice
# ==================================================

def same_card_twice():
    """
    Probability of drawing any card first,
    replacing it, and drawing the same card again.
    """

    first_draw = 1
    second_draw = 1 / 52

    return first_draw * second_draw


# ==================================================
# 3. Exercise 3: Combinations
# ==================================================

def combinations(n, k):
    """
    Calculate n choose k using factorials.
    """

    if n < 0 or k < 0 or k > n:
        raise ValueError("Require n >= 0 and 0 <= k <= n")

    return math.factorial(n) // (
        math.factorial(k) * math.factorial(n - k)
    )


# ==================================================
# 4. Exercise 4: Coin Flip Probability
# ==================================================

def coin_flip_prob(n, k):
    """
    Calculate the probability of getting exactly
    k heads in n independent flips of a fair coin.
    """

    if n < 0 or k < 0 or k > n:
        raise ValueError("Require n >= 0 and 0 <= k <= n")

    favorable_outcomes = combinations(n, k)
    total_outcomes = 2 ** n

    probability = favorable_outcomes / total_outcomes

    return probability


# ==================================================
# 5. Run All Exercises
# ==================================================

if __name__ == "__main__":

    # Exercise 1
    print("Exercise 1: Ace of Spades Twice")

    probability = ace_of_spades_twice()

    print(f"Probability: {probability:.8f}")
    print(f"Percentage: {probability * 100:.5f}%")

    print()

    # Exercise 2
    print("Exercise 2: Drawing the Same Card Twice")

    probability = same_card_twice()

    print(f"Probability: {probability:.8f}")
    print(f"Percentage: {probability * 100:.5f}%")

    print()

    # Exercise 3
    print("Exercise 3: Three Heads in Five Flips")

    n = 5
    k = 3

    favorable_outcomes = combinations(n, k)
    total_outcomes = 2 ** n
    probability = coin_flip_prob(n, k)

    print("Favorable outcomes:", favorable_outcomes)
    print("Total outcomes:", total_outcomes)
    print(f"Probability: {probability:.5f}")
    print(f"Percentage: {probability * 100:.2f}%")

    print()

    # Exercise 4
    print("Exercise 4: Probabilities for 0 to 5 Heads")

    n = 5

    total_probability = 0

    for k in range(n + 1):

        probability = coin_flip_prob(n, k)

        total_probability += probability

        print(
            f"{k} heads: "
            f"{probability:.5f} "
            f"({probability * 100:.2f}%)"
        )

    print()

    # Verify probability sum
    print("Probability verification:")
    print(f"Total probability: {total_probability:.5f}")

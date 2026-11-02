# ============================================================
# Machine Learning Foundations
# Probability and Information Theory
# Topic: Multiple Independent Observations
# ============================================================


# ------------------------------------------------------------
# 1. Two Independent Coin Flips
# ------------------------------------------------------------

print("\n1. Two Independent Coin Flips")

sample_space_two = [
    "HH",
    "HT",
    "TH",
    "TT"
]

event_two_heads = ["HH"]

probability_two_heads = (
    len(event_two_heads) / len(sample_space_two)
)

print("Sample space:", sample_space_two)
print("Probability of HH:", probability_two_heads)


# ------------------------------------------------------------
# 2. Three Independent Coin Flips
# ------------------------------------------------------------

print("\n2. Three Independent Coin Flips")

sample_space_three = [
    "HHH", "HHT", "HTH", "HTT",
    "THH", "THT", "TTH", "TTT"
]

event_three_heads = ["HHH"]

probability_three_heads = (
    len(event_three_heads) / len(sample_space_three)
)

print("Sample space:", sample_space_three)
print("Probability of HHH:", probability_three_heads)


# ------------------------------------------------------------
# 3. Exactly Two Heads in Three Flips
# ------------------------------------------------------------

print("\n3. Exactly Two Heads")

event_exactly_two = [
    outcome for outcome in sample_space_three
    if outcome.count("H") == 2
]

probability_exactly_two = (
    len(event_exactly_two) / len(sample_space_three)
)

print("Favorable outcomes:", event_exactly_two)
print("Probability:", probability_exactly_two)


# ------------------------------------------------------------
# 4. At Least Two Heads in Three Flips
# ------------------------------------------------------------

print("\n4. At Least Two Heads")

event_at_least_two = [
    outcome for outcome in sample_space_three
    if outcome.count("H") >= 2
]

probability_at_least_two = (
    len(event_at_least_two) / len(sample_space_three)
)

print("Favorable outcomes:", event_at_least_two)
print("Probability:", probability_at_least_two)


# ------------------------------------------------------------
# 5. Multiplication Rule
# ------------------------------------------------------------

print("\n5. Multiplication Rule")

p_heads = 0.5

p_two_heads = p_heads * p_heads
p_three_heads = p_two_heads * p_heads

p_five_heads = p_two_heads * p_three_heads

print("Probability of two heads:", p_two_heads)
print("Probability of three heads:", p_three_heads)
print("Probability of five heads:", p_five_heads)
print("Percentage:", p_five_heads * 100, "%")


# ------------------------------------------------------------
# 6. General Formula for Consecutive Heads
# ------------------------------------------------------------

print("\n6. Probability of Consecutive Heads")

for n in range(1, 11):
    probability = (0.5) ** n

    print(
        f"{n} flips: "
        f"{probability:.8f} "
        f"({probability * 100:.6f}%)"
    )


# ------------------------------------------------------------
# 7. Final Results
# ------------------------------------------------------------

print("\n7. Final Results")

print("Two consecutive heads:", probability_two_heads)
print("Three consecutive heads:", probability_three_heads)
print("Exactly two heads:", probability_exactly_two)
print("At least two heads:", probability_at_least_two)
print("Five consecutive heads:", p_five_heads)

print("\nAll examples completed.")

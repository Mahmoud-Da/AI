# ============================================================
# Machine Learning Foundations
# Probability and Information Theory
# Topic: Events and Sample Spaces
# ============================================================


# ------------------------------------------------------------
# 1. Sample Space: Fair Coin
# ------------------------------------------------------------

sample_space = {"H", "T"}

print("1. Coin Sample Space")
print("Sample space:", sample_space)
print("Number of outcomes:", len(sample_space))


# ------------------------------------------------------------
# 2. Events: Heads and Tails
# ------------------------------------------------------------

event_heads = {"H"}
event_tails = {"T"}

probability_heads = len(event_heads) / len(sample_space)
probability_tails = len(event_tails) / len(sample_space)

print("\n2. Coin Probabilities")
print("Probability of heads:", probability_heads)
print("Probability of tails:", probability_tails)


# ------------------------------------------------------------
# 3. Card Probability: Ace of Spades
# ------------------------------------------------------------

total_cards = 52

ace_of_spades = 1

probability_ace_of_spades = ace_of_spades / total_cards

print("\n3. Ace of Spades")
print("Probability:", probability_ace_of_spades)
print("Percentage:", probability_ace_of_spades * 100, "%")


# ------------------------------------------------------------
# 4. Card Probability: Any Ace
# ------------------------------------------------------------

number_of_aces = 4

probability_aces = number_of_aces / total_cards

print("\n4. Any Ace")
print("Probability:", probability_aces)
print("Percentage:", probability_aces * 100, "%")


# ------------------------------------------------------------
# 5. Card Probability: Spade
# ------------------------------------------------------------

number_of_spades = 13

probability_spades = number_of_spades / total_cards

print("\n5. Spade")
print("Probability:", probability_spades)
print("Percentage:", probability_spades * 100, "%")


# ------------------------------------------------------------
# 6. Card Probability: Ace OR Spade
# ------------------------------------------------------------

overlap = 1  # Ace of Spades

favorable_outcomes = (
    number_of_aces
    + number_of_spades
    - overlap
)

probability_ace_or_spade = favorable_outcomes / total_cards

print("\n6. Ace or Spade")
print("Favorable outcomes:", favorable_outcomes)
print("Probability:", probability_ace_or_spade)
print("Percentage:", probability_ace_or_spade * 100, "%")


# ------------------------------------------------------------
# 7. Certain Event
# ------------------------------------------------------------

any_card = 52

probability_certain = any_card / total_cards

print("\n7. Certain Event")
print("Probability:", probability_certain)


# ------------------------------------------------------------
# 8. Impossible Event
# ------------------------------------------------------------

turnip = 0

probability_impossible = turnip / total_cards

print("\n8. Impossible Event")
print("Probability:", probability_impossible)


# ------------------------------------------------------------
# 9. Summary
# ------------------------------------------------------------

print("\n9. Summary")

print("Heads:", probability_heads)
print("Tails:", probability_tails)
print("Ace of Spades:", probability_ace_of_spades)
print("Any Ace:", probability_aces)
print("Spade:", probability_spades)
print("Ace or Spade:", probability_ace_or_spade)
print("Certain Event:", probability_certain)
print("Impossible Event:", probability_impossible)

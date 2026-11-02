import numpy as np


# ============================================================
# 1. Classical Probability: Rolling a Fair Die
# ============================================================

print("1. Classical Probability")

outcomes = [1, 2, 3, 4, 5, 6]

total_outcomes = len(outcomes)
favorable_outcomes = outcomes.count(4)

probability = favorable_outcomes / total_outcomes

print("Possible outcomes:", outcomes)
print("Probability of rolling a 4:", probability)


# ============================================================
# 2. Discrete Random Variables
# ============================================================

print("\n2. Discrete Random Variables")

# Possible number of heads in three coin tosses
discrete_outcomes = np.array([0, 1, 2, 3])

print("Discrete outcomes:", discrete_outcomes)


# ============================================================
# 3. Continuous Random Variables
# ============================================================

print("\n3. Continuous Random Variables")

# Example continuous measurements
temperatures = np.array([
    20.5,
    21.2,
    19.8,
    22.1,
    20.9
])

print("Temperature measurements:", temperatures)
print("Average temperature:", np.mean(temperatures))


# ============================================================
# 4. Comparison
# ============================================================

print("\n4. Comparison")

print("Discrete values:", discrete_outcomes)
print("Continuous measurements:", temperatures)

print("\nLecture examples completed.")

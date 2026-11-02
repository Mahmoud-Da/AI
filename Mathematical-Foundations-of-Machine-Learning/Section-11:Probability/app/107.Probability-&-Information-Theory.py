
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm


# ==========================================
# 1. BASIC PROBABILITY
# ==========================================

p_heads = 0.5
p_tails = 0.5

print("1. Basic Probability")
print("Heads:", p_heads)
print("Tails:", p_tails)
print("Total probability:", p_heads + p_tails)


# ==========================================
# 2. RANDOM VARIABLES
# ==========================================

# Discrete random variable: dice roll
dice_result = random.randint(1, 6)

# Continuous random variable
continuous_value = random.uniform(0, 1)

print("\n2. Random Variables")
print("Dice result:", dice_result)
print("Continuous value:", continuous_value)


# ==========================================
# 3. PROBABILITY MASS FUNCTION (PMF)
# ==========================================

values = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6

print("\n3. Probability Mass Function")

for value, probability in zip(values, probabilities):
    print(f"P(X = {value}) = {probability:.4f}")


# ==========================================
# 4. PROBABILITY DENSITY FUNCTION (PDF)
# ==========================================

x = np.linspace(-4, 4, 500)
pdf = norm.pdf(x, loc=0, scale=1)

plt.figure()
plt.plot(x, pdf)
plt.title("Standard Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.show()


# ==========================================
# 5. EXPECTED VALUE
# ==========================================

expected_value = sum(
    value * probability
    for value, probability in zip(values, probabilities)
)

print("\n5. Expected Value")
print("Expected dice result:", expected_value)


# ==========================================
# 6. CENTRAL TENDENCY
# ==========================================

data = [2, 3, 3, 4, 5, 6, 7]

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=False).mode

print("\n6. Measures of Central Tendency")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)


# ==========================================
# 7. QUANTILES
# ==========================================

quartiles = np.percentile(data, [25, 50, 75])

print("\n7. Quartiles")
print("Q1:", quartiles[0])
print("Q2:", quartiles[1])
print("Q3:", quartiles[2])


# ==========================================
# 8. BOX-AND-WHISKER PLOT
# ==========================================

plt.figure()
plt.boxplot(data)
plt.title("Box-and-Whisker Plot")
plt.ylabel("Values")
plt.show()


# ==========================================
# 9. DISPERSION
# ==========================================

sample_data = [10, 12, 14, 16, 18, 20]

variance = np.var(sample_data, ddof=1)
standard_deviation = np.std(sample_data, ddof=1)
standard_error = standard_deviation / np.sqrt(len(sample_data))

print("\n9. Measures of Dispersion")
print("Sample variance:", variance)
print("Sample standard deviation:", standard_deviation)
print("Standard error:", standard_error)


# ==========================================
# 10. CORRELATION AND COVARIANCE
# ==========================================

x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

covariance = np.cov(x_data, y_data, ddof=1)[0, 1]
correlation = np.corrcoef(x_data, y_data)[0, 1]

print("\n10. Relationship Between Variables")
print("Covariance:", covariance)
print("Correlation:", correlation)

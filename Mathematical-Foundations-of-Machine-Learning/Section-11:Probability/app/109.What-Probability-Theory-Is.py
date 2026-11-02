import numpy as np
import matplotlib.pyplot as plt

# Generate a non-normal population
population = np.random.exponential(
    scale=2,
    size=100000
)

# Take repeated samples and calculate their means
sample_means = []

for _ in range(1000):
    sample = np.random.choice(
        population,
        size=50
    )

    sample_means.append(np.mean(sample))

# Plot the distribution of sample means
plt.hist(sample_means, bins=30, edgecolor="black")

plt.title("Central Limit Theorem")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.show()

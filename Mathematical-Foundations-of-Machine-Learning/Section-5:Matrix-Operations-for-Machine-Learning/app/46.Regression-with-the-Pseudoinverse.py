import numpy as np
import matplotlib.pyplot as plt

# Drug dosage feature
x1 = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# Forgetfulness scores
y = np.array([
    1.86,
    1.31,
    0.62,
    0.57,
    0.27,
    0.12,
    -0.40,
    -0.32
])

# Scatter plot
plt.scatter(x1, y)
plt.title("Clinical Trial")
plt.xlabel("Drug Dosage")
plt.ylabel("Forgetfulness")
plt.show()

# Intercept column
x0 = np.ones(len(x1))

# Feature matrix
X = np.column_stack((x0, x1))

# Solve for weights
w = np.linalg.pinv(X) @ y

print("Weights:")
print(w)

# Extract intercept and slope
b = w[0]
m = w[1]

print("Intercept:", b)
print("Slope:", m)

# Create regression line
xmin = np.min(x1)
xmax = np.max(x1)

ymin = m * xmin + b
ymax = m * xmax + b

# Plot data and fitted line
plt.scatter(x1, y)

plt.plot(
    [xmin, xmax],
    [ymin, ymax]
)

plt.title("Clinical Trial")
plt.xlabel("Drug Dosage")
plt.ylabel("Forgetfulness")

plt.show()

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("Original Shape:")
print(X.shape)

print("\nFirst 6 Rows:")
print(X[:6])

# -----------------------------
# PCA
# -----------------------------

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

print("\nCompressed Shape:")
print(X_pca.shape)

print("\nFirst 6 PCA Rows:")
print(X_pca[:6])

# -----------------------------
# PCA Plot Without Labels
# -----------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1]
)

plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()

# -----------------------------
# PCA Plot With Labels
# -----------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y
)

plt.title("PCA with Iris Species")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.show()

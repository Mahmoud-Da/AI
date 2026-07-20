from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = Image.open("oboe-with-book.jpg")

# Convert to grayscale
img_gray = img.convert("LA")

# Convert to matrix
X = np.array(img_gray)[:, :, 0]

# Compute SVD
U, s, VT = np.linalg.svd(X)

# Reconstruction function


def reconstruct(U, s, VT, k):
    return U[:, :k] @ np.diag(s[:k]) @ VT[:k, :]


# Show compressed versions
for k in [2, 4, 8, 16, 32, 64]:
    recon = reconstruct(U, s, VT, k)

    plt.figure(figsize=(5, 5))
    plt.imshow(recon, cmap="gray")
    plt.title(f"{k} Singular Values")
    plt.axis("off")
    plt.show()

# Compression statistics
rows, cols = X.shape

original_elements = rows * cols

k = 64

compressed_elements = (
    rows * k +
    k +
    cols * k
)

compression_ratio = (
    compressed_elements /
    original_elements
)

print("Original elements:", original_elements)
print("Compressed elements:", compressed_elements)
print("Percentage retained:", compression_ratio * 100)
print("Compression achieved:", (1 - compression_ratio) * 100)

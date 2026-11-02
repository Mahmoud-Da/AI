
import numpy as np
import matplotlib.pyplot as plt

# Illustrative ROC coordinates
fpr = np.array([0.0, 0.1, 0.3, 0.6, 1.0])
tpr = np.array([0.0, 0.6, 0.8, 0.9, 1.0])

# Calculate AUC without scikit-learn or SciPy
roc_auc = np.trapezoid(tpr, fpr)

print(f"ROC AUC: {roc_auc:.3f}")

# Plot the ROC curve
plt.figure(figsize=(7, 5))

plt.plot(
    fpr,
    tpr,
    marker="o",
    label=f"ROC curve (AUC = {roc_auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random classifier"
)

plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.title("Illustrative ROC Curve")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

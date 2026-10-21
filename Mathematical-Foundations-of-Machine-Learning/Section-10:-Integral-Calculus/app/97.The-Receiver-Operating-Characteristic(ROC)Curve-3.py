
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# 1. ROC CURVE DATA
# Each curve has:
# x-axis = False Positive Rate (FPR)
# y-axis = True Positive Rate (TPR)
# =========================================================

fpr = np.array([0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0])

models = {
    "Excellent": {
        "tpr": [0.0, 0.75, 0.90, 0.96, 0.98, 0.99, 1.0]
    },
    "Very Good": {
        "tpr": [0.0, 0.55, 0.75, 0.88, 0.94, 0.98, 1.0]
    },
    "Good": {
        "tpr": [0.0, 0.35, 0.60, 0.75, 0.85, 0.93, 1.0]
    },
    "Fair": {
        "tpr": [0.0, 0.20, 0.40, 0.60, 0.75, 0.88, 1.0]
    },
    "Poor / Random-like": {
        "tpr": [0.0, 0.10, 0.20, 0.40, 0.60, 0.80, 1.0]
    }
}

# =========================================================
# 2. CALCULATE AUC FOR EVERY MODEL
# =========================================================

print("=" * 45)
print("ROC AUC COMPARISON")
print("=" * 45)

for name, model in models.items():
    tpr = np.array(model["tpr"])

    # Area under the ROC curve
    auc = np.trapezoid(tpr, fpr)

    model["auc"] = auc

    print(f"{name:20s} AUC = {auc:.3f}")

# =========================================================
# 3. DRAW ALL FIVE ROC CURVES
# =========================================================

plt.figure(figsize=(10, 7))

for name, model in models.items():
    tpr = np.array(model["tpr"])
    auc = model["auc"]

    plt.plot(
        fpr,
        tpr,
        marker="o",
        linewidth=2,
        label=f"{name} (AUC = {auc:.3f})"
    )

# Random classifier baseline
plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    linewidth=2,
    label="Random classifier (AUC = 0.500)"
)

# =========================================================
# 4. GRAPH SETTINGS
# =========================================================

plt.xlabel("False Positive Rate (FPR)", fontsize=12)
plt.ylabel("True Positive Rate (TPR)", fontsize=12)

plt.title(
    "ROC Curve Comparison: Five Classifier Performance Levels",
    fontsize=14
)

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.xticks(np.arange(0, 1.01, 0.1))
plt.yticks(np.arange(0, 1.01, 0.1))

plt.grid(True, alpha=0.3)
plt.legend(loc="lower right")
plt.tight_layout()

plt.show()

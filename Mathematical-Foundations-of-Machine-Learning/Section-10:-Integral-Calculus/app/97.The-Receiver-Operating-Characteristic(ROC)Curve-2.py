
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. DATA
# ============================================================

y_actual = [0, 1, 0, 1]
y_score = [0.3, 0.5, 0.6, 0.9]

# Five cases: two endpoints and three example thresholds
thresholds = [float("inf"), 0.6, 0.5, 0.3, float("-inf")]

case_names = [
    "Case 1: Threshold = +infinity",
    "Case 2: Threshold = 0.6",
    "Case 3: Threshold = 0.5",
    "Case 4: Threshold = 0.3",
    "Case 5: Threshold = -infinity"
]

roc_points = []

# ============================================================
# 2. PROCESS EACH CASE
# ============================================================

for case_name, threshold in zip(case_names, thresholds):

    # Strict rule: score > threshold means positive
    y_predicted = [
        1 if score > threshold else 0
        for score in y_score
    ]

    TP = sum(
        actual == 1 and pred == 1
        for actual, pred in zip(y_actual, y_predicted)
    )
    TN = sum(
        actual == 0 and pred == 0
        for actual, pred in zip(y_actual, y_predicted)
    )
    FP = sum(
        actual == 0 and pred == 1
        for actual, pred in zip(y_actual, y_predicted)
    )
    FN = sum(
        actual == 1 and pred == 0
        for actual, pred in zip(y_actual, y_predicted)
    )

    TPR = TP / (TP + FN) if TP + FN else 0
    FPR = FP / (FP + TN) if FP + TN else 0

    roc_points.append((FPR, TPR))

    # --------------------------------------------------------
    # 3. DISPLAY EACH CASE
    # --------------------------------------------------------

    print("\n" + "=" * 65)
    print(case_name)
    print("=" * 65)

    results = pd.DataFrame({
        "Image": range(1, len(y_actual) + 1),
        "Actual": y_actual,
        "Score": y_score,
        "Predicted": y_predicted
    })

    print("\nPredictions:")
    print(results.to_string(index=False))

    confusion_matrix = pd.DataFrame(
        [[TN, FP], [FN, TP]],
        index=["Actual 0", "Actual 1"],
        columns=["Predicted 0", "Predicted 1"]
    )

    print("\nConfusion matrix:")
    print(confusion_matrix)

    print(f"\nTP = {TP}")
    print(f"TN = {TN}")
    print(f"FP = {FP}")
    print(f"FN = {FN}")

    print(f"\nTPR = TP / (TP + FN) = {TPR:.2f}")
    print(f"FPR = FP / (FP + TN) = {FPR:.2f}")
    print(f"ROC point = ({FPR:.2f}, {TPR:.2f})")


# ============================================================
# 4. SUMMARY TABLE
# ============================================================

summary = pd.DataFrame({
    "Case": case_names,
    "Threshold": thresholds,
    "FPR": [point[0] for point in roc_points],
    "TPR": [point[1] for point in roc_points]
})

print("\n\n" + "=" * 65)
print("SUMMARY OF ALL FIVE CASES")
print("=" * 65)
print(summary.to_string(index=False))


# ============================================================
# 5. ROC CURVE
# ============================================================

# Sort points by FPR, then TPR, for plotting
plot_points = sorted(set(roc_points))

# Include standard ROC endpoints
plot_points = sorted(
    set(plot_points + [(0.0, 0.0), (1.0, 1.0)])
)

fpr_values = [point[0] for point in plot_points]
tpr_values = [point[1] for point in plot_points]

# Calculate trapezoidal AUC
auc = 0.0

for i in range(1, len(plot_points)):
    x1, y1 = plot_points[i - 1]
    x2, y2 = plot_points[i]

    width = x2 - x1
    average_height = (y1 + y2) / 2

    auc += width * average_height

plt.figure(figsize=(8, 6))

plt.plot(
    fpr_values,
    tpr_values,
    marker="o",
    linewidth=2,
    label=f"ROC curve (AUC = {auc:.2f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random classifier"
)

for x, y in plot_points:
    plt.annotate(
        f"({x:.1f}, {y:.1f})",
        (x, y),
        xytext=(6, 6),
        textcoords="offset points"
    )

plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.title("ROC Curve: Hot Dog Classifier")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\nROC AUC = {auc:.2f}")

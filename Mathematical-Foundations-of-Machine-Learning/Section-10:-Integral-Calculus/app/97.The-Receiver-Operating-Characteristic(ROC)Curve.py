# ============================================================
# Machine Learning Foundations
# Topic: ROC Curve and ROC AUC
# ============================================================

# Step 1: Define actual labels and model scores
# 1 = hot dog, 0 = not a hot dog

y_actual = [0, 1, 0, 1]
y_score = [0.3, 0.5, 0.6, 0.9]

# Use the lecture's convention:
# score > threshold predicts positive.
thresholds = [0.3, 0.5, 0.6]


# Step 2: Define a function to calculate the confusion matrix

def confusion_counts(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("Actual and predicted lengths must match.")

    TP = sum(
        a == 1 and p == 1
        for a, p in zip(actual, predicted)
    )
    TN = sum(
        a == 0 and p == 0
        for a, p in zip(actual, predicted)
    )
    FP = sum(
        a == 0 and p == 1
        for a, p in zip(actual, predicted)
    )
    FN = sum(
        a == 1 and p == 0
        for a, p in zip(actual, predicted)
    )

    return TP, FN, FP, TN


# Step 3: Evaluate the model at each threshold

roc_points = []

print("CONFUSION MATRIX AND ROC RATES")
print("--------------------------------")

for threshold in thresholds:
    predicted = [
        1 if score > threshold else 0
        for score in y_score
    ]

    TP, FN, FP, TN = confusion_counts(
        y_actual,
        predicted
    )

    # TPR and FPR require both actual classes to be present.
    positive_total = TP + FN
    negative_total = FP + TN

    if positive_total == 0 or negative_total == 0:
        raise ValueError(
            "TPR and FPR require positive and negative examples."
        )

    TPR = TP / positive_total
    FPR = FP / negative_total

    roc_points.append((FPR, TPR))

    print(f"\nThreshold: {threshold}")
    print(f"Predictions: {predicted}")
    print(f"TP={TP}, FN={FN}, FP={FP}, TN={TN}")
    print(f"TPR={TPR:.2f}, FPR={FPR:.2f}")


# Step 4: Add the ROC endpoints and sort points
# Remove duplicate coordinates so vertical or horizontal
# segments are not counted more than once.

roc_points.extend([
    (0.0, 0.0),
    (1.0, 1.0),
])

roc_points = sorted(set(roc_points), key=lambda point: point[0])

# If multiple points have the same FPR, sort by TPR.
roc_points.sort(key=lambda point: (point[0], point[1]))

print("\nROC POINTS")
print("----------")

for FPR, TPR in roc_points:
    print(f"(FPR={FPR:.2f}, TPR={TPR:.2f})")


# Step 5: Calculate AUC using the trapezoidal rule

auc = 0.0

for i in range(1, len(roc_points)):
    x1, y1 = roc_points[i - 1]
    x2, y2 = roc_points[i]

    width = x2 - x1
    average_height = (y1 + y2) / 2

    auc += width * average_height


# Step 6: Display the final result

print("\nFINAL RESULT")
print("------------")
print(f"ROC AUC = {auc:.2f}")

if auc == 0.5:
    print("The model has chance-level ranking performance.")
elif auc > 0.5:
    print("The model ranks positive examples better than chance.")
else:
    print("The model ranks positive examples worse than chance.")

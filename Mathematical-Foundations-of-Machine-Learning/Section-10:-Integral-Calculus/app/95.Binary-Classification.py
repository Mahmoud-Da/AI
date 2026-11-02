# ============================================================
# Machine Learning Foundations
# Topic: Binary Classification and ROC AUC
# ============================================================


# ============================================================
# Step 1: Supervised learning and regression
# ============================================================

def predict_forgetfulness(dosage):
    """
    Simplified illustrative regression function.
    This is not a trained medical model.
    """
    return 20.0 - 2.0 * dosage


drug_dosage = 5.0
forgetfulness_prediction = predict_forgetfulness(drug_dosage)

print("STEP 1: Regression")
print("Drug dosage:", drug_dosage)
print("Predicted forgetfulness:", forgetfulness_prediction)


# ============================================================
# Step 2: Multiclass classification
# ============================================================

digit_names = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

predicted_digit = 7

print("\nSTEP 2: Multiclass classification")
print("Predicted digit:", digit_names[predicted_digit])


# ============================================================
# Step 3: Binary classification with a threshold
# ============================================================

threshold = 0.5

# Illustrative model scores for the positive class
scores = [0.05, 0.30, 0.49, 0.51, 0.90, 0.99]

print("\nSTEP 3: Threshold-based classification")

for score in scores:
    predicted_class = 1 if score >= threshold else 0

    class_name = (
        "hot dog"
        if predicted_class == 1
        else "not a hot dog"
    )

    print(
        f"Score: {score:.2f} -> "
        f"Predicted class: {class_name}"
    )


# ============================================================
# Step 4: Demonstrate the limitations of a single threshold
# ============================================================

model_a = [0.45, 0.52, 0.48, 0.55, 0.40]
model_b = [0.05, 0.95, 0.10, 0.90, 0.02]


def classify(scores, threshold=0.5):
    """Convert model scores into binary class predictions."""
    return [
        1 if score >= threshold else 0
        for score in scores
    ]


print("\nSTEP 4: Comparing two models")

print("Model A scores:", model_a)
print("Model A predictions:", classify(model_a, threshold))

print("Model B scores:", model_b)
print("Model B predictions:", classify(model_b, threshold))

print(
    "Note: Different scores can produce identical "
    "class predictions at the same threshold."
)


# ============================================================
# Step 5: Calculate TPR and FPR from a confusion matrix
# ============================================================

TP = 80
FN = 20
FP = 10
TN = 90

print("\nSTEP 5: Confusion matrix")
print("True Positives:", TP)
print("False Negatives:", FN)
print("False Positives:", FP)
print("True Negatives:", TN)

positive_total = TP + FN
negative_total = FP + TN

if positive_total > 0:
    TPR = TP / positive_total
else:
    TPR = None

if negative_total > 0:
    FPR = FP / negative_total
else:
    FPR = None

print("\nTrue Positive Rate (TPR):", TPR)
print("False Positive Rate (FPR):", FPR)


# ============================================================
# Step 6: Calculate ROC points at multiple thresholds
# ============================================================

# Example actual labels:
# 1 = positive class
# 0 = negative class

actual_labels = [
    1, 1, 1, 1, 0, 0, 0, 0
]

# Example model scores for the positive class
model_scores = [
    0.95, 0.85, 0.70, 0.40,
    0.80, 0.60, 0.30, 0.10
]


def calculate_roc_points(labels, scores):
    """
    Calculate ROC points by testing thresholds from high
    to low. The input scores are assumed to represent
    the positive class.
    """
    if len(labels) != len(scores):
        raise ValueError(
            "Labels and scores must have the same length."
        )

    if not labels:
        raise ValueError("The dataset must not be empty.")

    if any(label not in (0, 1) for label in labels):
        raise ValueError("Labels must be 0 or 1.")

    if any(not 0 <= score <= 1 for score in scores):
        raise ValueError("Scores must be between 0 and 1.")

    total_positive = sum(labels)
    total_negative = len(labels) - total_positive

    if total_positive == 0 or total_negative == 0:
        raise ValueError(
            "ROC calculation requires both positive "
            "and negative examples."
        )

    # Include thresholds that produce the all-negative
    # and all-positive predictions.
    thresholds = (
        [float("inf")]
        + sorted(set(scores), reverse=True)
        + [float("-inf")]
    )

    roc_points = []

    for threshold_value in thresholds:
        predictions = [
            1 if score >= threshold_value else 0
            for score in scores
        ]

        TP_count = sum(
            actual == 1 and predicted == 1
            for actual, predicted in zip(labels, predictions)
        )

        FN_count = sum(
            actual == 1 and predicted == 0
            for actual, predicted in zip(labels, predictions)
        )

        FP_count = sum(
            actual == 0 and predicted == 1
            for actual, predicted in zip(labels, predictions)
        )

        TN_count = sum(
            actual == 0 and predicted == 0
            for actual, predicted in zip(labels, predictions)
        )

        TPR_value = TP_count / (TP_count + FN_count)
        FPR_value = FP_count / (FP_count + TN_count)

        roc_points.append(
            (FPR_value, TPR_value, threshold_value)
        )

    return roc_points


roc_points = calculate_roc_points(
    actual_labels,
    model_scores
)

print("\nSTEP 6: ROC points")

for fpr, tpr, threshold_value in roc_points:
    print(
        f"Threshold: {threshold_value:>5}, "
        f"FPR: {fpr:.2f}, "
        f"TPR: {tpr:.2f}"
    )


# ============================================================
# Step 7: Calculate ROC AUC using the trapezoidal rule
# ============================================================

def calculate_auc(roc_points):
    """
    Calculate the area under the ROC curve using
    the trapezoidal rule.

    Each ROC point has the form:
        (false_positive_rate, true_positive_rate, threshold)
    """
    # Sort points from lowest to highest FPR.
    points = sorted(
        (fpr, tpr) for fpr, tpr, _ in roc_points
    )

    area = 0.0

    for i in range(1, len(points)):
        previous_fpr, previous_tpr = points[i - 1]
        current_fpr, current_tpr = points[i]

        width = current_fpr - previous_fpr
        average_height = (
            previous_tpr + current_tpr
        ) / 2.0

        area += width * average_height

    return area


auc = calculate_auc(roc_points)

print("\nSTEP 7: ROC AUC")
print(f"Area Under the ROC Curve: {auc:.4f}")


# ============================================================
# Step 8: Interpret the result
# ============================================================

print("\nSTEP 8: Interpretation")

if auc > 0.5:
    print(
        "The model demonstrates better-than-random "
        "ranking on this example dataset."
    )
elif auc == 0.5:
    print(
        "The model's ranking performance is equivalent "
        "to random ranking on this example dataset."
    )
else:
    print(
        "The model's ranking is worse than random "
        "on this example dataset."
    )

print(
    "\nReminder: This is a small illustrative dataset. "
    "Real model evaluation requires representative data "
    "and additional appropriate metrics."
)

# ============================================================
# Machine Learning Foundations
# Topic: The Confusion Matrix
# ============================================================


# Step 1: Define actual labels and model predictions
# 1 = hot dog
# 0 = not a hot dog

y_actual = [1, 0, 1, 1, 0, 0, 1, 0]
y_predicted = [1, 0, 0, 1, 1, 0, 1, 0]


# Step 2: Validate the input data

if len(y_actual) != len(y_predicted):
    raise ValueError(
        "Actual labels and predictions must have equal lengths."
    )

if any(label not in (0, 1) for label in y_actual):
    raise ValueError("Actual labels must be either 0 or 1.")

if any(label not in (0, 1) for label in y_predicted):
    raise ValueError("Predictions must be either 0 or 1.")


# Step 3: Initialize the confusion-matrix counts

TP = 0  # True Positive
TN = 0  # True Negative
FP = 0  # False Positive
FN = 0  # False Negative


# Step 4: Compare actual labels with predictions

for actual, predicted in zip(y_actual, y_predicted):

    if actual == 1 and predicted == 1:
        TP += 1

    elif actual == 0 and predicted == 0:
        TN += 1

    elif actual == 0 and predicted == 1:
        FP += 1

    elif actual == 1 and predicted == 0:
        FN += 1


# Step 5: Display the four outcomes

print("CONFUSION MATRIX COUNTS")
print("-----------------------")
print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)


# Step 6: Display the confusion matrix
# Rows represent actual labels.
# Columns represent predicted labels.

print("\nCONFUSION MATRIX")
print("----------------")
print("                 Predicted 1   Predicted 0")
print(f"Actual 1 (Positive)     {TP:>5}          {FN:>5}")
print(f"Actual 0 (Negative)     {FP:>5}          {TN:>5}")


# Step 7: Calculate accuracy

total = TP + TN + FP + FN

if total > 0:
    accuracy = (TP + TN) / total
    print(f"\nAccuracy: {accuracy:.2%}")
else:
    print("\nAccuracy cannot be calculated: no observations.")


# Step 8: Calculate the True Positive Rate (Recall)

actual_positives = TP + FN

if actual_positives > 0:
    TPR = TP / actual_positives
    print(f"True Positive Rate (Recall): {TPR:.2%}")
else:
    TPR = None
    print("TPR is undefined: there are no actual positives.")


# Step 9: Calculate the False Positive Rate

actual_negatives = FP + TN

if actual_negatives > 0:
    FPR = FP / actual_negatives
    print(f"False Positive Rate: {FPR:.2%}")
else:
    FPR = None
    print("FPR is undefined: there are no actual negatives.")


# Step 10: Final interpretation

print("\nINTERPRETATION")
print("--------------")
print(f"The model evaluated {total} observations.")
print(f"It correctly classified {TP + TN} observations.")
print(f"It made {FP + FN} classification errors.")

print(f"False positive errors: {FP}")
print(f"False negative errors: {FN}")

print(
    "\nThe TPR and FPR can be used to construct ROC points "
    "at different classification thresholds."
)

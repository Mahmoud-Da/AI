
from sklearn.metrics import auc

# Step 1: Define the False Positive Rate (X coordinates)
fpr = [0, 0, 0.5, 0.5, 1]

# Step 2: Define the True Positive Rate (Y coordinates)
tpr = [0, 0.5, 0.5, 1, 1]

# Step 3: Calculate the area under the ROC curve
roc_auc = auc(fpr, tpr)

# Step 4: Display the result
print("False Positive Rate:", fpr)
print("True Positive Rate:", tpr)
print("ROC AUC:", roc_auc)

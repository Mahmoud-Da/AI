import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

# 1. Create sample regression data
torch.manual_seed(42)

X = torch.randn(100, 3)
Y = (
    2 * X[:, 0:1]
    - 3 * X[:, 1:2]
    + 0.5 * X[:, 2:3]
    + 1
)

# 2. Create a neural network
model = nn.Sequential(
    nn.Linear(3, 8),
    nn.ReLU(),
    nn.Linear(8, 1)
)

# 3. Define the cost function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

# 4. Divide the dataset into mini-batches
dataset = TensorDataset(X, Y)

loader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)

# 5. Train the model
epochs = 100

for epoch in range(epochs):
    total_loss = 0.0

    for x_batch, y_batch in loader:

        # Step 1: Clear previous gradients
        optimizer.zero_grad()

        # Step 2: Forward pass
        y_hat = model(x_batch)

        # Step 3: Calculate cost
        loss = criterion(y_hat, y_batch)

        # Step 4: Backpropagation
        loss.backward()

        # Step 5: Update parameters
        optimizer.step()

        total_loss += loss.item() * len(x_batch)

    average_loss = total_loss / len(dataset)

    if (epoch + 1) % 10 == 0:
        print(
            f"Epoch {epoch + 1}/{epochs}, "
            f"Loss: {average_loss:.4f}"
        )

# 6. Make a prediction after training
with torch.no_grad():
    sample = X[:1]
    prediction = model(sample)

print("Prediction:", prediction.item())
print("Actual value:", Y[0].item())

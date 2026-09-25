import torch
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Input data
# --------------------------------------------------

x = torch.tensor([
    0.0,
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
    7.0
])


# The lecture uses fixed values for reproducibility.
y = torch.tensor([
    2.1, 1.4, 1.0, 0.3,
    0.2, -0.4, -1.1, -1.6
])

# --------------------------------------------------
# 2. Visualize the data
# --------------------------------------------------

plt.scatter(x, y)
plt.xlabel("Drug dosage")
plt.ylabel("Patient forgetfulness")
plt.show()


# --------------------------------------------------
# 3. Initialize model parameters
# --------------------------------------------------

m = torch.tensor(0.9)
b = torch.tensor(0.1)


# Enable gradient tracking
m.requires_grad_()
b.requires_grad_()


# --------------------------------------------------
# 4. Define the regression model
# --------------------------------------------------

def regression(x, m, b):
    return m * x + b


# --------------------------------------------------
# 5. Forward pass
# --------------------------------------------------

y_pred = regression(x, m, b)


# --------------------------------------------------
# 6. Plot the initial regression line
# --------------------------------------------------

plt.scatter(x, y)
plt.plot(x, y_pred.detach())
plt.xlabel("Drug dosage")
plt.ylabel("Patient forgetfulness")
plt.show()

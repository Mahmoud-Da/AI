import torch


# ----------------------------------------
# 1. Define the cylinder volume function
# ----------------------------------------

def cylinder_volume(R, L):
    return torch.pi * R**2 * L


# ----------------------------------------
# 2. Create input tensors
# ----------------------------------------

R = torch.tensor(3.0, requires_grad=True)
L = torch.tensor(5.0, requires_grad=True)


# ----------------------------------------
# 3. Forward pass
# ----------------------------------------

V = cylinder_volume(R, L)

print("Volume =", V.item())


# ----------------------------------------
# 4. Backward pass
# ----------------------------------------

V.backward()

print("∂V/∂R =", R.grad.item())
print("∂V/∂L =", L.grad.item())


# ----------------------------------------
# 5. Manual derivative calculations
# ----------------------------------------

manual_dV_dR = 2 * torch.pi * R
manual_dV_dL = torch.pi * R**2

print()
print("Manual ∂V/∂R =", manual_dV_dR.item())
print("Manual ∂V/∂L =", manual_dV_dL.item())


# ----------------------------------------
# 6. Compare volumes for different lengths
# ----------------------------------------

R_value = 3.0

V_length_5 = cylinder_volume(
    torch.tensor(R_value),
    torch.tensor(5.0)
)

V_length_6 = cylinder_volume(
    torch.tensor(R_value),
    torch.tensor(6.0)
)

print()
print("Volume at L=5 =", V_length_5.item())
print("Volume at L=6 =", V_length_6.item())

difference = V_length_6 - V_length_5

print("Difference =", difference.item())


# ----------------------------------------
# 7. Approximate ∂V/∂R using a tiny change
# ----------------------------------------

R_value = 3.0
L_value = 5.0
delta_R = 1e-6

V_original = cylinder_volume(
    torch.tensor(R_value),
    torch.tensor(L_value)
)

V_new = cylinder_volume(
    torch.tensor(R_value + delta_R),
    torch.tensor(L_value)
)

approx_dV_dR = (V_new - V_original) / delta_R

print()
print("Approximate ∂V/∂R =", approx_dV_dR.item())
print("Autodiff ∂V/∂R =", R.grad.item())

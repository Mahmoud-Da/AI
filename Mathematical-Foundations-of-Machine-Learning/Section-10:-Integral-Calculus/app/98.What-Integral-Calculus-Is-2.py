
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Original function: Distance
# ============================================================


def distance(t):
    return t**2


# ============================================================
# 2. Differentiation: Distance -> Speed
# d(t^2)/dt = 2t
# ============================================================

def speed(t):
    return 2 * t


# ============================================================
# 3. Integration: Speed -> Distance
# Integral of 2t = t^2 + C
# Assume initial distance is zero, so C = 0.
# ============================================================

def integrate_speed(t):
    return t**2


# ============================================================
# 4. Generate values
# ============================================================

t_values = np.linspace(0, 5, 100)

d = distance(t_values)
v = speed(t_values)
d_integrated = integrate_speed(t_values)


# ============================================================
# 5. Plot the three functions
# ============================================================

plt.figure(figsize=(15, 4))

# Distance
plt.subplot(1, 3, 1)
plt.plot(t_values, d, "b-", linewidth=2)
plt.xlabel("Time (t)")
plt.ylabel("Distance")
plt.title("Distance = t²")
plt.grid(True, alpha=0.3)

# Speed
plt.subplot(1, 3, 2)
plt.plot(t_values, v, "r-", linewidth=2)
plt.xlabel("Time (t)")
plt.ylabel("Speed")
plt.title("Speed = 2t (Derivative)")
plt.grid(True, alpha=0.3)

# Distance recovered through integration
plt.subplot(1, 3, 3)
plt.plot(t_values, d_integrated, "g-", linewidth=2)
plt.xlabel("Time (t)")
plt.ylabel("Distance")
plt.title("Integral of 2t = t²")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# ============================================================
# 6. Numerical verification
# ============================================================

print("Numerical Verification")
print("-" * 55)

for t in [1, 2, 3, 4, 5]:
    original_distance = distance(t)
    calculated_speed = speed(t)
    integrated_distance = integrate_speed(t)

    print(f"\nt = {t}")
    print(f"Original distance:     {original_distance}")
    print(f"Speed (derivative):    {calculated_speed}")
    print(f"Integrated distance:   {integrated_distance}")

    assert np.isclose(original_distance, integrated_distance)

print("\nAll distance verification tests passed!")

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Time values
t = np.linspace(0, 10, 100)

# Speed function
speed = t

# Integrate speed to get distance
distance = cumulative_trapezoid(speed, t, initial=0)

# Plot speed
plt.figure(figsize=(8, 4))
plt.plot(t, speed)
plt.title("Speed vs Time")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.show()

# Plot distance
plt.figure(figsize=(8, 4))
plt.plot(t, distance)
plt.title("Distance vs Time")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.show()

# Numerical integration example
speed_samples = np.array([0, 2, 4, 6, 8])
time_samples = np.array([0, 1, 2, 3, 4])

total_distance = np.trapz(speed_samples, time_samples)

print("Total Distance:", total_distance)

import numpy as np
import matplotlib.pyplot as plt

# Time values
t = np.linspace(0, 10, 100)

# Distance function
distance = t**2

# First derivative (speed)
speed = np.gradient(distance, t)

# Second derivative (acceleration)
acceleration = np.gradient(speed, t)

# Distance plot
plt.figure(figsize=(8, 4))
plt.plot(t, distance)
plt.title("Distance vs Time")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.show()

# Speed plot
plt.figure(figsize=(8, 4))
plt.plot(t, speed)
plt.title("Speed vs Time")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.show()

# Acceleration plot
plt.figure(figsize=(8, 4))
plt.plot(t, acceleration)
plt.title("Acceleration vs Time")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.show()

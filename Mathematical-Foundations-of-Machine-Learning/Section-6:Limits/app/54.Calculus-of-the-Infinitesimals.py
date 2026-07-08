import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 1000)

# Example function
y = x**2 + 2*x + 1

# Entire curve
plt.plot(x, y)
plt.title("Entire Curve")
plt.show()

# First zoom
plt.plot(x, y)
plt.xlim(-2, 0)
plt.ylim(0, 2)
plt.title("First Zoom")
plt.show()

# Second zoom
plt.plot(x, y)
plt.xlim(-1.5, -0.5)
plt.title("Second Zoom")
plt.show()

# Third zoom
plt.plot(x, y)
plt.xlim(-1.1, -0.9)
plt.title("Third Zoom")
plt.show()

# Final zoom
plt.plot(x, y)
plt.xlim(-1.01, -0.99)
plt.title("Final Zoom")
plt.show()

import tensorflow as tf

# Create the input variable
x = tf.Variable(5.0)

# Track the forward pass
with tf.GradientTape() as tape:
    # Tell TensorFlow to track gradients with respect to x
    tape.watch(x)

    # Forward pass: y = x²
    y = x**2

# Calculate dy/dx
dy_dx = tape.gradient(y, x)

# Display the values
print("x:", x.numpy())
print("y:", y.numpy())
print("dy/dx:", dy_dx.numpy())

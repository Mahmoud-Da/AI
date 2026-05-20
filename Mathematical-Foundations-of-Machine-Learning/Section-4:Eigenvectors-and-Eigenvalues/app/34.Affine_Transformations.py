import numpy as np
import matplotlib.pyplot as plt

# Plot helper


def plot_vectors(vectors, colors):

    plt.figure(figsize=(6, 6))

    for i in range(len(vectors)):
        plt.quiver(
            0, 0,
            vectors[i][0],
            vectors[i][1],
            angles='xy',
            scale_units='xy',
            scale=1,
            color=colors[i]
        )

    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    plt.grid()
    plt.axhline(y=0, color='black')
    plt.axvline(x=0, color='black')

    plt.show()


# Original vector
v = np.array([3, 1])

plot_vectors([v], ['lightblue'])

# Identity matrix
I = np.eye(2)

Iv = np.dot(I, v)

plot_vectors(
    [v, Iv],
    ['lightblue', 'blue']
)

# Reflection over x-axis
E = np.array([
    [1, 0],
    [0, -1]
])

Ev = np.dot(E, v)

plot_vectors(
    [v, Ev],
    ['lightblue', 'blue']
)

# Reflection over y-axis
F = np.array([
    [-1, 0],
    [0, 1]
])

Fv = np.dot(F, v)

plot_vectors(
    [v, Fv],
    ['lightblue', 'blue']
)

# General affine transformation
A = np.array([
    [1, 1],
    [-1, 2]
])

Av = np.dot(A, v)

plot_vectors(
    [v, Av],
    ['lightblue', 'blue']
)

# Additional vectors
v2 = np.array([1, 3])
v3 = np.array([-2, 2])
v4 = np.array([2, -3])

# Convert to column vectors
v_col = v.reshape(2, 1)
v2_col = v2.reshape(2, 1)
v3_col = v3.reshape(2, 1)
v4_col = v4.reshape(2, 1)

# Concatenate into matrix
V = np.concatenate(
    [v_col, v2_col, v3_col, v4_col],
    axis=1
)

# Apply matrix transformation
AV = np.dot(A, V)

# Helper function


def vectorfy(matrix, column):
    return matrix[:, column]


# Plot all vectors
plot_vectors(
    [
        vectorfy(V, 0),
        vectorfy(AV, 0),

        vectorfy(V, 1),
        vectorfy(AV, 1),

        vectorfy(V, 2),
        vectorfy(AV, 2),

        vectorfy(V, 3),
        vectorfy(AV, 3)
    ],
    [
        'lightblue', 'blue',
        'lightgreen', 'green',
        'lightgray', 'gray',
        'orange', 'red'
    ]
)

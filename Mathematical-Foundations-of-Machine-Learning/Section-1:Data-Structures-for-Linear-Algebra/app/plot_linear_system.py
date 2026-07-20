import numpy as np
import matplotlib.pyplot as plt


def main():
    # Step 1: Create time values
    t = np.linspace(0, 40, 1000)

    # Step 2: Define distance equations
    d_robber = 2.5 * t
    d_sheriff = 3 * (t - 5)

    # Step 3: Create plot
    plt.figure()
    plt.title("Bank Robber Caught")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Distance (km)")

    # Step 4: Set axis limits
    plt.xlim(0, 40)
    plt.ylim(0, 100)

    # Step 5: Plot lines
    plt.plot(t, d_robber, label="Robber (2.5 km/min)")
    plt.plot(t, d_sheriff, label="Sheriff (3 km/min, delayed start)")

    # Step 6: Mark intersection
    plt.axvline(x=30, linestyle="--")
    plt.axhline(y=75, linestyle="--")

    # Step 7: Show legend and plot
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the original function


def f(x):
    return x / 2


# 2. Define its antiderivative
def F(x):
    return x**2 / 4


# 3. Set the integration limits
a = 1
b = 2


# 4. Evaluate the antiderivative at each limit
lower_value = F(a)
upper_value = F(b)


# 5. Calculate the definite integral
area = upper_value - lower_value

print("Definite Integral")
print("-" * 30)
print(f"Lower limit: F({a}) = {lower_value}")
print(f"Upper limit: F({b}) = {upper_value}")
print(f"Area: F({b}) - F({a}) = {area}")


# 6. Generate points for plotting
x = np.linspace(0, 3, 200)
x_shaded = np.linspace(a, b, 100)


# 7. Plot the function and shade the area
plt.figure(figsize=(8, 5))

plt.plot(x, f(x), label="f(x) = x / 2")
plt.fill_between(
    x_shaded,
    f(x_shaded),
    0,
    alpha=0.3,
    label=f"Area = {area}"
)

plt.axvline(a, linestyle="--", alpha=0.6)
plt.axvline(b, linestyle="--", alpha=0.6)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Definite Integral from x = 1 to x = 2")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

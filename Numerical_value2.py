from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

# Limits of integration
a = 2
b = 5  # upper limit
N = 10000  # number of random samples

# Function definition


def func(x):
    return x**3


# Exact integral value
x = sy.Symbol("x")
e = sy.integrate(func(x), (x, a, b))

# Generate random x values
xrand = random.uniform(a, b, N)

# Monte Carlo integration
integral = 0.0
for i in range(N):
    integral += func(xrand[i])

answer = (b - a) / float(N) * integral
print("Simulated integral value = ", answer)
print("Actual integral value = ", float(e))

# Visualization
x_vals = np.linspace(a, b, 1000)
y_vals = func(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="$f(x) = x^3$", color='blue')
plt.scatter(xrand[:500], func(xrand[:500]), color='red',
            s=1, alpha=0.5, label='Random Samples')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function Plot and Monte Carlo Sample Points")
plt.legend()
plt.show()

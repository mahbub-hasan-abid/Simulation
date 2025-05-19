import numpy as np
import matplotlib.pyplot as plt

# Define range and number of samples
a = 2
b = 5
n = 10000

# Function definition


def f(x):
    return x**3


# Generate x values and corresponding y values for plotting the function
x = np.linspace(a, b, n)
y = f(x)

# Monte Carlo estimation
X = np.random.uniform(a, b, n)
Y = f(X) * (b - a)
ans = np.sum(Y) / n
print("Monte Carlo estimation:", ans)

# Plot function
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="$f(x) = x^3$", color='blue')
plt.scatter(X[:500], Y[:500], color='red', s=1,
            alpha=0.5, label='Random Samples')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function Plot and Monte Carlo Sample Points")
plt.legend()
plt.show()

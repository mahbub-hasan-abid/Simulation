import numpy as np
import matplotlib.pyplot as plt

N = 10000  # Number of random points
inside = 0  # Counter for points inside the quadrant
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Generate random points
for _ in range(N):
    x, y = np.random.uniform(0, 1, 2)  # Generate (x, y) in [0,1]x[0,1]
    if x**2 + y**2 <= 1:
        inside += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# Estimate the value of pi
pi_estimate = (inside / N) * 4
print(f"Estimated value of pi: {pi_estimate}")

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside')
plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte Carlo Estimation of Pi")
plt.legend()
plt.show()

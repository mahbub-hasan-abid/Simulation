import numpy as np
import matplotlib.pyplot as plt

def bernoulli_simulation(p, n):
    """Simulate n Bernoulli(p) trials"""
    trials = np.random.binomial(n=1, p=p, size=n)
    success = np.sum(trials)
    failure = n - success
    mean = np.mean(trials)
    var = np.var(trials)

    print("\n--- Bernoulli Simulation Result ---")
    print(f"Total Trials: {n}")
    print(f"Successes (1): {success}")
    print(f"Failures  (0): {failure}")
    print(f"Sample Mean: {mean:.4f}")
    print(f"Sample Variance: {var:.4f}")

    # Bar chart
    plt.bar(['Failure (0)', 'Success (1)'], [failure, success], color=['red', 'green'])
    plt.title(f'Bernoulli Distribution (p = {p})')
    plt.ylabel("Count")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# 📥 User Input
try:
    p = float(input("Enter probability of success (0 < p < 1): "))
    n = int(input("Enter number of trials: "))

    if not (0 < p < 1):
        raise ValueError("Probability must be between 0 and 1.")

    bernoulli_simulation(p, n)

except ValueError as e:
    print("Invalid input:", e)

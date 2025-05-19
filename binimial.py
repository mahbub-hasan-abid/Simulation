import numpy as np
import matplotlib.pyplot as plt

def binomial_simulation(trials, n, p):
    """Simulate Binomial distribution"""
    data = np.random.binomial(n=n, p=p, size=trials)
    mean = np.mean(data)
    var = np.var(data)

    print("\n--- Binomial Simulation Result ---")
    print(f"Total Simulations (Experiments): {trials}")
    print(f"Bernoulli Trials per Experiment (n): {n}")
    print(f"Success Probability (p): {p}")
    print(f"Sample Mean ≈ {mean:.4f}")
    print(f"Sample Variance ≈ {var:.4f}")

    # Histogram
    plt.hist(data, bins=range(0, n + 2), edgecolor='black', alpha=0.7)
    plt.title(f'Binomial Distribution (n={n}, p={p})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 📥 User Input
try:
    trials = int(input("Enter number of binomial experiments (e.g., 1000): "))
    n = int(input("Enter number of Bernoulli trials per experiment (e.g., 10): "))
    p = float(input("Enter probability of success in each trial (e.g., 0.4): "))

    if not (0 < p < 1):
        raise ValueError("Probability must be between 0 and 1.")

    binomial_simulation(trials, n, p)

except ValueError as e:
    print("Invalid input:", e)

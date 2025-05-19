import numpy as np
import matplotlib.pyplot as plt
from math import exp, factorial

def poisson_simulation(rate, max_k):
    """Simulate Poisson Distribution and visualize PMF"""
    print(f"\n--- Poisson PMF for λ = {rate} ---")
    pmf = [exp(-rate) * (rate**k) / factorial(k) for k in range(max_k + 1)]
    for k, prob in enumerate(pmf):
        print(f"P({k} events) = {prob:.4f}")

    # Simulate data
    simulated = np.random.poisson(lam=rate, size=10000)

    # Plot PMF histogram
    plt.hist(simulated, bins=range(0, max_k + 2), density=True, edgecolor='black', alpha=0.75)
    plt.title(f'Poisson Distribution (λ = {rate})')
    plt.xlabel('Number of Events')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 📥 User Input
try:
    rate = float(input("Enter average rate λ (e.g., 5): "))
    max_k = int(input("Enter max number of events to compute PMF (e.g., 10): "))

    if rate <= 0 or max_k < 0:
        raise ValueError("λ must be positive and max_k must be non-negative.")

    poisson_simulation(rate, max_k)

except ValueError as e:
    print("Invalid input:", e)

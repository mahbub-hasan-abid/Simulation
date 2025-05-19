import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def exponential_simulation(rate):
    try:
        t = float(input("Enter time threshold (e.g., 120 days): "))
        probability = np.exp(-rate * t)
        print(f"Probability next event occurs after {t} days: {probability:.4f}")

        # Plotting multiple exponential curves
        for lam in [0.5, 1.0, 2.0, 4.0]:
            data = np.random.exponential(scale=1 / lam, size=10000)
            plt.hist(data, bins=50, density=True, histtype='step', label=f"λ = {lam}")

        plt.title("Exponential Distribution Curves")
        plt.xlabel("Time")
        plt.ylabel("Density")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError as e:
        print("Invalid input:", e)

# 📥 User Input
rate = float(input("Enter rate (λ) for exponential distribution: "))
exponential_simulation(rate)

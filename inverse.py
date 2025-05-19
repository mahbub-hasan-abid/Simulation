import numpy as np
import matplotlib.pyplot as plt

def inverse_transform_exponential(rate, n):
    print("\n--- Inverse Transform Method for Exponential Random Variable ---")

    # Step 1: Generate U(0,1)
    u = np.random.uniform(0, 1, n)

    # Step 2: Apply inverse CDF transformation
    x = -np.log(u) / rate

    # Step 3: Print results
    print(f"Rate (λ): {rate}")
    print(f"Total Samples: {n}")
    print(f"Sample Mean ≈ {np.mean(x):.4f}")
    print(f"Sample Variance ≈ {np.var(x):.4f}")
    print(f"First 10 Generated Values:\n{x[:10]}")

    # Step 4: Plot Histogram
    plt.hist(x, bins=50, edgecolor='black', density=True)
    plt.title(f'Inverse Transform Exponential (λ = {rate})')
    plt.xlabel("Generated Value")
    plt.ylabel("Density")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 📥 User Input
try:
    rate = float(input("Enter rate: "))
    n = int(input("Enter number of samples: "))
    if rate <= 0 or n <= 0:
        raise ValueError("rate and sample size must be positive.")
    inverse_transform_exponential(rate, n)
except ValueError as e:
    print("Invalid input:", e)

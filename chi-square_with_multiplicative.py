import math
from scipy.stats import chi2

def multiplicative_rng(seed, a, m, n):
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x) % m
        numbers.append(x / m)  # Normalize to [0,1)
    return numbers

def chi_square_test(random_nums, k=10):
    n = len(random_nums)
    expected = n / k
    bins = [0] * k

    # Count frequencies
    for num in random_nums:
        index = min(int(num * k), k - 1)  # Avoid out of range
        bins[index] += 1

    # Calculate chi-square statistic
    chi_square_stat = sum(((obs - expected) ** 2) / expected for obs in bins)
    critical_value = chi2.ppf(0.95, df=k - 1)

    print(f"Observed frequencies: {bins}")
    print(f"Chi-Square statistic = {chi_square_stat:.4f}")
    print(f"Critical value (df={k - 1}, α=0.05) = {critical_value:.4f}")

    if chi_square_stat < critical_value:
        print("✅ Passed: The numbers are likely uniformly distributed.")
    else:
        print("❌ Failed: The numbers are not uniformly distributed.")

# Example usage
seed = 7       # Initial seed (non-zero)
a = 5          # Multiplier
m = 32         # Modulus (should be > a and power of 2 is common)
n = 100        # Number of random numbers

rand_nums = multiplicative_rng(seed, a, m, n)

print("Generated Random Numbers:")
print(rand_nums)

chi_square_test(rand_nums, k=10)

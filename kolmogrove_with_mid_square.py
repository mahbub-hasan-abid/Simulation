import math

def mid_square(seed, digits, count):
    results = []
    current = seed
    for _ in range(count):
        square = str(current ** 2).zfill(2 * digits)
        mid = len(square) // 2
        mid_digits = square[mid - digits//2 : mid + digits//2]
        current = int(mid_digits)
        results.append(current / (10 ** digits))  # Normalize to [0,1]
    return results

def kolmogorov_smirnov_test(samples):
    samples.sort()
    n = len(samples)
    D_plus = max((i + 1) / n - x for i, x in enumerate(samples))
    D_minus = max(x - i / n for i, x in enumerate(samples))
    D = max(D_plus, D_minus)
    return D

def ks_critical_value(n, alpha=0.05):
    return 1.36 / math.sqrt(n)

# Parameters
seed = 5735
digits = 4
count = 20  # Sample size

# Run Mid-Square and K-S Test
random_numbers = mid_square(seed, digits, count)
D_statistic = kolmogorov_smirnov_test(random_numbers)
D_critical = ks_critical_value(count)

# Output
print("Generated Random Numbers:", random_numbers)
print(f"D-statistic = {D_statistic:.4f}")
print(f"Critical value (α=0.05, n={count}) = {D_critical:.4f}")

# Decision
if D_statistic < D_critical:
    print("✅ The random numbers pass the K-S test (uniformly distributed).")
else:
    print("❌ The random numbers fail the K-S test (not uniformly distributed).")

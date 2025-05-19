import math
from scipy.stats import chi2

def additive_congruential_generator(seed1, seed2, m, n):
    sequence = [seed1, seed2]
    for _ in range(2, n):
        next_val = (sequence[-1] + sequence[-2]) % m
        sequence.append(next_val)
    # Normalize to [0,1)
    return [x / m for x in sequence]

def chi_square_autocorrelation_test(rand_nums):
    # Convert to binary (0 if < 0.5, else 1)
    bits = [0 if x < 0.5 else 1 for x in rand_nums]

    # Form pairs: (b0,b1), (b1,b2), ..., (bn-2,bn-1)
    pairs = list(zip(bits[:-1], bits[1:]))

    # Count frequencies of each bit pair
    freq = {'00': 0, '01': 0, '10': 0, '11': 0}
    for a, b in pairs:
        key = f"{a}{b}"
        freq[key] += 1

    observed = list(freq.values())
    total_pairs = len(pairs)
    expected = total_pairs / 4  # Equal expected frequency

    # Chi-Square Test
    chi_sq = sum((obs - expected) ** 2 / expected for obs in observed)
    critical_value = chi2.ppf(0.95, df=3)  # 4 categories => df = 3

    # Output
    print("Bit pair frequencies:", freq)
    print(f"Chi-Square Statistic = {chi_sq:.4f}")
    print(f"Critical Value (α=0.05, df=3) = {critical_value:.4f}")
    if chi_sq < critical_value:
        print("✅ Passed: No significant autocorrelation (random enough).")
    else:
        print("❌ Failed: Autocorrelation is present (not random enough).")

# Example usage
seed1 = 7
seed2 = 11
m = 32
n = 100  # Number of random numbers

rand_nums = additive_congruential_generator(seed1, seed2, m, n)
chi_square_autocorrelation_test(rand_nums)

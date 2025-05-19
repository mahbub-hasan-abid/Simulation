from collections import Counter
from scipy.stats import chi2

# Step 1: Multiplicative Congruential Generator
def mcg(seed, a, m, n):
    x = seed
    nums = []
    for _ in range(n):
        x = (a * x) % m
        num_str = str(x).zfill(5)[:5]  # Get 5 digits, zero-padded
        nums.append(num_str)
    return nums

# Step 2: Classify hands
def classify_hand(hand):
    count = Counter(hand)
    freq = sorted(count.values(), reverse=True)

    if freq == [5]:
        return "Five of a kind"
    elif freq == [4, 1]:
        return "Four of a kind"
    elif freq == [3, 2]:
        return "Full house"
    elif freq == [3, 1, 1]:
        return "Three of a kind"
    elif freq == [2, 2, 1]:
        return "Two pair"
    elif freq == [2, 1, 1, 1]:
        return "One pair"
    else:
        return "All different"

# Step 3: Poker test logic
def poker_test(random_numbers):
    categories = [
        "All different", "One pair", "Two pair",
        "Three of a kind", "Full house", "Four of a kind", "Five of a kind"
    ]
    counts = {cat: 0 for cat in categories}
    
    for num in random_numbers:
        cat = classify_hand(num)
        counts[cat] += 1

    n = len(random_numbers)
    observed = list(counts.values())

    # Approximate expected probabilities for 5-digit hands (base 10)
    expected_probs = {
        "All different": 0.3024,
        "One pair": 0.5040,
        "Two pair": 0.1080,
        "Three of a kind": 0.0720,
        "Full house": 0.0090,
        "Four of a kind": 0.0045,
        "Five of a kind": 0.0001,
    }

    expected = [expected_probs[cat] * n for cat in categories]

    # Chi-Square statistic
    chi_square = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    critical_value = chi2.ppf(0.95, df=len(categories) - 1)

    print("Category counts:")
    for cat in categories:
        print(f"{cat:17}: Observed = {counts[cat]}, Expected ≈ {expected_probs[cat] * n:.2f}")

    print(f"\nChi-Square Statistic = {chi_square:.4f}")
    print(f"Critical Value (α=0.05, df={len(categories)-1}) = {critical_value:.4f}")

    if chi_square < critical_value:
        print("✅ Passed: Random numbers follow expected digit distribution.")
    else:
        print("❌ Failed: Digit pattern deviates from expected randomness.")

# Example usage
seed = 7
a = 5
m = 32749  # Preferably a large prime
n = 100  # Number of 5-digit random numbers

random_nums = mcg(seed, a, m, n)
poker_test(random_nums)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def lcg(seed, n, a=1103515245, c=12345, m=2**31):
    print("\n--- Linear Congruential Generator ---")
    results = []
    for _ in range(n):
        seed = (a * seed + c) % m
        results.append(seed / m)  # Normalize to [0,1)
    print("Generated values:\n", results)

# 📥 User Input
try:
    seed = int(input("Enter seed value: "))
    n = int(input("Enter how many random numbers to generate: "))
    lcg(seed, n)
except ValueError as e:
    print("Invalid input:", e)


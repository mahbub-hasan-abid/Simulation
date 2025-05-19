import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a random sample (size = 200) from N(100, 20)
np.random.seed(42)  # For reproducibility
sample_data = np.random.normal(loc=100, scale=20, size=200)

# Generate diastolic blood pressure data (men) from N(80, 20)
blood_pressure = np.random.normal(loc=80, scale=20, size=200)

# Plot Unimodal Density Curve
plt.figure(figsize=(10, 6))
sns.kdeplot(sample_data, fill=True,
            label="Sample Data (N(100, 20))", color="blue")
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Unimodal Density Curve of Normal Distribution")
plt.legend()
plt.grid()
plt.show()

# Create a Multimodal Distribution by Combining Two Normal Distributions
mixed_data = np.concatenate([sample_data, blood_pressure])

# Plot Multimodal Density Curve
plt.figure(figsize=(10, 6))
sns.kdeplot(mixed_data, fill=True,
            label="Multimodal Data (Mixed N(100,20) & N(80,20))", color="purple")
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Multimodal Density Curve")
plt.legend()
plt.grid()
plt.show()

# Plot Histogram with Density Curve for Blood Pressure Data
plt.figure(figsize=(10, 6))
sns.histplot(blood_pressure, kde=True, bins=20, color="green",
             label="Diastolic Blood Pressure (N(80,20))", alpha=0.6)
plt.xlabel("Blood Pressure")
plt.ylabel("Frequency")
plt.title("Histogram of Blood Pressure with Density Curve")
plt.legend()
plt.grid()
plt.show()

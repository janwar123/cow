import numpy as np
import matplotlib.pyplot as plt
import simpy

# Create SimPy environment
env = simpy.Environment()

# Generate 100 random numbers
numbers100 = np.random.uniform(0, 1, 100)

# Generate 10,000 random numbers
numbers10000 = np.random.uniform(0, 1, 10000)

# Calculate statistics
mean100 = np.mean(numbers100)
mean10000 = np.mean(numbers10000)

max100 = np.max(numbers100)
min100 = np.min(numbers100)

max10000 = np.max(numbers10000)
min10000 = np.min(numbers10000)

# Display results
print("Statistics for 100 Random Numbers")
print("Mean:", mean100)
print("Maximum:", max100)
print("Minimum:", min100)

print("\nStatistics for 10,000 Random Numbers")
print("Mean:", mean10000)
print("Maximum:", max10000)
print("Minimum:", min10000)

print("\nTheoretical Mean = 1")

print("Error for 100 Numbers:", abs(mean100 - 1))
print("Error for 10,000 Numbers:", abs(mean10000 - 1))

# Visualization
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(numbers100, bins=20, color="skyblue",
         edgecolor="black", density=True)
plt.axvline(mean100, color="red", linestyle="--",
            label=f"Mean = {mean100:.4f}")
plt.title("Distribution of 100 Random Numbers")
plt.xlabel("Random Number")
plt.ylabel("Density")
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(numbers10000, bins=20, color="lightgreen",
         edgecolor="black", density=True)
plt.axvline(mean10000, color="red", linestyle="--",
            label=f"Mean = {mean10000:.4f}")
plt.title("Distribution of 10,000 Random Numbers")
plt.xlabel("Random Number")
plt.ylabel("Density")
plt.legend()

plt.tight_layout()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import simpy

# Create SimPy environment
env = simpy.Environment()

# Generate two sets of 100 random numbers between 0 and 1
numbers1 = np.random.uniform(0, 1, 100)
numbers2 = np.random.uniform(0, 1, 100)

# Calculate maximum, minimum, and mean
max_num = np.max(numbers1)
min_num = np.min(numbers1)

mean1 = np.mean(numbers1)
mean2 = np.mean(numbers2)

std1 = np.std(numbers1)
std2 = np.std(numbers2)

# Display results
print("First 100 Random Numbers:")
print(numbers1)

print("\nMaximum Number:", max_num)
print("Minimum Number:", min_num)

print("\nMean of First 100 Numbers:", mean1)
print("Mean of Second 100 Numbers:", mean2)

print("\nAre both means exactly equal?", mean1 == mean2)

print("\nStandard Deviation of First 100 Numbers:", std1)
print("Standard Deviation of Second 100 Numbers:", std2)
print("Are both standard deviations exactly equal?", std1 == std2)

# Visualization
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(numbers1, bins=15, color="skyblue", edgecolor="black")
plt.axvline(mean1, color="red", linestyle="--",
            label=f"Mean = {mean1:.4f}")
plt.title("First 100 Random Numbers")
plt.xlabel("Random Number")
plt.ylabel("Frequency")
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(numbers2, bins=15, color="lightgreen", edgecolor="black")
plt.axvline(mean2, color="red", linestyle="--",
            label=f"Mean = {mean2:.4f}")
plt.title("Second 100 Random Numbers")
plt.xlabel("Random Number")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()

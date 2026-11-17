import numpy as np
import matplotlib.pyplot as plt
import simpy

# Create SimPy environment
env = simpy.Environment()

# Set the same random seed
np.random.seed(42)
numbers1 = np.random.uniform(0, 1, 100)

# Reset the same seed
np.random.seed(42)
numbers2 = np.random.uniform(0, 1, 100)

# Calculate mean, maximum, and minimum
mean1 = np.mean(numbers1)
mean2 = np.mean(numbers2)

print("First Set of Random Numbers:")
print(numbers1)

print("\nSecond Set of Random Numbers:")
print(numbers2)

print("\nMean of First Set:", mean1)
print("Mean of Second Set:", mean2)

print("\nMaximum:", np.max(numbers1))
print("Minimum:", np.min(numbers1))

print("\nAre both arrays identical?",
      np.array_equal(numbers1, numbers2))

print("Are both means equal?", mean1 == mean2)

# Visualization
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(numbers1, color="blue", label="First Set")
plt.title("First Set (Seed = 42)")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(numbers2, color="orange", label="Second Set")
plt.title("Second Set (Seed = 42)")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()

plt.tight_layout()
plt.show()
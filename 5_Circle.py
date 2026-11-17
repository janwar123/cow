import numpy as np
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Generate 100,000 random points
N_max = 100000

x = np.random.uniform(0, 1, N_max)
y = np.random.uniform(0, 1, N_max)

# Check which points fall inside the quarter-circle
inside = (x**2 + y**2) <= 1

# Different sample sizes
sample_sizes = [100, 1000, 10000, 100000]

# Store estimated values of pi
pi_estimates = []

print("ESTIMATION OF PI USING MONTE CARLO METHOD")
print("------------------------------------------")

for n in sample_sizes:

    # Count points inside the quarter-circle
    inside_count = np.sum(inside[:n])

    # Calculate proportion
    proportion = inside_count / n

    # Estimate pi
    pi_estimate = 4 * proportion

    # Store result
    pi_estimates.append(pi_estimate)

    # Display results
    print("\nNumber of points:", n)
    print("Points inside:", inside_count)
    print("Proportion:", proportion)
    print("Estimated Pi:", pi_estimate)

# Create visualizations
plt.figure(figsize=(13, 5))

# Plot 1: Random points inside the square
plt.subplot(1, 2, 1)

plt.scatter(x[:5000][inside[:5000]],
            y[:5000][inside[:5000]],
            color="green", s=5, label="Inside quarter-circle")

plt.scatter(x[:5000][~inside[:5000]],
            y[:5000][~inside[:5000]],
            color="red", s=5, label="Outside quarter-circle")

plt.title("Random Points Inside a Square")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.legend()
plt.axis("equal")

# Plot 2: Estimated pi against number of points
plt.subplot(1, 2, 2)

plt.plot(sample_sizes, pi_estimates,
         marker="o", color="blue", label="Estimated Pi")

plt.axhline(y=np.pi, color="red",
            linestyle="--", label="Actual Pi = 3.14159")

plt.xscale("log")
plt.xlabel("Number of Random Points")
plt.ylabel("Estimated Pi")
plt.title("Monte Carlo Estimation of Pi")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
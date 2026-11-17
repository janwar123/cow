import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducible results
np.random.seed(42)

# Number of customers
n = 1000

# Generate 1000 inter-arrival times
# Exponential distribution with mean = 5 minutes
inter_arrival_times = np.random.exponential(scale=5, size=n)

# Generate 1000 service times
# Uniform distribution between 2 and 8 minutes
service_times = np.random.uniform(low=2, high=8, size=n)

# Calculate sample statistics
arrival_mean = np.mean(inter_arrival_times)
arrival_std = np.std(inter_arrival_times, ddof=1)

service_mean = np.mean(service_times)
service_std = np.std(service_times, ddof=1)

# Calculate theoretical statistics
theoretical_arrival_mean = 5
theoretical_arrival_std = 5

theoretical_service_mean = (2 + 8) / 2
theoretical_service_std = np.sqrt((8 - 2)**2 / 12)

# Print comparison
print("INTER-ARRIVAL TIME (Exponential Distribution)")
print(f"Sample Mean: {arrival_mean:.4f} minutes")
print(f"Theoretical Mean: {theoretical_arrival_mean:.4f} minutes")
print(f"Sample Standard Deviation: {arrival_std:.4f} minutes")
print(f"Theoretical Standard Deviation: {theoretical_arrival_std:.4f} minutes")

print("\nSERVICE TIME (Uniform Distribution)")
print(f"Sample Mean: {service_mean:.4f} minutes")
print(f"Theoretical Mean: {theoretical_service_mean:.4f} minutes")
print(f"Sample Standard Deviation: {service_std:.4f} minutes")
print(f"Theoretical Standard Deviation: {theoretical_service_std:.4f} minutes")

# Plot both histograms
plt.figure(figsize=(12, 5))

# Inter-arrival time histogram
plt.subplot(1, 2, 1)
plt.hist(inter_arrival_times, bins=30, color="skyblue",
         edgecolor="black")
plt.title("Inter-Arrival Times (Exponential)")
plt.xlabel("Time (minutes)")
plt.ylabel("Frequency")

# Service time histogram
plt.subplot(1, 2, 2)
plt.hist(service_times, bins=30, color="lightgreen",
         edgecolor="black")
plt.title("Service Times (Uniform)")
plt.xlabel("Time (minutes)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

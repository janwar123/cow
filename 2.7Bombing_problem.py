
import numpy as np

# Step 1: Given Information
N = 20

sigma_x = 500
sigma_y = 300

# Target Area
x_min = -500
x_max = 500

y_min = -300
y_max = 300

# Step 2: Generate Random Normal Numbers
np.random.seed(10)

Zx = np.random.normal(0, 1, N)
Zy = np.random.normal(0, 1, N)

# Step 3: Calculate X and Y Coordinates
X = sigma_x * Zx
Y = sigma_y * Zy

# Step 4: Check Hit or Miss
hits = 0
misses = 0

print("Bomb\tX\tY\tResult")

for i in range(N):

    if x_min <= X[i] <= x_max and y_min <= Y[i] <= y_max:
        print(i + 1, "\t", round(X[i], 2), "\t", round(Y[i], 2), "\tHit")
        hits = hits + 1

    else:
        print(i + 1, "\t", round(X[i], 2), "\t", round(Y[i], 2), "\tMiss")
        misses = misses + 1

# Step 5: Calculate Hit Percentage
hit_percentage = (hits / N) * 100

print("\nTotal Bombs =", N)
print("Number of Hits =", hits)
print("Number of Misses =", misses)
print("Hit Percentage =", round(hit_percentage, 2), "%")

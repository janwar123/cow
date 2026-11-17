
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Rectangle Area
A = 3 * 140

# Step 2: Generate Random Points
N = 1000

x = 2 + np.random.rand(N) * 3
y = np.random.rand(N) * 140

# Step 3: Check Inside or Outside
inside = y < x**3        #bolean akare value store korbe 

# Step 4: Count Inside Points
M = 0

for i in range(N):
    if inside[i]:
        M = M + 1

# Step 5: Calculate Integral
I = (M / N) * A

print("Total Points =", N)
print("Inside Points =", M)
print("Rectangle Area =", A)
print("Estimated Integral =", round(I, 2))

# Step 6: Draw Graph
plt.figure(figsize=(7, 7))

plt.scatter(x[inside], y[inside], color="green", s=8)
plt.scatter(x[~inside], y[~inside], color="red", s=8)

# Draw Boundary
xx = np.linspace(2, 5, 100)
yy = xx**3

plt.plot(xx, yy, color="blue")

plt.xlim(2, 5)
plt.ylim(0, 140)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte Carlo Numerical Integration")

plt.grid()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Step 1: Square Area
A = 9 * 9

# Step 2: Generate Random Points
N = 1000

x = np.random.rand(N) * 9
y = np.random.rand(N) * 9

# Step 3: Check Inside or Outside
inside = y < (2 + 0.5*x + 0.04*x*x)  #boolean array akare store hocche 

# Step 4: Count Inside Points
M = 0

for i in range(N):
    if inside[i]:
        M = M + 1

# Step 5: Calculate Area
F = (M / N) * A

print("Total Points =", N)
print("Inside Points =", M)
print("Square Area =", A)
print("Estimated Area =", round(F, 2), "cm2")

# Step 6: Draw Graph
plt.figure(figsize=(7, 7))

plt.scatter(x[inside], y[inside], color="green", s=8)
plt.scatter(x[~inside], y[~inside], color="red", s=8)

# Draw Boundary
xx = np.linspace(0, 9, 100)
yy = 2 + 0.5*xx + 0.04*xx*xx

plt.plot(xx, yy, color="blue")

plt.xlim(0, 9)
plt.ylim(0, 9)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte Carlo Method")

plt.grid()
plt.show()

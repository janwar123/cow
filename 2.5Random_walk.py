
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Random Numbers
N = 50

random = np.random.randint(0, 10, N)

# Step 2: Starting Position
x = 0
y = 0

# Store Positions
X = [x]
Y = [y]

# Step 3: Check Direction and Move
for i in range(N):

    if random[i] <= 4:
        y = y + 1

    elif random[i] <= 7:
        x = x - 1

    else:
        x = x + 1

    X.append(x)
    Y.append(y)

# Step 4: Print Final Position
print("Total Steps =", N)
print("Final X Position =", x)
print("Final Y Position =", y)
print("Final Position =", (x, y))

# Step 5: Draw Graph
plt.figure(figsize=(7, 7))

plt.plot(X, Y, marker="o", color="blue")

plt.scatter(X[0], Y[0], color="green", s=100, label="Start")
plt.scatter(X[-1], Y[-1], color="red", s=100, label="End")

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Random Walk Simulation")

plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Number of Epochs
N = 50

# Step 2: Starting Position
x = 0
y = 0

# Store Positions
X = [x]
Y = [y]

# Step 3: Simulate Movements
for i in range(N):

    move = np.random.choice(
        ['L', 'R', 'F', 'B'],
        p=[0.25, 0.35, 0.30, 0.10]
    )

    if move == 'L':
        x = x - 1

    elif move == 'R':
        x = x + 1

    elif move == 'F':
        y = y + 1

    else:
        y = y - 1

    # Store New Position
    X.append(x)
    Y.append(y)

# Step 4: Display Final Position
print("Total Epochs =", N)
print("Final X Position =", x)
print("Final Y Position =", y)
print("Final Location =", (x, y))

# Step 5: Draw Graph
plt.figure(figsize=(8, 6))

plt.plot(X, Y, marker='o', markersize=3, color='blue')

plt.scatter(X[0], Y[0], color='green', s=100, label='Start')
plt.scatter(X[-1], Y[-1], color='red', s=100, label='End')

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Random Walk After 50 Epochs")

plt.legend()
plt.grid()
plt.show()
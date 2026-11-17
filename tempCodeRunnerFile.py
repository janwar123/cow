import numpy as np
import matplotlib.pyplot as plt

# Number of epochs
n = 50

# Initial position
x = 0
y = 0
z = 0

# Store positions
X = [x]
Y = [y]

# Simulate 50 movements
for i in range(n):

    # Horizontal movement
    move = np.random.choice(
        ['L', 'R', 'F', 'B'],
        p=[0.25, 0.35, 0.30, 0.10]
    )

    if move == 'L':
        x -= 1
    elif move == 'R':
        x += 1
    elif move == 'F':
        y += 1
    else:
        y -= 1

    # Vertical movement
    vertical = np.random.choice(
        ['U', 'D'],
        p=[0.80, 0.20]
    )

    if vertical == 'U':
        z += 1
    else:
        z -= 1

    # Store position
    X.append(x)
    Y.append(y)

# Display final position
print("Final X Position:", x)
print("Final Y Position:", y)
print("Final Z Position:", z)

print("Final Location:", (x, y, z))

# Draw 2D graph
plt.figure(figsize=(8, 6))

plt.plot(X, Y, marker='o', markersize=3)

plt.scatter(0, 0, color='green', label='Starting Point')
plt.scatter(x, y, color='red', label='Final Point')

# Show four quadrants
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Flying Object Movement After 50 Epochs")

plt.grid()
plt.legend()
plt.show()
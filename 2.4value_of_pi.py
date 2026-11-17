
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Random Points
N = 1000

x = np.random.rand(N)
y = np.random.rand(N)

# Step 2: Check Inside or Outside
inside = x**2 + y**2 <= 1

# Step 3: Count Inside Points
M = 0

for i in range(N):
    if inside[i]:
        M = M + 1

# Step 4: Calculate Value of Pi
pi = (4 * M) / N

print("Total Points =", N)
print("Inside Points =", M)
print("Estimated Value of Pi =", round(pi, 4))

# Step 5: Draw Graph
plt.figure(figsize=(7, 7))

plt.scatter(x[inside], y[inside], color="green", s=8)
plt.scatter(x[~inside], y[~inside], color="red", s=8)

# Draw Circle Boundary
t = np.linspace(0, np.pi/2, 100) #0 = Starting Angle (0 Degree)
                                 #np.pi/2 = Ending Angle (90 Degree)
                                 #100 = মোট 100টি Angle তৈরি করবে।


cx = np.cos(t)  #এখানে cos() প্রতিটি Angle-এর Cosine Value বের করবে।

cy = np.sin(t)  #এখানে sin() প্রতিটি Angle-এর Sine Value বের করবে।

plt.plot(cx, cy, color="blue")

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte Carlo Method to Calculate Pi")

plt.grid()
plt.show()

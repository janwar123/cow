
import numpy as np

# Step 1: Total Games
N = 1000

# Step 2: Initialize Variables
total_flips = 0     #সব Game-এ মোট কতবার Toss হয়েছে
total_return = 0    #মোট কত টাকা পুরস্কার পেয়েছি

win = 0
lose = 0

# Step 3: Simulate Games
for game in range(N):

    heads = 0
    tails = 0
    flips = 0

    while abs(heads - tails) < 3:

        r = np.random.rand()

        if r < 0.5:
            heads = heads + 1
        else:
            tails = tails + 1

        flips = flips + 1

    # Step 4: Count Total Flips
    total_flips = total_flips + flips

    # Step 5: Calculate Win or Lose
    if flips < 8:
        total_return = total_return + 8
        win = win + 1

    elif flips > 8:
        lose = lose + 1

# Step 6: Calculate Cost and Profit
total_cost = total_flips
profit = total_return - total_cost

average_flips = total_flips / N

# Step 7: Display Result
print("Total Games =", N)
print("Total Flips =", total_flips)
print("Total Cost =", total_cost, "Rs.")
print("Total Return =", total_return, "Rs.")
print("Winning Games =", win)
print("Losing Games =", lose)
print("Average Flips =", round(average_flips, 2))
print("Total Profit/Loss =", profit, "Rs.")

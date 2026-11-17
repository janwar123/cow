import numpy as np
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Game settings
cost_per_trial = 1
target_difference = 20
prize = 100  # Assumed prize; change if necessary

# Monte Carlo simulation
def play_game():

    H = 0
    T = 0
    trials = 0

    while abs(H - T) < target_difference:

        # Roll a six-sided die
        dice = np.random.randint(1, 7)

        trials += 1

        # Odd = H, Even = T
        if dice % 2 == 1:
            H += 1
        else:
            T += 1

    # Find winner
    if H > T:
        winner = "H"
    else:
        winner = "T"

    # Calculate cost and net profit
    total_cost = trials * cost_per_trial
    net_profit = prize - total_cost

    return trials, H, T, winner, total_cost, net_profit


# Repeat the game 1000 times
games = 1000

results = []

for i in range(games):
    results.append(play_game())

# Convert results into NumPy array
results = np.array(results, dtype=object)

trials = results[:, 0].astype(int)
costs = results[:, 4].astype(float)
profits = results[:, 5].astype(float)

# Display results
print("GAMBLING GAME SIMULATION")
print("------------------------")
print("Total Games:", games)
print("Average Trials:", np.mean(trials))
print("Average Cost: $", np.mean(costs))
print("Average Net Profit/Loss: $", np.mean(profits))

print("H Wins:", np.sum(results[:, 3] == "H"))
print("T Wins:", np.sum(results[:, 3] == "T"))

print("Winning Probability of H:",
      np.mean(results[:, 3] == "H"))

# Visualization 1: Number of trials
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(trials, bins=30, edgecolor="black")
plt.title("Distribution of Game Duration")
plt.xlabel("Number of Trials")
plt.ylabel("Frequency")

# Visualization 2: Profit and loss
plt.subplot(1, 2, 2)
plt.hist(profits, bins=30, edgecolor="black")
plt.axvline(0, color="red", linestyle="--",
            label="Break-even")
plt.title("Profit and Loss Distribution")
plt.xlabel("Net Profit / Loss ($)")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()

import numpy as np

# Step 1: Given Information
N = 30000

life = [1000, 1100, 1200, 1300, 1400,
        1500, 1600, 1700, 1800, 1900]

prob = [0.10, 0.14, 0.24, 0.14, 0.12,
        0.10, 0.06, 0.05, 0.03, 0.02]

delay = [4, 6, 8]
delay_prob = [0.3, 0.6, 0.1]

bearing_cost = 20
downtime_cost = 5
repairman_cost = 25

np.random.seed(42)

# Step 2: Existing Policy
count1 = 0
total_delay1 = 0

for i in range(3):

    clock = 0

    while True:

        bearing_life = np.random.choice(life, p=prob)

        if clock + bearing_life > N:
            break

        clock = clock + bearing_life

        repair_delay = np.random.choice(delay, p=delay_prob)

        total_delay1 = total_delay1 + repair_delay

        count1 = count1 + 1

# Calculate Existing Policy Cost
replace_time1 = count1 * 20

downtime1 = total_delay1 + replace_time1

cost1 = count1 * bearing_cost
cost2 = downtime1 * downtime_cost
cost3 = replace_time1 * repairman_cost / 60

total_cost1 = cost1 + cost2 + cost3

print("EXISTING POLICY")
print("Bearing Replaced =", count1)
print("Total Delay =", total_delay1)
print("Total Downtime =", downtime1)
print("Total Cost =", round(total_cost1, 2))


# Step 3: Proposed Policy
count2 = 0
total_delay2 = 0

clock = 0

while True:

    b1 = np.random.choice(life, p=prob)
    b2 = np.random.choice(life, p=prob)
    b3 = np.random.choice(life, p=prob)

    first_failure = min(b1, b2, b3)

    if clock + first_failure > N:
        break

    clock = clock + first_failure

    repair_delay = np.random.choice(delay, p=delay_prob)

    total_delay2 = total_delay2 + repair_delay

    count2 = count2 + 1

# Calculate Proposed Policy Cost
total_bearings = count2 * 3

replace_time2 = count2 * 40

downtime2 = total_delay2 + replace_time2

cost4 = total_bearings * bearing_cost
cost5 = downtime2 * downtime_cost
cost6 = replace_time2 * repairman_cost / 60

total_cost2 = cost4 + cost5 + cost6

print("\nPROPOSED POLICY")
print("Replacement Events =", count2)
print("Bearing Replaced =", total_bearings)
print("Total Delay =", total_delay2)
print("Total Downtime =", downtime2)
print("Total Cost =", round(total_cost2, 2))


# Step 4: Compare Both Policies
print("\nCOST COMPARISON")

print("Existing Policy Cost =", round(total_cost1, 2))
print("Proposed Policy Cost =", round(total_cost2, 2))

saving = total_cost1 - total_cost2

print("Saving =", round(saving, 2))

if saving > 0:
    print("Proposed Policy is Better")
else:
    print("Existing Policy is Better")

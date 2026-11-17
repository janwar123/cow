import simpy
import numpy as np

# Input parameters
mean_interarrival = 5
mean_service = 4
max_customers = 1000

# Set random seed
np.random.seed(42)

# Create SimPy environment
env = simpy.Environment()

# Create a single server
server = simpy.Resource(env, capacity=1)

# Store simulation statistics
waiting_times = []
total_service_time = 0

# Customer process
def customer(env, customer_id, server):

    global total_service_time

    # Record customer arrival time
    arrival_time = env.now

    # Request the server (FIFO)
    with server.request() as request:

        yield request

        # Record service start time
        service_start = env.now

        # Calculate waiting time
        waiting_time = service_start - arrival_time
        waiting_times.append(waiting_time)

        # Generate service time
        service_time = np.random.exponential(
            mean_service
        )

        total_service_time += service_time

        # Serve customer
        yield env.timeout(service_time)


# Customer arrival process
def customer_generator(env, server):

    for i in range(max_customers):

        # Generate inter-arrival time
        interarrival_time = np.random.exponential(
            mean_interarrival
        )

        # Wait for next arrival
        yield env.timeout(interarrival_time)

        # Create new customer
        env.process(customer(env, i, server))


# Start customer generator
env.process(customer_generator(env, server))

# Run simulation
env.run()

# Simulation ending time
simulation_end_time = env.now

# Calculate average delay
average_delay = np.mean(waiting_times)

# Calculate average number in queue
average_queue = sum(waiting_times) / simulation_end_time

# Calculate server utilization
server_utilization = (
    total_service_time / simulation_end_time
) * 100

# Theoretical arrival and service rates
arrival_rate = 1 / mean_interarrival
service_rate = 1 / mean_service

print("M/M/1 QUEUE SIMULATION")
print("---------------------")

print("Total Customers:", max_customers)

print("Average Delay in Queue:",
      round(average_delay, 4), "minutes")

print("Average Number in Queue:",
      round(average_queue, 4))

print("Server Utilization:",
      round(server_utilization, 2), "%")

print("Simulation Ending Time:",
      round(simulation_end_time, 4), "minutes")

print("Arrival Rate:", arrival_rate)
print("Service Rate:", service_rate)
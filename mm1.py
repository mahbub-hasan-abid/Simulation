import numpy as np
import matplotlib.pyplot as plt

def exponential(mean):
    """Generate exponential random variable"""
    return np.random.exponential(scale=mean)

def mm1_queue(mean_interarrival, mean_service, max_customers):
    arrival_times = [0]  # Time of arrival for each customer
    service_start_times = [0]
    service_times = [exponential(mean_service)]
    departure_times = [service_start_times[0] + service_times[0]]

    for i in range(1, max_customers):
        arrival_time = arrival_times[-1] + exponential(mean_interarrival)
        start_service = max(arrival_time, departure_times[-1])
        service_time = exponential(mean_service)
        departure_time = start_service + service_time

        arrival_times.append(arrival_time)
        service_start_times.append(start_service)
        service_times.append(service_time)
        departure_times.append(departure_time)

    # Calculations
    delays_in_queue = [service_start_times[i] - arrival_times[i] for i in range(max_customers)]
    queue_lengths = [sum(1 for t in arrival_times if t <= current_time) - 
                     sum(1 for t in departure_times if t < current_time)
                     for current_time in arrival_times]

    avg_delay = np.mean(delays_in_queue)
    avg_queue_len = np.mean(queue_lengths)
    total_busy_time = sum(service_times)
    server_utilization = total_busy_time / departure_times[-1]
    simulation_end_time = departure_times[-1]

    print("\n--- M/M/1 Queue Simulation Summary ---")
    print(f"Mean Interarrival Time: {mean_interarrival} minutes")
    print(f"Mean Service Time: {mean_service} minutes")
    print(f"Number of Customers: {max_customers}")
    print(f"Average Delay in Queue: {avg_delay:.3f} minutes")
    print(f"Average Number in Queue: {avg_queue_len:.3f}")
    print(f"Server Utilization: {server_utilization:.3f}")
    print(f"Time Simulation Ended: {simulation_end_time:.3f} minutes")

    # Plotting queue length over time
    plt.plot(arrival_times, queue_lengths, label='Queue Length Over Time')
    plt.xlabel("Time (minutes)")
    plt.ylabel("Number in Queue")
    plt.title("M/M/1 Queue Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# === Accept User Input ===
try:
    mean_interarrival = float(input("Enter Mean Interarrival Time (e.g. 1.0): "))
    mean_service = float(input("Enter Mean Service Time (e.g. 0.5): "))
    max_customers = int(input("Enter Number of Customers (e.g. 1000): "))

    mm1_queue(mean_interarrival, mean_service, max_customers)

except ValueError:
    print("Invalid input! Please enter numeric values.")

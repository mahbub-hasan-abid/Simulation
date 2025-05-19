import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.random.seed(42)  # For reproducibility

# Parameters
N = 3  # Number of bearings
Tmax = 200
lambda_failure = 0.01  # Failure rate (exponential distribution)
cost_per_bearing = 100

# Generate initial failure times for 3 bearings
def generate_failure_times():
    return np.random.exponential(scale=1/lambda_failure, size=N)

# --- Policy 1: Replace bearing individually when it fails ---
def policy1(failure_times):
    total_cost = 0
    current_time = 0
    failure_times = failure_times.copy()
    cost_timeline = []
    times = []

    while current_time < Tmax:
        next_failure_time = np.min(failure_times)
        failed_bearing = np.argmin(failure_times)
        if next_failure_time > Tmax:
            break
        current_time = next_failure_time
        total_cost += cost_per_bearing
        cost_timeline.append(total_cost)
        times.append(current_time)
        failure_times[failed_bearing] = current_time + np.random.exponential(1/lambda_failure)

    return times, cost_timeline

# --- Policy 2: Replace all bearings when any one fails ---
def policy2(failure_times):
    total_cost = 0
    current_time = 0
    failure_times = failure_times.copy()
    cost_timeline = []
    times = []

    while current_time < Tmax:
        next_failure_time = np.min(failure_times)
        if next_failure_time > Tmax:
            break
        current_time = next_failure_time
        total_cost += cost_per_bearing * N
        cost_timeline.append(total_cost)
        times.append(current_time)
        failure_times = current_time + np.random.exponential(1/lambda_failure, size=N)

    return times, cost_timeline

# Simulate initial failure times
initial_failures = generate_failure_times()

# Get cost timelines
times1, costs1 = policy1(initial_failures)
times2, costs2 = policy2(initial_failures)

# Print summary
print("Policy 1 (Replace individually):")
print(f"Total cost = {costs1[-1] if costs1 else 0}")
print("Policy 2 (Replace all when one fails):")
print(f"Total cost = {costs2[-1] if costs2 else 0}")

# --- Elegant Plot ---
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10,6))

# Plot step lines
ax.step(times1, costs1, where='post', label='Replace individually', linewidth=2, color='#1f77b4')
ax.step(times2, costs2, where='post', label='Replace all when one fails', linewidth=2, color='#ff7f0e')

ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Accumulated Cost', fontsize=14)
ax.set_title('Bearing Replacement Policy Cost Comparison', fontsize=16, weight='bold')
ax.legend(fontsize=12)
ax.grid(True, which='both', linestyle='--', alpha=0.6)

# Improve ticks and spines
ax.tick_params(axis='both', which='major', labelsize=12)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('gray')
    spine.set_linewidth(0.8)

plt.tight_layout()
plt.show()

# --- Animation showing bearing states for Policy 1 ---
fig, ax = plt.subplots(figsize=(8,3))
ax.set_xlim(0, Tmax)
ax.set_ylim(-1, N)
ax.set_yticks(np.arange(N))
ax.set_yticklabels([f'Bearing {i+1}' for i in range(N)])
ax.set_xlabel('Time', fontsize=12)
ax.set_title('Bearing States Over Time (Policy 1)', fontsize=14)

dots = ax.scatter([], [], s=200)

def build_timeline_policy1():
    failure_times = initial_failures.copy()
    events = []
    current_time = 0
    while current_time < Tmax:
        next_failure_time = np.min(failure_times)
        failed_bearing = np.argmin(failure_times)
        if next_failure_time > Tmax:
            break
        current_time = next_failure_time
        # Failed (red)
        events.append((current_time, failed_bearing, 0))
        # Replaced (blue) shortly after
        events.append((current_time + 0.5, failed_bearing, 1))
        failure_times[failed_bearing] = current_time + 0.5 + np.random.exponential(1/lambda_failure)
    return events

events = build_timeline_policy1()

frames = np.linspace(0, Tmax, 400)
bearing_states = np.ones((len(frames), N))  # all working initially

event_idx = 0
for i, t in enumerate(frames):
    while event_idx < len(events) and events[event_idx][0] <= t:
        _, bearing_ev, state_ev = events[event_idx]
        bearing_states[i:, bearing_ev] = state_ev
        event_idx += 1

def init_anim():
    dots.set_offsets([])
    return dots,

def update_anim(frame_idx):
    x = np.full(N, frames[frame_idx])
    y = np.arange(N)
    colors = ['#1f77b4' if s == 1 else '#d62728' for s in bearing_states[frame_idx]]  # blue/red
    dots.set_offsets(np.column_stack((x, y)))
    dots.set_color(colors)
    ax.set_title(f'Bearing States Over Time (Policy 1) - Time={frames[frame_idx]:.1f}', fontsize=14)
    return dots,

ani = animation.FuncAnimation(fig, update_anim, frames=len(frames),
                              init_func=init_anim, interval=50, blit=True, repeat=False)

plt.show()

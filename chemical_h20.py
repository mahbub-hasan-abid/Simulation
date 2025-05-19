import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial concentrations (in arbitrary units)
H2_0 = 2.0
O2_0 = 1.0
H2O_0 = 0.0

# Reaction rate constant
k = 0.5

# Time settings
t_max = 10
dt = 0.05
time_steps = int(t_max / dt)

# Arrays to store concentrations
H2 = np.zeros(time_steps)
O2 = np.zeros(time_steps)
H2O = np.zeros(time_steps)
time = np.linspace(0, t_max, time_steps)

# Initial concentrations
H2[0] = H2_0
O2[0] = O2_0
H2O[0] = H2O_0

# Reaction: 2 H2 + O2 -> 2 H2O
for i in range(1, time_steps):
    rate = k * (H2[i - 1] ** 2) * O2[i - 1]
    dH2 = -2 * rate * dt
    dO2 = -1 * rate * dt
    dH2O = 2 * rate * dt

    H2[i] = max(H2[i - 1] + dH2, 0)
    O2[i] = max(O2[i - 1] + dO2, 0)
    H2O[i] = H2O[i - 1] + dH2O

# Print data table in terminal
print(f"{'Time':>6} | {'H2':>8} | {'O2':>8} | {'H2O':>8}")
print("-" * 36)
for t, h2, o2, h2o in zip(time[::20], H2[::20], O2[::20], H2O[::20]):  # print every 20th for brevity
    print(f"{t:6.2f} | {h2:8.4f} | {o2:8.4f} | {h2o:8.4f}")

# Plotting animation
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, t_max)
ax.set_ylim(0, max(H2_0, O2_0) * 1.2)
ax.set_xlabel('Time')
ax.set_ylabel('Concentration')
ax.set_title('Simulation of H2 + O2 → H2O Reaction')

line_H2, = ax.plot([], [], label='H2', color='blue')
line_O2, = ax.plot([], [], label='O2', color='red')
line_H2O, = ax.plot([], [], label='H2O', color='green')

ax.legend()

def init():
    line_H2.set_data([], [])
    line_O2.set_data([], [])
    line_H2O.set_data([], [])
    return line_H2, line_O2, line_H2O

def update(frame):
    line_H2.set_data(time[:frame], H2[:frame])
    line_O2.set_data(time[:frame], O2[:frame])
    line_H2O.set_data(time[:frame], H2O[:frame])
    return line_H2, line_O2, line_H2O

ani = animation.FuncAnimation(fig, update, frames=time_steps, init_func=init,
                              interval=50, blit=True, repeat=False)

plt.show()

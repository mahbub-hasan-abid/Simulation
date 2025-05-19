import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points in the chase
n_points = 3

# Labels for points
labels = ['A', 'B', 'C']

# Initial positions (x, y) of points in a line
positions = np.zeros((n_points, 2))
positions[:, 0] = np.arange(n_points)  # x-coords 0,1,2
positions[:, 1] = 0  # y-coords all zero initially

fig, ax = plt.subplots(figsize=(7, 4))
ax.set_xlim(-1, n_points + 6)
ax.set_ylim(-3, 3)
ax.set_title("Serial Chase Animation (A, B, C)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True, linestyle='--', alpha=0.5)

scatter = ax.scatter(positions[:, 0], positions[:, 1], c='red', s=100)

# Create text objects for labels, positioned initially above points
texts = []
for i, label in enumerate(labels):
    txt = ax.text(positions[i, 0], positions[i, 1] + 0.3, label,
                  fontsize=12, fontweight='bold', ha='center', color='blue')
    texts.append(txt)

def update(frame):
    # Move leader point (A) in a sine wave path
    positions[0, 0] = frame * 0.1
    positions[0, 1] = np.sin(frame * 0.1)

    # Each follower moves towards the previous point
    for i in range(1, n_points):
        positions[i] += 0.1 * (positions[i - 1] - positions[i])

    # Update scatter plot points
    scatter.set_offsets(positions)

    # Update labels position
    for i, txt in enumerate(texts):
        txt.set_position((positions[i, 0], positions[i, 1] + 0.3))

    # Print positions to console
    print(f"Frame {frame}:")
    for i, pos in enumerate(positions):
        print(f"  {labels[i]}: x={pos[0]:.3f}, y={pos[1]:.3f}")
    print("-" * 30)

    return scatter, *texts

# Animate for 100 frames, then stop
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()

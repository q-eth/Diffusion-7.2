import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.stats import norm

def random_walk(N, steps, dh):
    positions = np.zeros(N)
    history = np.zeros((steps, N))
    
    for t in range(steps):
        steps_random = np.random.uniform(-dh, dh, N)  
        positions += steps_random  
        history[t] = positions
    
    return history

N = 2000
steps = 100
dh = 1.0
bins = 40

data = random_walk(N, steps, dh)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))
ax1.set_xlim(-20, 20)
ax1.set_ylim(0, N+1)
ax1.set_xlabel("X coordinate")
ax1.set_ylabel("Particles")
points, = ax1.plot([], [], 'ko', markersize=3)

ax2.set_xlabel("X coordinate")
ax2.set_ylabel("Frequency")
hist_data = ax2.hist([], bins=bins, density=True, alpha=0.5, color='#777777')[2]
gauss_line, = ax2.plot([], [], 'r', lw=2)

step_text = fig.text(0.5, 0.02, "", ha="center", fontsize=16)

def init():
    points.set_data([], [])
    for rect in hist_data:
        rect.set_height(0)
    gauss_line.set_data([], [])
    step_text.set_text("")
    return points, *hist_data, gauss_line, step_text

def update(frame):
    points.set_data(data[frame], np.arange(N)+1)

    ax2.cla()
    ax2.set_xlabel("X coordinate")
    ax2.set_ylabel("Frequency")
    counts, bins_edges, _ = ax2.hist(data[frame], bins=bins, density=True, alpha=0.5, color='#777777')

    mean = np.mean(data[frame])
    std_dev = np.std(data[frame])

    x_vals = np.linspace(np.min(data), np.max(data), 100)
    y_vals = norm.pdf(x_vals, mean, std_dev)
    ax2.set_xlim(-20, 20)
    ax2.set_ylim(0, 1)
    ax2.plot(x_vals, y_vals, 'r', lw=2)

    step_text.set_text(f"Step: {frame+1}/{steps}")
    
    return points, step_text

ani = animation.FuncAnimation(fig, update, frames=steps, init_func=init, interval=10, blit=False)
plt.show()

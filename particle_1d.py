#For Brownian motion increments ΔW = W(t + Δt) - W(t) 
# are independent and zero mean with var proportional to Δt

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


np.random.seed(189)
N = 1000
dt = 0.01
stdev = dt**0.5


#generate normal increments N(0, sqrt(dt))
inc = np.random.randn(N) * stdev
W = np.insert(np.cumsum(inc), 0, 0)
# Create time array corresponding to the increments
t = np.linspace(0, N*dt, N+1)


fig, ax = plt.subplots()
ax.set_xlim(t[0], t[-1])
ax.set_ylim(W.min() - 1, W.max() + 1)
ax.set_xlabel('Time')
ax.set_ylabel('Position')

# Line for the path and point for the particle
line, = ax.plot([], [], lw=2, label='Path')
point, = ax.plot([], [], 'ro', label='Brownian particle')
ax.legend()

time = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12,
                    verticalalignment='top')

def init():
    line.set_data([], [])
    point.set_data([], [])
    time.set_text('')
    return line, point, time
def update(frame):
    line.set_data(t[:frame+1], W[:frame+1])
    point.set_data([t[frame]], [W[frame]])
    time.set_text(f"W: {round(W[frame],1)}\nTime: {frame*dt:.2f}")
    return line, point, time

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1, N+1), init_func=init,
                    blit=True, interval=20, repeat=False)

plt.show()
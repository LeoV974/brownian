#For Brownian motion increments ΔW = W(t + Δt) - W(t) 
# are independent and zero mean with var proportional to Δt

#now in 3d case need x,y,z increments and we plot x,y,z

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


np.random.seed(189)
N = 1000
dt = 0.01
stdev = dt**0.5


#generate normal increments N(0, sqrt(dt))
inc_x = np.random.randn(N) * stdev
inc_y = np.random.randn(N) * stdev
inc_z = np.random.randn(N) * stdev
W_x = np.insert(np.cumsum(inc_x), 0, 0)
W_y = np.insert(np.cumsum(inc_y), 0, 0)
W_z = np.insert(np.cumsum(inc_z), 0, 0)

# Create time array corresponding to the increments
t = np.linspace(0, N*dt, N+1)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim(W_x.min() - 1, W_x.max() + 1)
ax.set_ylim(W_y.min() - 1, W_y.max() + 1)
ax.set_zlim(W_z.min() - 1, W_z.max() + 1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Brownian Motion of a Single Particle')

# Line for the path and point for the particle
line, = ax.plot([], [], [], lw=2, label='Path')
point, = ax.plot([], [], [], 'ro', label='Brownian particle')
ax.legend()

time = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=12,
                    verticalalignment='top')

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    time.set_text('')
    return line, point, time

#only show last tail points in the line
def update(frame):
    tail = 20
    lowerbd = max(0, frame - tail)
    line.set_data(W_x[lowerbd:frame+1], W_y[lowerbd:frame+1])
    line.set_3d_properties(W_z[lowerbd:frame+1])
    point.set_data([W_x[frame]], [W_y[frame]])
    point.set_3d_properties(W_z[frame])
    
    time.set_text(f"(x,y,z): {round(W_x[frame], 1), round(W_y[frame], 1), round(W_z[frame], 1)}\nTime: {frame*dt:.2f}")
    return line, point, time

ani = FuncAnimation(fig, update, frames=range(1, N+1), init_func=init,
                    blit=False, interval=20, repeat=False)

plt.show()
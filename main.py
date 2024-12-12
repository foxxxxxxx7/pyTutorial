import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Lorenz system parameters
sigma = 10
rho = 28
beta = 8 / 3

# Time parameters
dt = 0.01
num_steps = 5000

# Initialize arrays
x = np.empty(num_steps)
y = np.empty(num_steps)
z = np.empty(num_steps)

# Initial conditions
x[0], y[0], z[0] = (0.1, 0.0, 0.0)

# Solve the Lorenz system
for i in range(1, num_steps):
    dx = sigma * (y[i-1] - x[i-1]) * dt
    dy = (x[i-1] * (rho - z[i-1]) - y[i-1]) * dt
    dz = (x[i-1] * y[i-1] - beta * z[i-1]) * dt
    x[i] = x[i-1] + dx
    y[i] = y[i-1] + dy
    z[i] = z[i-1] + dz

# Set up the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the line
line, = ax.plot([], [], [], lw=0.5)
ax.set_xlim(-20, 20)
ax.set_ylim(-30, 30)
ax.set_zlim(0, 50)

# Initialize function
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Update function
def update(frame):
    step = 100  # Number of points to show
    line.set_data(x[frame:frame + step], y[frame:frame + step])
    line.set_3d_properties(z[frame:frame + step])
    return line,

# Animate
ani = FuncAnimation(fig, update, frames=range(0, num_steps - 100, 10), init_func=init, blit=True)

# Display the animation
plt.show()

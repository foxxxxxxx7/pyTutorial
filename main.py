import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def initialize_grid(size, random_fill=True):
    """
    Initializes the grid with a specified size.
    If random_fill is True, randomize the grid; otherwise, create an empty grid.
    """
    if random_fill:
        return np.random.choice([0, 1], size=(size, size))
    return np.zeros((size, size), dtype=int)

def update_grid(grid, ruleset):
    """
    Updates the grid based on user-defined ruleset.
    - A ruleset is a function that defines the next state of a cell.
    """
    new_grid = grid.copy()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            neighbors = grid[max(x-1, 0):x+2, max(y-1, 0):y+2]
            new_grid[x, y] = ruleset(grid[x, y], neighbors.sum() - grid[x, y])
    return new_grid

def game_of_life_rules(current_state, live_neighbors):
    """
    Classic Conway's Game of Life ruleset.
    """
    if current_state == 1 and live_neighbors in (2, 3):
        return 1
    elif current_state == 0 and live_neighbors == 3:
        return 1
    return 0

# Simulation parameters
grid_size = 50
frames = 100
interval = 100  # milliseconds

# Initialize the grid
grid = initialize_grid(grid_size, random_fill=True)

# Set up the plot
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap="binary")
ax.axis('off')

def animate(frame):
    global grid
    grid = update_grid(grid, game_of_life_rules)
    im.set_array(grid)
    return [im]

# Create the animation
ani = FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True)

# Display the animation
plt.title("Cellular Automaton Simulator")
plt.show()

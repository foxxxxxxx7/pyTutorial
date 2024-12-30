import random
import matplotlib.pyplot as plt
import numpy as np


def random_walk_simulation(grid_size=20, steps=1000, initial_life=100, food_probability=0.02):
    # Initialize the grid and variables
    grid = np.zeros((grid_size, grid_size), dtype=int)
    x, y = grid_size // 2, grid_size // 2  # Start in the center
    life = initial_life
    path = [(x, y)]

    # Generate random "food" on the grid
    for _ in range(int(grid_size * grid_size * food_probability)):
        fx, fy = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        grid[fx, fy] = 1  # 1 represents food

    # Simulate random walk
    for _ in range(steps):
        if life <= 0:
            break

        # Random step: up, down, left, or right
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x, y = (x + dx) % grid_size, (y + dy) % grid_size  # Wrap around edges
        path.append((x, y))

        # Check if the particle lands on food
        if grid[x, y] == 1:
            life += 20  # Replenish life
            grid[x, y] = 0  # Food is consumed
        else:
            life -= 1  # Decrease life

    return path, grid


def plot_random_walk(path, grid):
    grid_size = grid.shape[0]
    path_x, path_y = zip(*path)

    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap='Greens', extent=(0, grid_size, 0, grid_size))
    plt.plot(path_x, path_y, color='blue', linewidth=1, label='Path')
    plt.scatter(path_x[-1], path_y[-1], color='red', label='End Point')
    plt.title("Random Walk Simulation")
    plt.legend()
    plt.show()


# Run the simulation
path, grid = random_walk_simulation(grid_size=30, steps=500, initial_life=200, food_probability=0.05)
plot_random_walk(path, grid)

import random
import time
import os

def initialize_grid(rows, cols, fill_probability=0.2):
    """Creates a grid with random live (1) or dead (0) cells."""
    return [
        [1 if random.random() < fill_probability else 0 for _ in range(cols)]
        for _ in range(rows)
    ]

def print_grid(grid):
    """Prints the grid to the terminal."""
    os.system("cls" if os.name == "nt" else "clear")
    for row in grid:
        print("".join("█" if cell else " " for cell in row))

def count_neighbors(grid, x, y):
    """Counts the number of live neighbors for a given cell."""
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            count += grid[nx][ny]
    return count

def next_generation(grid):
    """Calculates the next generation of the grid."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            alive_neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1 and (alive_neighbors == 2 or alive_neighbors == 3):
                new_grid[x][y] = 1  # Cell survives
            elif grid[x][y] == 0 and alive_neighbors == 3:
                new_grid[x][y] = 1  # Cell is born
    return new_grid

def game_of_life(rows=20, cols=40, generations=50, speed=0.2):
    """Runs Conway's Game of Life."""
    grid = initialize_grid(rows, cols)
    for _ in range(generations):
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(speed)

# Run the simulation
game_of_life(rows=20, cols=40, generations=100, speed=0.1)

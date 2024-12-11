import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_ulam_spiral(size):
    grid = np.zeros((size, size), dtype=bool)
    x, y = size // 2, size // 2  # Start in the middle
    dx, dy = 0, -1
    for i in range(1, size**2 + 1):
        if is_prime(i):
            grid[y, x] = True
        # Change direction at corners
        if (x == y or (x > y and x + y == size - 1) or (x < y and x + y == size - 1)):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return grid

def plot_ulam_spiral(grid):
    plt.figure(figsize=(8, 8))
    plt.imshow(grid, cmap="binary", interpolation="nearest")
    plt.axis("off")
    plt.title("Ulam Spiral of Prime Numbers")
    plt.show()

size = 101  # Adjust grid size (odd numbers work best)
grid = generate_ulam_spiral(size)
plot_ulam_spiral(grid)

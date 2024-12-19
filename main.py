import random


def generate_maze(size, fortune):
    """
    Generates a square maze of given size with walls (#), empty spaces ( ),
    and a fortune (F) hidden in one of the empty spaces.
    """
    maze = [["#" for _ in range(size)] for _ in range(size)]

    # Create random paths
    for _ in range(size * size // 2):  # Approx. 50% open paths
        x, y = random.randint(1, size - 2), random.randint(1, size - 2)
        maze[x][y] = " "

    # Add the fortune to a random empty space
    while True:
        fx, fy = random.randint(1, size - 2), random.randint(1, size - 2)
        if maze[fx][fy] == " ":
            maze[fx][fy] = "F"
            break

    return maze, (fx, fy)


def print_maze(maze, player_pos):
    """
    Displays the maze in the terminal with the player's position (P).
    """
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                print("P", end="")
            else:
                print(cell, end="")
        print()


def move_player(maze, player_pos, direction):
    """
    Moves the player in the maze if the move is valid.
    """
    x, y = player_pos
    if direction == "w":  # Up
        new_pos = (x - 1, y)
    elif direction == "s":  # Down
        new_pos = (x + 1, y)
    elif direction == "a":  # Left
        new_pos = (x, y - 1)
    elif direction == "d":  # Right
        new_pos = (x, y + 1)
    else:
        return player_pos, "Invalid direction!"

    nx, ny = new_pos
    if maze[nx][ny] == "#":
        return player_pos, "You hit a wall!"
    return new_pos, "Moved!"


def play_maze_game():
    """
    Main function to play the maze game.
    """
    size = 10  # Maze size
    fortune = "You will achieve greatness!"  # The hidden message
    maze, fortune_pos = generate_maze(size, fortune)

    player_pos = (1, 1)  # Starting position
    maze[1][1] = " "  # Ensure the starting position is open

    print("Welcome to the Fortune Maze!")
    print("Navigate using 'w', 'a', 's', 'd' to find your hidden fortune!")
    print("Type 'quit' to exit.\n")

    while player_pos != fortune_pos:
        print_maze(maze, player_pos)
        move = input("Your move: ").strip().lower()
        if move == "quit":
            print("Thanks for playing!")
            break
        player_pos, message = move_player(maze, player_pos, move)
        print(message)

    if player_pos == fortune_pos:
        print("\nCongratulations! You've found the fortune:")
        print(f"-> {fortune} <-")
        print("\nGame Over!")


# Start the game
play_maze_game()

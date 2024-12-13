import turtle

def draw_branch(t, branch_length, angle, depth):
    """
    Recursively draws a fractal tree.

    Parameters:
    t (Turtle): The turtle object.
    branch_length (int): Length of the current branch.
    angle (int): Angle between branches.
    depth (int): Current recursion depth.
    """
    if depth == 0:
        return

    # Draw the main branch
    t.forward(branch_length)

    # Draw the left subtree
    t.left(angle)
    draw_branch(t, branch_length * 0.7, angle, depth - 1)
    t.right(angle * 2)

    # Draw the right subtree
    draw_branch(t, branch_length * 0.7, angle, depth - 1)
    t.left(angle)

    # Go back to the original position
    t.backward(branch_length)

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fractal Tree")

tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)  # Fastest speed
tree.left(90)  # Start pointing upwards
tree.penup()
tree.goto(0, -200)  # Move to the starting position
tree.pendown()

# Parameters for the fractal tree
initial_branch_length = 100
branch_angle = 30
recursion_depth = 8

# Draw the fractal tree
draw_branch(tree, initial_branch_length, branch_angle, recursion_depth)

# Keep the screen open
screen.mainloop()

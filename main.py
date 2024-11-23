import turtle
import random

def random_color():
    """Generate a random color in RGB format."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def random_shape(t):
    """Draw a random shape on the canvas."""
    shapes = ["circle", "square", "triangle"]
    shape = random.choice(shapes)

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    size = random.randint(20, 100)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(random_color())

    t.begin_fill()
    if shape == "circle":
        t.circle(size // 2)
    elif shape == "square":
        for _ in range(4):
            t.forward(size)
            t.right(90)
    elif shape == "triangle":
        for _ in range(3):
            t.forward(size)
            t.right(120)
    t.end_fill()

def generate_art(num_shapes):
    """Generate the random art on the canvas."""
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.colormode(255)

    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()

    for _ in range(num_shapes):
        random_shape(t)

    print("Artwork generated! Close the window to finish.")
    screen.mainloop()

def main():
    print("Welcome to the Random Art Generator!")
    try:
        num_shapes = int(input("Enter the number of shapes to draw (e.g., 50): "))
        if num_shapes <= 0:
            print("Please enter a positive number.")
        else:
            generate_art(num_shapes)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

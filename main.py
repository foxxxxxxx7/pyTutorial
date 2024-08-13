import random
from tkinter import *

GAME_WIDTH = 700
GAME_HEIGHT = 550
SPEED = 50
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#0000FF"
FOOD_COLOR = "#00FF00"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = [canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                        for x, y in self.coordinates]

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    x += direction == "right" and SPACE_SIZE or direction == "left" and -SPACE_SIZE
    y += direction == "down" and SPACE_SIZE or direction == "up" and -SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    snake.squares.insert(0, canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR))

    if snake.coordinates[0] == food.coordinates:
        global score
        score += 1
        label.config(text=f"Score:{score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares.pop())

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    opposites = {"left": "right", "right": "left", "up": "down", "down": "up"}
    if direction != opposites[new_direction]:
        direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    return (x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT or
            any([x, y] == body for body in snake.coordinates[1:]))

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=("Impact", 100), text="GAME OVER",
                       fill="red", tag="game over")

window = Tk()
window.title("Snake")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=f"Score:{score}", font=("Impact", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window.geometry(f'{window.winfo_width()}x{window.winfo_height()}+{(window.winfo_screenwidth() - window.winfo_width()) // 2}+{(window.winfo_screenheight() - window.winfo_height()) // 2}')

# Fixing key bindings
for key, dir in zip(["<Left>", "<a>", "<A>", "<Right>", "<d>", "<D>", "<Up>", "<w>", "<W>", "<Down>", "<s>", "<S>"],
                    ["left", "left", "left", "right", "right", "right", "up", "up", "up", "down", "down", "down"]):
    window.bind(key, lambda event, d=dir: change_direction(d))

snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()

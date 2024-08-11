from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and not check_winner():
        buttons[row][column]["text"] = player

        if check_winner():
            label.config(text=f"{player} wins")
        elif not empty_spaces():
            label.config(text="Tie")
            color_all_buttons("yellow")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} turn")

def check_winner():
    for trio in winning_combos:
        if buttons[trio[0]][trio[1]]["text"] == buttons[trio[2]][trio[3]]["text"] == buttons[trio[4]][trio[5]]["text"] != "":
            for i in range(0, 6, 2):
                buttons[trio[i]][trio[i+1]].config(bg="green")
            return True
    return False

def empty_spaces():
    return any(buttons[row][column]["text"] == "" for row in range(3) for column in range(3))

def color_all_buttons(color):
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(bg=color)

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player} turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0] * 3 for _ in range(3)]

label = Label(text=f"{player} turn", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="Reset", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

winning_combos = [
    (0, 0, 0, 1, 0, 2), (1, 0, 1, 1, 1, 2), (2, 0, 2, 1, 2, 2),  # rows
    (0, 0, 1, 0, 2, 0), (0, 1, 1, 1, 2, 1), (0, 2, 1, 2, 2, 2),  # columns
    (0, 0, 1, 1, 2, 2), (0, 2, 1, 1, 2, 0)  # diagonals
]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

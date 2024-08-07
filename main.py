from tkinter import *

class CalculatorButton(Button):
    def __init__(self, parent, text, row, column, command, width=9, height=4, font=35):
        super().__init__(parent, text=text, width=width, height=height, font=font, command=command)
        self.grid(row=row, column=column)

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Divide by Zero? eh?")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas", 20), bg="light grey", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('/', 3, 3),
]

for (text, row, column) in buttons:
    if text == '=':
        CalculatorButton(frame, text, row, column, command=equals)
    else:
        CalculatorButton(frame, text, row, column, command=lambda t=text: button_press(t))

button_clear = Button(window, text="Clear", height=4, width=19, font=35, command=clear)
button_clear.pack()

window.mainloop()

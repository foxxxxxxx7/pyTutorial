import os
from tkinter import *
from tkinter import filedialog, colorchooser, font, messagebox


def change_colour():
    colour = colorchooser.askcolor(title="Choose your colour")[1]
    if colour:
        text_area.config(fg=colour)


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            window.title(os.path.basename(file_path))
            text_area.delete(1.0, END)
            text_area.insert(1.0, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt",
                                             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            window.title(os.path.basename(file_path))
            file.write(text_area.get(1.0, END))


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    messagebox.showinfo("About this program", "This is a simple text editor")


def quit():
    window.destroy()


# Initialize the main window
window = Tk()
window.title("Text Editor")

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

font_name = StringVar(value="Arial")
font_size = StringVar(value="25")

# Text area setup
text_area = Text(window, font=(font_name.get(), font_size.get()))
text_area.grid(sticky=N + E + S + W)

# Scrollbar setup
scroll_bar = Scrollbar(text_area, command=text_area.yview)
text_area.config(yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)

# Toolbar setup
frame = Frame(window)
frame.grid()

Button(frame, text="Color", command=change_colour).grid(row=0, column=0)
OptionMenu(frame, font_name, *font.families(), command=change_font).grid(row=0, column=1)
Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font).grid(row=0, column=2)

# Menu setup
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()

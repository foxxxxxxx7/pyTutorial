from random import choice, randint
from string import ascii_uppercase as letters

names = set()

def create_name():
    while True:
        name = f"{choice(letters)}{choice(letters)}{str(randint(100, 999))}"
        if name not in names:
            names.add(name)
            return name

class Robot:
    def __init__(self):
        self.name = create_name()

    def reset(self):
        names.discard(self.name)
        new_name = create_name()
        if new_name == self.name:
            new_name = create_name()
        self.name = new_name
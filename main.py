import random, string
from random import randint
letters = string.ascii_uppercase
class Robot:
    def __init__(self):
        self.generateName()
    def generateName(self):
        random.seed()
        name = ''
        name += random.choice(letters)
        name += random.choice(letters)
        name += str(randint(100,999))
        self.name = name
    def reset(self):
        self.generateName()
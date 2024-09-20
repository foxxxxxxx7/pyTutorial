from random import randint
def modifier(constitution_stat):
    return (constitution_stat - 10)//2
class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
    def ability(self):
        dices = [randint(1, 6) for i in range(4)]
        return sum(dices) - min(dices)
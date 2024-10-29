class Allergies:
    ALLERGENS = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        item_score = self.ALLERGENS.get(item, 0)
        return (self.score & item_score) != 0

    @property
    def lst(self):
        allergies_list = []

        for item, item_score in self.ALLERGENS.items():
            if (self.score & item_score) != 0:
                allergies_list.append(item)

        return allergies_list

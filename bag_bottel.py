import random
class Bag():
    def __init__(self):
        self.number_bottle = 0

    def bottle_selection(self, new_bottle):
        new_bottle = random.randrange(0, 99)
        self.number_bottle += new_bottle

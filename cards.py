import random
from bag_bottel import Bag
number = Bag()
class Card():
    def __init__(self):
        self.ranks_num = 0
        self.card = 0

    def separator(self, sep):
        sep = print('*' * 23)
        return sep
    def ranks(self, numbers):
        for i in range(3):
            numbers = random.sample(range(99), 5)
            numbers.sort()
            self.ranks_num = print('   '.join(map(str, numbers)))




# if __name__=='__main__':

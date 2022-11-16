from cards import Card
from bag_bottel import Bag
from functools import reduce
new_card = Card()
new_card1 = Card()
new_bottle1 = Bag()
print('Начать игру')
choice = input('Введите Y/N:  ')
if choice == 'Y':
    print('выберите игру: компьютер или человек')
    choice_game = input('если компьютер, то 1, если человек, то 2: ')
    if choice_game == '1':
        print('Карточка игрока:')
        new_card.separator(1)
        new_card.ranks(1)
        print(new_card.ranks_num)
        new_card.separator(1)
        print('Компьютерная карточка')
        new_card.separator(1)
        new_card1.ranks(1)
        print(new_card1.ranks_num)
        new_card.separator(1)
        new_bottle1.bottle_selection(1)
        print('Бочонок с номером из мешка:')
        print(new_bottle1.number_bottle)
        new_card1 = reduce(lambda x, y: '-'if (x == str(new_bottle1)) else y, new_card1)
        print(new_card1)
    else:
        choice_game == '2'
        print('Сыграем')

else:
    choice == 'N'
    print('до встречи!')
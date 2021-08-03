import random

class uno_player:
    def __init__(self,name):
        self.name = name
        self.level = 7
        self.cards = []
    def get_cards(self):
        if self.level == 7:
            for i in range(7):
                self.cards.append(deck.pop())
    def add_to_dump(self):
        dump_pile.append(self.cards.pop())


def cards(color): 
    card = []
    for i in range(0,10):
        card.append(f'{color} {i}')
    for i in range(1,10):
        card.append(f'{color} {i}')
    for i in range(2):
        card.append(f'{color} DRAW 2')
        card.append(f'{color} REVERSE')
        card.append(f'{color} SKIP')
    return card


def decks():
    color = ['RED', 'BLUE', 'YELLOW', 'GREEN']
    decklist = []
    for i in range(4):
        color[i] = cards(color[i])
        for x in range(len(color[i])):
            decklist.append(color[i][x])
    for i in range(4):
        decklist.append('WILD')
        decklist.append('WILD DRAW 4')
    random.shuffle(decklist)
    return decklist
    
def add_player():
    peoples = {} 
    while True:        
        names = input("what is your name? ") 
        peoples[names] = uno_player(names)
        while True:
            continues = input("do you want to add another person? (yes/no) ")
            if continues == 'yes':
                names = input("what is your name? ") 
                if names in peoples:
                    print('plz try another name that name is already taken')
                    continue
                else:
                    peoples[names] = uno_player(names)
                    continue
            else: break
        break
    return peoples
if __name__ == '__main__': 
    peoples = add_player()
    dump_pile = []
    deck = decks()
    while True:
        if len(deck) == 3:
            for i in range(len(dump_pile)):
                deck.append(dump_pile.pop())
        names = input("what is your name? ")
        print('deck',len(deck))
        print('dump_pille',len(dump_pile))
        if names not in peoples:
            print(f'{names} is not a valid name')
            if len(peoples) == 1:
                print('this is a valid name')
            else:
                print('these are all  names:')
            for i in peoples:
                print(i)
            continue
        if len(peoples[names].cards) == 0:
            if peoples[names].level == 7:
                peoples[names].get_cards()
        peoples[names].add_to_dump()
        print(peoples[names].cards)
        amountcard = []
        for i in peoples:
            amountcard.append(len(peoples[i].cards))
        amountcard.append(len(deck))
        amountcard.append(len(dump_pile))
        sums = sum(amountcard)
        if sums == 108:
            del amountcard
        else:
            print('incorrect amount of cards')
        print('sum',sums)
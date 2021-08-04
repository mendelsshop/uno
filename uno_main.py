import random

class uno_player:
    def __init__(self,name,age):
        self.name = name
        self.level = 7
        self.cards = []
        self.age = age
    def get_cards(self):
        if self.level == 7:
            for i in range(7):
                self.cards.append(deck.pop())
        elif self.level == 6:
            for i in range(6):
                self.cards.append(deck.pop())
    def add_to_dump(self,x):
        dump_pile.append(self.cards.pop(x))
    def __str__(self):
        return self.name

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
    playeramount = 1

    while True:
            if playeramount >= 3:
                continues = input("do you want to add another person? (yes/no) ")
                if continues == 'yes':
                    pass
                else:
                    break
            while True:
                names = input(f"player {playeramount} what is your name? ")   
                if names in peoples:
                    print('plz try another name that name is already taken')
                    continue
                break
            while True:
                age = input(f'player {playeramount} what is your age? ')
                try:
                    age = int(age)
                except:
                    print('what you entered for age is not an number please try again')
                    continue
                break
            peoples[names] = uno_player(names,age) 
            playeramount += 1
    return peoples
if __name__ == '__main__': 
    peoples = add_player()
    dump_pile = []
    deck = decks()


    while True:
        if len(deck) == 1:
            for i in range(len(dump_pile)):
                deck.append(dump_pile.pop())
        ages = {}
        for i in peoples:
            ages[peoples[i].name] = (peoples[i].age)
        ages = sorted(ages.items(),key=lambda x: x[1] )
        for i in range(len(ages)):
            names = str(peoples[ages[i][0]])
            name = peoples[names]
            print(f'{name.name}\'s turn')
            if len(name.cards) == 0:
                    name.get_cards()
                    name.level = name.level - 1
            cardss = {}
            for z in range(len(name.cards)):
                cardss[z] = (name.cards[z])


            print(cardss)

            x = int(input())
            for z in cardss.keys():
                if z == x:
                    print(f'removing {name.cards[x]}..')
                    name.add_to_dump(x)
            del cardss

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
        
    

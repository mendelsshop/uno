import random
# stuff to do
# add funtions to cards when their called 
# add the function that are not in class to game class
# add stuff from if __name__ == '__main__': to main method in game class
# clean up code
# make nicer variables
# use comments and docstring to describe whats going on
# add clear function(s)
# create leader board for games
# in game split each card into 2 catagories color and function
def make_car_longer(cardname,card_length, space_length):
    if  card_length == space_length:
        pass
    else:
        sum_len_blank = space_length - card_length
        left_pad = sum_len_blank % 2
        if left_pad != 0:
            left_pad = (sum_len_blank // 2) + 1
        else:
            left_pad = sum_len_blank / 2
        right_pad = sum_len_blank // 2
    blank = '' 
    extended_name = f'|{blank: <{right_pad}}{cardname}{blank: >{left_pad}}| '
    return extended_name
    
        
def cardify(card):
    '''a funnction to display a(n) uno card(s)'''
    z = len(card)
    blanks = len('                ')
    for q in range(z):
        print(' ________________  ', end = '')
    print()
    for q in range(z):
        print('/                \\ ',end = '')    
    print()
    for q in range(z):
        print('|                | ', end = '')    
    print()
    for q in range(z):
        print('|                | ', end = '')
    print()
    for x in range(z):
        len_of_cards = len(card[x])
        crds_extended = make_car_longer(cardname = card[x], card_length = len_of_cards,space_length = blanks)
        print(crds_extended,end='')
    print()    
    for card in range(z):
        print('|                | ', end = '')  
    print()  
    for card in range(z):
        print('|                | ', end = '')
    print()
    for card in range(z):
        print('\________________/ ',end='')
    print()
    for card in range(z):
        z = card
        print('','option:',z,'        ',end='')
    print()
def cardify1(card):
    '''a funnction to display a(n) uno card(s)'''
    z = 1
    blanks = len('                ')
    for q in range(z):
        print('   ________________  ', end = '')
    print()
    for q in range(z):
        print('  /                \\ ',end = '')    
    print()
    for q in range(z):
        print(' _|                | ', end = '')    
    print()
    for q in range(z):
        print('/ |                | ', end = '')
    print()
    for x in range(z):
        len_of_cards = len(card)
        crds_extended = make_car_longer(cardname = card, card_length = len_of_cards,space_length = blanks)
        print('|',crds_extended,end='')
    print()    
    for card in range(z):
        print('| |                | ', end = '')  
    print()  
    for card in range(z):
        print('| |                | ', end = '')
    print()
    for card in range(z):
        print('| \________________/ ',end='')
    print()
    for card in range(z):
        print('|                |  ',end='')
    print()
    for card in range(z):
        print('\________________/ ',end='')
    print()
class uno_player:
    def __init__(self,name,age):
        self.name = name
        self.level = 7
        self.cards = []
        self.age = age
    def draw_card(self):
        self.cards.append(deck.pop())
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
        if len(dump_pile) == 0:
            dump_pile.append(deck.pop())
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
            if len(name.cards) == 0:
                    name.get_cards()
                    name.level = name.level - 1
            turns = 0
            while True:

                print(f'{name.name}\'s turn')

                exit = False
                good = False
                cardss = {}
                cardsss = []
                for z in range(len(name.cards)):
                    cardss[z] = (name.cards[z])
                    cardsss.append(name.cards[z])
                len_of_dump_pile = len(dump_pile)
                len_of_dump_piles = len_of_dump_pile -1 
                tpdp = dump_pile[len_of_dump_piles].split(' ',1)
                print(dump_pile[len_of_dump_piles])
                if len(tpdp) == 1:
                    tpdp.append("WILD")
                c_color = tpdp[0]
                c_func_number = tpdp[1]
                for i in range(10):
                    if turns >= 1:
                        try:
                            int(c_func_number)
                            exit = True
                        except :
                            pass
                    break
                if exit == True:
                    break
                cardify1(dump_pile[len_of_dump_piles])
                cardify(cardsss)
                x = int(input('enter an option: '))
                if x == len(name.cards):
                    del cardsss
                    del cardss
                    cardss = {}
                    cardsss = []
                    for z in range(len(name.cards)):
                        cardss[z] = (name.cards[z])
                        cardsss.append(name.cards[z])
                    name.draw_card()
                    cardify(cardsss)
                    break
                    
                for z in range(len(name.cards)):
                    if z == x:  
                        crdslcd = name.cards[x].split(' ',1)
                        n_color = crdslcd[0]
                        
                        if len(crdslcd) == 1:
                            crdslcd.append("WILD")
                        n_func_number = crdslcd[1]
                        if c_color == n_color:
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)
                            del cardsss
                            del cardss
                            good = True
                        elif c_func_number == n_func_number:
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)
                            del cardsss
                            del cardss
                            good = True
                        elif name.cards[x] == 'WILD' or name.cards[x] == "WILD DRAW 4":
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)
                            del cardsss
                            del cardss
                            good = True
                        
                        elif dump_pile[len_of_dump_piles] == name.cards[x]:
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)
                            del cardsss
                            del cardss
                            good = True
                            

                        elif dump_pile[len_of_dump_piles] == 'WILD' or dump_pile[len_of_dump_piles] == 'WILD DRAW 4':
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)  
                            del cardsss
                            del cardss
                            good = True
                        break
              

                    elif z != x:
                        good = False
                if not good:
                    print('invalid option please try a different card or pick another card')
                else:
                    turns += 1

            del cardss
            del cardsss
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
        
    

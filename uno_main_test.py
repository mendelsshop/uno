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
def make_car_longer(cardname,card_length, space_length):
    ''''
    this function extends the length of string to match the length of another string
    '''
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
    # not the best way to do this needs to be improved for smaller dispalys
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
    '''a funnction to display an uno cards'''
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
        self.num_of_cards = 0
        self.age = age
    def draw_cards(self,times):
        '''pop a card from the deck and add it to the players cards'''
        for i in range(times):
            self.cards.append(deck.pop())
    def get_cards(self):
        '''
        similar to draw_card but draws cards based on the level of the player'''
        z = self.level
        for i in range(z):
            self.cards.append(deck.pop())
    def add_to_dump(self,x):
        '''remove a card from the player and add it to the dump_pile'''
        dump_pile.append(self.cards.pop(x))
    def __str__(self):
        '''return a string representation of the player'''
        return self.name

def cards(color): 
    '''a function that returns 1 color set of cards'''
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
    '''a function that returns a list of the uno cards uses the cards function and a for loop to generate most of the cards 
    besides for the wild cards which are appended to the list and then shuffles the list
    '''
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
    '''
    a function that adds 2 players from the uno_player class and then asks if you want to add more players
    '''
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
        '''
        this loop make sure that there is something in dump_pile(so that we can compare it to players card) make sure that there is something in deck so players can pick cards
        sorts palyers by age to choose which player starts
        '''
        if len(dump_pile) == 0:
            dump_pile.append(deck.pop())
        if len(deck) == 1:
            for i in range(len(dump_pile)):
                deck.append(dump_pile.pop())
        ages = {}
        for i in peoples:
            ages[peoples[i].name] = (peoples[i].age)
        ages = sorted(ages.items(),key=lambda x: x[1] ) #sorting ages in reverse so younest person starts
        for i in range(len(ages)):
            names = str(peoples[ages[i][0]])
            name = peoples[names]
            try:
                player_num = str(peoples[ages[i+1][0]])
            except:
                player_num = str(peoples[ages[0][0]])
            if name.num_of_cards == 0:
                    name.get_cards()
                    name.level = name.level - 1
            turns = 0
            while True:
                '''
                this is the loop for each players turn first we add the player players cards to a list and a and a dictinary 
                then we find the top card of dump_pile and split it into a list of color and function
                next we check if the player already put a card down if the player a number down we goto the next player or else we continue
                then we use cardify1 to show the top of dump_pile and cardify to show the players cards
                then ask the player to choose a card from their deck(the card that they want add to the dump_pile)
                from know on when the docstring says playercard it means the card that the player selected in the above input
                first we check if the player wants to pick a card from the deck by inputing the number above the amount of cards the player has 
                then we check if the players input matches any index of the the list of the player's card's
                if it does we split playcard into a list color and function
                then we check if the playcard color is the same as the top dump_piles color then we add playcard to dump_pile
                same if playcard function and top of dump_piles functon the same
                '''
                

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
                print(f'{name.name}\'s turn')
                cardify1(dump_pile[len_of_dump_piles])
                cardify(cardsss)
                x = int(input('enter an option: '))
                if x == len(name.cards):
                    del cardsss
                    del cardss
                    cardss = {}
                    cardsss = []
                    name.draw_cards(1)
                    for z in range(len(name.cards)):
                        cardss[z] = (name.cards[z])
                        cardsss.append(name.cards[z])
                    cardify(cardsss)
                    if len(name.cards) > 0:
                        name.num_of_cards = 1
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
                            c_func_number = n_func_number
                            good = True
                        elif c_func_number == n_func_number:
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)
                            del cardsss
                            del cardss
                            c_func_number = n_func_number
                            good = True
                        elif name.cards[x] == 'WILD' or name.cards[x] == "WILD DRAW 4":
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)
                            del cardsss
                            del cardss
                            c_func_number = n_func_number
                            good = True
                        
                        elif dump_pile[len_of_dump_piles] == name.cards[x]:
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)
                            del cardsss
                            del cardss
                            c_func_number = n_func_number
                            good = True
                            

                        elif dump_pile[len_of_dump_piles] == 'WILD' or dump_pile[len_of_dump_piles] == 'WILD DRAW 4':
                            print(f'removing {name.cards[x]}..')
                            name.add_to_dump(x)  
                            del cardsss
                            del cardss
                            c_func_number = n_func_number
                            good = True
                        break
              

                    elif z != x:
                        good = False
                if len(name.cards) > 0:
                    name.num_of_cards = 1
                if not good:
                    print('invalid option please try a different card or pick another card')
                else:
                    turns += 1
                    if c_func_number == "DRAW 4":
                        peoples[player_num].draw_cards(4)
                    elif c_func_number == "DRAW 2":
                        peoples[player_num].draw_cards(2)
                    elif c_func_number == "SKIP":
                        print(f'skip {peoples[player_num]}\'s turn')
                    elif c_func_number == "REVERSE":
                        print(f'reversing order')

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
        
    
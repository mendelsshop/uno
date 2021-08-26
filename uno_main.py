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
# use center instead of make_car_longer
# reference an instance of a class in a different class for deck, dump_pile modification by an uno_player instnce posiibly done by adding parameter to uno_player methods that need stuff from uno_game for the instance of uno_game running
class card:
    @staticmethod
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
    @staticmethod
    def cardify1(cards):
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
            len_of_cards = len(cards)
            crds_extended = card.make_car_longer(cardname = cards, card_length = len_of_cards,space_length = blanks)
            print('|',crds_extended,end='')
        print()    
        for q in range(z):
            print('| |                | ', end = '')  
        print()  
        for q in range(z):
            print('| |                | ', end = '')
        print()
        for q in range(z):
            print('| \________________/ ',end='')
        print()
        for q in range(z):
            print('|                |  ',end='')
        print()
        for q in range(z):
            print('\________________/ ',end='')
        print()
    @staticmethod
    def cardify(cards):
        '''a funnction to display a(n) uno card(s)'''
        z_d = len(cards)
        blanks = len('                ')
        if z_d > 5:
            zlp = z_d // 5
            if z_d %  5 > 0:
                zlp += 1
        else:
            zlp = 1
        x = 1
        zdd = len(cards)
        while zdd > 5:
            zdd -= 5
            
        print(zlp, 'lines')
        for i in range(zlp):
            if x > 1:
                if x == zlp:
                    z = zdd
                else: 
                    z = 5
            else:
                if zlp == 1:
                    z = zdd
                else:
                    z = 5
            tzl = []
            for y in range(z):
                if x > 1:
                    tz = y + (5 * (x-1)) 
                else: 
                    tz = y
                tzl.append(tz)
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
            for y in range(z):
                len_of_cards = len(cards[tzl[y]])
                crds_extended = card.make_car_longer(cardname = cards[tzl[y]], card_length = len_of_cards,space_length = blanks)
                print(crds_extended,end='')
            print()
               
            for q in range(z):
                print('|                | ', end = '')  
            print()  
            for q in range(z):
                print('|                | ', end = '')
            print()
            for q in range(z):
                print('\________________/ ',end='')
            print()
            for q in range(z):
                t = tzl[q]
                print('','option:',t,'        ',end='')
            print()

            x += 1
    @staticmethod
    def decks():
        '''a function that returns a list of the uno cards uses the cards function and a for loop to generate most of the cards 
        besides for the wild cards which are appended to the list and then shuffles the list
        '''
        color = ['RED', 'BLUE', 'YELLOW', 'GREEN']
        decklist = []
        for i in range(4):
            color[i] = card.cards(color[i])
            for x in range(len(color[i])):
                decklist.append(color[i][x])
        for i in range(4):
            decklist.append('WILD')
            decklist.append('WILD DRAW 4')
        random.shuffle(decklist)
        return decklist
    @staticmethod
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
class uno_game:
    def __init__(self):
        self.playercount = 0
        self.playername = []
        self.dump_pile = []
        self.deck = card.decks()
        self.current_p = None
    def find_next_p(self,instance):
        index_p = self.playername.index(instance) 
        print(self.playercount, index_p)
        if index_p == self.playercount - 1:
            return repr(self.playername[0])
        return repr(self.playername[index_p+1])
    
    def set_next(self,instance):
        self.current_p = self.find_next_p(instance)
    def set_current(self):
        self.current_p = self.playername[0]
    def add_player(self):
        '''
        a function that adds 2 players from the uno_player class and then asks if you want to add more players
        '''
        while True:
                if self.playercount >= 2:
                    continues = input("do you want to add another person? (yes/no) ")
                    if continues == 'yes':
                        pass
                    else:
                        break
                while True:
                    names = input(f"player {self.playercount} what is your name? ")   
                    if names in self.playername:
                        print('plz try another name that name is already taken')
                        continue
                    break
                while True:
                    age = input(f'player {self.playercount} what is your age? ')
                    try:
                        age = int(age)
                    except:
                        print('what you entered for age is not an number please try again')
                        continue
                    break
                
                self.playername.append(uno_player(names,age))
                self.playercount += 1
        self.sort_player_foward()
    def sort_player_foward(self):
       '''
       a function that sorts the playername list by age ascending
       ''' 
       self.playername  = sorted(self.playername, key= lambda x:x.age )
    def sort_player_backward(self):
       '''
       a function that sorts the playername list by age descending
       ''' 
       self.playername  = sorted(self.playername, key= lambda x:x.age , reverse=True)
    def player_turn(self):
        pass
    def uno_main(self):
        # a lot of oop stuffs needs to be don here like dump_pile
        self.add_player()
        self.set_current()
        while True:
            '''
            this loop make sure that there is something in dump_pile(so that we can compare it to players card) make sure that there is something in deck so players can pick cards
            sorts palyers by age to choose which player starts
            '''
            if len(self.dump_pile) == 0:
                self.dump_pile.append(self.deck.pop())
            if len(self.deck) == 1:
                for i in range(len(self.dump_pile)):
                    self.deck.append(self.dump_pile.pop())
            while True:
                turns = 0
                name = self.current_p
                player_next = self.find_next_p(name)
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
                    if name.num_of_cards == 0:
                        name.get_cards(instance = self)
                        name.level = name.level - 1
                    for z in range(len(name.cards)):
                        cardss[z] = (name.cards[z])
                        cardsss.append(name.cards[z])
                    len_of_dump_pile = len(self.dump_pile)
                    len_of_dump_piles = len_of_dump_pile -1 
                    tpdp = self.dump_pile[len_of_dump_piles].split(' ',1)
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
                    
                    card.cardify1(self.dump_pile[len_of_dump_piles])
                    card.cardify(cardsss)
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
                        card.cardify(cardsss)
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
                                name.add_to_dump(x,self)
                                del cardsss
                                del cardss
                                c_func_number = n_func_number
                                good = True
                            elif c_func_number == n_func_number:
                                print(f'removing {name.cards[x]}..')
                                name.add_to_dump(x,self)
                                del cardsss
                                del cardss
                                c_func_number = n_func_number
                                good = True
                            elif name.cards[x] == 'WILD' or name.cards[x] == "WILD DRAW 4":
                                print(f'removing {name.cards[x]}..')
                                name.add_to_dump(x,self)
                                del cardsss
                                del cardss
                                c_func_number = n_func_number
                                good = True
                            
                            elif self.dump_pile[len_of_dump_piles] == name.cards[x]:
                                print(f'removing {name.cards[x]}..')
                                name.add_to_dump(x,self)
                                del cardsss
                                del cardss
                                c_func_number = n_func_number
                                good = True
                                

                            elif self.dump_pile[len_of_dump_piles] == 'WILD' or self.dump_pile[len_of_dump_piles] == 'WILD DRAW 4':
                                print(f'removing {name.cards[x]}..')
                                name.add_to_dump(x,self)  
                                del cardsss
                                del cardss
                                c_func_number = n_func_number
                                good = True
                            break
                  

                        elif z != x:
                            good = False
                    if len(name.cards) > 0:
                        name.num_of_cards = 1
                    elif len(name.cards) == 0:
                        name.num_of_cards = 0
                    if not good:
                        print('invalid option please try a different card or pick another card')
                    else:
                        turns += 1
                        if c_func_number == "DRAW 4":
                            player_next.draw_cards(4)
                        elif c_func_number == "DRAW 2":
                            player_next.draw_cards(2)
                        elif c_func_number == "SKIP":
                            print(f'skip {player_next}\'s turn')
                        elif c_func_number == "REVERSE":
                            print(f'reversing order')

                del cardss
                del cardsss
                amountcard = []
                for i in self.playername:
                    amountcard.append(len(i.cards))
                amountcard.append(len(self.deck))
                amountcard.append(len(self.dump_pile))
                sums = sum(amountcard)
                if sums == 108:
                    del amountcard
                else:
                    print('incorrect amount of cards')
            


class uno_player:
    def __init__(self,name,age):
        self.name = name
        self.level = 7
        self.cards = []
        self.num_of_cards = 0
        self.age = age
        self.next = None
    def draw_cards(self,times,instance):
        '''pop a card from the deck and add it to the players cards'''
        for i in range(times):
            self.cards.append(instance.pop())
    def get_cards(self,instance):
        '''
        similar to draw_card but draws cards based on the level of the player'''
        z = self.level
        for i in range(z):
            self.cards.append(instance.deck.pop())
    def add_to_dump(self,x,instance):
        '''remove a card from the player and add it to the dump_pile'''
        instance.dump_pile.append(self.cards.pop(x))
    def set_next(self,data):
        self.next = data
    def __str__(self):
        '''return a string representation of the player'''
        return [self.name, self.age]
    def __repr__(self):
        return f'name = {self.name} age = {self.age} cards = {self.cards}'





    

if __name__ == '__main__': 
    game1 = uno_game()
    game1.uno_main()
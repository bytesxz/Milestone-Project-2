'''

War card game inside of python.

'''
import random


#define global level variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card: #card object, multiple ones handled and returned by the deck class
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self): ##inits and creates the list of card objects, makes 52
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create card obj
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self): #self explanatory
        random.shuffle(self.all_cards)

    def deal_one(self):#gets one of the cards from the internal deck.
        return self.all_cards.pop()


class Player():
    def __init__(self, name):
       self.name = name
       self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        #if statement takes care of multiple cards added to player's collection of cards, while else deals with just one card.
        #appending multiple card objects will add it as a list item inside the list
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'



#game logic/game start

'''
1. create two player objects
2. shuffle deck
3. give it to the players (half each)
4. Check if someone has already lost -- do this all throughout
5. game loop
6. each player then draws a card
7. compare
8. if equal, draw additional three cards (at war == another loop) 
9. compare, player with higher ranking cards gets to keep all the cards
10. check if someone has won. 

'''

player_one = Player('one')
player_two = Player('two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True
round_num = 0

while game_on:
    
    round_num += 1
    print(f'Round {round_num}')


    if len(player_one.all_cards) == 0:
        print('player one has lost the game!')
        game_on = False
        break # redundant


    if len(player_two.all_cards) == 0:
        print('player two has lost the game!')
        game_on = False
        break

    #reset, start new round

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    #while at "war" stage

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:

            at_war = False

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

        elif player_two_cards[-1].value > player_one_cards[-1].value:

            at_war = False

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

        else:
            print(" :::WAR::: ")

            if len(player_one.all_cards) < 3:
                print("Player one is unable to declare war.")
                print("Player two wins this game.")
                game_on = False #stops the main game loop from running since the game is already done.
                break

            elif len(player_two.all_cards) < 3:
                print("Player two is unable to declare war.")
                print("Player one wins this game.")
                game_on = False #stops the main game loop from running since the game is already done.
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
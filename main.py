from random import choice, shuffle
import itertools as it

from copy import deepcopy
from pprint import pprint

import os, time




welcome = '''
            Welcome to Uno Màs
-------------------------------------------

 ----------
|1. Cooler |
 ----------
Cooler does not see shapes, only colors.
He can put (for example) a heart on a diamond, or a spade on a club.
 
 ---------
|2. Moddo |
 ---------
Moddo has a tolerance of 1 on the value of cards.
He can put (for example) a 7 on a 6, or a Queen on a Jack.

 -----------
|3. Twisted |
 -----------
Twisted has a hidden pocket to make cards disappear.
Everytime he plays one card, he can discard another one for free.
 
 ----------
|4. Draggo |
 ----------
Draggo is a very offensive player.
Every bonus he gets is doubled.
 
 -----------
|5. Pegasus |
 -----------
Pegasus is a handsome french man.
Also, he can see his opponent's cards.

-------------------------------------------
        Please choose your player (1/2/3/4/5):
'''


# Constants
SUITS = ['C', 'D', 'H', 'S']
VALUES = [str(n + 1) for n in range(10)] + ['J', 'Q', 'K']

_CARDS = [*it.product(VALUES, SUITS)]
CARDS = {}
for card in _CARDS:
    CARDS[card[0] + ' of ' + card[1]] = (card[0], card[1])

WAIT_SYMBOL = chr(8987)
CARD_SYMBOL = chr(8718)
ARROW_ICON = chr(10144)

VALUES_ICONS = {
    '1': chr(10122),
    '2': chr(10123),
    '3': chr(10124),
    '4': chr(10125),
    '5': chr(10126),
    '6': chr(10127),
    '7': chr(10128),
    '8': chr(10129),
    '9': chr(10130),
    '10': chr(10131),
    'J': chr(9822),
    'Q': chr(9819),
    'K': chr(9818)
}

SUITS_ICONS = {
    'C': chr(9831),
    'D': chr(9826),
    'H': chr(9825),
    'S': chr(9828),
}

BONUS_ON_ICON = chr(9733)
BONUS_OFF_ICON = chr(9734)

PLAYABLE_CHARACTERS = [str(n) for n in range(1, 6)]

CHARACTER_ALIASES = {
    '1': 'Cooler',
    '2': 'Moddo',
    '3': 'Twisted',
    '4': 'Draggo',
    '5': 'Pegasus'
}


W, H = os.get_terminal_size()


# Game Parameters
STARTING_N_OF_CARDS = 7





# Classes
class Player:
    def __init__(self, player_name, player_cards):
        self.name = player_name
        self.cards = player_cards








class Enemy:
    def __init__(self, enemy_name, enemy_cards):
        self.name = enemy_name
        self.cards = enemy_cards
    
    
    




# Functions
def choose_players(player_number):
    player_name = CHARACTER_ALIASES[player_number]
    
    _playable_characters = PLAYABLE_CHARACTERS[:]
    _playable_characters.remove(player_number)
    
    enemy_number = choice(_playable_characters)
    enemy_name = CHARACTER_ALIASES[enemy_number]
    
    return player_name, enemy_name









def get_icons(card):
    card_name = card[0]
    value, suit = CARDS[card_name]
    return VALUES_ICONS[value] + SUITS_ICONS[suit]










def shuffle_stack(stack):
    list_of_cards = [*stack.keys()]
    shuffle(list_of_cards)
    
    shuffled_stack = {}
    for card in list_of_cards:
        shuffled_stack[card] = stack[card]
    
    return shuffled_stack




def is_game_over(game_state):
    stack, current_card, player, enemy = game_state
    
    if not player.cards or not enemy.cards:
        return True
    else:
        return False
        




def game_update(game_state):
    ...
    






def generate_characters_names():
    player_number = input(ARROW_ICON + ' ')
    
    if player_number in PLAYABLE_CHARACTERS:
        player_name, enemy_name = choose_players(player_number)
        return player_name, enemy_name
    else:
        return 0, 0
    
    
    
    
    
def ask_for_inputs(game_state):
    ...



def game_display(game_state):
    stack, current_card, player, enemy = game_state
    
    msg = "Current card : " + get_icons(current_card)
    print(msg.center(W))
    
    print()
    
    player_cards = " ".join(map(get_icons, [card for card in player.cards]))
    msg = "Your cards : " + player_cards
    print(msg)
    
    enemy_cards = " ".join(map(get_icons, [card for card in enemy.cards]))
    msg = f"{enemy.name}'s cards : " + enemy_cards
    print(msg)
    
    print()
    
    msg = 'Cards remaining : ' + str(len(stack))
    print(msg.rjust(W))
    
    msg = 'Press "h" to display help'
    print(msg.rjust(W))
    


def start_game():
    
    stack = deepcopy(CARDS)
    
    stack = shuffle_stack(stack)
    
    player_name, enemy_name = generate_characters_names()
    
    player_cards = []
    for i in range(STARTING_N_OF_CARDS):
        player_cards.append(stack.popitem())
        
    enemy_cards = []
    for i in range(STARTING_N_OF_CARDS):
        enemy_cards.append(stack.popitem())
    
    current_card = stack.popitem()
    
    player = Player(player_name, player_cards)
    enemy = Enemy(enemy_name, enemy_cards)
    
    game_state = (stack, current_card, player, enemy)
    
    return game_state
    
    
    
    
def main():
    print(welcome)
    
    game_state = start_game()
    
    game_over = False
    
    while not game_over:
        game_display(game_state)
        game_inputs = ask_for_inputs(game_state)
        #game_state = game_update(game_state)
        game_over = is_game_over(game_state)
        
        game_over = True

    print('A winner is you!')
    
main()

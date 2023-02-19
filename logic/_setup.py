# modules
import arcade
import random
from Card import Card
from ._constants import *
from ._controls import *



def setup(self):
    self.held_cards = []
    self.held_cards_original_position = []
    self.card_list = arcade.SpriteList()
    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)

    # Create every card
    for card_suit in CARD_SUITS:
        for card_value in CARD_VALUES:
            card = Card(card_suit, card_value, CARD_SCALE)
            card.position = START_X, BOTTOM_Y
            self.card_list.append(card)
    
    # Shuffle the cards
    for pos1 in range(len(self.card_list)):
        pos2 = random.randrange(len(self.card_list))
        self.card_list.swap(pos1, pos2)


    # Create the MATS the cards go on.
    self.pile_mat_list: arcade.SpriteList = arcade.SpriteList() 

    pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
    pile.position = START_X, BOTTOM_Y
    self.pile_mat_list.append(pile)

    pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
    pile.position = START_X + X_SPACING, BOTTOM_Y
    self.pile_mat_list.append(pile)

    for i in range(7):
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X + i * X_SPACING, MIDDLE_Y
        self.pile_mat_list.append(pile)

    for i in range(4):
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X + i * X_SPACING, TOP_Y
        self.pile_mat_list.append(pile)
    # Create the MATS the cards go on.


    

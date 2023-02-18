# modules
import arcade
from Card import Card
from ._constants import *

def setup(self):
    self.card_list = arcade.SpriteList()

    i= START_X
    for card_suit in CARD_SUITS:
        j = BOTTOM_Y
        for card_value in CARD_VALUES:
            j+=5
            card = Card(card_suit, card_value, CARD_SCALE)
            card.position = i, j
            self.card_list.append(card)
        i=+CARD_WIDTH*2
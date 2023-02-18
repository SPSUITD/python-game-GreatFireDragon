# modules
import arcade
from Card import Card
from ._constants import *

def setup(self):
    self.held_cards = []
    self.held_cards_original_position = []
    self.card_list = arcade.SpriteList()
    self.cursor_sprite = arcade.Sprite()

    # Create every card
    for card_suit in CARD_SUITS:
        for card_value in CARD_VALUES:
            card = Card(card_suit, card_value, CARD_SCALE)
            card.position = START_X, BOTTOM_Y
            self.card_list.append(card)
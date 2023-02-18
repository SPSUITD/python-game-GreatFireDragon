# modules
import arcade
from Card import Card
from ._constants import *

def on_mouse_press(self, x, y, button, key_modifiers):
    cards = arcade.get_sprites_at_point((x, y), self.card_list)

    # Have we clicked on a card?
    if len(cards) > 0:

        # Might be a stack of cards, get the top one
        primary_card = cards[-1]

        # All other cases, grab the face-up card we are clicking on
        self.held_cards = [primary_card]
        # Save the position
        self.held_cards_original_position = [self.held_cards[0].position]
        # Put on top in drawing order
        self.pull_to_top(self.held_cards[0])

def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to render, looks on-top) """

        # Remove, and append to the end
        self.card_list.remove(card)
        self.card_list.append(card)
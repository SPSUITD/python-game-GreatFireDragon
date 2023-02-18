# modules
import arcade
from Card import Card
from ._constants import *

def on_mouse_press(self, x, y, button, key_modifiers):
    cards = arcade.get_sprites_at_point((x, y), self.card_list)

    # Have we clicked on a card?
    if len(cards) > 0:
        primary_card = cards[-1]

        self.held_cards = [primary_card]
        self.held_cards_original_position = [self.held_cards[0].position]
        self.pull_to_top(self.held_cards[0])

        # КУРСОС
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_3.png", 1)
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y



def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

        # КУРСОР
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y





def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    # If we don't have any cards, who cares
    if len(self.held_cards) == 0:
        return

    self.held_cards = {}




def pull_to_top(self, card: arcade.Sprite):
        self.card_list.remove(card)
        self.card_list.append(card)
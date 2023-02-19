# modules
import arcade
from Card import Card
from ._constants import *

def cursor_coordinates(self, x, y):
    self.cursor_sprite.center_x = x
    self.cursor_sprite.center_y = y

def cursor_on_hover(self, x, y):
    cards = arcade.get_sprites_at_point((x, y), self.card_list)
    if len(cards) > 0:
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_2.png", 1)
    else:
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)


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
    cursor_coordinates(self, x, y)



def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    if len(self.held_cards) > 0:
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy
    else:
        cursor_on_hover(self, x, y)

    # КУРСОР
    cursor_coordinates(self, x, y)

        



def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    # If we don't have any cards
    if len(self.held_cards) == 0:
        pass
    else:
        # SNAP to MATS
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)

        if arcade.check_for_collision(self.held_cards[0], pile):    # if collision
            for i, dropped_card in enumerate(self.held_cards):
                dropped_card.position = pile.center_x, pile.center_y
        else:                                                       # if no collision
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]
        # SNAP to MATS

        
    
    cursor_on_hover(self, x, y)
    cursor_coordinates(self, x, y)
    self.held_cards = {}




def pull_to_top(self, card: arcade.Sprite):
    self.card_list.remove(card)
    self.card_list.append(card)



def on_mouse_enter(self, x, y):
    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    self.cursor_coordinates(self, x, y)
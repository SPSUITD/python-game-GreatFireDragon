# modules
import arcade
from Card import Card
from ._constants import *

def cursor_coordinates(self, x, y):
    self.cursor_sprite.center_x = x
    self.cursor_sprite.center_y = y

def cursor_on_hover(self, x, y):
    # HOVER
    # cards = arcade.get_sprites_at_point((x, y), self.card_list)
    # if len(cards) > 0:
    #     self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_2.png", 1)
    # else:
    #     self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    pass


def on_mouse_press(self, x, y, button, key_modifiers):
    # ВЗЯТЬ ОБЪЕКТ
    # cards = arcade.get_sprites_at_point((x, y), self.card_list)

    if button == arcade.MOUSE_BUTTON_LEFT:
        print("left button bressed")
    elif button == arcade.MOUSE_BUTTON_RIGHT:
        print("right button pressed")
    else:
        print("wheel button pressed")

    # КУРСОС
    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_3.png", 1)
    cursor_coordinates(self, x, y)

def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    # ПЕРЕМЕЩЕНИЕ ОБъЕКТОВ
    # if len(self.held_cards) == 0:
    #     pass
    # else:
    #     # SNAP to MATS
    #     pass

    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    cursor_on_hover(self, x, y)
    cursor_coordinates(self, x, y)

def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    # ПЕРЕМЕЩЕНИЕ ОБъЕКТОВ
    # if len(self.held_cards) > 0:
    #     for card in self.held_cards:
    #         card.center_x += dx
    #         card.center_y += dy
    # else:
    #     cursor_on_hover(self, x, y)

    # КУРСОР
    cursor_coordinates(self, x, y)

        








def pull_to_top(self, card: arcade.Sprite):
    # Стопка наверх
    # self.card_list.remove(card)
    # self.card_list.append(card)
    pass



def on_mouse_enter(self, x, y):
    self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    self.cursor_coordinates(self, x, y)
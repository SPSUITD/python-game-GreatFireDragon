import arcade
import arcade.gui
from pyglet.math import Vec2
from static.constants import *

def cursor_coordinates(self, x, y):
    self.cursor_sprite.center_x = x
    self.cursor_sprite.center_y = y

def cursor_hover_fruit(self, x, y):
    fruits_at_cursor = arcade.get_sprites_at_point((x, y), self.fruit_list)
    if len(self.held_fruits) == 0:         # Если мы ничего не держим
        if len(fruits_at_cursor)>0:     # Если находимся над фруктом
            self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_2.png", CURSOR_SCALE)
            cursor_coordinates(self, x, y)
        else:
            self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", CURSOR_SCALE)
            cursor_coordinates(self, x, y)
    else:
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_3.png", CURSOR_SCALE)
        cursor_coordinates(self, x, y)

# В ситуации, когда мы кликнули на объект, который находистя позади 
# другого объекта. Мы хотим, чтобы кликнутый нами "активный" объект
# окахался наверху. Это приятнее для восприятия.
def pull_to_top(self, fruit: arcade.Sprite):
        self.fruit_list.remove(fruit)
        self.fruit_list.append(fruit)

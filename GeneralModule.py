import arcade
import arcade.gui
from static.constants import *

def cursor_coordinates(self, x, y):
    self.cursor_sprite.center_x = x
    self.cursor_sprite.center_y = y

def cursor_on_hover(self, x, y):
    fruits_at_cursor = arcade.get_sprites_at_point((x, y), self.fruit_list)
    if len(fruits_at_cursor)>0:
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_2.png", CURSOR_SCALE)
        cursor_coordinates(self, x, y)

# В ситуации, когда мы кликнули на объект, который находистя позади 
# другого объекта. Мы хотим, чтобы кликнутый нами "активный" объект
# окахался наверху. Это приятнее для восприятия.
def pull_to_top(self, fruit: arcade.Sprite):
        self.fruit_list.remove(fruit)
        self.fruit_list.append(fruit)